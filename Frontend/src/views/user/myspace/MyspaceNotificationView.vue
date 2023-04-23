<template>
    <ContentBaseSecondary>
        <el-empty description="空空如也" v-if="total == 0" />
        <div v-for="(obj, index) in notifications" :key="index">
            <div class="row" style="margin-top: 12px; margin-bottom: 12px;">
                <div class="col-xs-2 col-sm-1">
                    <router-link :to=obj.path>
                        <img class="img-circle" :src="obj.target.photo" width="50" alt="用户头像">
                    </router-link>
                </div>
                <div class="col-xs-7 col-sm-7">
                    <div style="">
                        <router-link :to=obj.path style="text-decoration:none">
                            <span style="color:#337ab7;">{{ obj.target.name }}</span>

                        </router-link>
                    </div>
                    <div>
                        <span>
                            <router-link :to=obj.path style="text-decoration:none">
                                <span style="color:#337ab7;">{{ obj.target.name }}</span>

                            </router-link></span>&nbsp;
                            <span style="color:#6a737c;font-size:15px;font-weight: lighter;">{{ obj.notification_type }}</span>
                    </div>
                </div>
                <div class="col-xs-3 col-sm-4">
                    <span style="color:grey">{{ obj.time }}</span>
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
import  router  from '@/router';
import $ from 'jquery'
export default {
    name: 'MyspaceNotificationView',
    components: {
        ContentBaseSecondary,
    },
    setup() {
        const route = useRoute(), store = useStore();
        let notifications = ref([]), total = ref(0), current_page = ref(1);
        const current_change = (val) => {
            current_page.value = val;
            getNotifications();

        }
        const getNotifications = () => {
            $.ajax({
                url: store.state.net.ip + "/user/notification/",
                type: "GET",
                async: true,
                data: {
                    page: current_page.value
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        store.state.user.notification_count = 0;
                        total.value = res.total;
                        res = res.data;
                        notifications.value = res;
                        for (let i = 0; i < res.length; i++) {
                            notifications.value[i]['path'] = '/user/myspace/' + res[i].target.id + '/';
                        }

                    }
                },

            });
        }
        if (parseInt(route.params.userId) !== store.state.user.id) {
            router.push({ name: '404' });
            return;
        }
        else {
            getNotifications();
        }
        return {
            notifications,
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

</style>