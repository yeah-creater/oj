<template>
    <ContentBaseSecondary>
        <u-fold unfold line="1">
            <p>
               {{data.record }}
            </p>
        </u-fold>
        <hr>
    </ContentBaseSecondary>
</template>
<script>
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import router from '@/router';
import $ from 'jquery';
import { ref } from 'vue';
export default {
    name: 'MyspaceRecordView',
    components: {
        ContentBaseSecondary,
    },
    setup() {
        const store = useStore();
        const route = useRoute();

        let data = ref({
        })
        const getUserInfo = () => {
            $.ajax({
                url: store.state.net.ip + "/user/user_info/",
                type: "GET",
                async: false,
                data: {
                    user_id: parseInt(store.state.user.id),
                    visit_id: parseInt(route.params.userId)
                },
                // headers: {
                //     Authorization: "Bearer " + localStorage.getItem('access'),
                // },
                success(res) {
                    if (res.result === 'success') {
                        res = res.data;
                        data.value = res;
                    }
                    else {
                        router.push({ name: '404' });
                    }
                },

            });
        }
        getUserInfo();
        return {
            data,
        }
    }
}
</script>