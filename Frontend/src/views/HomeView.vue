<template>
  <ContentBase>
    <div class="container justify-content-md-center">
      <div class="row">
        <div class="col-md-6 col-sm-12">
          <u-search style="width:80%" :config="config" @submit="submit"></u-search>
        </div>
        <br>
        <div class="col-md-6 col-sm-12">
          <WeatherBase></WeatherBase>
        </div>
      </div>
    </div>
  </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';
import { ref } from 'vue'
import router from '@/router'
import WeatherBase from '@/components/WeatherBase';
export default {
  name: 'HomeView',
  components: {
    ContentBase,
    WeatherBase,
  },
  setup() { 
    const config = ref({
      keywords: ['根据ID搜索用户'], 
      hotSearchList: [
      ] 
    })

    const submit = (val) => {
      router.push({ name: 'user_myspace', params: { userId: val } });
    }
    return {
      config,
      submit,

    }
  }
  
}

</script>

<style scoped>

</style>