<template>
    <ContentBase>
        <SearchBase :show="show" @addContent="addContent" :operation="operation"></SearchBase>
       
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import SearchBase from '@/components/SearchBase.vue';
import router from '@/router';
export default {
    name: 'AdminContestView',
    components: {
        ContentBase,
        SearchBase,
    },
    setup() {
        let operation = "添加竞赛",show=true;
        const addContent = () => {
            router.push({ name: 'admin_contest_add' });
        }
        return {
            operation,
            show,
            addContent,
        }
    }

}

</script>

<style scoped>

</style>