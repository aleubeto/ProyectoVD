<script setup>
    import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
        <div class="container">
            <div class="right-section">
                <slot name="icon"></slot>
                <a class="navbar-brand" href="#"><slot name="heading"></slot></a>
            </div>
            <div class="left-section">
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                        <router-link v-for="(navItem, index) in navItems" :key="index" :to="navItem.route" class="nav-link">{{ navItem.text }}</router-link>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        name: 'Navbar',
        props: {
            navItems: {
                type: Array,
                required: true
                }
        }
    }
</script>

<style>
.container{
    display: flex;
    justify-content: space-between;
}
</style>