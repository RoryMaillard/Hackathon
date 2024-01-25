<!-- src/vues/homepage.vue -->
<template>
  <div>
    <div class="container mt-5">
      <h1 class="mb-4">Cultural Events</h1>
      <categorySelection
          :categories="categories"
          :selectedCategories="selectedCategories"
          :key="categories"
          @updateFilteredEvents="updateFilteredEvents"
      />
      <div class="mt-4">
        <eventsDisplay :filteredEvents="filteredEvents" :key="filteredEvents" />
      </div>
    </div>
  </div>
</template>

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
          "Content-Type": "application/json",
        },
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
          "Content-Type": "application/json",
        },
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
        key.startsWith("categorie_") && event[key] != null ? acc.push(event[key]) : null;
        return acc;
      }, []);
    },
  },
  async beforeMount() {
    this.categories = await this.getCategories();
    this.filteredEvents = await this.getFilteredEvents([]);
  },
};
</script>
