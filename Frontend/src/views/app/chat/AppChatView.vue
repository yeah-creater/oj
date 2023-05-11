<template>
  <ContentBase>
    <div class="row">
      <div class="col-md-3 col-sm-12">
        <p style="color: #606266; border-bottom: 3px solid #f5f7fa">最近联系</p>
        <div
          @click="select(item.id, item.name)"
          :class="{ select: item.id === select_id }"
          class="row friend"
          style="
            height: 60px;
            display: flex;
            align-items: center;
            border-bottom: 1px solid #e4e7ed;
          "
          v-for="(item, index) in friends"
          :key="index"
        >
          <div class="col-2">
            <router-link :to="item.path">
              <img :src="item.photo" width="35" style="border-radius: 50%" />
            </router-link>
          </div>
          <div class="col-7">
            <span style="color: #909399">{{ item.name }}</span>
          </div>
          <div class="col-3">
            <div class="unread-warning" v-if="item.unread > 0">
              <span class="unread-count">{{ item.unread }}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-9 col-sm-12">
        <div class="u-chat">
          <div class="chat-container translate active">
            <!-- 标题 -->
            <div class="header">
              <div style="margin-left: 12px">
                <strong>{{ select_name }}</strong>
              </div>
            </div>
            <!-- 对话内容 -->
            <ChatMessage ref="messageRef" :data="data" :id="user.id" />
            <!-- 输入框 -->
            <div v-if="select_id !== 0" id="chat-footer" class="footer">
              <!-- 文字输入 -->
              <el-input
                resize="none"
                id="emojiInput"
                maxlength="1024"
                show-word-limit
                v-model="content"
                type="textarea"
                :autosize="{ minRows: 2, maxRows: 4 }"
                placeholder="请输入内容"
              ></el-input>
              <el-button
                @click="submit"
                type="primary"
                round
                style="margin-left: 5px"
              >
                发送
                <u-icon
                  size="16"
                  class="select-none cursor-pointer"
                  style="padding-bottom: 5px"
                >
                  <svg
                    viewBox="0 0 1025 1024"
                    version="1.1"
                    xmlns="http://www.w3.org/2000/svg"
                    p-id="15072"
                  >
                    <path
                      d="M1008.00076 6.285714q18.857143 13.714286 15.428571 36.571429l-146.285714 877.714286q-2.857143 16.571429-18.285714 25.714286-8 4.571429-17.714286 4.571429-6.285714 0-13.714286-2.857143l-258.857143-105.714286-138.285714 168.571429q-10.285714 13.142857-28 13.142857-7.428571 0-12.571429-2.285714-10.857143-4-17.428571-13.428571t-6.571429-20.857143l0-199.428571 493.714286-605.142857-610.857143 528.571429-225.714286-92.571429q-21.142857-8-22.857143-31.428571-1.142857-22.857143 18.285714-33.714286l950.857143-548.571429q8.571429-5.142857 18.285714-5.142857 11.428571 0 20.571429 6.285714z"
                      p-id="15073"
                    ></path>
                  </svg>
                </u-icon>
              </el-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </ContentBase>
</template>

<script>
import ContentBase from "@/components/ContentBase";
import { ref, reactive } from "vue";
import ChatMessage from "./ChatMessage.vue";
import $ from "jquery";
import { useStore } from "vuex";
export default {
  name: "AppChatView",
  components: {
    ContentBase,
    ChatMessage,
  },
  unmounted() {
    const store = useStore();
    store.state.user.socket.close();
  },
  setup() {
    const store = useStore();
    let content = ref(""),
      select_id = ref(0),
      select_name = ref("");
    let socket = new WebSocket(
      "wss://app2105.acapp.acwing.com.cn/wss/chat/?token=" +
        store.state.user.access
    );
    let messageRef = ref();
    let data = reactive([]),
      friends = reactive([]),
      user = reactive({
        id: store.state.user.id,
        photo: store.state.user.photo,
        name: store.state.user.name,
      });
    store.state.user.socket = new WebSocket(
      "wss://app2105.acapp.acwing.com.cn/wss/chat/list/?token=" +
        store.state.user.access
    );
    store.state.user.socket.onmessage = (e) => {
      let message = JSON.parse(e.data);
      let event = message["event"];
      //有人发消息 更新最近联系列表
      if (event === "message") {
        getChatList();
      }
    };

    const clear = () => {
      content.value = "";
      messageRef.value.scroll();
    };
    const select = (id, name) => {
      for (let i = 0; i < friends.length; i++) {
        if (friends[i].id === id) {
          friends[i].unread = 0;
          //更新
          socket.send(
            JSON.stringify({
              event: "init",
              target: parseInt(id),
            })
          );
        }
      }
      if (id !== select_id.value) {
        if (socket != "") {
          socket.close();
        }
        socket = new WebSocket(
          "wss://app2105.acapp.acwing.com.cn/wss/chat/?token=" +
            store.state.user.access
        );
        socket.onopen = () => {
          socket.send(
            JSON.stringify({
              event: "init",
              target: parseInt(id),
            })
          );
        };
        socket.onmessage = (e) => {
          let message = JSON.parse(e.data);
          let event = message["event"];
          if (event === "message") {
            data.push({
              id: message["id"],
              name: message["name"],
              photo: message["photo"],
              content: message["content"],
              create_time: message["create_time"],
            });
          }
          clear();
        };
        data.length = 0;
        select_id.value = id;
        select_name.value = name;
        getChatMessage(id);
        clear();
      }
    };
    const getChatList = () => {
      $.ajax({
        url: store.state.net.ip + "/chat/list/",
        type: "GET",
        async: false,
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access"),
        },
        success(res) {
          if (res.result === "success") {
            res = res.data;
            friends.splice(0, friends.length);
            for (let i = 0; i < res.length; i++) {
              friends.push(res[i].target);
              friends[i]["unread"] = res[i].unread;
              friends[i]["path"] = "/user/myspace/" + res[i].target.id + "/";
            }
          }
        },
      });
    };
    const getChatMessage = (target) => {
      $.ajax({
        url: store.state.net.ip + "/chat/message/",
        type: "GET",
        async: false,
        data: {
          target: parseInt(target),
        },
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access"),
        },
        success(res) {
          if (res.result === "success") {
            res = res.data;
            for (let i = 0; i < res.length; i++) {
              data.push({
                id: res[i].source.id,
                name: res[i].source.name,
                photo: res[i].source.photo,
                content: res[i].content,
                create_time: res[i].create_time,
              });
            }
          }
        },
      });
    };
    const submit = () => {
      if (content.value.trim() != "") {
        $.ajax({
          url: store.state.net.ip + "/chat/message/",
          type: "POST",
          data: {
            target: select_id.value,
            content: content.value,
          },
          headers: {
            Authorization: "Bearer " + localStorage.getItem("access"),
          },
          success(res) {
            if (res.result === "success") {
              socket.send(
                JSON.stringify({
                  event: "message",
                  target: select_id.value,
                  name: user.name,
                  photo: user.photo,
                  content: content.value,
                  create_time: res.data.create_time,
                })
              );
              store.state.user.socket.send(
                JSON.stringify({
                  event: "message",
                  target: select_id.value,
                })
              );
            }
          },
        });
      }
    };
    getChatList();
    return {
      content,
      data,
      friends,
      user,

      select_id,
      select_name,
      messageRef,
      submit,
      select,
    };
  },
};
</script>







<style lang="scss" scoped>
.unread-warning {
  width: 14px;
  height: 14px;
  border-radius: 7px;
  background-color: #ff3b30;
}

.unread-count {
  display: block;
  width: 100%;
  height: 14px;
  line-height: 14px;
  text-align: center;
  color: #fff;
  font-size: 12px;
}
.friend {
  cursor: pointer;
}
.friend:hover {
  background: #f2f3f5;
}
.select {
  background: #f2f3f5;
}
.u-chat {
  font-size: 14px;
  .chat-container {
    height: 445px;
    width: 100%;
    box-shadow: 0px 5px 40px rgba(0, 0, 0, 0.12);
    background: #f4f6fb;
    border-radius: 10px;

    .header {
      display: flex;
      align-items: center;
      padding: 20px 24px;
      background: #ffffff;
      border-radius: 1em 1em 0 0;
      box-shadow: 0 10px 15px -16px rgba(52, 52, 63, 0.08),
        0 4px 6px -8px rgba(50, 50, 93, 0.04);
    }

    .footer {
      position: absolute;
      width: 100%;
      box-sizing: border-box;
      bottom: 0;
      padding: 8px 16px;
      background: #f7f7f7;
      fill: #515767;
      border-radius: 0 0 1em 1em;
      display: flex;
      align-items: center;
    }
  }

  .translate {
    opacity: 0;
    -webkit-transform: translateY(-20px);
    transform: translateY(-20px);
    -webkit-transition: all 0.3s ease;
    transition: all 0.3s ease;
  }

  .active {
    display: block;
    opacity: 1;
    -webkit-transform: translateY(0px);
    transform: translateY(0px);
  }
}
</style>