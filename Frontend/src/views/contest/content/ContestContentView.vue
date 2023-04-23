<template>
    <ContentBase>
        <div class="header">
            <div>
                <img width="100" src="https://cdn.acwing.com/static/web/img/activity/competition_total_ranklist.png" alt="">
                <div v-if="status!==3" class="info">
                    <div v-if="status===1">
                        距离比赛开始,还有
                        <countDown :endTime="time" :endText="text">
                        </countDown>
                    </div>
                    <div v-else>
                        距离比赛结束,还有
                        <countDown :endTime="time" :endText="text">
                        </countDown>
                    </div>
                   
                    <el-button v-if="!is_register" type="success" @click="register">报名</el-button>
                    <div v-else>报名人数:{{total }}</div>
                </div>
                <div v-else>
                    <el-button  type="light">比赛已结束</el-button>
                    <!-- <el-button @click="clear1" v-if="$store.state.user.id === 1 && !clear" type="success">结算积分</el-button>
                    <el-button v-if="$store.state.user.id === 1 && clear" type="light">已结算</el-button> -->
                </div>
            </div>
        </div>
        
        <div class="row">
            <div class="col-12 col-xs-12">
                <ContentBaseSecondary>
                    <ul class="row nav nav-tabs">
                        <li :class="{active: item.path==$route.fullPath }" class="item col-4 col-xs-4" v-for="(item, index) in navs" :key="index" >
                            <router-link style="text-decoration: none;" :to=item.path>{{ item.title }}</router-link>
                        </li>
                    </ul>
                    <router-view :key="$route.fullPath" />
                </ContentBaseSecondary>
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import router from '@/router';
import { reactive, ref } from 'vue';
import $ from 'jquery';
import CountDown from '@/components/CountDown'

export default {
    name: 'ContestContentView',
    components: {
        ContentBase,
        CountDown,
    },
    setup() { 
        const route = useRoute(),store=useStore();
        const navs = reactive([
            { title: '问题', path: '/contest/content/' + route.params.id+ '/problem/' },
            { title: '排名', path: '/contest/content/' + route.params.id + '/standing/' },
            { title: '讨论', path: '/contest/content/' + route.params.id + '/discussion/' },
        ])
        //其中status的1代表未开始 2代表进行中 3代表已结束
        let is_register = ref(false), total = ref(0), status = ref(0),clear=ref(false);
        let time = ref(0) ,text = '比赛已开始';
        const getContestContent = () => {
            $.ajax({
                url: store.state.net.ip + "/contest/content/",
                type: "GET",
                data: {
                    contest_id: route.params.id,
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        status.value = res.status;
                        clear.value = res.data.clear;
                        if (status.value === 1) {
                            time.value = new Date(res.data.start_time)/1000+'';
                            text = '比赛已开始';
                        }
                        else if (status.value === 2) {
                            time.value = new Date(res.data.over_time) / 1000 + ''
                            text = '比赛已结束';
                        }
                    }
                },
            });
        }
        const getContestParticipants = () => { 
            $.ajax({
                url: store.state.net.ip + "/contest/participant/",
                type: "GET",
                data: {
                    contest_id: route.params.id,
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        res = res.data;
                        total.value = res.length;
                        for (let i = 0; i < res.length; i++) { 
                            if (res[i]['user']['id'] === store.state.user.id) { 
                                is_register.value = true;
                                break;
                            }
                        }
                    }
                },
            });
        }
        const register = () => {
            if (!store.state.user.is_login) {
                router.push({ name: 'login' });
            }
            $.ajax({
                url: store.state.net.ip + "/contest/participant/",
                type: "POST",
                data: {
                    contest_id: parseInt(route.params.id),
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        router.push({ name: 'contest_content' });
                    }
                },
            });
        }
        const clear1 = () => {
            $.ajax({
                url: store.state.net.ip + "/contest/rating/",
                type: "POST",
                data: {
                    contest_id: parseInt(route.params.id),
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        router.push({ name: 'contest_content' });
                    }
                },
            });
        }
        getContestContent();
        if (store.state.user.is_login) { 
            getContestParticipants();
        }
        return {
            navs,
            is_register,
            status,
            time,
            text,
            total,
            clear,
            register,
            clear1,
        }
    }

}

</script>

<style scoped>
.header{
    width: 100%;
    height: 200px;
    text-align: center;
    line-height: 100px;
    border-radius: 20px;
    background: linear-gradient(to bottom, rgba(255, 255, 255, 0.15) 0%, rgba(0, 0, 0, 0.15) 100%), radial-gradient(at top center, rgba(255, 255, 255, 0.40) 0%, rgba(0, 0, 0, 0.40) 120%) #989898;
    background-blend-mode: multiply, multiply;
    margin-bottom: 120px;
}
.item{
    height: 40px;
    line-height: 40px;
    font-size: 20px;
    text-align: center;
    color:#909399;
}
.active{
    background: #F2F3F5;
    border-radius: 10px;
}
</style>