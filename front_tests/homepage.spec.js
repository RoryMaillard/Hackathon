import { mount } from "@vue/test-utils";
import {describe, it, jest, expect} from '@jest/globals';
import App from "../front_src/App.vue";

describe("App.vue", () => {
  it("renders correctly", () => {
    const wrapper = mount(App);
    expect(wrapper.element).toMatchSnapshot();
  });

  it("updates filtered events when selected categories change", async () => {
    const wrapper = mount(App);

    // Mocking axios.post for getFilteredEvents
    jest.spyOn(wrapper.vm, "getFilteredEvents").mockResolvedValueOnce([
      {"nom":"Conversation en français", "accueil_enfant":"non","adresse":"1 Rue Eugène Thomas","annule":"non","categorie_1":"Activité à partager","categorie_2":null,"categorie_3":null,"categorie_4":null,"categorie_5":null},
      {"accueil_enfant":"oui","adresse":"1 Rue Eugène Thomas","annule":"non","categorie_1":"Enfant","categorie_2":"Lecture","categorie_3":null,"categorie_4":null,"categorie_5":null,"nom":"Enfantines"}
    ]);

    // Simulate a change in selected categories
    await wrapper.setData({ selectedCategories: ["Activité à partager"] });

    // Expectations
    expect(wrapper.vm.filteredEvents).toEqual([
      {"nom":"Conversation en français", "accueil_enfant":"non","adresse":"1 Rue Eugène Thomas","annule":"non","categorie_1":"Activité à partager","categorie_2":null,"categorie_3":null,"categorie_4":null,"categorie_5":null}
    ]);
  });
});