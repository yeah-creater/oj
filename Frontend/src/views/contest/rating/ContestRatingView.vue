<template>
    <ContentBase>
        <TitleBase :title="title">
        </TitleBase>
        <hr>
        <div class="row justify-content-md-left">
             <div class="col-md-12 col-sm-12">
                    <MyspaceContestView></MyspaceContestView>
                </div>
            <div class="col-md-12 col-sm-12">
                <el-table size="large" empty-text="空空如也" :data="data" stripe>
                        <el-table-column  prop="standing" label="排名" width="auto" min-width="25%" />
                        <el-table-column  :formatter="formatter_user" prop="name" label="玩家" width="auto" min-width="45%" />
                        <el-table-column prop="rating" label="竞赛积分" width="auto" min-width="30%" />
                </el-table>
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase.vue';
import TitleBase from '@/components/TitleBase.vue';
import { reactive, ref} from 'vue';
import { useStore } from 'vuex';
import $ from 'jquery';
import MyspaceContestView from '@/views/user/myspace/MyspaceContestView.vue';
export default {
    name: 'ContestRatingView',
    components: {
        ContentBase,
        TitleBase,
        MyspaceContestView,
    },
    setup() { 
        let title = ref('积分排行榜'), data = ref([]);
        const store = useStore();
        
        const formatter_user = (row, column, value, index) => {
            let color = '#CCCCCC';
            let rating = data.value[index]['rating']
            if (rating < 1200) color = '#CCCCCC';
            else if (rating < 1400) color = '#77FF77';
            else if (rating < 1600) color = '#77DDBB';
            else if (rating < 1900) color = '#AAAAFF';
            else if (rating < 2100) color = '#FF88FF';
            else if (rating < 2300) color = '#FFCC88';
            else if (rating < 2400) color = '#FFBB55';
            else if (rating < 2600) color = '#FF7777';
            else if (rating < 3000) color = '#FF3333';
            else color = '#AA0000';
            const style = reactive({
                color: color,
            });
            let user_path = "/user/myspace/" + data.value[index]['id'] + "/";
            return <router-link  style="size:20px;color: #337ab7;text-decoration: none;" to={user_path}>
                <img style="border-radius:50%" width={30} src={data.value[index]['photo']} alt="~">
                </img>&nbsp;
                <span style={style}> {data.value[index]['name']}</span>
            </router-link>
        }
        const getContestRatings = () => {
            $.ajax({
                url: store.state.net.ip + "/contest/rating/",
                type: "GET",
                success(res) {
                    if (res.result === 'success') {
                        data.value = res.data;
                    }
                },
            });
        }
        getContestRatings();
        return {
            title,
            data,
            formatter_user,
        }
    }
}
</script>

<style scoped>

</style>
