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
    url:"http://127.0.0.1:5000/activites",
    headers:{
      'Content-Type': 'application/json'
    }
  }
  try{
    const events = (await axios.request(configHTTP));
    console.log("events", events)
    return [{"accueil_enfant":"non","adresse":"1 Rue Eugène Thomas","annule":"non","categorie_1":"Activité à partager","categorie_2":null,"categorie_3":null,"categorie_4":null,"categorie_5":null,"code_postal":"44300","complet":"non","courriel":null,"date":"2024-02-08","date_report":null,"description":"Un atelier en petit groupe pour échanger, partager, pratiquer et améliorer votre français en toute convivialité.","emetteur":"BIBLIOTHEQUE DE NANTES","gratuit":"oui","heure_debut":"14:30","heure_fin":null,"id_manif":"40494","info_suppl":null,"libelle_courriel":null,"libelle_site":null,"libelle_telephone":null,"lien_agenda":"https://metropole.nantes.fr/infonantes/agenda/40494","lieu":"Médiathèque Luce Courville","lieu_quartier":"Nantes Nord","lieu_siteweb":"http://bm.nantes.fr","lieu_tel":"02 40 41 53 50","media_url":"https://metropole.nantes.fr//banque/public/images/culture/c/40494-1-conversation-en-francais.jpg","nom":"Conversation en français","organisateurs":null,"precisions_public":"Tout public","precisions_tarifs":null,"reporte":"non","rubrique":"Culture","telephone":null,"url_site":null,"ville":"Nantes"}]
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