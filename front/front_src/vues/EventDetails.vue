<!-- src/vues/EventDetails.vue -->
<template>
  <div class="container mt-4">
    <div class="card mb-4" style="background-color: #e3c080; border: 2px solid #592f14;">
      <img :src="event.media_url" alt="Event Image" class="card-img-top">
      <div class="card-body" style="color: #592f14;">
        <h2 class="card-title event-title">{{ event.nom }}</h2>

        <!-- Available Dates Dropdown -->
        <div class="mb-3">
          <label for="dateSelector" class="form-label"><strong>Dates disponibles:</strong></label>
          <select v-model="selectedDate" @change="updateSchedules" class="form-select" id="dateSelector" style="background-color: #e3c080;">
            <option v-for="date in allDates" :key="date" :value="date">{{ date }}</option>
          </select>
        </div>

        <!-- Schedules Section -->
        <div class="mb-3">
          <strong>Horaires disponibles le {{ selectedDate }}:</strong>
          <p v-if="filteredSchedules.length">{{ filteredSchedules.join(', ') }}</p>
          <p v-else>Aucun horaire disponible pour cette date.</p>
        </div>

        <!-- Event Details -->
        <div class="mb-3">
          <strong>Lieu:</strong> {{ event.lieu }}, {{ event.lieu_quartier }}, {{ event.ville }}
        </div>
        <div class="mb-3">
          <strong>Description:</strong> {{ event.description }}
        </div>
        <div class="mb-3">
          <strong>Prix:</strong> {{ event.precisions_tarifs }}
        </div>
        <div class="mb-3">
          <strong>Organisateurs:</strong> {{ event.organisateurs }}
        </div>
        <div class="mb-3">
          <strong>Site web:</strong> <a :href="event.url_site" target="_blank">{{ event.url_site }}</a>
        </div>

        <!-- Back to Homepage Button -->
        <div class="text-center">
          <button @click="goToHomepage" class="btn btn-dark" style="background-color: #592f14;">Retour à l'accueil</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    id: String,
    eventDetails: String,
  },
  data() {
    return {
      event: null,
      eventWithAllDates: null,
      selectedDate: null,
      filteredSchedules: [],
    };
  },
  async beforeMount() {
    await this.fetchEventDetails();
  },
  watch: {
    selectedDate: 'updateSchedules',
  },
  methods: {
    async fetchEventDetails() {
      try {
        const response = await axios.get(`/api/activity/${this.id}`);
        this.eventWithAllDates = response.data.results;
        this.event = this.eventWithAllDates[0];
        this.selectedDate = this.event.date;
        this.updateSchedules();
      } catch (error) {
        console.error(error);
      }
    },
    updateSchedules() {
      this.filteredSchedules = this.getSchedulesByDate(this.selectedDate);
    },
    goToHomepage() {
      // Use $router instead of useRouter
      this.$router.push('/');
    },
    getSchedulesByDate(date) {
      const schedules = this.eventWithAllDates
          .filter((event) => event.date === date)
          .map((event) => `${event.heure_debut} - ${event.heure_fin}`);
      return [...new Set(schedules)];
    },
  },
  computed: {
    allDates() {
      return [...new Set(this.eventWithAllDates.map((event) => event.date))];
    },
  },
};
</script>


<style scoped>
/* Customized title style */
.event-title {
  color: #592f14; /* Dark brown color */
  font-size: 2.5rem; /* Set the title font size */
  font-weight: bold; /* Set the title font weight to bold */
}
/* Add your styles if needed */
</style>
