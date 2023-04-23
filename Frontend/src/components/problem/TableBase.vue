<template>
    
    <el-table  :data="data" border stripe style="width: 100%">
        <el-table-column prop="id" label="#" width="auto" min-width="15%" />
        <el-table-column :formatter="formatter" prop="title" label="标题" width="auto" min-width="60%" />
        <!-- <el-table-column prop="passing_rate" label="通过率" width="300"/> -->
        <el-table-column :formatter="beautify" prop="difficulty" label="难度" width="auto" min-width="25%" />
    </el-table>
</template>

<script>

export default {
    name: 'TableBase',
    props: {
        data: {
            type: Object,
            required:true,
        }
    },
    setup(props) { 
       
        const formatter = (row, column, value, index) => { 
            
            let path = "/problem/content/" + props.data[index]['id']+"/";
            return <router-link style="text-decoration:none;color:#337ab7" to={ path }>{ value}</router-link>
        }
        const beautify = (row, column, value) => {
            if (value === '简单') return <el-tag class="ml-2" type="success">简单</el-tag>
            else if (value === '中等') return <el-tag class="ml-2" type="warning">中等</el-tag>
            else if (value === '困难') return <el-tag class="ml-2" type="danger">困难</el-tag>
        }
        return {
            formatter,
            beautify,
        }
    }
    
   
}

</script>