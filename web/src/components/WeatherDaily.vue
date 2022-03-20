<template>
  <div>
    <div v-if="isLoaded" width="500px" class="">
      Location: {{ this.location }} [{{ this.lat }},{{ this.lon }}]
      <ul>
        <li v-for="day in weatherData">
          {{ day.timestamp }}: {{ day.response.weather[0].description }}
          <ul>
            <li>Min: {{ day.response.temp.min | KtoC | decimalPlaces(2) }}C</li>
            <li>Max: {{ day.response.temp.max | KtoC | decimalPlaces(2) }}C</li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import api from "@/api.js";
import appTools from "@/appTools.js";
export default {
  name: "WeatherDaily",
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
      // return this.isLoaded ? this.KtoC(this.weatherData.temp) : null;
      return null;
    }
  },
  methods: {
    KtoC: function(kelvin) {
      return kelvin - 273.15;
    }
  },

  mounted() {
    // debugger;
    api.fetchWeatherDaily().then(resp => {
      console.log(resp);
      this.weatherData = resp.data;
      this.lat = resp.data[0].lat;
      this.lon = resp.data[0].lon;
      this.isLoaded = true;
    });
    // console.log("weatherCurrent", weatherRes);
  }
};
</script>
<style></style>
