<template>
    <ContentBase>
        <div class="row">
            <div class="col-lg-3 col-md-12">
                <MyspaceProfile :data=data @chat="chat" @follow="follow" @unfollow="unfollow"/>
            </div>
            <div class="col-lg-9 col-md-12">
                <ContentBaseSecondary>
                    <ul class="nav nav-tabs">
                        <li class="nav-item" v-for="(item, index) in navs" :key="index">
                            <router-link :class="$route.fullPath===item.path? 'nav-link active':'nav-link'" :to=item.path>{{item.title}}</router-link>
                        </li>
                    </ul>
                    <router-view :key="$route.fullPath" />
                    <div v-if="$route.name === 'user_myspace'" style="background:url('https://app2105.acapp.acwing.com.cn/media/background/door.jpg' ); background-size:cover; height: 400px;">
                    <el-empty description=" " image=" ">
                            <router-link class="nav-link" :to="{name:'user_mysapce_record'}"><el-button type="info"
                            plain>进入空间</el-button></router-link></el-empty>
                    </div>
                </ContentBaseSecondary>
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import router from '@/router';
import $ from 'jquery';
import { reactive, ref} from 'vue';
import MyspaceProfile from '@/components/user/MyspaceProfile.vue';

export default {
    name: 'MyspaceView',
    components: {
        ContentBase,
        ContentBaseSecondary,
        MyspaceProfile,
    },
    
    setup() {
        const store = useStore();
        const route = useRoute();
        
        let data = ref({
        })
        let prefix = 'Ta的';
        const navs = reactive([
            { title: '个性签名', path: '/user/myspace/' + route.params.userId + '/record/' },
            { title: '题解', path: '/user/myspace/' + route.params.userId + '/solution/' },
            { title: 'blog', path: '/user/myspace/' + route.params.userId + '/blog/' },
        ])
        if (parseInt(store.state.user.id) === parseInt(route.params.userId)) {
            prefix = '我的';
            navs.push({ title: '通知', path: '/user/myspace/' + route.params.userId + '/notification/' });
        }
        navs.push({ title: prefix + '关注', path: '/user/myspace/' + route.params.userId + '/following/' })
        navs.push({ title: prefix + '粉丝', path: '/user/myspace/' + route.params.userId + '/follower/' },)
        const getUserInfo = () => { 
            $.ajax({
                url: store.state.net.ip +"/user/user_info/",
                type: "GET",
                async:false,
                data: {
                    user_id: parseInt(store.state.user.id),
                    visit_id: parseInt(route.params.userId)
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        res = res.data;
                        data.value = res;
                    }
                    else { 
                        router.push({ name: '404' });
                    }
                },

            });
        }
        getUserInfo();

        const follow = () => { 
            $.ajax({
                url: store.state.net.ip +"/user/follow/",
                type: "POST",
                async: false,
                data: {
                    target_id: data.value.id,
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        data.value.followers++;
                        data.value.is_follow = true;
                    }
                    else {
                        router.push({ name: '404' });
                    }
                },
            })
        }
        const unfollow = () => {
            $.ajax({
                url: store.state.net.ip +"/user/follow/",
                type: "POST",
                async: false,
                data: {
                    target_id: data.value.id,
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        data.value.followers--;
                        data.value.is_follow = false;
                        console.log("unfollow");
                    }
                    else {
                        router.push({ name: '404' });
                    }
                },
            })
        }
        const chat = () => { 
            
            $.ajax({
                url: store.state.net.ip + "/chat/list/",
                type: "POST",
                async: false,
                data: {
                    target: parseInt(route.params.userId),
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        router.push({ name: 'app_chat' });
                    }
                    else {
                        router.push({ name: '404' });
                    }
                },
            })
        }
        return {
            data,
            follow,
            unfollow,
            chat,
            navs,
        }
    },

}

</script>

<style scoped>

</style>