import { createRouter, createWebHistory } from 'vue-router'
import AboutUs from '../views/AboutUsView.vue'
import Gallery from '../views/GalleryView.vue'
import JoinUs from '../views/JoinUsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'About Us',
      component: AboutUs
    },
    {
      path: '/gallery',
      name: 'Gallery',
      component: Gallery
    },
    {
      path: '/joinus',
      name: 'Join Us',
      component: JoinUs
    }
  ]
})

export default router