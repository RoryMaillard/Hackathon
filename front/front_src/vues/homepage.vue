<script setup>
import { ref } from 'vue';
import categorySelection from "../components/categorySelection.vue";
import eventsDisplay from "../components/eventsDisplay.vue";
import axios from "axios";
const emits = defineEmits(["updateFilteredEvents"]);

const categories = ref(await getCategories());
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
    url: "https://hackathonlogin2023.osc-fr1.scalingo.io/allcategories",
    headers: {
      'Content-Type': 'application/json',
    }
  }
  try{
    const categories = (await axios.request(configHTTP)).data.results.categories;
    return categories;
  }catch(error){
    console.error(error);
    return [];
  }
}

async function getFilteredEvents(categories){
  console.log(categories)
  const configHTTP = {
    method:"POST",
    url:"https://hackathonlogin2023.osc-fr1.scalingo.io/categories",
    data:{"categories_list" : categories },
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
    console.error(error);
    return [];
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
      <div class="mb-4 d-flex">
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
