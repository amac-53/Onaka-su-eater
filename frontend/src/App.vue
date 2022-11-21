<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from './components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';
import { ref } from 'vue'

// emitでとりあえず受け取るための変数
const tmp_receiver = ref('')

const onChange = (val?: string) => {
  tmp_receiver.value = val
}
</script>

<template>
<div class="outer-wrapper">
  <AppHeader @change="onChange" />
  <div class="inner-wrapper">
  <RouterView :val="tmp_receiver"/>
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