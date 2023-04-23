<template>
    <ContentBase>
        <div class="row justify-content-md-center">
            <div class="col-lg-6 col-md-10 col-sm-12">
                <ContentBaseSecondary>
                        <form @submit.prevent="register">
                            <div class="mb-3">
                                <label for="username" class="form-label">用户名或QQ邮箱</label>
                                <input required v-model="username" class="form-control" />
                            </div>
                            <div class="mb-3">
                                <label for="password" class="form-label">密码</label>
                                <input required v-model="password" type="password" class="form-control" />
                            </div>
                            <div class="mb-3">
                                <label for="password" class="form-label">确认密码</label>
                                <input required v-model="password_confirm" type="password" class="form-control" />
                            </div>
                            <div class="mb-3">
                                <div class="form-group">
                                    <label for="id_code">邮箱验证码</label>
                                    <div class="row">
                                        <div class="col-6">
                                            <input required v-model="code" type="text" class="form-control" placeholder="请输入6位验证码">
                                        </div>
                                        <div class="col-6">
                                            <button class="btn btn-light" @click="sendEmail" :disabled="send_email">获取验证码</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div v-if="error_msg" class="error-msg">{{ error_msg }}</div>
                            <button type="submit" class="btn btn-primary">注册</button>
                        </form>
                </ContentBaseSecondary>
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from "../components/ContentBase.vue";
import ContentBaseSecondary from "@/components/ContentBaseSecondary.vue";

import { ref } from "vue";
import { useStore } from "vuex";
import router from "@/router/index";
import $ from "jquery";
import { ElMessage } from 'element-plus'

export default {
    setup() {
        const store = useStore();

        let username = ref(""), password = ref(""), password_confirm = ref("");
        let code = ref(""), error_msg = ref(""),send_email=ref(false);
        const sendEmail = () => { 
            if (username.value.trim().length === 0) { 
                ElMessage({
                    message: '请输入邮箱',
                    grouping: true,
                    type: 'error',
                });
                return;
            }
            send_email.value = true;
            $.ajax({
                url: store.state.net.ip + "/settings/send_email/",
                type: "GET",
                data: {
                    username: username.value,
                },
                success(res) {
                    if (res.result === 'success') {
                        ElMessage({
                            message: '发送成功',
                            grouping: true,
                            type: 'success',
                        });
                        setTimeout(() => {
                            send_email.value = false;
                        }, 1000 * 10)
                    }
                    else {
                        ElMessage({
                            message: res.result,
                            grouping: true,
                            type: 'error',
                        });
                        setTimeout(() => {
                            send_email.value = false;
                        }, 1000 * 10)
                     }
                },
                error() {
                    error_msg.value = "系统错误，请稍后重试";
                },
            });
        }
        const register = () => {
            $.ajax({
                url: store.state.net.ip +"/settings/register/",
                type: "POST",
                data: {
                    username: username.value,
                    password: password.value,
                    password_confirm: password_confirm.value,
                    code: code.value,
                },
                success(res) {
                    if (res.result === "success") {
                        store.dispatch("login", {
                            username: username.value,
                            password: password.value,
                            uuid: res.uuid,
                            code:res.code,
                            success() {
                                router.push({ name: "home" });
                                ElMessage({
                                    message: '注册成功',
                                    grouping: true,
                                    type: 'success',
                                })
                            },
                            error() {
                                error_msg.value = "系统错误，请稍后重试";
                            },
                        });
                    } else {
                        error_msg.value = res.result;
                        password.value = "";
                        password_confirm.value = "";
                    }
                },
            });
        };
        return {
            username,
            password,
            error_msg,
            password_confirm,
            code,
            send_email,
            register,
            sendEmail,

        };
    },
    components: {
    ContentBase,
    ContentBaseSecondary
},
};
</script>

<style scoped>
button {
    width: 100%;
}

.error-msg {
    margin: -5px 0 10px;
    color: red;
}
</style>
