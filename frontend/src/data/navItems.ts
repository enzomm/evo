import type { NavItem } from '@/types/Sidebar';
import { h } from 'vue';
import { reactive } from 'vue';
import { LayoutDashboard } from 'lucide-vue-next';

const navItems = reactive<NavItem[]>([
  { title: 'Dashboard', icon: h(LayoutDashboard), link: '/' },
]);

export default navItems;
