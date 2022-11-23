<script setup lang="ts">
import { useRoute, RouterLink } from 'vue-router';

const emits = defineEmits<{(e: 'change', selected: string): void}>();

const route = useRoute();

// 初期値を近い順で設定
const selected = "0";

const onChange = (selected: string): void => {
  emits('change', selected);
}
</script>

<template>
  <header class="sticky-top">
    <div class="container-fluid" style="background: linear-gradient(to bottom, rgb(247 147 6), rgb(250 208 104));">
      <div class="row justify-content-between">
        <div class="col-4">
          <nav class="navbar navbar-light">
            <RouterLink class="text-white navbar-brand" to="/">
              Onaka-su-eater
            </RouterLink>
          </nav>
        </div>
        <!-- 結果ページのみに示すソート順 -->
        <div class="col-4 d-flex align-items-center justify-content-end " v-if="route.path == '/result'">
          <select v-model="selected" class="form-select form-select-sm" @change="onChange(selected)" style="max-width: 200px;">
            <option disabled value="-1">並び順を選択してください</option>
            <option value="0">近い順</option>
            <option value="4">おすすめ順</option>
          </select>
        </div>
      </div>
    </div>
  </header>
</template>
