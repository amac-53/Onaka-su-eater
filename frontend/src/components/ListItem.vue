<script setup lang="ts">
const props = defineProps<{name: String, access: String, thumbnail: String, genre: String, catch: String}>();
</script>

<template>
<div class="container">
    <div class="row justify-content-center">
        <div class="card bg-white" style="max-width: 800px;">
            <div class="row g-0">
                <div class="col-md-4">
                    <img :src="props.thumbnail" alt="" class="img-thumbnail float-start">
                </div>
                <div class="col-md-8">
                    <div class="card-header">
                        <div class="fs-6">{{ genre }}</div>      
                        <div class="card-title fs-3">{{ name }}</div>
                        <div>{{ access }}</div>
                    </div>
                    <div class="card-body">
                        <div>{{ catch }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>