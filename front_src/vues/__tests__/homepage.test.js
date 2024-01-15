import { vi, test, expect } from "vitest";
import { shallowMount } from "@vue/test-utils";
import { mount } from "@vue/test-utils";
import homepage from '../homepage.vue';

vi.mock('axios', () => ({
  request: vi.fn(() => Promise.resolve({ data: { results: { categories: ['Category1', 'Category2'] } } })),
}));


test('Homepage renders correctly', async () => {
  const wrapper = shallowMount(homepage);

  await wrapper.vm.$nextTick();

  // Check if the component is rendered
  expect(wrapper.html()).toMatchSnapshot();

  // Check if categories are loaded
  expect(wrapper.vm.categories).toEqual(['Category1', 'Category2']);
});

test('updateFilteredEvents updates filteredEvents correctly', async () => {
  const wrapper = shallowMount(homepage);

  // Assuming the "getCategories" and "getFilteredEvents" functions are asynchronous
  await wrapper.vm.$nextTick();

  // Mock emitted event from child component
  wrapper.findComponent({ name: 'categorySelection' }).emits('updateFilteredEvents', [['Category1']]);

  // Assuming the "getFilteredEvents" function is asynchronous
  await wrapper.vm.$nextTick();

  // Check if filteredEvents are updated correctly
  expect(wrapper.vm.filteredEvents).toEqual(/* Expected filtered events array based on the provided categories */);
});

// Add more tests as needed based on your components and functionalities.
