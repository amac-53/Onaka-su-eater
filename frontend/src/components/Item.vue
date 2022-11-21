<!-- 店のリスト一覧を表示したときの１アイテム -->
<script setup lang="ts">
defineProps<{itemName: String}>()
</script>


<template>
    <div class="items">
        {{ ItemName }}
    </div>
</template>