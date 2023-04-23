<template>
    <ContentBaseSecondary>
        <el-table empty-text="无人之榜" :data="data"  stripe style="width: 100%">
            <el-table-column prop="ranking" label="排名" width="auto" min-width="15%" />
            <el-table-column :formatter="formatter_user" prop="user" label="用户" width="auto" min-width="45%" />
            <el-table-column prop="score" label="分数" width="auto" min-width="20%" />
            <el-table-column prop="penalty" label="罚时/s" width="auto" min-width="20%" />
        </el-table>
        <PaginationBase :total="total" @current_change="current_change" :current_page="current_page">
        </PaginationBase>
    </ContentBaseSecondary>
</template>
<script>
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import PaginationBase from "@/components/PaginationBase.vue"
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';
import { ref} from 'vue';
export default {
    name: 'ContestContentStaandingView',
    components: {
        ContentBaseSecondary,
        PaginationBase,
    },
    setup() {
        const route = useRoute(), store = useStore();
        let data = ref([]), total = ref(1), current_page = ref(1);
        const formatter_user = (row, column, value, index) => {
            let user_path = "/user/myspace/" +data.value[index]['user']['id'] + "/";
            return <router-link style="color: #337ab7;text-decoration: none;" to={user_path}>
                <img style="border-radius:50%" width={30} src={data.value[index]['user']['photo']} alt="~">
                </img>&nbsp;
                <span>{data.value[index]['user']['name']}</span>

            </router-link>
        }
        const current_change = (val) => {
            current_page.value = val;
            getContestStandings();
        }
        const getContestStandings = () => {
            $.ajax({
                url: store.state.net.ip + "/contest/standing/",
                type: "GET",
                data: {
                    contest_id: parseInt(route.params.id),
                    page: parseInt(current_page.value),
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        total.value = res.total;
                        data.value = res.data;
                    }
                },
            });
        }  
        getContestStandings();
        return {
            formatter_user,
            current_change,
            data,
            current_page,
            total,
        }
    }
}
</script>