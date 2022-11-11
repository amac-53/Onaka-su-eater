<template>
    <div class="page-btn">
        <button @click="btnPressed"
            :class="{active: isCurrentPage}"
        >{{ pageNumber }} </button>
    </div>
</template>

<script setup lang="ts">
const props = defineProps<{pageNumber: Number, curPage: Number}>()
const emits = defineEmits<{(e: 'change', pageNumber: number):void}>()

const isCurrentPage = () => {
    return pageNumber === curPage;

}

const btmPressed = () => {
    emits('changePage', pageNumber);
}
</script>