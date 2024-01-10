<script setup>
import { ref } from 'vue';
import categorySelection from "../components/categorySelection.vue";
import eventsDisplay from "../components/eventsDisplay.vue";
const emits = defineEmits(["updateFilteredEvents"]);
const categories = ref([
  { name: 'Music' },
  { name: 'Art' },
]);

const selectedCategories = ref([]);
const events = ref([
  { name: 'Concert 1', categories: ['Music'] },
  { name: 'Art Exhibition', categories: ['Art'] },
]);

const filteredEvents = ref(events.value.slice(0));

/**
 * Updates the filtered events thanks to the new list of selected categories
 * @param {Array} updatedSelectedCategories New list of selected categories
 */
const updateFilteredEvents = (updatedSelectedCategories) => {
  selectedCategories.value = updatedSelectedCategories;
  if (selectedCategories.value.length === 0) {
    filteredEvents.value = events.value;
  } else {
    filteredEvents.value = events.value.filter((event) =>{
          return selectedCategories.value.every((category) => event.categories.includes(category))
        }
    );
  }
};

const exempleEvent = {categorie_1: "Activité à partager",
  categorie_2: "musique",
  categorie_3: "art",
  categorie_4: "cinéma",
  categorie_5: "bebe dringdring",
  trucAuPif: "ouinouin"
}

/**
 * Retrieve all the categories of an event and return them in a list
 * @param {Object} event
 * @returns {Array}
 */
function getCategoriesListFromEvent(event){
  return Object.keys(event).reduce((acc, key) =>{
    key.startsWith("categorie_")? acc.push(event[key]):null;
    return acc;
  }, []);
}
console.log("Toutes les categories devraient être ajoutées à la liste: ", getCategoriesListFromEvent(exempleEvent));
</script>


<template>
  <div>
    <div class="container mt-5">
      <h1 class="mb-4">Cultural Events</h1>
      <div class="mb-4">
       <categorySelection
            :categories="categories"
            :selectedCategories="selectedCategories"
            :key="categories"
            @updateFilteredEvents="updateFilteredEvents"
        />
      </div>
      <div>
        <eventsDisplay :filteredEvents="filteredEvents"
        :key="filteredEvents"/>
      </div>
    </div>
  </div>
</template>


<style scoped>

</style>