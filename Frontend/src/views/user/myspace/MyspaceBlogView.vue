<template>
    <ContentBaseSecondary>
        <el-table empty-text="空空如也" :data="data" stripe style="width: 100%">
            <el-table-column :formatter="formatter_title" prop="title" label="标题" width="auto" min-width="50%" />
            <el-table-column prop="create_time" label="时间" width="auto" min-width="50%" />
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
    name: 'MyspaceBlogView',
    components: {
        ContentBaseSecondary,
    },
    setup() {
        const store = useStore(),route=useRoute();
        let data = ref([]), total = ref(1), current_page = ref(1);
        const formatter_title = (row, column, value, index) => {
            let path = "/blog/content/" + data.value[index]['id'] + "/";
            return <router-link style="color: #337ab7;text-decoration: none;" to={path}>{value}</router-link>
        }
        const current_change = (val) => {
            current_page.value = val;
            getBlogList();

        }
        const getBlogList = () => {
            $.ajax({
                url: store.state.net.ip + "/blog/list/",
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
        getBlogList();
        return {
            data,
            current_page,
            total,
            current_change,
            formatter_title,
        }
    }
}
</script>