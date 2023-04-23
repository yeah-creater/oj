<template>
    <ContentBase>
        <div class="row">
            <div class="col-6">
                <el-input minlength="1" maxlength="50" class="col-6" size="large" v-model="tags" placeholder="请输入标签" />
            </div>
            <div class="col-6">
                <el-input minlength="1" maxlength="50" class="col-6" size="large" v-model="title" placeholder="请输入标题" />
            </div>
        </div>

        <ContentBaseSecondary>
            <v-md-editor height=500px v-model="content"></v-md-editor>
        </ContentBaseSecondary>
        <br>
        <el-button @click="submitBlog" style="float:right" type="success" round>提交</el-button>

    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router';
import $ from 'jquery';
export default {
    name: 'BlogAddView',
    components: {
        ContentBase,
        ContentBaseSecondary,
    },
    setup() {
        let title = ref(''),tags=ref(''), content = ref();
        const store = useStore();
        if (!store.state.user.is_login) {
            router.push({ name: 'login' });
            return;
        }
        const submitBlog = () => {
            $.ajax({
                url: store.state.net.ip + "/blog/operation/",
                type: "POST",
                data: {
                    title: title.value,
                    tags:tags.value,
                    content: content.value,
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        router.push({ name: 'blog', params: { id: 1 } });
                    }
                    else {
                        alert(res.result);
                    }
                },
            });
        }
        return {
            title,
            tags,
            content,
            submitBlog,
        }
    }

}

</script>

<style scoped>

</style>