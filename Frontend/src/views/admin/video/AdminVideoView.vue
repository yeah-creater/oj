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
    name: 'AdminVideoView',
    components: {
        ContentBase,
        SearchBase,
    },
    setup() {
        let operation = "添加视频题解", show = true;
        const addContent = () => {
            router.push({ name: 'admin_video_add' });
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