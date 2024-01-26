<template>
  <div class="width-100">
    <h2>Catégories</h2>
    <div>
      <button
        v-for="category in categories"
        :key="category"
        class="btn mb-1 mr-05 inline-text"
        :class="{ 'btn-secondary': !selectedCategories.includes(category), 'btn-primary': selectedCategories.includes(category) }"
        @click="toggleCategory(category)"
      >
        {{ category }}
      </button>
    </div>
    <div class="d-flex mt-4">
      <button
        class="btn mb-1 mr-05 inline-text"
        :class="{ 'btn-secondary': !selectedCategories.includes('Gratuit'), 'btn-primary': selectedCategories.includes('Gratuit') }"
        @click="toggleCategory('Gratuit')"
      >
        Gratuit
      </button>
      <button
        class="btn mb-1 mr-05 inline-text"
        :class="{ 'btn-secondary': !selectedCategories.includes('h_auditif'), 'btn-primary': selectedCategories.includes('h_auditif') }"
        @click="toggleCategory('h_auditif')"
      >
        Malentendant
      </button>
      <button
        class="btn mb-1 mr-05 inline-text"
        :class="{ 'btn-secondary': !selectedCategories.includes('h_intellectuel'), 'btn-primary': selectedCategories.includes('h_intellectuel') }"
        @click="toggleCategory('h_intellectuel')"
      >
        Déficient intellectuel
      </button>
      <button
        class="btn mb-1 mr-05 inline-text"
        :class="{ 'btn-secondary': !selectedCategories.includes('h_visuel'), 'btn-primary': selectedCategories.includes('h_visuel') }"
        @click="toggleCategory('h_visuel')"
      >
        Malvoyant
      </button>
      <button class="btn btn-success" @click="updateFilteredEvents">Rechercher</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    categories: Array,
    selectedCategories: Array,
  },
  computed: {
    selectedCategories: function() {
      return [...this.selectedCategories];
    }
  },
  methods: {
    toggleCategory(categoryName) {
      const index = this.selectedCategories.indexOf(categoryName);
      index === -1
        ? this.selectedCategories.push(categoryName)
        : this.selectedCategories.splice(index, 1);
    },
    updateFilteredEvents() {
      this.$emit('updateFilteredEvents', this.selectedCategories);
    },
  },
};
</script>

<style scoped>
.mr-05 {
  margin-right: 0.5rem;
}
.mb-1 {
  margin-bottom: 1rem;
}
.mt-4 {
  margin-top: 4rem;
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
  color: #000000; /* Change this to your preferred text color */
}
</style>
