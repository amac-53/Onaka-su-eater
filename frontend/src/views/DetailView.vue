<!-- 詳細画面 -->
<!-- 全ての情報をパラメータで渡す or 「id渡してaxiosで取得」（こっちな気がする） -->
<!-- さすがに一覧に戻るは必要かな -->
<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';
import { onMounted, reactive } from 'vue';

const router = useRouter()
const route = useRoute()

console.log(route.params);

const info = reactive({
    name: '',
    time: '',
    img_url: '',
    address: ''
});

const getDetail = onMounted(() => {

    const base_url = 'http://127.0.0.1:8000/items/detail/'
    const id = '?id=' + route.params.id
    const url = base_url + id

    axios.get(url)
        .then(res => {
            info.name = res.data.results.shop.name
            info.time = res.data.results.shop.open
            info.address = res.data.results.shop.address
            info.img_url = res.data.results.shop.logo_image
            console.log(res.data.results.shop)
        })
        .catch(error => {
            console.log(error)
        })
});
</script>

<template>
    <h1>{{info.name}}</h1>
    <p>
        住所: {{info.address}}
    </p>
    <p>
        営業時間: {{info.time}}
    </p>
    <img :src="info.img_url" alt="NoImage">
</template>
