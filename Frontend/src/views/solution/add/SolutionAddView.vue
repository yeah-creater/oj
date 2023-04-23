<template>
    <ContentBase>
        <div class="row">
            <div class="col-3">
                <el-select v-model="problem_id" placeholder="请选择题目" size="large">
                    <el-option v-for="item in data" :key="item.id" :label="item.label" :value="item.id" />
                </el-select>
            </div>
            <div class="col-9">
                <el-input minlength="1" maxlength="50" class="col-9" size="large" v-model="title" placeholder="请输入标题" />
            </div>
        </div>
        
        <ContentBaseSecondary>
            <v-md-editor height=500px v-model="content"></v-md-editor>
        </ContentBaseSecondary>
        <br>
        <el-button @click="submitSolution" style="float:right" type="success" round>提交</el-button>
       
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
    name: 'SolutionAddView',
    components: {
        ContentBase,
        ContentBaseSecondary,
    },
    setup() { 
        let title = ref(''),data=ref([]),problem_id=ref(''),content=ref();
        const store = useStore();
        if (!store.state.user.is_login) {
            router.push({ name: 'login' });
            return;
        }
        const getTitleList = () => {
            $.ajax({
                url: store.state.net.ip + "/problem/title/",
                type: "GET",
                data: {
                    type: 'all',
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        data.value = res.data;
                        for (let item of data.value) { 
                            item['label'] = item['id'] + '.' + item['title'];
                        }
                    }
                },
            });
        }
        getTitleList();
        const submitSolution = () => { 
            $.ajax({
                url: store.state.net.ip + "/solution/operation/",
                type: "POST",
                data: {
                    problem_id: parseInt(problem_id.value),
                    title:title.value,
                    content:content.value,
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        router.push({ name: 'solution', params: { id: 1 } });
                    }
                    else { 
                        alert(res.result);
                    }
                },
            });
        }
        return {
            problem_id,
            title,
            data,
            content,
            submitSolution,
        }
    }

}

</script>

<style scoped>

</style>