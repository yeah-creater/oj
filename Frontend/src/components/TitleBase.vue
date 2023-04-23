<template>
    <div class="container">
        <div class="row" style="text-align:center">
          <h2><slot></slot>{{ title }}</h2>
        </div>
    </div>
</template>
<script>
export default {
    name: 'TitleBase',
    props: {
        title: {
            type: String,
            required: true,
        },
    },
    
}
</script>