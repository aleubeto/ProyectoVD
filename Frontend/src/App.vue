<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <RouterLink to = "/" class="nav-link">About Us</RouterLink>
            <RouterLink to = "/gallery" class="nav-link">Gallery</RouterLink>
            <RouterLink to = "/joinus" class="nav-link">Join Us</RouterLink>
          </div>
        </div>
      </div>
    </nav>
  </header>
  <RouterView/>
</template>