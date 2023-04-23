<template>
  <div  style="background-color: gainsboro; border-radius: 10px; margin:20px ;">
    <table v-if="success">
          <caption>{{ data.province }}&nbsp;{{ data.city }}天气实况</caption>
          <tbody>
              <tr>
                  <td rowspan="4" width="40%">
                      <div class="icon"><img :src=data.data.dayIcon width="60"></div>
                      <p class="title">{{ data.data.dayTemp }}℃ {{ data.data.dayWeather }}</p>
                  </td>
              </tr>
              <tr>
                  <td class="text-left" width="60%">
                        <p>更新时间:{{ data.data.time}}</p>
                  </td>
              </tr>
              <tr>
                  <td class="text-left">
                      <p>相对湿度:{{ data.data.humidity }}</p>
                  </td>
              </tr>
              <tr>
                  <td class="text-left">
                      <p>PM2.5：<span class="level-2">{{ data.data.pm25 }}</span></p>
                  </td>
              </tr>
          </tbody>
      </table>
      <div v-else>获取天气失败,呜呜呜</div>
  </div>
</template>
<script>
import $ from 'jquery';
import { useStore } from 'vuex';
import { ref } from 'vue';
export default {
  name: 'WeatherBase',
  setup() {
    const store = useStore();
    let data = ref({
      province: '',
      city: '',
      data: {
        dayIcon: '',
        dayWeather: '',
        dayTemp: '',
        humidity: '',
        pm25: '',
      }
    }), success = ref(false);
    $.ajax({
      url: store.state.user.ip + '/settings/weather/',
      type: 'GET',
      async: false,
      success(res) { 
        if (res.result === 'success') { 
          res = JSON.parse(res.data);
          data.value = res;
          success.value = true;
        }
      }
    })
    return {
      data,
      success,
    }
  }
}

</script>