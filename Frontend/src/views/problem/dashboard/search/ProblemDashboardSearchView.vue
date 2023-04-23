<template>
    <ContentBase>
        <TitleBase :title="title"></TitleBase>
        <SearchBase @search="search" :show="show" @addContent="addContent" :operation="operation"></SearchBase>
        <hr>
        <TableBase :data="data"></TableBase>

        <PaginationBase :total="total" @current_change="current_change" :current_page="parseInt($route.params.page)">
        </PaginationBase>
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
import { ref } from 'vue'
export default {
    name: 'ProblemDashboardSearchView',
    components: {
        ContentBase,
        SearchBase,
        TitleBase,
        TableBase,
        PaginationBase,
    },
    setup() {
        const title = "至诚在线题库", operation = "", show = false;
        const route = useRoute(), store = useStore();
        let total = 0;
        let data = ref([]);
        const addContent = () => {
            router.push({ name: 'admin_problem_add' });
        }
        const getProblemList = () => {
            $.ajax({
                url: store.state.net.ip + "/problem/search/",
                type: "GET",
                async: false,
                data: {
                    search: route.params.search,
                    page: route.params.page,
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    //total指页数
                    total = Math.ceil(res.count / 10)*10;
                    data.value = res.results;
                },

            });
        }
        const current_change = (val) => {
            router.push({ name: 'problem_dashboard_search', params: { search: route.params.search , page: val } })
        }
        const search = (search_content) => {
            router.push({ name: 'problem_dashboard_search', params: { search: search_content,page:1 } })
        }
        getProblemList();
        return {
            title,
            operation,
            show,
            addContent,
            data,
            total,
            current_change,
            search,
        }
    }

}

</script>

<style scoped>

</style>