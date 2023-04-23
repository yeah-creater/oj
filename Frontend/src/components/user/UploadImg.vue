<template>
    <div style="margin: auto;">
        <el-button round @click="dialogVisible2 = true">上传头像</el-button>
        <el-dialog title="上传头像(仅支持jpg)" v-model="dialogVisible2" width="30%">
            <el-form :model="form">
                <el-form-item :label-width="formLabelWidth" ref="uploadElement">
                    <el-upload :auto-upload="false" ref="upload" :action=path accept="image/png,image/gif,image/jpg,image/jpeg"
                        list-type="picture-card" :limit=limitNum  :on-exceed="handleExceed"
                        :before-upload="handleBeforeUpload" :on-preview="handlePictureCardPreview"
                        :on-remove="handleRemove" :on-change="imgChange" :on-success="uploadSuccess" :on-error="uploadError" :class="{ hide: hideUpload }" :headers="headers">
                        <el-icon>
                            <Plus />
                        </el-icon>
                    </el-upload>
                    <el-dialog v-model="dialogVisible">
                        <img width="100%" :src="dialogImageUrl" alt="">
                    </el-dialog>
                </el-form-item>
                <el-form-item>
                    <el-button size="small" type="primary" @click="uploadFile">立即上传</el-button>
                    <el-button size="small" @click="tocancel">取消</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>
    </div>

</template>
 
<script>

import { Plus } from '@element-plus/icons-vue'
import { ref } from 'vue';
import router from '@/router';
import { useStore } from 'vuex';
import { ElMessage } from 'element-plus';
export default {
    name: 'UploadImg',
    components: {
        Plus,
    },
    
    data() {
        return {
            hideUpload: false,
            dialogImageUrl: '',
            dialogVisible: false,//图片预览弹窗
            formLabelWidth: '80px',
            limitNum: 1,
            form: {},
            dialogVisible2: false,//弹窗
            headers: {
                Authorization: "Bearer " + localStorage.getItem('access'),
            },
        }
    },
    setup() { 
        const store = useStore();
        const path = store.state.net.ip+'/user/profile/';
        let upload = ref();
        const uploadFile = () => {
            upload.value.submit();
        }
        const uploadSuccess = (res) => { 
            if (res.result === 'success') {
                store.state.user.photo = res.data;
                router.push({ name: 'user_myspace', params: { userId: store.state.user.id } });
                ElMessage({
                    message: '修改成功',
                    grouping: true,
                    type: 'success',
                })
            }
            
        }
        const uploadError= () => {
                ElMessage({
                    message: '系统错误，请稍后重试',
                    grouping: true,
                    type: 'error',
                })
        }
        
        return {
            upload,
            uploadFile,
            uploadSuccess,
            uploadError,
            path
        }
    },
    methods: {
        // 上传文件之前的钩子
        handleBeforeUpload(file){
            if (!(file.type === 'image/png' || file.type === 'image/gif' || file.type === 'image/jpg' || file.type === 'image/jpeg')) {
                this.$notify.warning({
                    title: '警告',
                    message: '请上传格式为image/png, image/gif, image/jpg, image/jpeg的图片'
                })
                return false;
            }
            let size = file.size
            if (size > 100 * 1024) {
                this.$notify.warning({
                    title: '警告',
                    message: '图片大小必须小于100KB'
                })
                return false;
            }
            return true;
        },
        // 文件超出个数限制时的钩子
        handleExceed() {
            this.$notify.warning({
                title: '警告',
                message: 'only one'
            })
        },
        // 文件列表移除文件时的钩子
        handleRemove(file, fileList) {
            this.hideUpload = fileList.length >= this.limitNum;

        },
        // 点击文件列表中已上传的文件时的钩子
        handlePictureCardPreview(file) {
            this.dialogImageUrl = file.url;
            this.dialogVisible = true;
        },
        
        imgChange(files, fileList) {
            this.hideUpload = fileList.length >= this.limitNum;
            if (fileList) {
                this.$refs.uploadElement.clearValidate();
            }
        },
        tocancel() {
            this.dialogVisible2 = false

        }
    }
}
</script>
 
<style >
.hide .el-upload--picture-card {
    display: none;
}
</style>