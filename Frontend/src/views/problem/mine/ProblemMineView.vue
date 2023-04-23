<template>
    <contentBase>
        <TitleBase :title="title"></TitleBase>
        <SearchBase :show="show" @addContent="addContent" :operation="operation"></SearchBase>
        <hr>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import SearchBase from '@/components/SearchBase.vue';
import TitleBase from '@/components/TitleBase.vue';
export default {
    name: 'ProbleMineView',
    components: {
        ContentBase,
        SearchBase,
        TitleBase,
    },
    setup() {
        const title = "我的题目集", operation = "添加题目", show = false;
        return {
            title,
            operation,
            show,
        }
     }

}

</script>

<style scoped>

</style>