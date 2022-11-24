<script setup lang="ts">
import { watch } from "vue";

const props = defineProps<{lat: Number, lng: Number}>();

// 緯度・経度が変われば地図を描く
watch(props, ()=>{
    const mymap = L.map('mapid').setView([props.lat, props.lng], 13);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, '
    }).addTo(mymap);
    // ピンを立てる
    L.marker([props.lat, props.lng]).addTo(mymap);
});
</script>

<template>
    <div id="mapid"></div>
</template>

<style scoped>
#mapid {
    max-width: 600px;
    height: 500px;
}
</style>