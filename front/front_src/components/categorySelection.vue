<!-- src/components/categorySelection.vue -->
<script setup>
import { ref } from 'vue';
const emits = defineEmits(["updateFilteredEvents"]);
const props = defineProps({
  categories: Array,
  selectedCategories: Array
});

const categories = ref(props.categories);
const selectedCategories = ref(props.selectedCategories);

/**
 * Toggle the selection of a category without removing previously selected ones
 * @param {String} categoryName Name of the category
 */
const toggleCategory = (categoryName) => {
  const index = selectedCategories.value.indexOf(categoryName);
  if (index === -1) {
    // If not selected, add the category to selected categories
    selectedCategories.value.push(categoryName);
  } else {
    // If selected, remove the category from selected categories
    selectedCategories.value.splice(index, 1);
  }
};
</script>

<template>
  <div class="width-100">
    <h2 class="mb-3 category-title">Choose Categories</h2>
    <div class="d-flex flex-wrap">
      <button
          v-for="category in categories"
          :key="category"
          class="btn category-button"
          :class="{ 'selected': selectedCategories.includes(category) }"
          @click="toggleCategory(category)"
      >
        {{ category }}
      </button>
    </div>
    <button
        class="btn btn-success mt-3"
        @click="$emit('updateFilteredEvents', selectedCategories)"
    >
      Search Events
    </button>
  </div>
</template>

<style scoped>
/* Add your styles if needed */

/* Customized button styles */
.category-button {
  background-color: #fff; /* Set the background color to white */
  color: #007bff; /* Set the text color to blue */
  border: 1px solid #007bff; /* Set the border color to blue */
  margin: 0.5rem; /* Add margin for spacing */
}

.category-button.selected {
  background-color: #007bff; /* Set the background color to blue for selected buttons */
  color: #fff; /* Set the text color to white for selected buttons */
}

.category-title {
  color: #b30000; /* Darker red color */
  font-size: 1.5rem; /* Set the title font size */
  font-weight: bold; /* Set the title font weight to bold */
}
</style>
