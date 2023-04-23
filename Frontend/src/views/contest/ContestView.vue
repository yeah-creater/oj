<template>
    <ContentBase>
        <TitleBase :title="title">
            <img width="36" src="https://cdn.acwing.com/static/web/img/activity/competition_total_ranklist.png" alt="">
        </TitleBase>
        <router-link :to="{name:'contest_rating'}">
            <el-button style="float:right" type="warning">排行榜</el-button>
        </router-link>
        <br>
        <hr>
    <ContentBaseSecondary>
        <UpcomingContest :data="upcoming_data"></UpcomingContest>
    </ContentBaseSecondary>
    <br>
    <ContentBaseSecondary>
        <PastContest :data="past_data" :contest_list_id="contest_list_id" :total="total" @current_change="current_change"></PastContest>
    </ContentBaseSecondary>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import TitleBase from '@/components/TitleBase.vue';
import UpcomingContest from '@/components/contest/UpcomingContest.vue';
import PastContest from '@/components/contest/PastContest.vue';
import {  ref } from 'vue';
import router from '@/router';
import $ from 'jquery';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
export default {
    name: 'ContestView',
    components: {
        ContentBase,
        ContentBaseSecondary,
        TitleBase,
        UpcomingContest,
        PastContest,
    },
    setup() { 
        let route = useRoute(), store = useStore();
        let title = ref('在线竞赛');
        let upcoming_data = ref([]);
        let past_data = ref([]);
        let contest_list_id = ref(route.params.id), total = ref(0)

        const getContestList=(type)=>{ 
            $.ajax({
                url: store.state.net.ip + "/contest/list/",
                type: "GET",
                data: {
                    page: route.params.id,
                    type: type,
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        if (type === 'upcoming') { 
                            upcoming_data.value = res.data;
                        }
                        else {
                            past_data.value = res.data;
                            total.value = res.total;
                        }
                    }
                },
            });
        }
        const current_change = (val) => {
            router.push({ name: 'contest', params: { id: val } })
        }
        getContestList('upcoming');
        getContestList('past');
        return {
            title,
            upcoming_data,
            past_data,
            contest_list_id,
            total,

            current_change,
        }
    }

}

</script>

<style scoped>

</style>