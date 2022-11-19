<script setup lang="ts">
import { useRouter, useRoute, RouterLink } from 'vue-router';
import axios from 'axios';
import { isRef, onMounted, reactive, ref, watch } from 'vue';
import DetailMap from '@/components/DetailMap.vue';
 

const router = useRouter()
const route = useRoute()

// 詳細情報を保持
const shop = ref({});

// idに一致する詳細情報を取得
const getDetail = onMounted(() => {

    const base_url = 'http://127.0.0.1:8080/items/detail/'
    const id = '?id=' + route.params.id
    const url = base_url + id
    axios.get(url)
        .then(res => {
            shop.value = res.data.results.shop[0]
            console.log(shop.value)
        })
        .catch(error => {
            console.log(error)
        })
});
</script>

<template>
    <!-- 店舗名など -->
    <div class="container pt-5 my-5" style="max-width: 600px;">
        <div class="row justify-content-center">
            <div class="card bg-white" style="max-width: 600px;">
                <div class="row g-0">
                    <div class="card-header">
                        <div class="row">
                            <div v-if="shop.logo_image" class="col-md-2">
                                <img :src="shop.logo_image" alt="" class="img-thumbnail float-start">
                            </div>
                            <div class="col-md-10">
                                <div class="fs-6" v-if="shop.genre">{{shop.genre.name }}</div>      
                                <div class="card-title fs-3">{{ shop.name }}</div>
                            </div>
                        </div>
                    </div>
                    <div class="card-body" v-if="shop.catch">
                        <div>{{ shop.catch }}</div>
                    </div>
                </div>
            </div>
            <nav class="nav nav-pills flex-column flex-sm-row bg-light p-0">
                <RouterLink :to="{ name: 'detail', params: {id: route.params.id }}" class="flex-sm-fill text-sm-center nav-link text-dark">Top</RouterLink>
                <RouterLink :to="{ name: 'detail_map', params: {id: route.params.id }}" class="flex-sm-fill text-sm-center nav-link active bg-dark" aria-current="page">地図</RouterLink>
            </nav>
        </div>
    </div>
    
    <!-- 地図 -->
    <div class="container mb-5" style="max-width: 600px;">
        <div class="row justify-content-center" >
            <DetailMap :lat="shop.lat" :lng="shop.lng" />
        </div>
    </div>
    
    <!-- 詳細情報 -->
    <div class="container">
        <div class="row justify-content-center fw-bold">
            店舗詳細情報
        </div>
        <div class="row justify-content-center mb-5">
            <table class="table table-bordered" style="max-width: 600px;">
                <tbody>
                    <tr v-if="shop.name">
                        <th scope="row">店名</th>
                        <td>{{shop.name}}</td>
                    </tr>
                    <tr v-if="shop.address">
                        <th scope="row">住所</th>
                        <td>{{shop.address}}</td>
                    </tr>
                    <tr v-if="shop.access">
                        <th scope="row">アクセス</th>
                        <td>{{shop.access}}</td>
                    </tr>
                    <tr v-if="shop.urls">
                        <th scope="row">店舗URL</th>
                        <td><a :href="shop.urls.pc">{{shop.urls.pc}}</a></td>
                    </tr>
                    <tr v-if="shop.open">
                        <th scope="row">営業時間</th>
                        <td>{{shop.open}}</td>
                    </tr>
                    <tr v-if="shop.close">
                        <th scope="row">定休日</th>
                        <td>{{shop.close}}</td>
                    </tr>
                    <tr v-if="shop.lunch">
                        <th scope="row">ランチ</th>
                        <td>{{shop.lunch}}</td>
                    </tr>
                    <tr v-if="shop.budget">
                        <th scope="row">平均予算</th>
                        <td> {{shop.budget.average }}</td>
                    </tr>
                    <tr v-if="shop.card">
                        <th scope="row">支払方法</th>
                        <td>カード：{{shop.card}}</td>
                    </tr>
                </tbody>
            </table>
        </div> 
    </div>
</template>
