import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ResultView from '../views/ResultView.vue'
import DetailView from '../views/DetailView.vue'
import DetailMapView from '../views/DetailMapView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/result/',
      name: 'result',
      component: ResultView
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: DetailView
    },
    {
      path: '/detail/:id/map',
      name: 'detail_map',
      component: DetailMapView
    },
  ]
})

export default router
