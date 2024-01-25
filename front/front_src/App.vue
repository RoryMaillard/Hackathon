<script setup>
import homepage from './vues/homepage.vue';
import EventDetails from "@/vues/EventDetails.vue";
</script>

<template>
  <main>
      <Suspense>
        <router-view></router-view>
        <template #fallback>
          Loading...
        </template>
      </Suspense>

  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
