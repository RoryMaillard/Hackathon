<script setup>
import { ref } from 'vue';
const emits = defineEmits(["updateFilteredEvents"]);
const props = defineProps({
    categories: Array,
    selectedCategories:Array
  })

const categories = ref(props.categories);
const selectedCategories = ref(props.selectedCategories);

/**
 * Add or delete the category from the selected categories depending on the previous state
 * If it was not selected,add the category to selected categories
 * otherwise delete it from selected categories
 * @param {String} categoryName Name of the category
 */
const toggleCategory = (categoryName) => {
  const index = selectedCategories.value.indexOf(categoryName);
  index==-1? selectedCategories.value.push(categoryName):selectedCategories.value.splice(index, 1);
};

</script>

<template>
  <div>
    <h2>Choose Categories</h2>
      <div v-for="category in categories" :key="category">
        <button
            class="btn"
            v-bind:class="{ 'btn-secondary': !selectedCategories.includes(category.name),
                              'btn-primary': selectedCategories.includes(category.name)
            }"
            @click="toggleCategory(category.name)"
        >
          {{ category.name }}
        </button>
      </div>
    <button
        class="btn btn-success"
        @click="$emit('updateFilteredEvents', selectedCategories)"
    >
      Rechercher
    </button>
  </div>
</template>

<style scoped>

</style>