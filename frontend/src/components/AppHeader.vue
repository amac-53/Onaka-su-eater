<script setup lang="ts">
import { ref } from 'vue'
import { useRouter, useRoute, RouterLink } from 'vue-router'

const emits = defineEmits<{(e: 'change', selected?: string): void}>();

const router = useRouter()
const route = useRoute()

// 初期値を近い順で設定
const selected = "0"

const onChange = (selected?: string): void => {
  console.log(selected);
  emits('change', selected);
}
</script>

<template>
  <header class="sticky-top">
    <div class="container-fluid bg-dark">
      <div class="row justify-content-between">
        <div class="col-4">
          <nav class="navbar navbar-light">
            <RouterLink class="text-white navbar-brand" to="/">
              Onaka-su-eater
            </RouterLink>
          </nav>
        </div>
        <!-- 結果ページのみに示すソート順 -->
        <div class="col-2 d-flex align-items-center" v-if="route.path == '/result'">
          <select v-model="selected" @change="onChange(selected)">
            <option disabled value="-1">並び順を選択してください</option>
            <option value="0">近い順</option>
            <option value="4">おすすめ順</option>
          </select>
        </div>
      </div>
    </div>
  </header>
</template>
