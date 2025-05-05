<script setup lang="ts">
  import { RouterLink } from 'vue-router';
  import { LifeBuoy } from 'lucide-vue-next';
  import navItems from '@/data/navItems';

  const isOpen = defineModel('toggleMenu', { required: true });
</script>

<template>
  <aside
    class="hidden bg-slate-100 transition-all dark:bg-slate-950 md:flex md:w-16 md:flex-col"
    :class="[isOpen ? 'xl:w-56' : 'xl:w-16']"
  >
    <header class="flex h-12 items-center justify-center bg-sky-500 shadow-md">
      <a
        href="#"
        class="hidden text-2xl font-bold text-zinc-300"
        :class="[isOpen ? 'xl:flex' : 'xl:hidden']"
      >
        <!-- <img class="h-10" src="@/assets/logo.png" alt="Logo"/> -->
      </a>
      <a
        href="#"
        class="text-2xl font-bold text-zinc-300"
        :class="[isOpen ? 'xl:hidden' : 'xl:flex']"
      >
        <!-- <img class="h-10" src="@/assets/logo_icon.png" alt="Icone Logo"/> -->
      </a>
    </header>

    <nav
      class="flex flex-1 flex-col justify-between border-r-2 border-slate-300 shadow-2xl dark:border-slate-900"
    >
      <ul class="mt-4 flex flex-col gap-2 px-2">
        <li v-for="ni in navItems" class="flex justify-start">
          <RouterLink
            class="flex w-full items-center gap-3 rounded-lg px-3 py-2 text-zinc-700 transition hover:bg-slate-200 hover:text-zinc-900 dark:text-zinc-600 dark:hover:bg-slate-900 dark:hover:text-zinc-300"
            :to="ni.link"
          >
            <component :is="ni.icon" class="icon" size="22" stroke-width="2" />
            <span v-if="isOpen" class="hidden text-sm xl:inline-block">
              {{ ni.title }}
            </span>
          </RouterLink>
        </li>
      </ul>

      <ul class="mb-2 mt-4 flex flex-col gap-2 px-2">
        <li class="flex items-center justify-start xl:w-full">
          <RouterLink
            class="flex w-full items-center gap-3 rounded-lg px-3 py-2 text-zinc-700 transition hover:bg-slate-200 hover:text-zinc-900 dark:text-zinc-600 dark:hover:bg-slate-900 dark:hover:text-zinc-300"
            to="/"
          >
            <LifeBuoy :size="22" :stroke-width="2" class="icon" />
            <span v-if="isOpen" class="hidden text-sm xl:inline-block">
              Suporte
            </span>
          </RouterLink>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<style scoped></style>
