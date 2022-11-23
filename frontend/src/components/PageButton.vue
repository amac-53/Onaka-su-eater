<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{page_number: number, cur_page: number}>();
const emits = defineEmits<{(e: 'changePage', page_number: number): void}>();

// 現在ページを指し示していればtrue
const isCurrentPage = computed(() => {
    return props.page_number === props.cur_page;
});

const btmPressed = () => {
    emits('changePage', props.page_number);
}
</script>

<template>
    <button class="btn btn-light btn-outline-dark"
        @click="btmPressed"
        :class="{active: isCurrentPage}"
    >{{ page_number }} </button>
</template>
