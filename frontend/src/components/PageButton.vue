<script setup lang="ts">
import { computed } from 'vue'
const props = defineProps<{pageNumber: Number, curPage: Number}>()
const emits = defineEmits<{(e: 'change', pageNumber: number):void}>()

const isCurrentPage = computed(() => {
    return props.pageNumber === props.curPage;
});

const btmPressed = () => {
    emits('changePage', props.pageNumber);
}
</script>

<template>
    <div class="page-btn">
        <button @click="btmPressed"
            :class="{active: isCurrentPage}"
        >{{ pageNumber }} </button>
    </div>
</template>