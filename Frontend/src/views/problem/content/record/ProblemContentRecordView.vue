<template>
    <ContentBaseSecondary>
        <el-table empty-text="没有提交记录"  :data="data" border stripe style="width: 100%">
            <el-table-column prop="time" label="时间"  min-width="150px" />
            <el-table-column :formatter="formatter_status" prop="status" label="状态" min-width="150px" />
            <el-table-column prop="language" label="语言" min-width="100px" />
        </el-table>

        <el-pagination style="float:right" :current-page="current_page" @current-change="current_change" background
            layout="prev, pager, next" :total="total" class="mt-4" />
        </ContentBaseSecondary>
</template>

<script>
import ContentBaseSecondary from '@/components/ContentBaseSecondary';
import $ from 'jquery';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';

import { ref} from 'vue';
export default {
    name: 'ProblemContentDescriptionView',
    components: {
        ContentBaseSecondary,
    },
    setup() { 
        const store = useStore();
        const route = useRoute();
        let data = ref([]), total = ref(1),current_page=ref(1);
        const problem_content_id = parseInt(route.params.id);
        const current_change = (val) => {
            current_page.value = val;
            getSubmitRecordList();
            
        }
        const formatter_status = (row, column, value, index) => { 
            let path = "/submit_record/" + data.value[index]['id'] + "/";
            
            if (value === 'Accepted') {
                return <router-link style="text-decoration:none;color:rgb(68, 157, 68);" to={path}>{value}</router-link>
            }
            else { 
                return <router-link style="text-decoration:none;color:rgb(208, 84, 81)" to={path}>{value}</router-link>
            }
        }
        const getSubmitRecordList = () => { 
            $.ajax({
                url: store.state.net.ip + "/submit_record/list/",
                type: "GET",
                async: false,
                data: {
                    'page': current_page.value,
                    'problem_id':problem_content_id,
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        data.value = res.data;
                        total.value = res.total;
                    }
                },
            });
        }
        getSubmitRecordList();
        return {
            data,
            total,
            current_page,
            current_change,
            formatter_status,
        }
    }

}

</script>

<style scoped>

</style>