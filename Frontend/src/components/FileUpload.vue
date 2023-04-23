<template>
    <div >
        <div class="row">
            <div class=" item col-12">
                <el-select v-model="problem_id" placeholder="请选择题目" size="large">
                    <el-option v-for="item in titles" :key="item.id" :label="item.label" :value="item.id" />
                </el-select>
            </div>
        </div>
        <br>
        <el-upload ref="uploadRef" class="upload-demo" :action=upload_path
            :data="data"
            :auto-upload="false" drag :multiple=true
            :on-success="uploadSuccess"
            :headers=headers>
            <el-icon class="el-icon--upload">
                <UploadFilled style="width:60px" />
            </el-icon>
            <div class="el-upload__text">
                <em>视频/测试样例</em>
            </div>
            <template #tip>
                <div class="el-upload__tip">
                    视频支持.mp4 压缩包支持.in .out
                </div>
            </template>
        
        </el-upload>
        <div @click="submitUpload" class="d-grid gap-2 col-6 mx-auto">
            <button class="btn btn-primary" type="button">提交</button>
        </div>
    </div>
    
</template>
<script >
import { UploadFilled } from '@element-plus/icons-vue'
import { reactive, ref } from 'vue'
import { useStore } from 'vuex'
import $ from 'jquery'
export default {
    name: 'FileUpload',
    components: {
        UploadFilled,
    },
    props: {
        upload_path: {
            type: String,
            required:true,
        }
    },
    setup() { 
        let uploadRef = ref(), data = ({ problem_id: '' });
        let problem_id = ref(''),titles=ref([]);
        const headers = reactive({
            Authorization: "Bearer " + localStorage.getItem('access'),
        })
        const store = useStore();
        const getTitleList = () => {
            $.ajax({
                url: store.state.net.ip + "/problem/title/",
                type: "GET",
                async:false,
                data: {
                    type: 'all',
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        titles.value = res.data;
                        for (let item of titles.value) {
                            item['label'] = item['id'] + '.' + item['title'];
                        }
                    }
                },
            });
        }
        getTitleList();
        const submitUpload = () => { 
            if (problem_id.value == '') {
                alert('输入题目ID')
            }
            else {
                data['problem_id'] = problem_id.value;
                uploadRef.value.submit();
            }
        }
        const uploadSuccess = () => { 
            alert('上传成功')
        }
        return {
            uploadRef,
            headers,
            data,
            problem_id,
            titles,
            submitUpload,
            uploadSuccess,
        }
    }
}

</script>
<style scoped>

</style>
