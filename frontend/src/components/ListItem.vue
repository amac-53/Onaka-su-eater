<script setup lang="ts">
const props = defineProps<{name: string, access: string, thumbnail: string, genre: string, catch: string}>();
</script>

<template>
<div class="container">
    <div class="row justify-content-center">
        <div class="card bg-white" style="max-width: 800px;">
            <div class="row">
                <div class="col-4">
                    <img :src="props.thumbnail" class="img-thumbnail float-start">
                </div>
                <div class="col-8">
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