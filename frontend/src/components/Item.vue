<!-- 店のリスト一覧を表示したときの１アイテム -->
<script setup lang="ts">
defineProps<{itemName: String}>()
</script>


<template>
    <!-- ここで何か箱型のデザインにしておく -->
    <div class="items">
        {{ ItemName }}
    </div>
    <!-- https://qiita.com/JunNishimura/items/e0bbd03cdb627df04261 -->
</template>