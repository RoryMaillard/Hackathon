<!-- src/components/categorySelection.vue -->
<template>
  <div class="width-100">
    <h2>Catégories</h2>
    <button
        v-for="category in categories"
        :key="category"
        class="btn mb-1 inline-text"
        :class="{ 'btn-secondary': !selectedCategories.includes(category), 'btn-primary': selectedCategories.includes(category) }"
        @click="toggleCategory(category)"
    >
      {{ category }}
    </button>
    <button class="btn btn-success" @click="$emit('updateFilteredEvents', selectedCategories)">Rechercher</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const emits = defineEmits(['updateFilteredEvents'])
const props = defineProps({
  categories: Array,
  selectedCategories: Array,
});

const selectedCategories = ref(props.selectedCategories);

const toggleCategory = (categoryName) => {
  const index = selectedCategories.value.indexOf(categoryName);
  index === -1 ? selectedCategories.value.push(categoryName) : selectedCategories.value.splice(index, 1);
};

</script>

<style scoped>
.mr-1 {
  margin-right: 1rem;
}
.mb-1 {
  margin-bottom: 1rem;
}
.inline-text {
  white-space: nowrap;
  text-align: center;
}
.width-100 {
  width: 100%;
}
/* Add the following styles for button background colors */
.btn-secondary {
  background-color: #eee; /* Change this to your preferred color */
  color: #000000; /* Change this to your preferred text color */
}
.btn-primary {
  background-color: #007bff; /* Change this to your preferred color */
  color: #ffffff; /* Change this to your preferred text color */
}
</style>
