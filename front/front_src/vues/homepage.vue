<!-- src/vues/homepage.vue -->
<script>
import CategorySelection from "@/components/categorySelection.vue";
import axios from "axios";
import EventsDisplay from "@/components/eventsDisplay.vue";

export default {
  name: "homepage",
  components: { EventsDisplay, CategorySelection },
  data() {
    return {
      categories: [],
      selectedCategories: [],
      filteredEvents: [],
    };
  },
  methods: {
    async updateFilteredEvents(updatedSelectedCategories) {
      this.selectedCategories = updatedSelectedCategories;
      this.filteredEvents = await this.getFilteredEvents(updatedSelectedCategories);
    },

    async getFilteredEvents(categories) {
      const configHTTP = {
        method: "POST",
        url: `/api/categories`,
        data: { categories_list: categories },
        headers: {
          'Content-Type': 'application/json'
        }
      };
      try {
        const events = (await axios.request(configHTTP)).data.results;
        events.map((event) => {
          event.categories = this.getCategoriesListFromEvent(event);
          return event;
        });
        return events;
      } catch (error) {
        console.error(error);
        return [];
      }
    },
    async getCategories() {
      const configHTTP = {
        method: "GET",
        url: `/api/allcategories`,
        headers: {
          'Content-Type': 'application/json',
        }
      };
      try {
        const categories = (await axios.request(configHTTP)).data.results.categories;
        return categories;
      } catch (error) {
        console.error(error);
        return [];
      }
    },
    getCategoriesListFromEvent(event) {
      return Object.keys(event).reduce((acc, key) => {
        (key.startsWith("categorie_") && event[key] != null) ? acc.push(event[key]) : null;
        return acc;
      }, []);
    }
  },
  async beforeMount() {
    this.categories = await this.getCategories();
    this.filteredEvents = await this.getFilteredEvents([]);
  },
}
</script>

<template>

  <div class="container mt-5 homepage-container" :style="{ backgroundImage: `url('https://images.unsplash.com/photo-1630348637723-25d84aac0dd9?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')` }">
    <h1 class="mb-4 homepage-title">Cultural Events</h1>
    <div class="row">
      <div class="col-md-4 mb-4">
        <categorySelection
            :categories="categories"
            :selectedCategories="selectedCategories"
            :key="categories"
            @updateFilteredEvents="updateFilteredEvents"
        />
      </div>
      <div class="col-md-8">
        <eventsDisplay :filteredEvents="filteredEvents" :key="filteredEvents" />
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Add your styles if needed */
.homepage-title {
  color: #b30000; /* Darker red color */
  font-size: 2.5rem; /* Set the title font size */
  font-weight: bold; /* Set the title font weight to bold */
}
</style>
