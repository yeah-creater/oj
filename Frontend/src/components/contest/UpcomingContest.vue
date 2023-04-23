<template>
    <div>
        <div style="background-color: #F2F3F5;font-size: 1.4rem;"><strong>Current or upcoming contests</strong></div>
        <el-table size="large" empty-text="空空如也" :data="data" stripe style="width: 100%">
            <el-table-column :formatter="formatter_title" prop="name" label="名称" min-width="120px"/>
                <el-table-column :formatter="formatter_user" prop="user" label="作者" min-width="160px" />
                <el-table-column prop="start_time" label="开始时间" width="200px"  />
                <el-table-column prop="over_time" label="结束时间" width="200px"/>
                <!-- <el-table-column prop="participants" label="报名人数" /> -->
        </el-table>
    </div>
</template>

<script>
export default {
    name: 'UpcomingContest',
    props: {
        data: {
            type: Object,
            required:true,
        }
    },
    setup(props) { 
        const formatter_title = (row, column, value, index) => {
            let path = "/contest/content/" + props.data[index]['id'] + "/problem/";
            return <router-link style="text-decoration:none;color:#337ab7" to={path}>{value}</router-link>
        }
        const formatter_user = (row, column, value, index) => {
            let user_path = "/user/myspace/" + props.data[index]['user']['id'] + "/";
            return <router-link style="color: #337ab7;text-decoration: none;" to={user_path}>
                <img style="border-radius:50%" width={30} src={props.data[index]['user']['photo']} alt="~">
                </img>&nbsp;
                <span>{props.data[index]['user']['name']}</span>

            </router-link>
        }
        return {
            formatter_title,
            formatter_user,
        }
    }
}
</script>