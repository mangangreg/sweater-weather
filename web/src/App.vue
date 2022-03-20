<template>
  <div id="app">
    <img id="applogo" src="./assets/logo.png" />
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
body {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
#app {
  max-width: 700px;
  width: 100%;
}
#applogo {
  width: 300px;
  text-align: center;
}
</style>
