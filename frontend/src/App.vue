<script setup lang="ts">
  import { RouterView } from 'vue-router';
  import Toaster from '@/components/ui/toast/Toaster.vue';
  import http from '@/services/http';
  import {
    setHeaderBearerAuthorization,
    setAxiosRetry,
  } from '@/services/interceptors';
  setHeaderBearerAuthorization([http]);
  setAxiosRetry([http]);
</script>

<template>
  <RouterView />
  <Toaster />
</template>

<style scoped></style>
