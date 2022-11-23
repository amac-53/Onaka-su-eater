<script setup lang="ts">
import { RouterView } from 'vue-router';
import AppHeader from './components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';
import { ref } from 'vue';

// emitでヘッダーからのソート順を受け取るための変数
const tmp_receiver = ref<string>('');

const onChange = (val: string): void => {
  tmp_receiver.value = val;
}
</script>

<template>
<div class="outer-wrapper">
  <AppHeader @change="onChange" />
  <div class="inner-wrapper">
    <RouterView :value="tmp_receiver"/>
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