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
  num: 10
})

// 現在地を受け取って，マウント時に一覧の情報を取得
onMounted(() => {
  // 緯度，経度，rangeを渡す（数字の処理はバックエンドで）
  // 長さが1つのときはundefined? 0のときの処理は？
  const base_url = 'http://127.0.0.1:8000/items/'
  const latitude = '?latitude=' + route.query.latitude
  const longitude = 'longitude=' + route.query.longitude
  const range = 'range=' + route.query.range
  const count = 'count=100'
  const url = base_url + latitude + '&' + longitude + '&' + range + '&' + count 
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

</script>

<template>
<div class="paging">
  <pagination :items="tables.items" :itemNumPerPage="tables.num" />
</div>
</template>
