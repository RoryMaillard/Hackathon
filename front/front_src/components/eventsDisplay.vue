<script setup>
import { ref } from 'vue';
const props = defineProps({
  filteredEvents:Array
})
const filteredEvents = ref(props.filteredEvents);
console.log(filteredEvents);
</script>

<template>
  <h2>Filtered Events</h2>
  <ul class="list-group">
    <li class="list-group-item" v-for="event in filteredEvents" :key="event.id">
      {{ event.nom }} - {{ event.categories.join(", ") }}
    </li>
  </ul>
</template>

<style scoped>

</style>