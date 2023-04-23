<template>
    <ContentBase>
        <TitleBase :title="title"></TitleBase>
        <FileUpload :upload_path="upload_path" />
        <hr>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import TitleBase from '@/components/TitleBase.vue';
import FileUpload from '@/components/FileUpload.vue';
import { useStore } from 'vuex';
export default {
    name: 'AdminProblemAddView',
    components: {
        ContentBase,
        TitleBase,
        FileUpload
    },
    setup() {
        const store = useStore();
        let title = "添加测试数据", upload_path = store.state.net.ip + '/problem/upload_test_case/';
        return {
            title,
            upload_path,
        }
    }

}

</script>

<style scoped>
.item {
    margin: 6px 0 6px 0;
    color: gray;
    font-weight: bold;
}
</style>