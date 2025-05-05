<script setup lang="ts">
  import { RouterLink } from 'vue-router';
  import { Avatar } from '@/components/ui/avatar';
  import {
    Cloud,
    CreditCard,
    Github,
    Keyboard,
    LifeBuoy,
    LogOut,
    Mail,
    MessageSquare,
    Plus,
    PlusCircle,
    Settings,
    User,
    UserPlus,
    Users,
    Bell,
    PanelLeftOpen,
    PanelLeftClose,
    UserRound,
    Menu,
    SunMoon,
  } from 'lucide-vue-next';
  import { Button } from '@/components/ui/button';
  import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuPortal,
    DropdownMenuSeparator,
    DropdownMenuShortcut,
    DropdownMenuSub,
    DropdownMenuSubContent,
    DropdownMenuSubTrigger,
    DropdownMenuTrigger,
  } from '@/components/ui/dropdown-menu';
  import { Toggle } from '@/components/ui/toggle';
  import {
    Sheet,
    SheetContent,
    SheetHeader,
    SheetTitle,
    SheetTrigger,
    SheetClose,
  } from '@/components/ui/sheet';
  import SidebarMobile from '@/components/SidebarMobile.vue';
  import { useAuthStore } from '@/stores/auth.store';

  const authStore = useAuthStore();
  const { logout } = authStore;
  const isOpen = defineModel('toggleMenu', { required: true });

  function handleToggleMenu() {
    return (isOpen.value = !isOpen.value);
  }

  function handleToggleTheme() {
    document.documentElement.classList.toggle('dark');
  }

  function Logout() {
    logout();
  }
</script>

<template>
  <header
    class="flex h-12 flex-row items-center justify-between gap-2 border-b-2 border-neutral-300 bg-neutral-200 transition-all dark:border-neutral-800 dark:bg-neutral-900"
  >
    <div class="">
      <Button
        @click="handleToggleMenu()"
        variant="outline"
        class="ml-1 hidden bg-neutral-200 p-2 text-zinc-900 shadow-none hover:bg-neutral-100 hover:text-sky-500 dark:bg-neutral-900 dark:text-zinc-300 dark:hover:bg-neutral-800 dark:hover:text-sky-500 xl:inline-block"
      >
        <PanelLeftClose v-if="isOpen" :size="20" :stroke-width="2" />
        <PanelLeftOpen v-else :size="20" :stroke-width="2" />
      </Button>
      <Sheet>
        <SheetTrigger class="md:hidden">
          <Button
            variant="outline"
            class="ml-1 bg-neutral-200 p-2 text-zinc-900 shadow-none hover:bg-neutral-100 hover:text-sky-500 dark:bg-neutral-900 dark:text-zinc-300 dark:hover:bg-neutral-800 dark:hover:text-sky-500"
          >
            <Menu :size="20" :stroke-width="2" />
          </Button>
        </SheetTrigger>
        <SheetContent class="bg-slate-100 dark:bg-slate-950" side="left">
          <SheetHeader>
            <SheetTitle>Menu</SheetTitle>
          </SheetHeader>
          <SheetClose as-child>
            <SidebarMobile />
          </SheetClose>
        </SheetContent>
      </Sheet>
    </div>

    <div class="inline-flex items-center justify-center gap-4 p-2">
      <Toggle
        @click="handleToggleTheme"
        class="bg-neutral-200 text-zinc-800 shadow-none hover:bg-neutral-100 hover:text-sky-500 dark:bg-neutral-900 dark:text-zinc-300 dark:hover:bg-neutral-800 dark:hover:text-sky-500"
      >
        <SunMoon :size="22" :stroke-width="2" />
      </Toggle>

      <DropdownMenu>
        <DropdownMenuTrigger>
          <Button
            variant="outline"
            class="bg-neutral-200 text-zinc-800 shadow-none hover:bg-neutral-100 hover:text-sky-500 dark:bg-neutral-900 dark:text-zinc-300 dark:hover:bg-neutral-800 dark:hover:text-sky-500"
            size="icon"
          >
            <Bell class="" :size="20" :stroke-width="2" />
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent>
          <DropdownMenuLabel>Notifications</DropdownMenuLabel>
          <DropdownMenuSeparator />
          <DropdownMenuItem>Message 1</DropdownMenuItem>
          <DropdownMenuItem>Message 2</DropdownMenuItem>
          <DropdownMenuItem>Message 3</DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>

      <DropdownMenu>
        <DropdownMenuTrigger>
          <Avatar size="sm">
            <UserRound :size="22" :stroke-width="2" />
          </Avatar>
        </DropdownMenuTrigger>
        <DropdownMenuContent class="w-56">
          <DropdownMenuLabel>My Account</DropdownMenuLabel>
          <DropdownMenuSeparator />
          <DropdownMenuGroup>
            <DropdownMenuItem>
              <User class="mr-2 h-4 w-4" />
              <span>Profile</span>
              <DropdownMenuShortcut>⇧⌘P</DropdownMenuShortcut>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <CreditCard class="mr-2 h-4 w-4" />
              <span>Billing</span>
              <DropdownMenuShortcut>⌘B</DropdownMenuShortcut>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <Settings class="mr-2 h-4 w-4" />
              <span>Settings</span>
              <DropdownMenuShortcut>⌘S</DropdownMenuShortcut>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <Keyboard class="mr-2 h-4 w-4" />
              <span>Keyboard shortcuts</span>
              <DropdownMenuShortcut>⌘K</DropdownMenuShortcut>
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuItem>
            <LifeBuoy class="mr-2 h-4 w-4" />
            <span>Support</span>
          </DropdownMenuItem>
          <DropdownMenuSeparator />
          <DropdownMenuItem @click="Logout()">
            <LogOut class="mr-2 h-4 w-4" />
            <span>Log out</span>
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  </header>
</template>

<style scoped></style>
