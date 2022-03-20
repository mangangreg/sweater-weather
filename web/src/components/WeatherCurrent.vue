<template>
  <div>
    <div v-if="isLoaded" width="500px" class="">
      The current weather in {{ this.location }} [{{ this.lat }},{{ this.lon }}]
      is described as "{{ weatherData.weather[0].description }}". The
      temperature is {{ this.temperature | decimalPlaces(2) }}C.
    </div>

    <div v-if="isLoaded" width="500px" class="">
      <ul>
        <li>Location: {{ this.location }} [{{ this.lat }},{{ this.lon }}]</li>
        <li>Conditions: "{{ weatherData.weather[0].description }}"</li>
        <li>Temperature: {{ this.temperature | decimalPlaces(2) }}C</li>
      </ul>
    </div>
  </div>
</template>

<script>
import api from "@/api.js";
import appTools from "@/appTools.js";
export default {
  name: "WeatherCurrent",
  data() {
    return {
      val: 2,
      weatherData: null,
      isLoaded: false,
      lat: null,
      lon: null,
      location: "Greenpoint"
    };
  },
  computed: {
    temperature: function() {
      //   if (!this.isLoaded) {
      //     return null;
      //   } else {
      //     return this.KtoC(this.weatherData.temp);
      //   }
      return this.isLoaded ? this.KtoC(this.weatherData.temp) : null;
    }
  },
  methods: {
    KtoC: function(kelvin) {
      return kelvin - 273.15;
    }
  },

  mounted() {
    // debugger;
    api.fetchWeatherCurrent().then(resp => {
      console.log(resp);
      this.weatherData = resp.data.response;
      this.lat = resp.data.lat;
      this.lon = resp.data.lon;
      this.isLoaded = true;
    });
    // console.log("weatherCurrent", weatherRes);
  }
};
</script>
<style></style>
