<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';
import { isRef, onMounted, reactive, ref, watch } from 'vue';
import DetailMap from '@/components/DetailMap.vue';
 

const router = useRouter()
const route = useRoute()

// 詳細情報を保持
const shop = ref({});

// idに一致する詳細情報を取得
const getDetail = onMounted(() => {

    const base_url = 'http://127.0.0.1:8000/items/detail/'
    const id = '?id=' + route.params.id
    const url = base_url + id
    axios.get(url)
        .then(res => {
            shop.value = res.data.results.shop[0]
        })
        .catch(error => {
            console.log(error)
        })
});
</script>

<template>
    <!-- 店舗名など -->
    <div class="container pt-5 my-5">
    <div class="row justify-content-center">
        <div class="card bg-white" style="max-width: 600px;">
            <div class="row g-0">
                <div class="col-md-4">
                    <img :src="shop.logo_image" alt="" class="img-thumbnail float-start">
                </div>
                <div class="col-md-8">
                    <div class="card-header">
                        <div class="fs-6" v-if="shop.genre">{{shop.genre.name }}</div>      
                        <div class="card-title fs-3">{{ shop.name }}</div>
                        <div>{{ shop.access }}</div>
                    </div>
                    <div class="card-body">
                        <div>{{ shop.catch }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>

    <!-- 画像 -->
    <!-- <div class="container mb-5">
        <div class="row justify-content-center">
            <img :src="shop.img.l" alt="" style="max-width: 600px;">
        </div> 
    </div> -->

    <div class="row justify-content-center" >
        <DetailMap :lat="shop.lat" :lng="shop.lng" />
    </div>

    <!-- 詳細情報 -->
    <div class="conatiner">
        <div class="row justify-content-center fw-bold">
            店舗詳細情報
        </div>
        <div class="row justify-content-center mb-5">
            <table class="table table-bordered" style="max-width: 600px;">
                <tbody>
                    <tr>
                        <th scope="row">店名</th>
                        <td>{{shop.name}}</td>
                    </tr>
                    <tr>
                        <th scope="row">住所</th>
                        <td>{{shop.address}}</td>
                    </tr>
                    <tr>
                        <th scope="row">アクセス</th>
                        <td>{{shop.access}}</td>
                    </tr>
                    <tr v-if="shop.urls">
                        <th scope="row">店舗URL</th>
                        <td><a :href="shop.urls.pc">{{shop.urls.pc}}</a></td>
                    </tr>
                    <tr>
                        <th scope="row">営業時間</th>
                        <td>{{shop.open}}</td>
                    </tr>
                    <tr>
                        <th scope="row">定休日</th>
                        <td>{{shop.close}}</td>
                    </tr>
                    <tr>
                        <th scope="row">ランチ</th>
                        <td>{{shop.lunch}}</td>
                    </tr>
                    <tr v-if="shop.budget">
                        <th scope="row">平均予算</th>
                        <td> {{shop.budget.average }}</td>
                    </tr>
                    <tr>
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
                    <tr>
                        <th scope="row">席数</th>
                        <td>{{shop.capacity}}</td>
                    </tr>
                    <tr>
                        <th scope="row">個室</th>
                        <td>{{shop.private_room}}</td>
                    </tr>
                    <tr>
                        <th scope="row">貸切</th>
                        <td>{{shop.charter}}</td>
                    </tr>
                    <tr>
                        <th scope="row">たばこ</th>
                        <td>{{shop.non_smoking}}</td>
                    </tr>
                    <tr>
                        <th scope="row">Wi-Fi</th>
                        <td>{{shop.wifi}}</td>
                    </tr>
                    <tr>
                        <th scope="row">バリアフリー</th>
                        <td>{{shop.barrier_free}}</td>
                    </tr>
                    <tr>
                        <th scope="row">駐車場</th>
                        <td>{{shop.parking}}</td>
                    </tr>
                    <tr>
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
                    <tr>
                        <th scope="row">飲み放題</th>
                        <td>{{shop.free_drink}}</td>
                    </tr>
                    <tr>
                        <th scope="row">食べ放題</th>
                        <td>{{shop.free_food}}</td>
                    </tr>
                    <tr>
                        <th scope="row">お子様連れ</th>
                        <td>{{shop.child}}</td>
                    </tr>
                    <tr>
                        <th scope="row">ペット可</th>
                        <td>{{shop.pet}}</td>
                    </tr>
                    <tr>
                        <th scope="row">ウェディングパーティー二次会</th>
                        <td>{{shop.wedding}}</td>
                    </tr>
                    <tr>
                        <th scope="row">備考</th>
                        <td>{{shop.shop_detail_memo}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
