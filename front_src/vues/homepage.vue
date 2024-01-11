<script setup>
import { ref } from 'vue';
import categorySelection from "../components/categorySelection.vue";
import eventsDisplay from "../components/eventsDisplay.vue";
import axios from "axios";
const emits = defineEmits(["updateFilteredEvents"]);

const categories = ref([
  { name: 'Activité à partager' },
  { name: 'Enfant' },
  { name: 'Atelier' },
  { name: 'Lecture' },
]);
const selectedCategories = ref([]);

const filteredEvents = ref(await getFilteredEvents([]));


/**
 * Updates the filtered events thanks to the new list of selected categories
 * @param {Array} updatedSelectedCategories New list of selected categories
 */
const updateFilteredEvents = async (updatedSelectedCategories) => {
  selectedCategories.value = updatedSelectedCategories;
  filteredEvents.value = await getFilteredEvents(updatedSelectedCategories);
  if (selectedCategories.value.length === 0) {
  } else {
    filteredEvents.value = filteredEvents.value.filter((event) =>{
          return selectedCategories.value.every((category) => event.categories.includes(category))
        }
    );
  }
};

async function getCategories() {
  const configHTTP = {
    method: "GET",
    url: "http://localhost:5001/categories",
    headers: {
      'Content-Type': 'application/json'
    }
  }
  try{
    const categories = (await axios.request(configHTTP)).data.results.categories;
    return categories;
  }catch(error){
    return [];
    alert(error);
  }
}

async function getFilteredEvents(categories){
  const configHTTP = {
    method:"GET",
    url:"http://localhost:5001/activites",
    headers:{
      'Content-Type': 'application/json'
    }
  }
  try{
    const events = (await axios.request(configHTTP)).data.results;
    events.map((event)=> {
      event.categories = getCategoriesListFromEvent(event)
      return event});
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
    (key.startsWith("categorie_") && event[key]!=null)? acc.push(event[key]):null;
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