<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue';
import { routeLocationKey, useRouter, useRoute } from 'vue-router';
import { RouterLink, RouterView } from 'vue-router';
import Item from '@/components/Item.vue';
import PageButton from '@/components/PageButton.vue';
import ListItem from '@/components/ListItem.vue';


const props = defineProps<{items: Array, itemNumPerPage: Number}>();

const router = useRouter()
const route = useRoute()


const curPage = ref(1);
const pageNum = ref(1);

// 表示する店の数
const displayItems = computed(() => {
    const startIdx = (curPage.value - 1) * props.itemNumPerPage;
    const endIdx   = startIdx + props.itemNumPerPage;
    console.log(startIdx)
    console.log(endIdx)
    return props.items.slice(startIdx, endIdx);
});

// ページ遷移
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
  <div v-for="item in displayItems" class="m-5">
    <RouterLink :to="{ name: 'detail', params: {id: item.id } }" class="text-decoration-none text-reset">
      <ListItem :name="item.name" :access="item.mobile_access" :thumbnail="item.photo.pc.l" :genre="item.genre.name" :catch="item.catch"/>
    </RouterLink>
  </div>

  <div class="page-button" :class="calcPageNum"> 
    <page-button
    @changePage="changePage" v-for="n in pageNum" 
    :key="n"
    :pageNumber="n"
    :curPage="curPage"
    />
  </div>
</template>