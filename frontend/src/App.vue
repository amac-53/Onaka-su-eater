<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from './components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';
</script>

<template>
<div class="outer-wrapper">
  <AppHeader />
  <div class="inner-wrapper">
  <RouterView />
  </div>
  <AppFooter />
</div>
</template>

<style scoped>
.outer-wrapper {
  display: flex;
  flex-flow: column;
  min-height: 100vh;
}
.inner-wrapper {
  flex: 1;
}
</style>