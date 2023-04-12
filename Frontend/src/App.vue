<script setup>
// Icons
import WhiteIsotype from './components/icons/Isotipo/Icon_Isotipo-white.vue'

// Components
import NavBar from './components/navbarItem.vue'
</script>

<!--Estructura de la aplicación-->
<template>
  <header>
    <NavBar :navItems="navItems">
      <template #icon><WhiteIsotype/></template>
      <template #heading>Spark Horizon</template>
    </NavBar>
  </header>
  <div class="container">
    <RouterView/>
  </div>
</template>

<!--Scripts-->
<script>
  export default {
    components: {
      NavBar
    },
    data() {
      return {
        navItems: [
          { text: 'Blog', route: '/' },
          { text: 'Our team', route: '/ourteam' },
          { text: 'Join Us', route: '/joinus' }
        ]
      }
    }
  }
</script>