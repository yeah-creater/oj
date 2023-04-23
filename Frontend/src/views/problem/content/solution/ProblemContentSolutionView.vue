<template>
    <ContentBaseSecondary>
        <el-table empty-text="空空如也" :data="data" stripe style="width: 100%">
            <el-table-column :formatter="formatter_title" prop="title" label="标题"  min-width="160px" />
            <el-table-column :formatter="formatter_user" prop="user_id" label="作者"  min-width="120px"  />

            <el-table-column prop="create_time" label="时间" width="auto" min-width="200px" />
        </el-table>

        <el-pagination style="float:right" :current-page="current_page" @current-change="current_change" background
            layout="prev, pager, next" :total="total" class="mt-4" />
    </ContentBaseSecondary>
</template>
<script>
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import { ref } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import $ from 'jquery';
export default {
    name: 'ProblemContentSolutionView',
    components: {
        ContentBaseSecondary,
    },
    setup() {
        const store = useStore(),route=useRoute();
        let data = ref([]), total = ref(1), current_page = ref(1);
       
        const formatter_title = (row, column, value, index) => {
            let path = "/solution/content/" + data.value[index]['id'] + "/";
            return <router-link style="color: #337ab7;text-decoration: none;" to={path}>{value}</router-link>
        }
        const formatter_user = (row, column, value, index) => {
            let user_path = "/user/myspace/" + data.value[index]['user_id'] + "/";
            return <router-link style="color: #337ab7;text-decoration: none;" to={user_path}>
                <img style="border-radius:50%" width={30} src={data.value[index]['user_info_photo']} alt="~">
                </img>&nbsp;
                <span>{data.value[index]['user_info_name']}</span>

            </router-link>
        }
        const current_change = (val) => {
            current_page.value = val;
            getSolutionList();

        }
        const getSolutionList = () => {
            $.ajax({
                url: store.state.net.ip + "/solution/list/",
                type: "GET",
                async: false,
                data: {
                    problem_id: parseInt(route.params.id),
                    page: parseInt(current_page.value),
                },
                success(res) {
                    if (res.result === 'success') {
                        total.value = res.total;
                        data.value = res.data;
                    }
                },

            });
        }
        getSolutionList();
        return {
            data,
            current_page,
            total,
            current_change,
            formatter_user,
            formatter_title,
        }
    }
}
</script>