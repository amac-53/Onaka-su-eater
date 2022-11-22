<script setup lang="ts">
import { ref, reactive, onMounted, watchEffect } from 'vue'
import { useRouter, useRoute, RouterLink } from 'vue-router'
import axios from 'axios' 
import pagination from "../components/Pagination.vue"

const router = useRouter()
const route = useRoute()

const props = defineProps(['val']);

// リストで受け取る
const tables = reactive({
  items: [],
  num: 10
})

// 現在地を受け取って，マウント時に一覧の情報を取得
watchEffect(() => {
  const base_url = 'http://127.0.0.1:8080/items/'
  const latitude = 'latitude=' + route.query.latitude
  const longitude = 'longitude=' + route.query.longitude

  const range = 'range=' + route.query.range
  const count = 'count=100'
  const order = 'order=' + props.val
  const kwd = 'keyword=' + route.query.keyword

  const url = base_url + '?' +latitude + '&' + longitude + '&' + range + '&' + count + '&' + kwd 
  axios.get((order == 'order=4' ? url + '&' + order : url))
  .then(res => {
    const tmp = order == 'order=4' ? url + '&' + order : url
    console.log(res.data)
    tables.items = res.data.results.shop;
  })
  .catch(error => {
    console.log(error);
  }) 
});

</script>


<template>
<div v-if="tables.items.length > 0" class="p-5">
  <pagination :items="tables.items" :itemNumPerPage="tables.num" />
</div>

<div v-else class="p-5 m-5">
  <div class="d-grid gap-2 d-md-flex justify-content-md-center m-5">
    {{route.query.range}}m以内にお店はありません
  </div>
  <div class="d-grid gap-2 d-md-flex justify-content-md-center">
    <RouterLink to="/">
      <button type="button" class="btn btn-secondary">homeに戻る</button>
    </RouterLink>
  </div>
</div>
</template>
