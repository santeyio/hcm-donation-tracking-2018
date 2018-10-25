<template>
  <div id="app">
    <router-view></router-view>
    <notifications group="donations"/>
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
.notification-content {
  font-size: 120px;
}
.notifications {
  left: calc(78% - 150px);
  width: 29% !important;
}
</style>
