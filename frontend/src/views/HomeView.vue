<script setup lang="ts">
import { ref, reactive } from "vue";
import { useRouter, useRoute } from 'vue-router';
import axios from "axios";

const router = useRouter()
const route = useRoute()

const latitude = ref(0)
const longitude = ref(0)
const range = ref(0)

// 検索結果を表示
const getResult = async(e) => {
    // 現在地を取得
    await navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    // 値を渡してページ遷移と同時に値渡し（現在地と半径）
    // とりあえず34.910047, 135.7805467, 100
    latitude.value = 34.910047;
    longitude.value = 135.7805467;
    range.value = 3000;
    
    router.push({path: '/result', query: {latitude: latitude.value, longitude: longitude.value, range: range.value}})
}

const successCallback = (position) => {
  latitude.value = position.coords.latitude;
  longitude.value = position.coords.longitude;
};

const errorCallback = (error) => {
  alert("位置情報が取得できませんでした");
};


</script>

<template>
  <main>
  <p>
    <label for="tmp">現在地からの何m以内までで検索しますか？</label>
    <select name="" id="tmp" required>
      <option value="">300m</option>
      <option value="">500m</option>
      <option value="">1000m</option>
      <option value="">2000m</option>
      <option value="">3000m</option>
    </select>
  </p>
  <p>
    <button @click="getResult">検索</button>
  </p>
  <div>{{ latitude }}</div>
  <div>{{ longitude }}</div>
  </main>
</template>
