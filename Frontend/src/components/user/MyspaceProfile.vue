<template>
    <div>
        <ContentBaseSecondary>
            <div style="margin:auto">
                <img style="width: 100%; height: auto;" :src=data.photo alt="">
            </div>
            <p style="margin: 8px; font-size: 1.25rem; font-weight: 700; text-align: center;">
                {{ data.name }}
            </p>
        </ContentBaseSecondary>
        <ContentBaseSecondary>
            <div class="row" style="text-align: center;">
                <div class="col-5 col-xs-5 user-info-item">
                    <router-link :to="{name:'user_mysapce_following'}" style="text-decoration: none;color: #99A2A9;">
                        <div>关注数</div>
                        <div class="user-info-item-value">{{ data.followings }}</div>
                    </router-link>
                </div>
                <div class="col-2 col-xs-5">
                    <div>|</div>
                </div>
                
                <div class="col-5 col-xs-5 user-info-item">
                    <router-link :to="{name:'user_mysapce_follower'}" style="text-decoration: none;color: #99A2A9;">
                        <div>粉丝数</div>
                        <div class="user-info-item-value">{{ data.followers }}</div>
                    </router-link>
                </div>
            </div>
            <div style="float:right;margin:5px">
                <div style="text-align: center;">
                    <el-icon>
                        <Location />
                    </el-icon>
                </div>
                <div class="address" style="color: rgb(147, 147, 147); font-size: 13px;">{{data.address}}</div>
             </div>
           

        </ContentBaseSecondary>
        <ContentBaseSecondary v-if="$store.state.user.is_login">
            <div v-if="!data.is_me" class="row" style="text-align: center;">
                <div class="col-6">
                    <button @click="chat" style="width:100%" type="button" class="btn btn-light">
                        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor"
                            class="bi bi-envelope" viewBox="0 0 16 16">
                            <path
                                d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z">
                            </path>
                        </svg>
                        <span style="font-size:13px">私信</span>
                    </button>
                </div>
                <div class="col-6">
                    <button @click="follow" v-if="!data.is_follow" style="width:100%" type="button" class="btn btn-success">
                        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor"
                            class="bi bi-plus-square" viewBox="0 0 16 16">
                            <path
                                d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z" />
                            <path
                                d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z" />
                        </svg>
                        <span style="font-size:13px">关注</span>
                    </button>
                    <button @click="unfollow" v-else style="width:100%" type="button" class="btn btn-secondary">
                        <span style="font-size:13px">取消关注</span>
                    </button>
                </div>
            </div>
            <div v-else class="row" style="text-align: center;">
                <router-link :to="{ name: 'user_setting', params: { userId: data.id } }"
                    style="text-decoration: none; color:rgb(45 181 93)">编辑资料</router-link>
            </div>
        </ContentBaseSecondary>
    </div>
</template>



<script>
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue'
import { Location }  from '@element-plus/icons-vue';
export default {
    name: 'MySpaceProfile',
    components: {
        ContentBaseSecondary,
        Location,
    },
    props: {
        data: {
            type: Object,
            require:true,
        }
    },
    setup(props, context) { 
        const follow = () => { 
            context.emit("follow");
        }
        const unfollow = () => { 
            context.emit("unfollow");
        }
        const chat = () => { 
            context.emit("chat");
        }
        return {
            follow,
            unfollow,
            chat,
        }
    }
    
}
</script>

<style scoped>
.user-info-item {
    color: #99A2A9;
    font-size: 13px;
    cursor: pointer;
}

.user-info-item-value {
    font-size: 10px;
    color: black;
}

.user-info-item-value:hover {
    color: #337ab7 !important;
}

.user-info-item:hover {
    color: #337ab7 !important;
}
</style>