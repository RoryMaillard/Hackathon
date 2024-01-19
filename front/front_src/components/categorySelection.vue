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
  <div class="width-100">
    <h2>Choose Categories</h2>
    <div class="d-flex wrapper justify-content-start">
      <div v-for="category in categories" :key="category">
        <button
            class="btn mr-1 mb-1 inline-text"
            v-bind:class="{ 'btn-secondary': !selectedCategories.includes(category),
                              'btn-primary': selectedCategories.includes(category)
            }"
            @click="toggleCategory(category)"
        >
          {{ category }}
        </button>
      </div>
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
.mr-1{
  margin-right: 1rem;
}
.mb-1{
  margin-bottom: 1rem;
}
.inline-text{
  white-space: nowrap;
  text-align: center;
}
.wrapper{
  flex-wrap: wrap;
}
.flex-start{
  justify-content: flex-start;
}
.width-100{
  width: 100%;
}
</style>