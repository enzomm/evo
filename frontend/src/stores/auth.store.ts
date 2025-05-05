import { Auth } from '@/services/auth';
import type { WebStorage } from '@/types/WebStorage';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

interface UserLogin {
  username: string;
  password: string;
}

export const useAuthStore = defineStore('auth', () => {
  const router = useRouter();
  const route = useRoute();
  const isAuthenticated = ref(false);
  const errorMessage = ref('');

  async function authenticate() {
    const token = getItem('access_token');
    if (!token) return false;
    try {
      const user = await getUser();
      if (user) {
        isAuthenticated.value = true;
      } else {
        isAuthenticated.value = false;
      }
      return true;
    } catch (error) {
      isAuthenticated.value = false;
      return Promise.reject(error);
    }
  }

  async function login({ username, password }: UserLogin) {
    try {
      const { data } = await Auth.login(username, password);
      if (data?.access_token) {
        const { access_token, refresh_token } = data;
        setItem('access_token', access_token);
        setItem('refresh_token', refresh_token);
        const user = await getUser();
        isAuthenticated.value = true;

        await sendLoginWebhook(user);
        if (!route.query?.redirect) {
          router.push({ name: 'home' });
        } else {
          router.push({ name: String(route.query?.redirect) });
        }
      }
    } catch (error: any) {
      if (error?.response) {
        const { data } = error.response;
        errorMessage.value = data?.detail;
        throw new Error(data?.detail);
      }
    }
  }

  async function sendLoginWebhook(user: any) {
    try {
      const payload = {
        id: user.id,
        name: 'test',
        email: user.email,
        loginAt: Math.floor(Date.now() / 1000),
      };

      await Auth.webhook(payload);
      console.log('Webhook enviado com sucesso:', payload);
    } catch (error) {
      console.error('Erro ao enviar o webhook:', error);
    }
  }

  async function logout() {
    clearStorage();
    isAuthenticated.value = false;
    router.push({ name: 'login' });
  }

  async function silentRefresh() {
    try {
      const refreshToken = getItem('refresh_token');
      const { data } = await Auth.refresh(refreshToken);
      if (data.access_token) {
        const { access_token } = data;
        setItem('access_token', access_token);
      }
    } catch (error) {
      return Promise.reject(error);
    }
  }

  async function getUser() {
    try {
      const { data } = await Auth.me();
      if (data?.id) {
        setItem('user_data', JSON.stringify(data));
        return data;
      }
    } catch (error) {
      return Promise.reject(error);
    }
  }

  const getItem = (key: WebStorage) => {
    return localStorage.getItem(key) || '';
  };

  const setItem = (key: WebStorage, content: string) => {
    localStorage.setItem(key, content);
  };

  const removeItem = (key: WebStorage) => {
    localStorage.removeItem(key);
  };

  const clearStorage = () => localStorage.clear();

  return {
    errorMessage,
    isAuthenticated,
    authenticate,
    login,
    logout,
    silentRefresh,
    getItem,
    setItem,
    removeItem,
  };
});
