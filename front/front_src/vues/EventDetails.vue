<!-- src/components/EventDetails.vue -->
<template>
  <div>
    <h1>{{ event.nom }}</h1>
    <p><strong>Available dates:</strong>
      <select v-model="selectedDate" @change="updateSchedules">
        <option v-for="date in allDates" :key="date" :value="date">{{ date }}</option>
      </select>
    </p>
    <p :key="selectedDate"><strong>Schedules available on that date:</strong> {{ getSchedulesByDate(selectedDate).join(', ') }}</p>

    <p><strong>Location:</strong> {{ event.lieu }}, {{ event.lieu_quartier }}, {{ event.ville }}</p>
    <p><strong>Description:</strong> {{ event.description }}</p>
    <p><strong>Price:</strong> {{ event.precisions_tarifs }}</p>
    <p><strong>Organizers:</strong> {{ event.organisateurs }}</p>
    <p><strong>Website:</strong> <a :href="event.url_site" target="_blank">{{ event.url_site }}</a></p>
    <p><img :src="event.media_url" alt="Event Image" style="max-width: 100%; height: auto;"></p>
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
      // Update the filtered schedules based on the selected date
      this.filteredSchedules = this.getSchedulesByDate(this.selectedDate);
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
/* Add your styles if needed */
</style>