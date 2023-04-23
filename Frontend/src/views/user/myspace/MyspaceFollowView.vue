<template>
    <ContentBaseSecondary>
        <el-empty description="空空如也" v-if="total == 0" />
        <div v-for="(obj, index) in follows" :key="index">
            <div class="row" style="margin-top: 12px; margin-bottom: 12px;">
                <div class="col-xs-2 col-sm-1">
                    <router-link :to=obj.path>
                        <img class="img-circle" :src="obj.photo" width="50" alt="用户头像">
                    </router-link>
                </div>
                <div class="col-xs-10 col-sm-11">
                    <div style="">
                        <router-link :to=obj.path style="text-decoration:none">
                            <span style="color:#337ab7;">{{ obj.name }}</span>

                        </router-link>
                    </div>
                    <div v-if="obj.gender === 'male'" style="color: #46B6EF;;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-gender-male" viewBox="0 0 16 16">
                            <path fill-rule="evenodd"
                                d="M9.5 2a.5.5 0 0 1 0-1h5a.5.5 0 0 1 .5.5v5a.5.5 0 0 1-1 0V2.707L9.871 6.836a5 5 0 1 1-.707-.707L13.293 2H9.5zM6 6a4 4 0 1 0 0 8 4 4 0 0 0 0-8z" />
                        </svg>
                    </div>
                    <div v-else style="color:#F37E7D">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-gender-female" viewBox="0 0 16 16">
                            <path fill-rule="evenodd"
                                d="M8 1a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM3 5a5 5 0 1 1 5.5 4.975V12h2a.5.5 0 0 1 0 1h-2v2.5a.5.5 0 0 1-1 0V13h-2a.5.5 0 0 1 0-1h2V9.975A5 5 0 0 1 3 5z" />
                        </svg>
                    </div>
                </div>

            </div>
            <hr>
        </div>
        <el-pagination style="float:right" :current-page="current_page" @current-change="current_change" background
            layout="prev, pager, next" :total="total" class="mt-4" />
    </ContentBaseSecondary>
</template>
<script>
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import { ref } from 'vue';
import $ from 'jquery'
export default {
    name: 'MyspaceFollowingView',
    components: {
        ContentBaseSecondary,
    },
    setup() {
        const route = useRoute(),store=useStore();
        const source = parseInt(route.params.userId);
        let follows = ref([]), total = ref(0), current_page = ref(1);
        let type = "following";
        if (route.name === 'user_mysapce_follower') { 
            type = 'follower';
        }
        const current_change = (val) => {
            current_page.value = val;
            getFollows();

        }
        const getFollows = () => {
            $.ajax({
                url: store.state.net.ip +"/user/follows/",
                type: "GET",
                async: true,
                data: {
                    type: type,
                    source: source,
                    page: current_page.value
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        total.value = res.total;
                        res = res.data;
                        follows.value = res;
                        for (let i = 0; i < res.length; i++) {
                            follows.value[i]['path'] = '/user/myspace/' + res[i].id + '/';
                        }

                    }
                },

            });
        }
        getFollows();
        return {
            follows,
            total,
            current_page,
            current_change,
        }
    }
}
</script>
<style scoped>
.img-circle {
    border-radius: 50%;
}

span:hover {
    font-size: 18px;
}
</style>