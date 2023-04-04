<script setup>
import WhiteIsotype from './components/icons/Isotipo/Icon_Isotipo-white.vue'
import NavBar from './components/navbarItem.vue'
</script>

<template>
  <header>
    <NavBar :navItems="navItems">
      <template #icon><WhiteIsotype/></template>
      <template #heading>Spark Horizon</template>
    </NavBar>
  </header>
  <RouterView/>
</template>

<script>
  export default {
    components: {
      NavBar
    },
    data() {
      return {
        navItems: [
          { text: 'About Us', route: '/' },
          { text: 'Our team', route: '/ourteam' },
          { text: 'Join Us', route: '/joinus' }
        ]
      }
    }
  }
</script>