<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios' 
import pagination from "../components/Pagination.vue"

const router = useRouter()
const route = useRoute()

// リストで受け取る
const tables = reactive({
  items: [],
  num: 5
})

// 現在地を受け取って，マウント時に一覧の情報を取得
onMounted(() => {
  // 店一覧のjsonを受け取る? それともデータ量だけまず？
  // 緯度，経度，rangeを渡す（数字の処理はバックエンドで）
  // 長さが1つのときはundefined? 0のときの処理は？
  const base_url = 'http://127.0.0.1:8000/items/'
  const latitude = '?latitude=' + route.query.latitude
  const longitude = 'longitude=' + route.query.longitude
  const range = 'range=' + route.query.range
  const url = base_url + latitude + '&' + longitude + '&' + range
  axios.get(url)
  .then(res => {
    // console.log(url);
    console.log(res.data.results.shop)
    tables.items = res.data.results.shop;
  })
  .catch(error => {
    console.log(error);
  }) 
});

// const getData = () => {
//   const url = 'api/users?page=ページ番号' // みたいな
//   axios.get(url)
//   .then(res => {
//     console.log(res);
//   }) 
//   .catch(error => {
//     console.log(error);
//   })
// }
</script>

<template>
<div class="paging">
  <!-- {{tables.items}} -->
  <!-- データ取得 -> paginationにする -->
  <!--  -->
  <pagination :items="tables.items" :itemNumPerPage="tables.num" />
  <!-- {{tables.items}} ok -->
</div>
</template>
