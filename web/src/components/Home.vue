<template>
  <div id="home">
    <h1>{{ msg }}</h1>
    <select v-model="period">
      <option v-for="opt in periodOptions" :value="opt">{{ opt }} </option>
    </select>

    <h2>Period: {{ period }}</h2>
    <WeatherCurrent v-if="period == 'current'" />
    <WeatherDaily v-if="period == 'daily'" />
  </div>
</template>

<script>
import WeatherCurrent from "@/components/WeatherCurrent";
import WeatherDaily from "@/components/WeatherDaily";
import api from "@/api.js";
export default {
  name: "Home",
  components: {
    WeatherCurrent,
    WeatherDaily
  },
  data() {
    return {
      msg: "Welcome to Sweater Weather",
      period: "current",
      periodOptions: ["current", "daily"]
    };
  },
  methods: {
    doSomething: function(arg) {}
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
