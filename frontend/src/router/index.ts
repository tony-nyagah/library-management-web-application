import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/ping",
      name: "ping",
      component: () => import("../views/PingView.vue"),
    },
    {
      path: "/books",
      name: "books",
      component: () => import("../views/BooksView.vue"),
    },
    {
      path: "/book_details/:book_id",
      name: "book_details",
      component: () => import("../components/BookDetails.vue"),
      props: true,
    },
  ],
});

export default router;
