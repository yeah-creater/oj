<template>
    <ContentBase>
        <div class="row">
            <div class="col-lg-3 col-md-12">
                <ContentBaseSecondary>
                    <div>
                        <img style="width: 100%; height: auto;" :src=$store.state.user.photo alt="">
                    </div>
                    <hr>
                    <div style="text-align: center;">
                        <UploadImg />
                    </div>
                    
                </ContentBaseSecondary>
                
            </div>
            <div class="col-lg-9 col-md-12">
                <ContentBaseSecondary>
                    <h3>个人资料</h3>
                    <hr>
                    <el-form @submit.prevent="onSubmit" ref="form" :model="sizeForm" :label-position="labelPosition">
                        <el-form-item label="昵称">
                            <el-input maxlength="16" v-model="sizeForm.name" required=true />
                        </el-form-item>
                        <el-form-item label="学号">
                                <el-input maxlength="16" v-model="sizeForm.sno" />
                            </el-form-item>
                        <el-form-item label="性别">
                            <el-select v-model="sizeForm.gender" placeholder="请选择你的性别">
                                <el-option label="男" value="male" />
                                <el-option label="女" value="female" />
                            </el-select>
                        </el-form-item>
                        <el-form-item label="注册日期">
                            <el-col :span="11">
                                <el-date-picker readonly v-model="sizeForm.birthday" type="date" label="生日" placeholder=""
                                    style="width: 100%" />
                            </el-col>

                        </el-form-item>
                        <el-form-item label="个性签名">
                            <el-input maxlength="16" v-model="sizeForm.record" type="textarea"/>
                        </el-form-item>
                        <el-form-item >
                            <el-button type="success" @click="onSubmit">提交</el-button>
                        </el-form-item>
                    </el-form>
                </ContentBaseSecondary>
                <ContentBaseSecondary>
                    <h3>账号安全</h3>
                    <hr>
                    <div class="row">
                        <div class="col-10">密码</div>
                        <div class="col-2">
                            <router-link style="color: #337ab7;text-decoration: none;" :to="{ name: 'user_setting_account' }" >修改密码
                            </router-link>
                        </div>
                    </div>
                </ContentBaseSecondary>
            </div>
        </div>
       
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import { useStore } from 'vuex';
import router from '@/router';
import UploadImg from '@/components/user/UploadImg.vue'
import { reactive, ref } from 'vue'
import $ from 'jquery';
import { ElMessage } from 'element-plus';
export default {
    name: 'SettingView',
    components: {
        ContentBase,
        ContentBaseSecondary,
        UploadImg,
    },
    setup() { 
        const store = useStore();
        if (!store.state.user.is_login) { 
            router.push({ name: '404' });
            return;
        }

        const size = ref('large')
        const labelPosition = ref('top')

        const sizeForm = reactive({
            name: store.state.user.name,
            sno:store.state.user.sno,
            gender: store.state.user.gender,
            birthday: store.state.user.birthday,
            record:store.state.user.record,
        })
        const onSubmit = () => { 
            $.ajax({
                url: store.state.net.ip +"/settings/getinfo/",
                type: "POST",
                async: false,
                data: {
                    name: sizeForm.name,
                    sno:sizeForm.sno,
                    gender: sizeForm.gender,
                    birthday: sizeForm.birthday,
                    record:sizeForm.record,
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        store.state.user.name = sizeForm.name;
                        store.state.user.gender = sizeForm.gender;
                        store.state.user.record = sizeForm.record;
                        ElMessage({
                            message: '修改成功',
                            grouping: true,
                            type: 'success',
                        })
                    }
                    else { 
                        ElMessage({
                            message: res.result,
                            grouping: true,
                            type: 'warning',
                        })
                    }
                },
                error() { 
                    ElMessage({
                        message: '系统错误',
                        grouping: true,
                        type: 'error',
                    })
                }
            });
        }
        return {
            size,
            labelPosition,
            sizeForm,
            onSubmit,
        }
    }

}

</script>

<style scoped>
h3{
    font-size: 24px;
    margin-bottom: 10px;
    margin-top:10px;
}
</style>