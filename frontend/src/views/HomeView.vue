<script setup lang="ts">
import { ref, reactive, computed } from "vue";
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
    const selectEl = document.getElementById("selectDistance");
    range.value = selectEl.options[selectEl.selectedIndex].value;
}

const successCallback = (position) => {
  latitude.value = position.coords.latitude;
  longitude.value = position.coords.longitude;
  // 当面の対応（後で修正）
  router.push({path: '/result', query: {latitude: latitude.value, longitude: longitude.value, range: range.value}})
};

const errorCallback = (error) => {
  alert("位置情報が取得できませんでした");
};
</script>

<template>
  <main>
    <div class="container m-5 pt-5">
    <div class="row justify-content-center">
      <div class="card bg-white" style="max-width: 600px;">
          <div class="card-body">
            <p class="row g-0">
              <div class="text-center">
                <label for="selectDistance">現在地から何m以内までで検索しますか？</label>
              </div>
            </p>
            <p class="row g-0">
              <select name="" id="selectDistance" required>
                <option value="300">300m</option>
                <option value="500">500m</option>
                <option value="1000">1000m</option>
                <option value="2000">2000m</option>
                <option value="3000">3000m</option>
              </select>
            </p>
            <p class="row g-0">
              <button type="button" class="btn btn-secondary" @click="getResult">検索</button>
            </p>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
