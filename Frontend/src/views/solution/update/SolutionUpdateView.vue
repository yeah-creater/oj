<template>
    <ContentBase>
        <div class="row">
            <div class="col-3">
                <span>题目序号</span>
                <el-input readonly v-model="problem_id" size="large"></el-input>
            </div>
            <div class="col-9">
                <span>标题</span>
                <el-input minlength="1" maxlength="50" class="col-9" size="large" v-model="title" placeholder="请输入标题" />
            </div>
        </div>

        <ContentBaseSecondary>
            <v-md-editor height=500px v-model="content"></v-md-editor>
        </ContentBaseSecondary>
        <br>
        <el-button @click="updateSolution" style="float:right" type="success" round>更新</el-button>

    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import { ref } from 'vue';
import { useStore } from 'vuex';
import { useRoute} from 'vue-router'  
import router from '@/router';
import $ from 'jquery';
import { ElMessage } from 'element-plus';
export default {
    name: 'SolutionUpdateView',
    components: {
        ContentBase,
        ContentBaseSecondary,
    },
    setup() {
        let title = ref(''), problem_id = ref(''), content = ref();
        const store = useStore(), route = useRoute();
        if (!store.state.user.is_login) {
            router.push({ name: 'login' });
            return;
        }
        const getSolution = () => {
            $.ajax({
                url: store.state.net.ip + "/solution/content/",
                type: "GET",
                data: {
                    md:1,
                    solution_id: parseInt(route.params.id),
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
                        problem_id.value = res.problem;
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
        getSolution();
        const updateSolution = () => {
            $.ajax({
                url: store.state.net.ip + "/solution/operation/",
                type: "PUT",
                data: {
                    solution_id: parseInt(route.params.id),
                    title: title.value,
                    content: content.value,
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        router.push({ name: 'solution', params: { id: 1 } });
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
            problem_id,
            title,
            content,
            updateSolution,
        }
    }

}

</script>

<style scoped>

</style>