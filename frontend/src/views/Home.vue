<script setup lang="ts">
  import DataTableUser from '@/components/tables/user/DataTable.vue';
  import { userColumns } from '@/components/tables/user/columns';
  import { ref, onMounted } from 'vue';
  import { UserService } from '@/services/user';
  import { toast } from '@/components/ui/toast/use-toast';

  const users = ref([]);

  onMounted(async () => {
    try {
      const response = await UserService.getAllUsers();
      users.value = response.data;
    } catch (error: any) {
      toast({
        title: 'Algo deu errado.',
        description: 'Não foi possível consultar os usuários cadastrados.',
        variant: 'destructive',
      });
    }
  });
</script>

<template>
  <DataTableUser :data="users" :columns="userColumns" />
</template>

<style scoped></style>
