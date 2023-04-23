<template>
    <ContentBase>
        <TitleBase :title="title"></TitleBase>
        <SearchBase @search="search" :show="show" @addContent="addContent" :operation="operation"></SearchBase>
        <hr>
        <el-table empty-text="空空如也" :data="data" stripe style="width: 100%">
            <el-table-column width="50" />
            <el-table-column :formatter="formatter_title" prop="title" label="标题" width="320" />
            <el-table-column :formatter="formatter_user" prop="user_id" label="作者" width="250" />
            <el-table-column prop="create_time" label="时间" />
        </el-table>

        <PaginationBase :total="total" @current_change="current_change" :current_page="blog_list_id">
        </PaginationBase>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import SearchBase from '@/components/SearchBase.vue';
import TitleBase from '@/components/TitleBase.vue';
import router from '@/router';
import PaginationBase from "@/components/PaginationBase.vue"
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';
import { reactive } from 'vue'
export default {
    name: 'SolutionView',
    components: {
        ContentBase,
        SearchBase,
        TitleBase,
        PaginationBase,
    },
    setup() {
        const title = "Blog", operation = "添加Blog", show = true;
        const route = useRoute(), store = useStore();
        let blog_list_id = parseInt(route.params.page), total = 0;
        let data = reactive([]);
        const addContent = () => {
            router.push({ name: 'blog_add' });
        }
        const formatter_title = (row, column, value, index) => {
            let path = "/blog/content/" + data[index]['id'] + "/";
            return <router-link style="color: #337ab7;text-decoration: none;" to={path}>{value}</router-link>
        }
        const formatter_user = (row, column, value, index) => {
            let user = JSON.parse(data[index]['user_id']);
            let user_path = "/user/myspace/" + user['user_id'] + "/";
            return <router-link style="color: #337ab7;text-decoration: none;" to={user_path}>
                <img style="border-radius:50%" width={30} src={user['user_info_photo']} alt="~">
                </img>&nbsp;
                <span>{user['user_info_name']}</span>

            </router-link>
        }
        const getBlogList = () => {
            $.ajax({
                url: store.state.net.ip + "/blog/search/",
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
                    total = Math.ceil(res.count / 10) * 10;
                    data = res.results;
                },

            });
        }
        const current_change = (val) => {
            router.push({ name: 'blog_search', params: { search: route.params.search, page:val } })
        }
        const search = (search_content) => {
            router.push({ name: 'blog_search', params: { search: search_content, page: route.params.page } })
        }
        getBlogList();
        return {
            title,
            operation,
            show,
            addContent,
            data,
            blog_list_id,
            total,
            current_change,
            formatter_title,
            formatter_user,
            search,
        }
    }

}

</script>

<style scoped>

</style>