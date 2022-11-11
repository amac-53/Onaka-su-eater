<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue';
import Item from '@/components/Item.vue';
import PageButton from '@/components/PageButton.vue';
import { routeLocationKey, useRouter, useRoute } from 'vue-router';
import { RouterLink, RouterView } from 'vue-router'


const props = defineProps<{items: Array, itemNumPerPage: Number}>();

const router = useRouter()
const route = useRoute()


const curPage = ref(1);
const pageNum = ref(1);

// // 表示する店の数
const displayItems = computed(() => {
    const startIdx = (curPage.value - 1) * props.itemNumPerPage;
    const endIdx   = startIdx + props.itemNumPerPage;
    console.log(startIdx)
    console.log(endIdx)
    return props.items.slice(startIdx, endIdx);
});

// // ページ遷移
const changePage = (v) => {
    curPage.value = v;
};

// ページ数を計算
const calcPageNum  = computed(() => {
    pageNum.value =  Math.ceil(props.items.length / props.itemNumPerPage);
    console.log(pageNum.value)
    return props.itemNumPerPage
});

</script>

<template>
  <!-- {{itemNumPerPage}} -->
  <!-- {{items}} -->
  <ul class="item-list">    
    <li v-for="item in displayItems">
      <RouterLink :to="{ name: 'detail', params: {id: item.id } }">{{item.name}}</RouterLink>
      <!-- <item  :itemName="item.name"/> -->
    </li>
  </ul>

  <div class="page-button" :class="calcPageNum"> 
    <page-button
    @changePage="changePage" v-for="n in pageNum" 
    :key="n"
    :pageNumber="n"
    :curPage="curPage"
    />
  </div>
</template>