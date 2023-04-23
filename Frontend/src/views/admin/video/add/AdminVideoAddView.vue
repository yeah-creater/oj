<template>
    <ContentBase>
        <TitleBase :title="title"></TitleBase>
        <FileUpload :upload_path="upload_path"/>
        <hr>

    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import TitleBase from '@/components/TitleBase.vue';
import FileUpload from '@/components/FileUpload.vue';
import { useStore } from 'vuex';
export default {
    name: 'AdminVideoAddView',
    components: {
        ContentBase,
        TitleBase,
        FileUpload
    },
    setup() {
        const store = useStore();
        let title = "添加视频",upload_path=store.state.net.ip+'/video/upload_video/';
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