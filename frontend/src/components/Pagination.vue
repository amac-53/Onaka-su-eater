<script setup lang="ts">
import { ref, computed } from 'vue';
import { RouterLink } from 'vue-router';
import PageButton from '@/components/PageButton.vue';
import ListItem from '@/components/ListItem.vue';


const props = defineProps<{items: Array<object>, item_num_per_page: number}>();

// 現在のページ数
const cur_page = ref<number>(1);
// ページ数
const page_num = ref<number>(1);

// 表示する店の数
const displayItems = computed(() => {
    const startIdx: number = (cur_page.value - 1) * props.item_num_per_page;
    const endIdx: number   = startIdx + props.item_num_per_page;
    return props.items.slice(startIdx, endIdx);
});

// ページ遷移
const changePage = (v:number): void => {
    cur_page.value = v;
};

// ページ数を計算
const calcPageNum  = computed(() => {
    page_num.value =  Math.ceil(props.items.length / props.item_num_per_page);
    return props.item_num_per_page;
});
</script>

<template>
  <div v-for="item in displayItems" class="m-5">
    <RouterLink :to="{ name: 'detail', params: {id: item.id } }" class="text-decoration-none text-reset">
      <ListItem :name="item.name" :access="item.mobile_access" :thumbnail="item.photo.pc.l" :genre="item.genre.name" :catch="item.catch"/>
    </RouterLink>
  </div>

  <div class="d-grid gap-2 d-md-flex justify-content-md-center" :class="calcPageNum">
    <PageButton
    @changePage="changePage" v-for="n in page_num" 
    :key="n"
    :page_number="n"
    :cur_page="cur_page"
    />
  </div>
</template>