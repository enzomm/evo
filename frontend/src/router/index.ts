import { useAuthStore } from '@/stores/auth.store';
import { storeToRefs } from 'pinia';
import { createWebHistory, createRouter } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: () => import('@/views/DashBoard.vue'),
    meta: { authRequire: true },
    children: [
      {
        path: '/',
        name: 'home',
        component: () => import('@/views/Home.vue'),
        meta: { authRequire: true },
      },
    ],
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/accounts/Login.vue'),
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/accounts/Register.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to: any, from: any, next: any) => {
  const authStore = useAuthStore();
  const { isAuthenticated } = storeToRefs(authStore);
  if (!isAuthenticated.value) await authStore.authenticate();
  if (to.meta.authRequire && !isAuthenticated.value) {
    next({ name: 'login', query: { redirect: to.name } });
  } else {
    if (to.name === 'login' && isAuthenticated.value) {
      next({ name: 'home' });
    } else next();
  }
});

export default router;
