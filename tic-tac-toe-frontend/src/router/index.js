import { createRouter, createWebHistory } from 'vue-router'
// import App from '../App.vue'
import Game from '../components/Game.vue'
import Main from '../components/Main.vue'
import Login from '../components/Login.vue'
import Logout from '../components/Logout.vue'

const routes = [
  {
    path: '/',
    name: 'main',
    component: Main,
    meta: { title: 'Главная' }
  },
  {
    path: '/game',
    name: 'game',
    component: Game,
    meta: { title: 'Игра' },
    props: true
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
