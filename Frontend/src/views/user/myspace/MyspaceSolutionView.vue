<template>
    <ContentBaseSecondary>
        <el-table empty-text="空空如也" :data="data" stripe style="width: 100%">
            <el-table-column :formatter="formatter_problem" prop="problem" label="问题编号" width="auto" min-width="30%" />
            <el-table-column :formatter="formatter_title" prop="title" label="标题" width="auto" min-width="35%"/>
            <el-table-column prop="create_time" label="时间" width="auto" min-width="35%" />
        </el-table>
        
        <el-pagination style="float:right" :current-page="current_page" @current-change="current_change" background
            layout="prev, pager, next" :total="total" class="mt-4" />
    </ContentBaseSecondary>
</template>
<script>
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
 import { ref } from 'vue';
import { useStore } from 'vuex';
import $ from 'jquery';
import { useRoute } from 'vue-router';
export default {
    name: 'MyspaceSolutionView',
    components: {
        ContentBaseSecondary,
    },
    setup() {
        const store = useStore(),route=useRoute();
        let data = ref([]),total = ref(1), current_page = ref(1);
        const formatter_problem = (row, column, value, index) => {
            let path = "/problem/content/" + data.value[index]['problem'] + "/";
            return <router-link style="color: #337ab7;text-decoration: none;" to={path}>{value}</router-link>
        }
        const formatter_title = (row, column, value, index) => {
            let path = "/solution/content/" + data.value[index]['id'] + "/";
            return <router-link style="color: #337ab7;text-decoration: none;" to={path}>{value}</router-link>
        }
        const current_change = (val) => {
            current_page.value = val;
            getSolutionList();
            
        }
        const getSolutionList = () => {
            $.ajax({
                url: store.state.net.ip + "/solution/list/",
                type: "GET",
                async: true,
                data: {
                    user_id: parseInt(route.params.userId),
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
            formatter_problem,
            formatter_title,
        }
    }
}
</script>