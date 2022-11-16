<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';
import { onMounted, reactive, ref } from 'vue';
 
const router = useRouter()
const route = useRoute()

// 詳細情報を保持
const shop = reactive({
    info: {},
    genre: {},
    img: {},
    budget: {},
    url: {}
});


// idに一致する詳細情報を取得
const getDetail = onMounted(() => {

    const base_url = 'http://127.0.0.1:8000/items/detail/'
    const id = '?id=' + route.params.id
    const url = base_url + id
    axios.get(url)
        .then(res => {
            shop.info = res.data.results.shop[0];
            shop.genre = res.data.results.shop.genre;
            shop.img = res.data.results.shop.photo.pc;
            shop.budget = res.data.results.shop.budget;
            shop.url = res.data.results.shop.urls;
            console.log(shop.info)
        })
        .catch(error => {
            console.log(error)
        })
});


</script>

<template>
    <!-- 店舗名など -->
    <div class="container mb-5">
    <div class="row justify-content-center">
        <div class="card bg-white" style="max-width: 600px;">
            <div class="row g-0">
                <div class="col-md-4">
                    <img :src="shop.info.logo_image" alt="" class="img-thumbnail float-start">
                </div>
                <div class="col-md-8">
                    <div class="card-header">
                        <!-- <div class="fs-6">{{shop.genre.name }}</div>       -->
                        <div class="card-title fs-3">{{ shop.info.name }}</div>
                        <div>{{ shop.info.access }}</div>
                    </div>
                    <div class="card-body">
                        <div>{{ shop.info.catch }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {{}}
    </div>

    <!-- 画像 -->
    <div class="container mb-5">
        <div class="row justify-content-center">
            <img :src="shop.img.l" alt="" style="max-width: 600px;">
        </div> 
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
                        <td>{{shop.info.name}}</td>
                    </tr>
                    <tr>
                        <th scope="row">住所</th>
                        <td>{{shop.info.address}}</td>
                    </tr>
                    <tr>
                        <th scope="row">アクセス</th>
                        <td>{{shop.info.access}}</td>
                    </tr>
                    <tr>
                        <th scope="row">店舗URL</th>
                        <td><a :href="shop.url.pc">{{shop.url.pc}}</a></td>
                    </tr>
                    <tr>
                        <th scope="row">営業時間</th>
                        <td>{{shop.info.open}}</td>
                    </tr>
                    <tr>
                        <th scope="row">定休日</th>
                        <td>{{shop.info.close}}</td>
                    </tr>
                    <tr>
                        <th scope="row">ランチ</th>
                        <td>{{shop.info.lunch}}</td>
                    </tr>
                    <tr>
                        <th scope="row">平均予算</th>
                        <td> {{shop.budget.average}}</td>
                    </tr>
                    <tr>
                        <th scope="row">支払方法</th>
                        <td>カード：{{shop.info.card}}</td>
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
                        <td>{{shop.info.capacity}}</td>
                    </tr>
                    <tr>
                        <th scope="row">個室</th>
                        <td>{{shop.info.private_room}}</td>
                    </tr>
                    <tr>
                        <th scope="row">貸切</th>
                        <td>{{shop.info.charter}}</td>
                    </tr>
                    <tr>
                        <th scope="row">たばこ</th>
                        <td>{{shop.url.non_smoking}}</td>
                    </tr>
                    <tr>
                        <th scope="row">Wi-Fi</th>
                        <td>{{shop.info.wifi}}</td>
                    </tr>
                    <tr>
                        <th scope="row">バリアフリー</th>
                        <td>{{shop.info.barrier_free}}</td>
                    </tr>
                    <tr>
                        <th scope="row">駐車場</th>
                        <td>{{shop.info.parking}}</td>
                    </tr>
                    <tr>
                        <th scope="row">その他の設備</th>
                        <td>{{shop.info.other_memo}}</td>
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
                        <td>{{shop.info.free_drink}}</td>
                    </tr>
                    <tr>
                        <th scope="row">食べ放題</th>
                        <td>{{shop.info.free_food}}</td>
                    </tr>
                    <tr>
                        <th scope="row">お子様連れ</th>
                        <td>{{shop.info.child}}</td>
                    </tr>
                    <tr>
                        <th scope="row">ペット可</th>
                        <td>{{shop.info.pet}}</td>
                    </tr>
                    <tr>
                        <th scope="row">ウェディングパーティー二次会</th>
                        <td>{{shop.url.wedding}}</td>
                    </tr>
                    <tr>
                        <th scope="row">備考</th>
                        <td>{{shop.info.shop_detail_memo}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
