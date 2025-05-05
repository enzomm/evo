import http from '@/services/http';

const UserService = {
  register: async (email: string, password: string) => {
    try {
      return await http.post('/users', { email, password });
    } catch (error: any) {
      if (error?.response?.status === 422 && error?.response?.data?.detail) {
        const validationErrors = error.response.data.detail
          .map((err: { msg: string }) => err.msg)
          .join(', ');
        throw new Error(validationErrors);
      }
      throw new Error('Erro desconhecido ao tentar realizar o cadastro.');
    }
  },
  getAllUsers: async () => {
    return await http.get('/users');
  },
};

export { UserService };
