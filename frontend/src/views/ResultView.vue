<script setup lang="ts">
import { ref, watchEffect } from 'vue';
import { useRouter, useRoute, RouterLink } from 'vue-router';
import axios from 'axios';
import Pagination from "../components/Pagination.vue";

const route = useRoute();

const props = defineProps(['val']);

// 店舗一覧
const items = ref<Array<object>>([]);
// ページネーション
const items_per_page: number = 10;

// 現在地を受け取って，マウント時に一覧の情報を取得
// ソート指定部分 (order) に変更があれば再度データ取得
watchEffect(() => {
  const base_url = 'http://127.0.0.1:8080/items/';

  // クエリ
  const latitude = 'latitude=' + route.query.latitude;
  const longitude = 'longitude=' + route.query.longitude;
  const range = 'range=' + route.query.range;
  const count = 'count=100';
  const order = 'order=' + props.val;
  const kwd = 'keyword=' + route.query.keyword;

  const url = base_url + '?' +latitude + '&' + longitude + '&' + range + '&' + count + '&' + kwd;
  // 並び替えの指定があれば order を加えてデータ取得
  axios.get((order == 'order=4' ? url + '&' + order : url))
  .then(res => {
    const tmp = order == 'order=4' ? url + '&' + order : url;
    items.value = res.data.results.shop;
  })
  .catch(error => {
    console.log(error);
  }) 
});
</script>


<template>
<!-- 店舗一覧 -->
<div v-if="items.length > 0" class="p-5">
  <Pagination :items="items" :item_num_per_page="items_per_page" />
</div>
<!-- 店舗が一つもなければ -->
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
