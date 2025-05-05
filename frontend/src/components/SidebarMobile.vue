<script setup lang="ts">
  import { RouterLink } from 'vue-router';
  import navItems from '@/data/navItems';
  import { LifeBuoy } from 'lucide-vue-next';
</script>

<template>
  <nav class="flex w-full flex-1 flex-col justify-between">
    <ul class="mt-4 flex flex-col gap-2 px-2">
      <li v-for="ni in navItems" class="flex justify-start">
        <RouterLink
          class="flex w-full items-center gap-3 rounded-lg px-3 py-2 text-zinc-700 transition hover:bg-slate-200 hover:text-zinc-900 dark:text-zinc-600 dark:hover:bg-slate-900 dark:hover:text-zinc-300"
          :to="ni.link"
        >
          <component :is="ni.icon" class="icon" size="22" stroke-width="2" />
          <span class="text-sm">{{ ni.title }}</span>
        </RouterLink>
      </li>
    </ul>

    <ul class="mb-2 mt-2 flex flex-col gap-2 px-2">
      <li class="flex items-center justify-start xl:w-full">
        <RouterLink
          class="flex w-full items-center gap-3 rounded-lg px-3 py-2 text-zinc-700 transition hover:bg-slate-200 hover:text-zinc-900 dark:text-zinc-600 dark:hover:bg-slate-900 dark:hover:text-zinc-300"
          to="/"
        >
          <LifeBuoy :size="22" :stroke-width="2" class="icon" />
          <span class="text-sm">Suporte</span>
        </RouterLink>
      </li>
    </ul>
  </nav>
</template>

<style scoped></style>
