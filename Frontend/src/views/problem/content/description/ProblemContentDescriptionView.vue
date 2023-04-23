<template>
    <ContentBaseSecondary>
        <div class="row">
            <div class="col-sm-9 col-xs-12">
                <h4>题目描述</h4>
                <div v-html="problem_content.description"></div> 
                <h4>输入格式</h4>
                <div v-html="problem_content.input_format"></div>
                <h4>输出格式</h4>
                <div v-html="problem_content.output_format"></div>
                <h4>数据范围</h4>
                <div v-html="problem_content.data_range"></div>
                <h4>样例输入</h4>
                <div v-html="problem_content.input_example"></div>
                <h4>样例输出</h4>
                <div v-html="problem_content.output_example"></div>
            </div>
            <div class="col-sm-3 hidden-xs" style="padding-left: 0;top: -10px; margin-top: 10px;">
                <div class="table-responsive">
                    <table class="table table-striped table-responsive" style="border-left: 1px solid #f0f0f0;font-family: Helvetica Neue,Helvetica,Arial,sans-serif; font-size: 14px;">
                        <tbody>
                            <tr>
                                <td style="padding: 15px 8px 15px 8px;">
                                    难度：
                                    <el-tag style="float:right" class="ml-2" :type="tag">{{ problem_content.difficulty }}</el-tag>

                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 15px 8px 15px 8px;">
                                    时/空限制：
                                    <span style="float:right;">{{problem_content.time_limit+'s/'+problem_content.space_limit+'M' }}</span>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 15px 8px 15px 8px;">
                                    总通过数：
                                    <span style="float:right;">{{problem_content.ac_nums }}</span>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 15px 8px 15px 8px;">
                                    总尝试数：
                                    <span style="float: right;">{{problem_content.submit_nums }}</span>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 15px 8px 15px 8px;">
                                    来源：
                                    <span style="float: right;">{{problem_content.source}}</span>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding: 15px 8px 15px 8px;">
                                    <span class="problem-algorithm-tag" style="cursor: pointer">算法标签<span>
                                            <svg @click="showAlgoTag" xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                fill="currentColor" class="bi bi-caret-down-fill" viewBox="0 0 16 16">
                                                <path
                                                    d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z">
                                                </path>
                                            </svg>
                                        </span>
                                        <div v-show="showTag" class="problem-algorithm-tag-field" style="">
                                            <span  v-for="tag in problem_content.tags.split(/\s+/)" 
                                                :key="tag.id" class="problem-algorithm-tag-field-item">{{ tag }}</span>
                                        </div>
            
                                    </span>
                                </td>
            
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <hr>
        <AceEditor ref="editor_child" @judgeCode="judgeCode"></AceEditor>
    </ContentBaseSecondary>
</template>

<script>
import ContentBaseSecondary from '@/components/ContentBaseSecondary';
import AceEditor from '@/components/problem/content/AceEditor.vue';

import $ from 'jquery';
import { reactive, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import router from '@/router';
import { ElMessage } from 'element-plus'
export default {
    name: 'ProblemContentDescriptionView',
    components: {
        ContentBaseSecondary,
        AceEditor,
    },
    setup() {
        const route = useRoute();
        const store = useStore();
        let problem_content_id = parseInt(route.params.id);
        let showTag = ref(''), problem_content = reactive({});
        let tag = "success", debug_code_stdout_val = '';
        const editor_child = ref(null);
        showTag.value = false;

        const getProblemContent = () => {
            $.ajax({
                url: store.state.net.ip+"/problem/content/",
                type: "GET",
                async: false,
                data: {
                    user_id:store.state.user.id,
                    problem_content_id: problem_content_id,
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result !== 'success') {
                        problem_content = {
                            tags:'',
                        }
                        router.push({ name: '404' });
                        return;
                    }
                    else { 
                        problem_content = res.data;
                        if (problem_content['difficulty'] === '中等') tag = "warning";
                        else if (problem_content['difficulty'] === '困难') tag = "danger";
                    }
                   
                },
            });
        }
        getProblemContent();
        const showAlgoTag = () => {
            showTag.value = showTag.value ? false : true;
        }
        const judgeCode = (code,language,type,debug_code_input) => { 
            if (!store.state.user.is_login) { 
                router.push({ name: 'login' });
                return;
            }
            const info = {
                'user_id': store.state.user.id,
                'problem_content_id': problem_content_id,
                'problem_content_language': language,
                'problem_content_code': code,
                'code_judge_type': type,
                'debug_code_input':debug_code_input,
            }
            $.ajax({
                url: store.state.net.ip + "/problem/judge/",
                type: "POST",
                async:true,
                data: info,
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        res = JSON.parse(res.data);
                        if (type === 'debug') {
                            editor_child.value.changeDebugOutput(res['status'], res['result'], res['real_time']);
                        }
                        else {
                            editor_child.value.changeSubmitOutput(res['status']);
                        }
                    }
                    else { 
                        ElMessage({
                            message: '该题暂无测试数据',
                            grouping: true,
                            type: 'error',
                        })
                        router.push({ name: 'problem_dashboard' ,params:{id:1}});
                    }
                },
            });
        }
        
        return {
            tag,
            showTag,
            showAlgoTag,
            problem_content,
            judgeCode,
            debug_code_stdout_val,
            editor_child,
        }
    }

}

</script>

<style scoped>
.problem-algorithm-tag-field-item {
    margin-right: 5px;
    margin-bottom: 3px;
    color: #505050;
    font-size: 12px;
    padding: 2.5px 12px 2.5px 12px;
    background: #f4f4f4;
    border-radius: 15px;
    border: 1px solid #f4f4f4;
    cursor: pointer;
    display: inline-block;
}
h4{
    font-weight: bold;
    color:  #a0cfff;
    font-size: large;
}
</style>