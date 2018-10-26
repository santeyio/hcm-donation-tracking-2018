<template>
  <div id="app">
    <router-view></router-view>
    <notifications group="donations" />
    <notifications group="fieldValidation" position="top center"/>
    <notifications />
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style lang="scss">
</style>
