<template>
    <ContentBase>
        <div class="container text-center">
            <div class="row align-items-center">
                <h3 style="color:#303133">核心板块</h3>
                <div class="col-md-6 col-sm-12 manage_item">
                    <router-link :to="{name:'admin_problem'}">
                        <ContentBaseSecondary>
                            测试数据
                        </ContentBaseSecondary>
                    </router-link>
                </div>
                <div class="col-md-6 col-sm-12 manage_item">
                    <router-link :to="{name:'admin_video'}">
                        <ContentBaseSecondary>
                            视频题解
                        </ContentBaseSecondary>
                    </router-link>
                </div>
                <el-divider>
                ***
                </el-divider>
                 <el-button type="success" plain>
                    <a href="https://app2105.acapp.acwing.com.cn/admin/">进入后台</a>
                 </el-button>
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import ContentBaseSecondary from '@/components/ContentBaseSecondary';
export default {
    name: 'AdminView',
    components: {
        ContentBase,
        ContentBaseSecondary,
    },

}

</script>

<style scoped>

.manage_item :hover{
    cursor: pointer;
    transform: scale(1.05);
    transition: 100ms;
    box-shadow: 2px 3px 5px lightgray;
}
</style>