<script setup lang="ts">
import { ref, reactive, onMounted, computed } from 'vue';
import Item from '@/components/Item.vue';
import PageButton from '@/components/PageButton.vue';

const props = defineProps<{items: Array, itemNumPerPage: Number}>();


const curPage = ref(1);
const pageNum = ref(1);

// // 表示する店の数
const displayItems = computed(() => {
    const startIdx = (1 - 1) * 10;
    const endIdx   = startIdx + 10;
    console.log(startIdx)
    console.log(endIdx)
    // return items.slice(startIdx, endIdx);
});

const tmp = () => {
  const startIdx = (curPage.value - 1) * props.itemNumPerPage;
  const endIdx   = startIdx + props.itemNumPerPage;
  console.log(startIdx)
  console.log(endIdx)
  console.log(props.items.slice(startIdx, endIdx))
  console.log(props.items[0].name)
  return props.items.slice(startIdx, endIdx);
};
// // ページ遷移
// const changePage = (value) => {
//     curPage = value;
// }

// // ページ数を計算
// const calcPageNum  = () => {
//     pageNum =  Math.ceil(items.length / itemNumPerPage);
// }
</script>

<template>
  <!-- {{itemNumPerPage}} -->
  <!-- {{items}} -->
  <input type="button" @click="tmp">
  <ul class="item-list">    
    <li v-for="item in tmp">
      {{item.name}}
      <!-- <item  :itemName="item.name"/> -->
    </li>
  </ul>
  <div class="page-button"> 
    <!-- <page-button
    @changePage="changePage" v-for="n in pageNum" 
    :key="n" 
    :pageNumber="n"
    :curPage="curPage"
    /> -->
  </div>
</template>