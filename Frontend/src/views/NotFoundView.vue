<template>
    <ContentBase>
        <div class="row" style="text-algin:center">
            <div class="col-md-4 col-md-offset-2 col-sm-5 col-sm-offset-1">
                <img src="https://cdn.acwing.com/static/web/img/404.jpg" alt="">
            </div>
            <div class="col-md-4 col-sm-5">
                <h2><strong>找不到页面</strong></h2>
                <p style="font-size: 25px">抱歉，我们找不到您想要的页面……</p>
                <router-link to="/"><button type="button" class="btn btn-light">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-house-fill"
                        viewBox="0 0 16 16">
                        <path
                            d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z">
                        </path>
                        <path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Z"></path>
                    </svg>
                    返回主页
                </button></router-link>
            </div>
        </div>

    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase.vue';

export default {
    name: 'NotFoundView',
    components: {
        ContentBase,
    }
}
</script>

<style scoped>

</style>
