import http from '@/services/http';

const Auth = {
  login: async (email: string, password: string) => {
    const params = new URLSearchParams();
    params.append('username', email);
    params.append('password', password);
    return await http.post('/auth/token', params);
  },
  refresh: async (token: string) => {
    return await http.post(`/auth/refresh_token?token=${token}`);
  },
  me: async () => {
    return await http.get('/auth/me');
  },
  webhook: async (payload: any) => {
    return await http.post(
      'https://evoflow.evotalks.com.br/webhook/registerLogin',
      payload
    );
  },
};

export { Auth };
