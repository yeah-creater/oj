<template>
    <ContentBase>
        <TitleBase :title="title"></TitleBase>
        <SearchBase @search="search" :show="show" @addContent="addContent" :operation="operation"></SearchBase>
        <hr>
        <el-table empty-text="空空如也" :data="data" stripe style="width: 100%">
            <el-table-column :formatter="formatter_title" prop="title" label="标题" min-width="100px"  />
            <el-table-column :formatter="formatter_user" prop="user_id" label="作者" min-width="100px"  />
            <el-table-column prop="create_time" label="时间" min-width="200px" />
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
        let blog_list_id = parseInt(route.params.id), total = 0;
        let data = reactive([]);
        const addContent = () => {
            router.push({ name: 'blog_add' });
        }
        const formatter_title = (row, column, value, index) => {
            let path = "/blog/content/" + data[index]['id'] + "/";
            return <router-link style="color: #337ab7;text-decoration: none;" to={path}>{value}</router-link>
        }
        const formatter_user = (row, column, value, index) => {
            let user_path = "/user/myspace/" + data[index]['user_id'] + "/";
            return <router-link style="color: #337ab7;text-decoration: none;" to={user_path}>
                <img style="border-radius:50%" width={30} src={data[index]['user_info_photo']} alt="~">
                </img>&nbsp;
                <span>{data[index]['user_info_name']}</span>

            </router-link>
        }
        const getBlogList = () => {
            $.ajax({
                url: store.state.net.ip + "/blog/list/",
                type: "GET",
                async: false,
                data: {
                    page: parseInt(blog_list_id),
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    data.length = 0;
                    if (res.result === 'success') {
                        total = res.total;
                        data = res.data;
                    }
                },

            });
        }
        const current_change = (val) => {
            router.push({ name: 'blog', params: { id: val } })
        }
        const search = (search_content) => {
            router.push({ name: 'blog_search', params: { search: search_content, page: 1 } })
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