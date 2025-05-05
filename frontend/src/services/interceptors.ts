import { useAuthStore } from '@/stores/auth.store';
import { AxiosHeaders, AxiosError, AxiosInstance } from 'axios';

export const setHeaderBearerAuthorization = (apiList: AxiosInstance[]) => {
  apiList.forEach((apiInstance) => {
    apiInstance.interceptors.request.use((config) => {
      const authStore = useAuthStore();
      const accessToken = authStore.getItem('access_token');
      if (!accessToken) return config;
      if (config.headers) {
        config.headers['Authorization'] = 'Bearer ' + accessToken;
      } else {
        config.headers = new AxiosHeaders();
        config.headers.set('Authorization', 'Bearer ' + accessToken);
      }
      return config;
    });
  });
};

export const setAxiosRetry = (apiList: AxiosInstance[]) => {
  apiList.forEach((apiInstance) => {
    apiInstance.interceptors.response.use(
      (response) => {
        return response;
      },
      async (error: AxiosError) => {
        if (
          error?.config &&
          error?.response?.status === 401 &&
          error?.config?.headers?.Authorization
        ) {
          if (error?.config?.url?.includes('refresh_token'))
            return Promise.reject(error);
          const originalConfig = error.config;
          const authStore = useAuthStore();
          try {
            await authStore.silentRefresh();
            if (originalConfig.headers) {
              const accessToken = authStore.getItem('access_token');
              originalConfig.headers.Authorization = 'Bearer ' + accessToken;
            }
            return apiInstance.request(originalConfig);
          } catch (_error) {
            await authStore.logout();
          }
        }
        return Promise.reject(error);
      }
    );
  });
};
