<template>
    <ContentBase>
        <div>
            <div class="nice_font problem-content-title">
                {{ title }}
            </div>
            <el-tabs type="border-card" >
                <el-tab-pane label="题目">
                    <ProblemContentDescriptionView>
                    </ProblemContentDescriptionView>
                </el-tab-pane>
                <el-tab-pane  label="提交记录" v-if="$store.state.user.is_login">
                    <ProblemContentRecordView>

                    </ProblemContentRecordView>
                </el-tab-pane>
                <el-tab-pane  label="题解">
                    <ProblemContentSolutionView />
                </el-tab-pane>
                <el-tab-pane  label="视频题解">
                    <ProblemContentVideoView />
                </el-tab-pane>
            </el-tabs>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';
import {  ref } from 'vue';
import ProblemContentDescriptionView from '@/views/problem/content/description/ProblemContentDescriptionView.vue';
import ProblemContentRecordView from '@/views/problem/content/record/ProblemContentRecordView.vue';
import ProblemContentSolutionView from '@/views/problem/content/solution/ProblemContentSolutionView.vue';
import ProblemContentVideoView from '@/views/problem/content/video/ProblemContentVideoView.vue';

export default {
    name: 'ProblemContentView',
    components: {
        ContentBase,
        ProblemContentDescriptionView,
        ProblemContentRecordView,
        ProblemContentSolutionView,
        ProblemContentVideoView,
    },
    
    setup() { 
        const route = useRoute(),store=useStore();
        const problem_content_id = parseInt(route.params.id);
        let title = ref('');
        const getProblemContent = () => { 
            $.ajax({
                url: store.state.net.ip+"/problem/title/",
                type: "GET",
                data: {
                    problem_id: problem_content_id,
                    type:'one',
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        res = res.data;
                        title.value = res.id + '.' + res.title;
                    }
                },
            });
        }
        getProblemContent();
    return {
        title,
    }
    }

}

</script>

<style scoped>
.problem-content-title {
    font-size: 28px;
    margin: 10px 0 8px 0;
    font-weight: 300;
}

.nice_font {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

</style>