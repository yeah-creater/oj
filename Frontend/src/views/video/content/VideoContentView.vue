<template>
    <ContentBase>
        <ContentBaseSecondary>
            <h2 style="margin-top: 10px;">{{ data.title }}</h2>
            <div style="color: #999999; font-size:14px;">
                作者：
                <router-link style="text-decoration: none; color:#337ab7" :to=data.user_path>
                    <img style="border-radius: 50%;" width="30" :src=data.user_info_photo alt="作者的头像">
                    &nbsp;
                    <span style="font-size: 18px;">{{ data.user_info_name }}</span>
                </router-link>

                ,&nbsp;
                {{ data.create_time }}
            </div>
            <br>
            <vue3VideoPlay width="100%" v-bind="options" />
        </ContentBaseSecondary>
            <br>
        <ContentBaseSecondary>
            <CommentBase :latest_id="latest_id" :comment="comment" :user_info="user_info" @submitComment="submitComment"
                @removeComment="removeComment"></CommentBase>
        </ContentBaseSecondary>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import { ref } from 'vue';
import $ from 'jquery';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import router from '@/router';

import CommentBase from '@/components/CommentBase.vue';
import { getFormatTime } from '@/utils/tools.js'
export default {
    name: 'VideoContentView',
    components: {
        ContentBase,
        ContentBaseSecondary,
        CommentBase,
    },
    setup() {
        let data = ref({
            title: '',
            user_path:'',
            user_info_name:'',
            user_info_photo:'',
            create_time:'',
        });
        let options = ref({
            width: "100%", //播放器高度
            height: "450px", //播放器高度
            color: "#409eff", //主题色
            title: "", //视频名称
            src: "", //视频源
            muted: false, //静音
            webFullScreen: false,
            speedRate: ["0.75", "1.0", "1.25", "1.5", "2.0"], //播放倍速
            autoPlay: false, //自动播放
            loop: false, //循环播放
            mirror: false, //镜像画面
            ligthOff: false, //关灯模式
            volume: 0.3, //默认音量大小
            control: true, //是否显示控制
            controlBtns: [
                "audioTrack",
                "quality",
                "speedRate",
                "volume",
                "setting",
                "pip",
                "pageFullScreen",
                "fullScreen",
            ], //显示所有按钮,
        })
        let comment = ref([]), user_info = ref({}), latest_id = ref(0);
        const store = useStore(), route = useRoute();
        const getVideoContent = () => {
            $.ajax({
                url: store.state.net.ip + "/video/content/",
                type: "GET",
                async: false,
                data: {
                    md: 0,
                    video_id: route.params.id
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        res = res.data;
                        data.value = res;
                        data.value['user_path'] = '/user/myspace/' + data.value['user_id'] + '/';
                        options.value.src = data.value['content'];
                    }
                    else {
                        router.push({ name: '404' });
                    }
                },

            });
        }
        getVideoContent();
        const loadComments = () => {

            $.ajax({
                url: store.state.net.ip + "/file/comment/",
                type: "GET",
                async: false,
                data: {
                    type: 'video',
                    user_id: store.state.user.id,
                    video_id: route.params.id,
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
                },
            });
        }
        loadComments();
        const submitComment = (data) => {
            $.ajax({
                url: store.state.net.ip + "/file/operation/",
                type: "POST",
                async: false,
                data: {
                    type: 'video',
                    video_id: parseInt(route.params.id),
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
        return {
            data,
            options,
            comment,
            user_info,
            latest_id,
            submitComment,
            removeComment,

        }
    }

}

</script>

<style scoped>

</style>