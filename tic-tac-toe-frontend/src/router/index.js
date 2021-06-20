import { createRouter, createWebHistory } from 'vue-router'
import App from '../App.vue'
import Game from '../components/Game.vue'

const routes = [
  {
    path: '/',
    name: 'App',
    component: App
  },
  {
    path: '/game',
    name: 'App',
    component: Game
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
