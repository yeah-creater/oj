<template>
  <div class="container">
    <div class="card" style="padding: 0">
      <div class="card-body">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ContentBaseSecondary",
};
</script>

<style scoped>
.container {
  margin-top: 10px;
  padding: 0;
}
</style>
