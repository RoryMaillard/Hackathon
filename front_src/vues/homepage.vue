<script setup>
import { ref } from 'vue';
import categorySelection from "../components/categorySelection.vue";
import eventsDisplay from "../components/eventsDisplay.vue";
import axios from "axios";
const emits = defineEmits(["updateFilteredEvents"]);


const categories = ref([
  { name: 'Music' },
  { name: 'Art' },
]);
const selectedCategories = ref([]);
const events = ref(getFilteredEvents([]));

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

async function getFilteredEvents(categories){
  const configHTTP = {
    method:"GET",
    url:"http://localhost:5001/activites",
    headers:{
      'Content-Type': 'application/json'
    },
    withCredentials:true,
  }
  try{
    const events = (await axios.request(configHTTP)).data;
    console.log("events", events)
    return events;
  }catch(error){
    return [];
    alert(error);
  }

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