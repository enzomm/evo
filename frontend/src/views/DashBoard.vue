<script setup lang="ts">
  import { RouterView } from 'vue-router';
  import Sidebar from '@/components/Sidebar.vue';
  import Header from '@/components/Header.vue';
  import { ref } from 'vue';

  const isOpen = ref<boolean>(true);
</script>

<template>
  <div class="flex h-svh max-h-svh">
    <Sidebar v-model:toggleMenu="isOpen" />
    <main class="flex flex-1 flex-col bg-neutral-50 dark:bg-neutral-950">
      <Header v-model:toggleMenu="isOpen" />
      <section class="flex flex-col overflow-y-auto p-4">
        <RouterView />
      </section>
    </main>
  </div>
</template>

<style scoped></style>
