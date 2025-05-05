<script setup lang="ts">
  import { RouterLink } from 'vue-router';
  import { Button } from '@/components/ui/button';
  import {
    FormControl,
    FormDescription,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
  } from '@/components/ui/form';
  import { vAutoAnimate } from '@formkit/auto-animate';
  import { toTypedSchema } from '@vee-validate/zod';
  import { useForm } from 'vee-validate';
  import * as z from 'zod';
  import { Input } from '@/components/ui/input';
  import { toast } from '@/components/ui/toast/use-toast';
  import { UserService } from '@/services/user';
  import { useRouter } from 'vue-router';
  import { ref } from 'vue';
  import { Loader2 } from 'lucide-vue-next';

  const router = useRouter();
  const loading = ref(false);

  const formSchema = toTypedSchema(
    z.object({
      name: z
        .string()
        .min(3, {
          message: 'Deve ter pelo menos 3 caracteres.',
        })
        .max(64, {
          message: 'Não deve ter mais de 64 caracteres.',
        }),
      email: z
        .string()
        .email({ message: 'Deve ser um e-mail válido.' })
        .min(3, {
          message: 'Deve ter pelo menos 3 caracteres.',
        })
        .max(64, {
          message: 'Não deve ter mais de 64 caracteres.',
        }),
      password: z
        .string()
        .min(8, { message: 'A senha deve ter pelo menos 8 caracteres.' })
        .max(64, { message: 'A senha não deve ter mais de 64 caracteres.' })
        .regex(/[A-Z]/, {
          message: 'A senha deve conter pelo menos uma letra maiúscula.',
        })
        .regex(/[a-z]/, {
          message: 'A senha deve conter pelo menos uma letra minúscula.',
        })
        .regex(/[0-9]/, {
          message: 'A senha deve conter pelo menos um número.',
        })
        .regex(/[@$!%*?&#]/, {
          message: 'A senha deve conter pelo menos um caractere especial.',
        }),
    })
  );

  const { isFieldDirty, handleSubmit } = useForm({
    validationSchema: formSchema,
  });

  const onSubmit = handleSubmit(async (values) => {
    loading.value = true;
    try {
      await UserService.register(values.name, values.email, values.password);
      toast({
        title: 'Sucesso!',
        description: 'Cadastro concluído! Agora faça login na sua conta.',
        variant: 'success',
      });
      router.push({ name: 'login' });
    } catch (error: any) {
      toast({
        title: 'Algo deu errado.',
        description: error.message || 'Não foi possível concluir o cadastro.',
        variant: 'destructive',
      });
    } finally {
      loading.value = false;
    }
  });
</script>
<template>
  <div class="flex h-svh w-full">
    <div class="hidden lg:flex lg:w-3/5">
      <div
        class="flex w-full items-center justify-center bg-gradient-to-tr from-blue-900 from-10% to-slate-950 to-90% p-5"
      >
        <div class="flex flex-col items-center justify-center gap-6">
          <div class="flex flex-col gap-2">
            <h2 class="text-center text-4xl font-bold text-sky-500">
              Registre-se na plataforma
            </h2>
            <p class="text-center text-xl font-normal text-gray-200">
              Para descobrir um novo mundo cheio de possibilidades
            </p>
          </div>
          <div class="grid place-items-center">
            <img src="@/assets/register_draw.svg" />
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
                Quero me registrar
              </h1>
            </div>
            <div class="divide-y divide-gray-200">
              <form class="grid items-start gap-4 px-4 py-8" @submit="onSubmit">
                <FormField
                  v-slot="{ componentField }"
                  name="name"
                  :validate-on-blur="!isFieldDirty"
                  class="grid gap-2"
                >
                  <FormItem v-auto-animate>
                    <FormLabel>Nome</FormLabel>
                    <FormControl>
                      <Input
                        type="text"
                        placeholder="Meu Nome..."
                        v-bind="componentField"
                        required
                        autocomplete="off"
                      />
                    </FormControl>
                    <FormDescription>Qual o seu nome?</FormDescription>
                    <FormMessage />
                  </FormItem>
                </FormField>
                <FormField
                  v-slot="{ componentField }"
                  name="email"
                  :validate-on-blur="!isFieldDirty"
                  class="grid gap-2"
                >
                  <FormItem v-auto-animate>
                    <FormLabel>Email</FormLabel>
                    <FormControl>
                      <Input
                        type="email"
                        placeholder="meu@email.com"
                        v-bind="componentField"
                        required
                        autocomplete="off"
                      />
                    </FormControl>
                    <FormDescription>Qual o seu email?</FormDescription>
                    <FormMessage />
                  </FormItem>
                </FormField>
                <FormField
                  v-slot="{ componentField }"
                  name="password"
                  :validate-on-blur="!isFieldDirty"
                  class="grid gap-2"
                >
                  <FormItem v-auto-animate>
                    <FormLabel>Senha</FormLabel>
                    <FormControl>
                      <Input
                        type="password"
                        placeholder="Digite sua senha"
                        v-bind="componentField"
                        required
                        autocomplete="off"
                      />
                    </FormControl>
                    <FormDescription>Escolha uma senha segura.</FormDescription>
                    <FormMessage />
                  </FormItem>
                </FormField>
                <Button type="submit" :disabled="loading">
                  <template #default>
                    <span v-if="!loading">Enviar</span>
                    <Loader2 v-else class="animate-spin" />
                  </template>
                </Button>
              </form>
            </div>
          </div>

          <div class="relative flex w-full flex-col items-start gap-2">
            <RouterLink
              class="text-sm text-gray-400 transition-all hover:text-gray-500 hover:underline"
              :to="{ name: 'login' }"
            >
              Entrar
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
