<template>
    <ContentBaseSecondary>
        <el-table size="large" empty-text="报名后查看" :data="data" stripe style="width: 100%">
            <el-table-column prop="num" label="#" width="auto" min-width="10%" />
            <el-table-column :formatter="formatter_title" prop="title" label="题目" width="auto" min-width="30%" />
            <el-table-column prop="ac_nums" label="通过次数" width="auto" min-width="25%" />
            <el-table-column prop="submit_nums" label="尝试次数" width="auto" min-width="25%" />
            <el-table-column :formatter="formatter_status" prop="status" label="状态" width="auto" min-width="10%" />
        </el-table>
    </ContentBaseSecondary>
</template>
<script>
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import { reactive} from 'vue';
import $ from 'jquery';
export default {
    name: 'ContestContentProblemView',
    components: {
        ContentBaseSecondary,
    },
    setup() {
        const route = useRoute(), store = useStore();
        let data = reactive([])
        const formatter_title = (row, column, value, index) => {
            let path = "/problem/content/" + data[index]['id'] +'/';
            return <router-link style="text-decoration:none;color:#337ab7" to={path}>{value}</router-link>
        }
        const formatter_status = (row, column, value) => {
            if (value === '通过') return <strong style="color:green">{value}</strong>
            return <strong style="color:red">{value}</strong>
        }
        const getContestProblems = () => { 
            $.ajax({
                url: store.state.net.ip + "/contest/problem/",
                type: "GET",
                data: {
                    contest_id: parseInt(route.params.id),
                },
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        data.splice(0, data.length);
                        res = res.data;
                        for (let i = 0; i < res.length; i++) { 
                            data.push(res[i]);
                            data[i]['num'] = i +1;
                        }
                    }
                },
            });
        }
        if (store.state.user.is_login) { 
            getContestProblems();
        }
        return {
            data,
            formatter_title,
            formatter_status,
        }
    }
}
</script>