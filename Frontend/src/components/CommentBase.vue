<template>
  <div class="comment-view">
    <u-comment
      :config="config"
      :show-size="5"
      style="width: 100%"
      @submit="submit"
      @like="like"
      @remove="remove"
      @report="report"
    >
    </u-comment>
  </div>
</template>

<script>
import { reactive } from "vue";
import { ElMessage } from "element-plus";
import emoji from "../../public/emoji";
import { useStore } from "vuex";
import router from "@/router";
export default {
  name: "CommentBase",
  props: {
    comment: {
      type: Object,
      required: true,
    },
    user_info: {
      type: Object,
      required: true,
    },
    latest_id: {
      type: Number,
      required: true,
    },
  },
  setup(props, context) {
    const store = useStore();
    const config = reactive({
      user: props.user_info,
      emoji: emoji,
      // 评论id数组 建议:存储方式用户id和文章id和评论id组成关系,根据用户id和文章id来获取对应点赞评论id,然后加入到数组中返回
      comments: props.comment,
    });

    //获取文件url
    // const createObjectURL=(blob)=> {
    //     if (window.URL) {
    //         return window.URL.createObjectURL(blob)
    //     } else if (window.webkitURL) {
    //         return window.webkitURL.createObjectURL(blob)
    //     } else {
    //         return ''
    //     }
    // }
    // 提交评论事件
    const submit = ({ content, parentId, files, finish }) => {
      /**
       * 上传文件后端返回图片访问地址，格式以', '为分割; 如:  '/static/img/program.gif, /static/img/normal.webp'
       */
      // let contentImg = files.map(e => createObjectURL(e)).join(', ')
      if (files !== "") {
        console.log(files);
      }
      if (!store.state.user.is_login) {
        router.push({ name: "login" });
        ElMessage({
          message: "请先登录",
          grouping: true,
          type: "warning",
        });
        return;
      }
      if (content.length == 0) {
        ElMessage({
          message: "评论不能为空",
          grouping: true,
          type: "warning",
        });
        return;
      }
      if (parentId === null) parentId = 0;
      context.emit("submitComment", {
        parentId,
        content,
        success() {
          if (parentId === 0) parentId = null;
          //将评论上传至后端 并获取最新评论ID
          let comment = {
            id: props.latest_id,
            parentId: parentId,
            uid: config.user.id,
            address: config.user.address,
            content: content,
            likes: 0,
            createTime: "刚刚",
            // contentImg: contentImg,
            user: {
              username: config.user.username,
              avatar: config.user.avatar,
              level: config.user.level,
              homeLink: "/user/myspace/" + config.user.id + "/",
            },
            reply: null,
          };

          finish(comment);
          ElMessage({
            message: "评论成功",
            grouping: true,
            type: "success",
          });
        },
        error(res) {
          ElMessage({
            message: res,
            grouping: true,
            type: "error",
          });
        },
      });
    };

    // 删除评论
    const remove = (id, finish) => {
      context.emit("removeComment", {
        id,
        success() {
          finish();
          ElMessage({
            message: "删除成功",
            grouping: true,
            type: "success",
          });
        },
      });
    };

    //举报用户
    const report = (id, finish) => {
      finish();
      ElMessage({
        message: "举报成功" + id,
        grouping: true,
        type: "success",
      });
    };

    // 点赞按钮事件
    const like = (id, finish) => {
      ElMessage({
        message: "敬请期待" + id,
        grouping: true,
        type: "warning",
      });
      finish();
    };
    return {
      config,
      submit,
      like,
      remove,
      report,
    };
  },
};
</script>

<style  scoped>
</style>
