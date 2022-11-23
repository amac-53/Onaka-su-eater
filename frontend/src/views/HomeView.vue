<script setup lang="ts">
import { ref, computed } from "vue";
import { useRouter } from 'vue-router';

const router = useRouter();

// 取得する情報
const latitude = ref<number>(0);
const longitude = ref<number>(0);
const range = ref<number>(300);
const keyword = ref<string>("");

  // 現在地を取得
const getResult = () => {
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
}

// 成功時のコールバック関数
const successCallback = (position: any) => {
  latitude.value = position.coords.latitude;
  longitude.value = position.coords.longitude;
  //緯度・経度を受け取ったらページ遷移
  router.push({path: '/result', query: {latitude: latitude.value, longitude: longitude.value, range: range.value, keyword: keyword.value}});
};

// 取得失敗の時の処理
const errorCallback = (error: any) => {
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
              <select v-model="range"  class="form-select form-select-lg mb-3" aria-label=".form-select-lg example" required>
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
