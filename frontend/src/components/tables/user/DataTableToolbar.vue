<script setup lang="ts">
  import type { Table } from '@tanstack/vue-table';
  import type { User } from '@/data/schema';
  import { Button } from '@/components/ui/button';
  import { Input } from '@/components/ui/input';
  import { computed } from 'vue';
  import { X } from 'lucide-vue-next';
  import DataTableViewOptions from './DataTableViewOptions.vue';

  interface DataTableToolbarProps {
    table: Table<User>;
  }
  const props = defineProps<DataTableToolbarProps>();
  const isFiltered = computed(
    () => props.table.getState().columnFilters.length > 0
  );
</script>

<template>
  <div class="flex items-center justify-between">
    <div class="flex flex-1 items-center space-x-2">
      <Input
        placeholder="Filtrar nomes..."
        :model-value="
          (table.getColumn('name')?.getFilterValue() as string) ?? ''
        "
        class="h-8 w-[150px] lg:w-[250px]"
        @input="table.getColumn('name')?.setFilterValue($event.target.value)"
      />

      <Button
        v-if="isFiltered"
        variant="ghost"
        class="h-8 px-2 lg:px-3"
        @click="table.resetColumnFilters()"
      >
        Reiniciar
        <X class="ml-2 h-4 w-4" />
      </Button>
    </div>
    <DataTableViewOptions :table="table" />
  </div>
</template>
