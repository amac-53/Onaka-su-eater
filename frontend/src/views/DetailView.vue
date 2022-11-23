<script setup lang="ts">
import { useRoute } from 'vue-router';
import axios from 'axios';
import { onMounted, ref } from 'vue';
 
const route = useRoute();

// 詳細情報を保持
const shop = ref<object>({});

// idに一致する詳細情報を取得
onMounted(() => {

    const base_url: string = 'http://127.0.0.1:8080/items/detail/';
    const id: string = 'id=' + route.params.id;
    const url: string = base_url + '?' + id;
    axios.get(url)
        .then(res => {
            shop.value = res.data.results.shop[0];
        })
        .catch(error => {
            console.log(error);
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
            <!-- リンク -->
            <nav class="nav nav-pills flex-column flex-sm-row bg-light">
                <RouterLink :to="{ name: 'detail', params: {id: route.params.id }}" class="flex-sm-fill text-sm-center nav-link active bg-dark" aria-current="page">Top</RouterLink>
                <RouterLink :to="{ name: 'detail_map', params: {id: route.params.id }}" class="flex-sm-fill text-sm-center nav-link text-dark">地図</RouterLink>
            </nav>
        </div>
    </div>

    <!-- 画像 -->
    <div class="container mb-5" style="max-width: 600px;">
        <div v-if="shop.photo" class="row justify-content-center">
            <img :src="shop.photo.pc.l" alt="" >
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

        <div class="row justify-content-center fw-bold">
            席・設備
        </div>
        <div class="row justify-content-center mb-5">
            <table class="table table-bordered" style="max-width: 600px;">
                <tbody>
                    <tr v-if="shop.capacity">
                        <th scope="row">席数</th>
                        <td>{{shop.capacity}}</td>
                    </tr>
                    <tr v-if="shop.private_room">
                        <th scope="row">個室</th>
                        <td>{{shop.private_room}}</td>
                    </tr>
                    <tr v-if="shop.charter">
                        <th scope="row">貸切</th>
                        <td>{{shop.charter}}</td>
                    </tr>
                    <tr v-if="shop.non_smoking">
                        <th scope="row">たばこ</th>
                        <td>{{shop.non_smoking}}</td>
                    </tr>
                    <tr v-if="shop.wifi">
                        <th scope="row">Wi-Fi</th>
                        <td>{{shop.wifi}}</td>
                    </tr>
                    <tr v-if="shop.barrier_free">
                        <th scope="row">バリアフリー</th>
                        <td>{{shop.barrier_free}}</td>
                    </tr>
                    <tr v-if="shop.parking">
                        <th scope="row">駐車場</th>
                        <td>{{shop.parking}}</td>
                    </tr>
                    <tr v-if="shop.other_memo">
                        <th scope="row">その他の設備</th>
                        <td>{{shop.other_memo}}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="row justify-content-center fw-bold">
            その他
        </div>
        <div class="row justify-content-center mb-5">
            <table class="table table-bordered" style="max-width: 600px;">
                <tbody>
                    <tr v-if="shop.free_drink">
                        <th scope="row">飲み放題</th>
                        <td>{{shop.free_drink}}</td>
                    </tr>
                    <tr v-if="shop.free_food">
                        <th scope="row">食べ放題</th>
                        <td>{{shop.free_food}}</td>
                    </tr>
                    <tr v-if="shop.child">
                        <th scope="row">お子様連れ</th>
                        <td>{{shop.child}}</td>
                    </tr>
                    <tr v-if="shop.pet">
                        <th scope="row">ペット可</th>
                        <td>{{shop.pet}}</td>
                    </tr>
                    <tr v-if="shop.wedding">
                        <th scope="row">ウェディングパーティー二次会</th>
                        <td>{{shop.wedding}}</td>
                    </tr>
                    <tr v-if="shop.shop_detail_memo">
                        <th scope="row">備考</th>
                        <td>{{shop.shop_detail_memo}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>