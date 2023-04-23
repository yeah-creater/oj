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
    name: 'AdminProblemView',
    components: {
        ContentBase,
        SearchBase,
    },
    setup() {
        let operation = "添加测试数据",show=true;
        const addContent = () => {
            router.push({ name: 'admin_problem_add' });
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