<template>
    <ContentBaseSecondary>
        <CommentBase :latest_id="latest_id" :comment="comment" :user_info="user_info" @submitComment="submitComment"
            @removeComment="removeComment"></CommentBase>
    </ContentBaseSecondary>
</template>
<script>
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import CommentBase from '@/components/CommentBase.vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import { ref } from 'vue';
import $ from 'jquery';
import { getFormatTime } from '@/utils/tools.js'

export default {
    name: 'ContestContentDiscussionView',
    components: {
        ContentBaseSecondary,
        CommentBase,
    },
    setup() {
        const store = useStore(), route = useRoute();
        let data = ref({}), comment = ref([]), user_info = ref({}), latest_id = ref(0);
        const loadComments = () => {

            $.ajax({
                url: store.state.net.ip + "/file/comment/",
                type: "GET",
                async: false,
                data: {
                    type: 'contest',
                    user_id: store.state.user.id,
                    contest_id: route.params.id,
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
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
                    }
                    else {
                        alert(res.result);
                    }
                },
            });
        }
        const submitComment = (data) => {
            console.log(data.content);
            $.ajax({
                url: store.state.net.ip + "/file/operation/",
                type: "POST",
                async: false,
                data: {
                    type: 'contest',
                    contest_id: parseInt(route.params.id),
                    parentId: parseInt(data.parentId),
                    content: data.content,
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        latest_id.value = res.data;
                        setTimeout(() => {
                            data.success();
                        }, 300)
                    }
                    else {
                        alert(res.result);
                    }
                },
            });
        }
        const removeComment = (data) => {
            $.ajax({
                url: store.state.net.ip + "/file/operation/",
                type: "DELETE",
                async: false,
                data: {
                    comment_id: parseInt(data.id),
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        setTimeout(() => {
                            data.success();
                        }, 300)
                    }
                    else {
                        alert(res.result);
                    }
                },
            });
        }
        loadComments();
        return {
            latest_id,
            data,
            comment,
            user_info,

            loadComments,
            submitComment,
            removeComment,
        }
    }
}
</script>