<script setup lang="ts">
import { ref, reactive, computed } from "vue";
import { useRouter, useRoute } from 'vue-router';
import axios from "axios";

const router = useRouter()
const route = useRoute()

const latitude = ref(0)
const longitude = ref(0)
const range = ref(0)

const keyword = ref("");

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
  console.log(keyword)
  router.push({path: '/result', query: {latitude: latitude.value, longitude: longitude.value, range: range.value, keyword: keyword.value}})
};

const errorCallback = (error) => {
  alert("位置情報が取得できませんでした");
};

</script>

<template>
  <main>
    <div class="d-flex justify-content-center m-5 p-5 fs-3">
        現在地近くのお店を探しましょう
    </div>
    <div class="d-flex justify-content-center pb-5">
      <div class="card bg-white" style="width: 800px;">
        <div class="card-body">
          <div class="row">
            <div class="col">
              キーワード
              <div class="input-group mb-3">
                <input type="text" v-model="keyword" class="form-control form-control-lg" placeholder="店名・ジャンルなど">
              </div>
            </div>
            <div class="col">
              現在地からの距離
              <select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example" id="selectDistance" required>
                <option value="300">300m</option>
                <option value="500">500m</option>
                <option value="1000">1000m</option>
                <option value="2000">2000m</option>
                <option value="3000">3000m</option>
              </select>
            </div>
          </div>
          <p class="row g-0">
            <button type="button" class="btn btn-secondary" @click="getResult">検索</button>
          </p>
        </div>
      </div>
    </div>
  </main>
</template>
