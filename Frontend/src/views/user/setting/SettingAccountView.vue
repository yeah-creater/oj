<template>
    <ContentBase>
        <div class="justify-content-md-center row">
            <div class="col-lg-6 col-md-10 col-sm-12" >
                <ContentBaseSecondary>
                    <form @submit.prevent="changePassword">
                        <div class="mb-3">
                            <label  class="form-label">原始密码</label>
                            <input required type="password" v-model="row_password" class="form-control" />
                        </div>
                        <div class="mb-3">
                            <label  class="form-label">新密码</label>
                            <input required v-model="password" type="password" class="form-control" />
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">确认密码</label>
                            <input required v-model="password_confirm" type="password" class="form-control" />
                        </div>
                        <div v-if="error_msg" class="error-msg">{{ error_msg }}</div>

                        <button style="width:100%" type="submit" class="btn btn-primary">提交</button>
                    
                    </form>
                </ContentBaseSecondary>
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import { useStore } from 'vuex';
import router from '@/router'
import { ref } from 'vue';
import $ from 'jquery';
import { ElMessage } from 'element-plus';
export default {
    name: 'SettingAccountView',
    components: {
        ContentBase,
        ContentBaseSecondary,
    },
    setup() { 
        const store = useStore();
        if (!store.state.user.is_login) {
            router.push({ name: '404' });
            return;
        }
        let row_password = ref(''), password = ref(''), password_confirm = ref();
        let error_msg = ref('');
        const changePassword = () => { 
            $.ajax({
                url: store.state.net.ip+"/settings/change_password/",
                type: "POST",
                data: {
                    row_password: row_password.value,
                    password: password.value,
                    password_confirm:password_confirm.value,
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        router.push({ name: 'home' });
                        ElMessage({
                            message: '修改成功',
                            grouping: true,
                            type: 'success',
                        })
                    }
                    else {
                        error_msg.value = res.result;
                    }
                },
            });
        }
        return {
            row_password,
            password,
            password_confirm,
            error_msg,
            changePassword,
        }

    }

}

</script>

<style scoped>
.error-msg {
    margin: -5px 0 10px;
    color: red;
}
</style>