<!-- src/components/EventDisplay.vue -->
<template>
  <div class="container mt-4">
    <h2 class="mb-4 event-title">Événements à venir</h2>
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
      <div v-for="event in filteredEvents" :key="event.id" class="col">
        <router-link :to="{ name: 'eventDetails', params: { id: event.id_manif.toString() }}" class="text-decoration-none">
          <div class="card h-100">
            <img :src="event.media_url" class="card-img-top" alt="Event Image">
            <div class="card-body">
              <h5 class="card-title">{{ event.nom }}</h5>
              <p class="card-text">{{ event.description.slice(0, 100) }}...</p>
            </div>
            <div class="card-footer">
              <small class="text-muted">{{ event.date }} - de {{ event.heure_debut }} à {{ event.heure_fin }}</small>
            </div>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  filteredEvents: Array,
});

const filteredEvents = ref(props.filteredEvents);
</script>

<style scoped>
/* Add your styles if needed */
.event-title {
  color: #b30000; /* Darker red color */
  font-size: 2rem; /* Set the title font size */
  font-weight: bold; /* Set the title font weight to bold */
}
</style>
