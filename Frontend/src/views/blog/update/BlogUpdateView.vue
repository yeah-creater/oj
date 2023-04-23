<template>
    <ContentBase>
        <div class="row">
            <div class="col-6">
                <span>标签</span>
                <el-input minlength="1" maxlength="64" class="col-6" size="large" v-model="tags" placeholder="请输入标签" />
            </div>
            <div class="col-6">
                <span>标题</span>
                <el-input minlength="1" maxlength="50" class="col-6" size="large" v-model="title" placeholder="请输入标题" />
            </div>
        </div>

        <ContentBaseSecondary>
            <v-md-editor height=500px v-model="content"></v-md-editor>
        </ContentBaseSecondary>
        <br>
        <el-button @click="updateBlog" style="float:right" type="success" round>更新</el-button>

    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import { ref } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router'
import router from '@/router';
import $ from 'jquery';
import { ElMessage } from 'element-plus';
export default {
    name: 'BlogUpdateView',
    components: {
        ContentBase,
        ContentBaseSecondary,
    },
    setup() {
        let title = ref(''),tags= ref(''), content = ref();
        const store = useStore(), route = useRoute();
        if (!store.state.user.is_login) {
            router.push({ name: 'login' });
            return;
        }
        const getBlog = () => {
            $.ajax({
                url: store.state.net.ip + "/blog/content/",
                type: "GET",
                data: {
                    md: 1,
                    blog_id: parseInt(route.params.id),
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        res = res.data;
                        if (res.user_id != store.state.user.id) {
                            router.push({ name: '404' });
                        }
                        tags.value = res.tags;
                        title.value = res.title;
                        content.value = res.content;
                    }
                    else {
                        router.push({ name: '404' });
                    }
                },
                error() {
                    router.push({ name: '404' });
                }
            });
        }
        getBlog();
        const updateBlog = () => {
            $.ajax({
                url: store.state.net.ip + "/blog/operation/",
                type: "PUT",
                data: {
                    blog_id: parseInt(route.params.id),
                    title: title.value,
                    content: content.value,
                    tags:tags.value,
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        router.push({ name: 'blog', params: { id: 1 } });
                        ElMessage({
                            message: '修改成功',
                            grouping: true,
                            type: 'success',
                        })
                    }
                    else {
                        router.push({ name: '404' });
                    }
                },
                error() {
                    router.push({ name: '404' });
                }
            });
        }
        return {
            tags,
            title,
            content,
            updateBlog,
        }
    }

}

</script>

<style scoped>

</style>