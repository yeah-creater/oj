<template>
  <ContentBase>
    <div class="row justify-content-md-center">
      <div class="col-lg-6 col-md-10 col-sm-12"   >
       <ContentBaseSecondary>
          <form @submit.prevent="login">
            <div class="mb-3">
              <label for="username" class="form-label">用户名或QQ邮箱</label>
              <input required v-model="username" type="text" class="form-control" id="username">
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">密码</label>
              <input required v-model="password" type="password" class="form-control" id="password">
            </div>
            <div class="mb-3">
              <div class="form-group">
                <label for="id_code">图片验证码</label>
                <div class="row">
                  <div class="col-7">
                    <input required v-model="code" type="text" class="form-control" placeholder="请输入图片验证码">
                  </div>
                  <div class="col-5">
                    <img :src="img" @click="getImageCode" alt="~~~">
                  </div>
                </div>
              </div>
            </div>
            <div class="error-message">{{ error_message }}</div>
            <button type="submit" class="btn btn-primary">登录</button>
          </form>
       </ContentBaseSecondary>
      </div>
    </div>
  </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase'
import ContentBaseSecondary from '../components/ContentBaseSecondary'
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router/index';
import { ElMessage } from 'element-plus'
import $ from "jquery";


export default {
  name: 'LoginView',
  components: {
    ContentBase,
      ContentBaseSecondary,
  },
  
  setup() {
    const store = useStore();
    let username = ref('');
    let password = ref('');
    let code = ref(""), error_message = ref(""), img = ref(''), uuid = ref('');
    const getImageCode = () => {
      $.ajax({
        url: store.state.net.ip + "/settings/image_code/",
        type: "GET",
        success(res) {
          if (res.result === 'success') {
            img.value = 'data:image/jpg;base64,' + res.img;
            uuid.value = res.uuid;
          }
        },
        error() {
          ElMessage({
            message: '请求太快,慢一点',
            grouping: true,
            type: 'error',
          })
        },
      });
    }
    const login = () => {
      error_message.value = "";
      store.dispatch("login", {
        username: username.value,
        password: password.value,
        code: code.value,
        uuid:uuid.value,
        success() {
          router.push({ name: 'home' });
          ElMessage({
            message: '登录成功',
            grouping: true,
            type: 'success',
          })
        },
        error() {
          error_message.value = "验证码或用户名或密码错误";
        }
      });
    };
    getImageCode();

    return {
      username,
      password,
      error_message,
      code,
      img,
      uuid,
      login,
      getImageCode,
    }
  },

    

}
</script>

<style scoped>
button {
  width: 100%;
}

.error-message {
  color: red;
}
</style>