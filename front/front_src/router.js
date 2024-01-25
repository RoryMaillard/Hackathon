import { createRouter, createWebHistory } from 'vue-router';
import eventDetails from "@/vues/EventDetails.vue";
import homepage from "@/vues/homepage.vue";
const routes = [
    {
        path: '/',
        name:'homepage',
        component: homepage,
        props:true,
    },
    {
        path: '/event/:id',
        name:'eventDetails',
        component: eventDetails,
        props: true,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
