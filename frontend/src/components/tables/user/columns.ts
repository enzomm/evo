import type { ColumnDef } from '@tanstack/vue-table';
import type { User } from '@/data/schema';
import { h } from 'vue';
import DataTableColumnHeader from './DataTableColumnHeader.vue';

export const userColumns: ColumnDef<User>[] = [
  {
    accessorKey: 'name',
    header: ({ column }) =>
      h(DataTableColumnHeader, { column, title: 'Nome' }),
    cell: ({ row }) =>
      h(
        'span',
        { class: 'max-w-[500px] truncate' },
        row.getValue('name')
      ),
    enableSorting: true,
    enableHiding: false,
  },
  {
    accessorKey: 'email',
    header: ({ column }) =>
      h(DataTableColumnHeader, { column, title: 'Email' }),
    cell: ({ row }) =>
      h(
        'span',
        { class: 'max-w-[500px] truncate font-medium' },
        row.getValue('email')
      ),
    enableSorting: true,
    enableHiding: true,
  },
];
