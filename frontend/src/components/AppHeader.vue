<script setup lang="ts">
import { RouterLink } from 'vue-router';
</script>

<template>
    <header class="fixed-top">
      <nav class="navbar navbar-light bg-dark">
        <div class="container-fluid">
        <RouterLink class="text-white navbar-brand" to="/">
          <img src="/src/logo.svg" alt="">
            Onaka-su-eater
        </RouterLink>
        </div>
      </nav>
  </header>
</template>