<template>
    <div class="container-md">
        <div class="card">
            <div class="card-body">
                <slot></slot>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'ContentBase',
}
</script>

<style scoped>
.container-md {
    margin-top: 100px;
    margin-bottom:100px;
    padding: 0;
}

</style>
