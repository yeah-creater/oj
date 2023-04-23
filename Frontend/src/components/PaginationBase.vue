<template>
    <el-pagination style="float:right"
     :current-page="current_page"
     @current-change="current_change"
    background layout="prev, pager, next" :total="total" class="mt-4" />
</template>

<script>

export default {
    name: 'PaginationBase',
    props: {
        current_page: {
            type: Number,
            required:true,
        },
        total: {
            type: Number,
            required: true,
        }
    },
    setup(props,context) { 
        const current_change=(val) => { 
            context.emit("current_change", val);
        }
        return {
            current_change,
        }
    }
}
</script>