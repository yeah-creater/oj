<template>
    <ContentBase>
        <TitleBase :title="title"></TitleBase>
        <SearchBase @search="search" :show="show" @addContent="addContent" :operation="operation"></SearchBase>
        <hr>
        <TableBase :data="data"></TableBase>

        <PaginationBase :total="total" @current_change="current_change" :current_page="problem_list_id"></PaginationBase>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import SearchBase from '@/components/SearchBase.vue';
import TitleBase from '@/components/TitleBase.vue';
import router from '@/router';
import TableBase from '@/components/problem/TableBase.vue';
import PaginationBase from "@/components/PaginationBase.vue"
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';
import {ref} from 'vue'
export default {
    name: 'ProblemDashboardView',
    components: {
        ContentBase,
        SearchBase,
        TitleBase,
        TableBase,
        PaginationBase,
    },
    setup() { 
        const title = "至诚在线题库",operation = "",show=false;
        const route = useRoute(), store = useStore();
        let problem_list_id = parseInt(route.params.id),total=0;
        let data = ref([]);
        const addContent = () => { 
            router.push({ name: 'admin_problem_add' });
        }
        const getProblemList = () => { 
            $.ajax({
                url: store.state.net.ip+"/problem/list/",
                type: "GET",
                async: false,
                data: {
                    page: problem_list_id,
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        total = res.total;
                        data = res.data;
                    }
                },
                
            });
        }
        const current_change=(val)=>{
            router.push({ name: 'problem_dashboard', params: {id:val} })
        }
        const search = (search_content) => { 
            router.push({ name: 'problem_dashboard_search', params: { search: search_content,page:1} })
        } 
        getProblemList();
        return {
            title,
            operation,
            show,
            addContent,
            data,
            problem_list_id,
            total,
            current_change,
            search,
        }
    }

}

</script>

<style scoped>

</style>