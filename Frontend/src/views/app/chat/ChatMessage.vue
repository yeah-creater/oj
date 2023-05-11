<template>
  <div class="message">
    <el-scrollbar ref="scrollbarRef">
      <div class="chat-list">
        <div class="chat-item" active="false"></div>
        <div
          v-for="(item, index) in data"
          :key="index"
          :class="{ self: id == item.id }"
          class="chat-item"
        >
          <!-- 头像 -->
          <div>
            <el-avatar>
              <img :src="item.photo" />
            </el-avatar>
          </div>
          <!-- 内容  -->
          <div class="content">
            <!-- 日期 -->
            <div class="date" style="text-align: center">
              {{ item.create_time }}
            </div>
            <div class="card-box">
              {{ item.content }}
            </div>
          </div>
        </div>
      </div>
    </el-scrollbar>
  </div>
</template>
<script >
import { nextTick, ref } from "vue";

export default {
  name: "ChatMesaage",
  props: {
    data: {
      type: Object,
      required: true,
    },
    id: {
      type: Number,
      required: true,
    },
  },
  setup() {
    const scrollbarRef = ref();

    const scroll = () => {
      nextTick(() => {
        const tar = document.querySelector(".chat-item:last-child");
        scrollbarRef.value.setScrollTop(tar.offsetTop);
      });
    };
    return {
      scrollbarRef,
      scroll,
    };
  },
};
</script>






<style lang="scss" scoped>
.date {
  color: #3c3c4399;
  font-size: 8px;
}
.message {
  position: absolute;
  width: 100%;
  top: 80px;
  bottom: 50px;

  .chat-list {
    padding: 20px 16px 0 16px;

    .chat-item {
      display: flex;
      margin-bottom: 20px;

      .content {
        margin: 0 50px 0 10px;

        .card-box {
          margin-top: 5px;
          background: #ffffff;
          padding: 5px 10px;
          border-radius: 4px;
          word-break: break-all;
        }
      }
    }
  }
}

.self {
  flex-direction: row-reverse;

  .username {
    text-align: right;
  }

  .content {
    margin: 0 10px 0 50px !important;

    .card-box {
      background-color: #95ec69 !important;
    }
  }
}
</style>
