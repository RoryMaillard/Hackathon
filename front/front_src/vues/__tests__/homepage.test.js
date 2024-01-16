import { vi, test, expect } from "vitest";
import { shallowMount } from "@vue/test-utils";
import homepage from '../homepage.vue';

test('Homepage renders correctly', async () => {
  const wrapper = shallowMount(homepage);

  expect(wrapper).toBeTruthy();
});
