<template>
    <nav class="bg-dark navbar navbar-dark navbar-expand-lg" >
        <div class="container">
            <router-link class="text-light navbar-brand" :to="{ name: 'home' }">ZCOJ</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="text-light nav-link"  :to="{ name: 'home' }">首页</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link class="text-light nav-link" 
                            :to="{ name: 'problem' }">题库</router-link>
                    </li>
                <!-- <li class="nav-item dropdown">
                    <a :class="{ active:$route.name.indexOf('problem')==0 }" class="text-light nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                        aria-expanded="false">
                        题库
                    </a>
                    <ul class="text-light dropdown-menu">
                        <li>
                            <hr class="dropdown-divider">
                        </li>
                        <li><router-link class="dropdown-item" :to="{ name: 'problem_dashboard', params: {id:1} }">系统题库</router-link></li> -->
                        <!-- <li v-if="$store.state.user.is_login"><router-link class="dropdown-item" :to="{ name: 'problem_mine' }">个人题库</router-link></li>
                        <li>
                            <hr class="dropdown-divider">
                        </li> -->
                    <!-- </ul> -->
                <!-- </li> -->
                    <li class="nav-item">
                        <router-link  class="text-light nav-link" :to="{ name: 'contest', params: {id:1} }">竞赛</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="text-light nav-link" :to="{ name: 'app' }">应用</router-link>
                    </li>
                    <li class="nav-item dropdown">
                        <a  class="text-light nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                            aria-expanded="false">
                            其他
                        </a>
                        <ul class="text-light dropdown-menu">
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><router-link class="dropdown-item" :to="{ name: 'solution', params: {id:1} }">题解</router-link></li>
                            <li><router-link class="dropdown-item" :to="{ name: 'blog', params: { id: 1 } }">分享</router-link></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                        </ul>
                    </li>
                    
                </ul>
                
                <ul v-if="$store.state.user.is_login" class="navbar-nav me-right mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="text-light nav-link"  :to="{ name: 'user_mysapce_notification',params:{userId:$store.state.user.id} }">
                            <div>
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-bell" viewBox="0 0 16 16">
                                <path d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2zM8 1.918l-.797.161A4.002 4.002 0 0 0 4 6c0 .628-.134 2.197-.459 3.742-.16.767-.376 1.566-.663 2.258h10.244c-.287-.692-.502-1.49-.663-2.258C12.134 8.197 12 6.628 12 6a4.002 4.002 0 0 0-3.203-3.92L8 1.917zM14.22 12c.223.447.481.801.78 1H1c.299-.199.557-.553.78-1C2.68 10.2 3 6.88 3 6c0-2.42 1.72-4.44 4.005-4.901a1 1 0 1 1 1.99 0A5.002 5.002 0 0 1 13 6c0 .88.32 4.2 1.22 6z"></path>
                                </svg>
                                <span v-if="$store.state.user.notification_count > 0" class="unread" style="width: 10px;height: 10px; border-radius: 5px;background-color: #FF3B30; font-size: 6px;text-align: center;color: #fff;">{{$store.state.user.notification_count}}</span>
                            </div>
                        </router-link>
                    </li>
                    <li class="nav-item dropdown">
                    <a class="text-light nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                        aria-expanded="false">
                        <img style="border-radius: 50%;" class="img-circle" width="35" height="35" :src=$store.state.user.photo alt="图片不见了~~">
                    </a>
                    <ul class="text-light dropdown-menu">
                        <li>
                            <hr class="dropdown-divider">
                        </li>
                        <li><router-link class="dropdown-item" :to="{ name: 'user_myspace', params: { userId: $store.state.user.id }}"> 我的空间
                            </router-link>
                        </li>
                        <li><router-link class="dropdown-item" :to="{ name: 'user_setting'}"> 设置
                            </router-link>
                        </li>
                        <li><router-link v-if="$store.state.user.id===1" class="dropdown-item" :to="{ name: 'admin' } "> 管理员中心
                            </router-link>
                        </li>
                        <li>
                            <hr class="dropdown-divider">
                        </li>
                        <li><a class="dropdown-item" @click="logout">退出</a></li>
                    </ul>
                </li>
                </ul>
                <ul v-else class="navbar-nav me-right mb-2 mb-lg-0">
                    <li class="">
                        <router-link class="text-secondary nav-link" :to="{ name: 'login' }">登录</router-link>
                    </li>
                    <li class="">
                        <router-link class="text-secondary nav-link" :to="{ name: 'register' }">注册</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>
<script>
import ModuleUser from '../store/user.js';
import { useStore } from 'vuex';
import router from '@/router/index';

export default {
    name: 'NavBar',
    compeoents: {
        ModuleUser,
    },
    setup() {
        const store = useStore();
        
        const logout = () => {
            store.dispatch("logout");
            router.push({ name: 'home' });
        }

        return {
            logout
        }
    }
}

</script>
<style scoped>
.navbar{
    position: fixed !important;
    top: 0 !important;
    z-index: 999;
    width: 100%;
}
.navbar-brand{
    font-family: 'Satisfy',cursive;
    font-style: italic;
    font-size: 30px;
}
.nav-item{
    padding-right: 50px;
}
.nav-link:hover{
    color: darkgoldenrod!important;;
}
</style>