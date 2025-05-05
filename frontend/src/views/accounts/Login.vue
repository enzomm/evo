<script setup lang="ts">
  import { RouterLink } from 'vue-router';
  import { reactive, ref } from 'vue';
  import { storeToRefs } from 'pinia';
  import { useToast } from '@/components/ui/toast/use-toast';
  import { useAuthStore } from '@/stores/auth.store';
  import { Loader2 } from 'lucide-vue-next';

  const { toast } = useToast();
  const authStore = useAuthStore();
  const { login } = authStore;
  const { errorMessage } = storeToRefs(authStore);
  const user = reactive({
    email: '',
    pass: '',
  });
  const loading = ref(false);

  const handleLogin = async () => {
    try {
      loading.value = true;
      await login({ username: user.email, password: user.pass });
      toast({
        title: 'Sucesso!',
        description: 'Bem-vindo(a) de volta!',
        variant: 'success',
      });
      errorMessage.value = '';
    } catch (error) {
      toast({
        title: 'Algo deu errado.',
        description: errorMessage.value,
        variant: 'destructive',
      });
    } finally {
      loading.value = false;
    }
  };
</script>
<template>
  <div class="flex h-svh w-full">
    <div class="hidden lg:flex lg:w-3/5">
      <div
        class="flex w-full items-center justify-center bg-gradient-to-tr from-blue-900 from-10% to-slate-950 to-90% p-5"
      >
        <div class="flex flex-col gap-6">
          <div class="flex flex-col gap-2">
            <h2 class="text-center text-4xl font-bold text-sky-500">
              Acesse a plataforma
            </h2>
            <p class="text-center text-xl font-normal text-gray-200">
              E experimente um novo mundo cheio de possibilidades
            </p>
          </div>
          <div class="grid place-items-center">
            <img class="" src="@/assets/login_draw.svg" />
          </div>
        </div>
      </div>
    </div>

    <div
      class="flex flex-1 flex-col items-center justify-center bg-gray-100 sm:p-8 lg:w-2/5"
    >
      <div class="relative w-full sm:w-auto">
        <div
          class="absolute inset-0 -skew-y-6 transform bg-gradient-to-r from-sky-500 to-indigo-300 shadow-lg sm:-rotate-6 sm:skew-y-0 sm:rounded-3xl"
        ></div>
        <div
          class="relative bg-white px-4 py-10 shadow-lg sm:rounded-3xl sm:p-20"
        >
          <div class="mx-auto max-w-md">
            <div class="relative flex flex-col items-center gap-8">
              <!-- <img src="@/assets/logo.png" alt="Logo"/> -->
              <h1 class="text-2xl font-semibold text-gray-600">
                Bem-vindo de volta
              </h1>
            </div>
            <div
              v-if="errorMessage"
              class="relative mt-2 flex flex-col items-center gap-8"
            >
              <span class="text-lg font-semibold text-red-500">
                {{ errorMessage }}
              </span>
            </div>
            <div class="divide-y divide-gray-200">
              <form
                @submit.prevent="handleLogin"
                class="space-y-4 py-8 text-base leading-6 text-gray-700 sm:text-lg sm:leading-7"
              >
                <div class="relative">
                  <input
                    v-model="user.email"
                    autocomplete="off"
                    id="email"
                    name="email"
                    type="text"
                    class="peer h-10 w-full border-b-2 border-gray-300 text-gray-900 placeholder-transparent focus:border-indigo-500 focus:outline-none"
                    placeholder="E-mail"
                    required
                  />
                  <label
                    for="email"
                    class="peer-placeholder-shown:text-gray-440 absolute -top-3.5 left-0 text-sm text-gray-600 transition-all peer-placeholder-shown:top-2 peer-placeholder-shown:text-base peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-gray-600"
                  >
                    E-mail
                  </label>
                </div>
                <div class="relative">
                  <input
                    v-model="user.pass"
                    autocomplete="off"
                    id="password"
                    name="password"
                    type="password"
                    class="peer h-10 w-full border-b-2 border-gray-300 text-gray-900 placeholder-transparent focus:border-indigo-500 focus:outline-none"
                    placeholder="Senha"
                    required
                  />
                  <label
                    for="password"
                    class="peer-placeholder-shown:text-gray-440 absolute -top-3.5 left-0 text-sm text-gray-600 transition-all peer-placeholder-shown:top-2 peer-placeholder-shown:text-base peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-gray-600"
                  >
                    Senha
                  </label>
                </div>
                <div class="relative flex w-full justify-center">
                  <button
                    v-if="loading"
                    class="mt-2 flex w-full justify-center rounded-md bg-indigo-400 px-2 py-2 text-white transition-all hover:scale-105 hover:bg-indigo-500 focus:outline-none"
                    disabled
                  >
                    <Loader2 class="mr-2 h-6 w-6 animate-spin" />
                  </button>
                  <button
                    v-else
                    type="submit"
                    class="mt-2 w-full rounded-md bg-indigo-400 px-2 py-2 text-white transition-all hover:scale-105 hover:bg-indigo-500 focus:outline-none"
                  >
                    Entrar
                  </button>
                </div>
              </form>
            </div>
          </div>

          <div class="relative flex w-full flex-col items-start gap-2">
            <RouterLink
              class="text-sm text-gray-400 transition-all hover:text-gray-500 hover:underline"
              to="#"
            >
              Esqueci a senha
            </RouterLink>
            <RouterLink
              class="text-sm text-gray-400 transition-all hover:text-gray-500 hover:underline"
              :to="{ name: 'register' }"
            >
              Criar conta
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
