<template>
    <div class="container">
        <div class="row" >
            <div class="col-md-7 col-sm-12" style="margin:auto">
                 <div class="input-group" >
                    <input  v-model="serach_content" maxlength="127" type="text" class="form-control" placeholder='输入内容，标题，标签，作者ID'>
                    <button @click="search" type="button" class="btn btn-outline-secondary">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search"
                            viewBox="0 0 16 16">
                            <path
                                d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z">
                            </path>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        <div  v-show="show" style="text-align:right">
            <button @click="addContent" type="button" class="btn btn-info btn-lg">{{operation}}</button>
        </div>
    </div>
</template>
<script>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
export default {
    name: 'SearchBase',
    props: {
        operation: {
            type: String,
            required: false,
        },
        show: {
            type: Boolean,
            required:true,
        }
    },
    setup(props, context) {
        let serach_content = ref('');
        const route = useRoute();
        if (String(route.name).search("search") != -1) { 
            serach_content.value = route.params.search;
        }
        const addContent = () => {
            context.emit("addContent");
        }
        const search = () => { 
            if (serach_content.value === '') {
                serach_content.value = ' ';
            }
            context.emit('search', serach_content.value);
        }
        return {
            serach_content,
            addContent,
            search,
        }
    }
}
</script>

<style>
.btn-info{
    border-radius: 5px;
    background-color: #66afe9;
    color: #fff;
}
</style>