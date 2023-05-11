<template>
  <ContentBase>
    <ContentBaseSecondary>
      <h2 style="margin-top: 10px">{{ data.title }}</h2>
      <div style="color: #999999; font-size: 14px">
        作者：
        <router-link
          style="text-decoration: none; color: #337ab7"
          :to="data.user_path"
        >
          <img
            style="border-radius: 50%"
            width="30"
            :src="data.user_info_photo"
            alt="作者的头像"
          />
          &nbsp;
          <span style="font-size: 18px">{{ data.user_info_name }}</span>
        </router-link>

        ,&nbsp;
        {{ data.create_time }}
      </div>
      <div>
        <span style="color: #4c4948">标签:</span>
        <el-tag
          style="margin-left: 8px"
          v-for="tag in data.tags.split(/\s+/)"
          :key="tag.id"
          type="success"
          class="article-tag-field-item"
          @click="tagClick(tag)"
        >
          {{ tag }}</el-tag
        >
      </div>
      <div align="right" v-if="data.user_id === $store.state.user.id">
        <router-link :to="{ name: 'blog_update', params: { id: data.id } }">
          <button type="button" class="btn btn-primary">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-pencil-square"
              viewBox="0 0 16 16"
            >
              <path
                d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
              ></path>
              <path
                fill-rule="evenodd"
                d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
              ></path>
            </svg>
            编辑
          </button>
        </router-link>
        &nbsp;
        <button
          @click="delete_dialog = true"
          type="button"
          class="btn btn-outline-danger"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-trash3-fill"
            viewBox="0 0 16 16"
          >
            <path
              d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"
            ></path>
          </svg>
          删除
        </button>
        <el-dialog v-model="delete_dialog" title="Warning" width="30%" center>
          <span> 确定要删除吗? </span>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="delete_dialog = false">取消</el-button>

              <el-button type="primary" @click="deleteBlog"> 确定 </el-button>
            </span>
          </template>
        </el-dialog>
      </div>
      <hr style="margin-bottom: 10px" />
      <div class="row">
        <div
          class="article col-lg-8 col-md-12"
          v-html="data.content"
          style="
            border-radius: 2px;
            margin: left;
            border-radius: 8px;
            background-color: #f2f3f5;
            box-shadow: 0 3px 8px 6px rgba(7, 17, 27, 0.05);
          "
        ></div>
        <div class="col-lg-1 col-md-12"></div>
        <div
          class="recommend col-lg-3 col-md-12"
          style="
            border-radius: 2px;
            margin: right;
            border-radius: 8px;
            background-color: #f2f3f5;
            box-shadow: 0 2px 4px 3px rgba(7, 17, 27, 0.05);
          "
        >
          <h3 style="text-align: center">相关推荐</h3>
        </div>
      </div>
    </ContentBaseSecondary>
    <br />
    <ContentBaseSecondary>
      <CommentBase
        :latest_id="latest_id"
        :comment="comment"
        :user_info="user_info"
        @submitComment="submitComment"
        @removeComment="removeComment"
      ></CommentBase>
    </ContentBaseSecondary>
  </ContentBase>
</template>

<script>
import ContentBase from "@/components/ContentBase";
import ContentBaseSecondary from "@/components/ContentBaseSecondary.vue";
import router from "@/router";
import { useStore } from "vuex";
import { ref, nextTick } from "vue";
import $ from "jquery";
import { useRoute } from "vue-router";
import { getFormatTime } from "@/utils/tools.js";
import CommentBase from "@/components/CommentBase.vue";
import { addCopy } from "@/utils/tools";

export default {
  name: "BlogContentView",
  components: {
    ContentBase,
    ContentBaseSecondary,
    CommentBase,
  },
  mounted() {
    addCopy();
  },
  setup() {
    const store = useStore(),
      route = useRoute();
    let data = ref({}),
      comment = ref([]),
      user_info = ref({}),
      latest_id = ref(0);
    let delete_dialog = ref(false);
    const getBlogContent = () => {
      $.ajax({
        url: store.state.net.ip + "/blog/content/",
        type: "GET",
        async: false,
        data: {
          md: 0,
          blog_id: parseInt(route.params.id),
        },
        // headers: {
        //     Authorization: "Bearer " + localStorage.getItem('access'),
        // },
        async success(res) {
          if (res.result === "success") {
            res = res.data;
            data.value = res;
            data.value["user_path"] =
              "/user/myspace/" + data.value["user_id"] + "/";
            await nextTick();
            window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
          } else {
            router.push({ name: "404" });
          }
        },
      });
    };
    const deleteBlog = () => {
      $.ajax({
        url: store.state.net.ip + "/blog/operation/",
        type: "DELETE",
        data: {
          blog_id: route.params.id,
        },
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access"),
        },
        success(res) {
          if (res.result === "success") {
            setTimeout(() => {
              router.push({ name: "blog", params: { id: 1 } });
            }, 500);
          } else {
            alert(res.result);
          }
        },
      });
    };
    const loadComments = () => {
      $.ajax({
        url: store.state.net.ip + "/file/comment/",
        type: "GET",
        async: false,
        data: {
          type: "blog",
          user_id: store.state.user.id,
          blog_id: route.params.id,
        },
        // headers: {
        //     Authorization: "Bearer " + localStorage.getItem('access'),
        // },
        success(res) {
          if (res.result === "success") {
            comment.value = res.data;
            user_info.value = JSON.parse(res.user_info);
            for (let i = 0; i < comment.value.length; i++) {
              let t = comment.value[i].createTime;
              comment.value[i].createTime = getFormatTime(t);
              if (comment.value[i].parentId === 0) {
                comment.value[i].parentId = null;
              }
              if (comment.value[i].parentId === null) {
                for (let j = 0; j < comment.value[i].reply.total; j++) {
                  t = comment.value[i].reply.list[j].createTime;
                  comment.value[i].reply.list[j].createTime = getFormatTime(t);
                }
              }
            }
          } else {
            alert(res.result);
          }
        },
      });
    };
    const submitComment = (data) => {
      console.log(data.content);
      $.ajax({
        url: store.state.net.ip + "/file/operation/",
        type: "POST",
        async: false,
        data: {
          type: "blog",
          blog_id: parseInt(route.params.id),
          parentId: parseInt(data.parentId),
          content: data.content,
        },
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access"),
        },
        success(res) {
          if (res.result === "success") {
            latest_id.value = res.data;
            setTimeout(() => {
              data.success();
            }, 300);
          } else {
            data.error(res.result);
          }
        },
      });
    };
    const removeComment = (data) => {
      $.ajax({
        url: store.state.net.ip + "/file/operation/",
        type: "DELETE",
        async: false,
        data: {
          comment_id: parseInt(data.id),
        },
        headers: {
          Authorization: "Bearer " + localStorage.getItem("access"),
        },
        success(res) {
          if (res.result === "success") {
            setTimeout(() => {
              data.success();
            }, 300);
          } else {
            alert(res.result);
          }
        },
      });
    };
    const tagClick = (tag) => {
      router.push({ name: "blog_search", params: { search: tag, page: 1 } });
    };
    getBlogContent();
    loadComments();
    return {
      latest_id,
      data,
      comment,
      user_info,
      delete_dialog,

      deleteBlog,
      loadComments,
      submitComment,
      removeComment,
      tagClick,
    };
  },
};
</script>

<style scoped>
.article-tag-field-item:hover {
  cursor: pointer;
  font-size: 14px;
}
</style>