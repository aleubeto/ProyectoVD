<!--Template de vista-->
<template>
    <main>
        <h2 class="mb-5">Our team</h2>
        <Card v-for="(item, index) in data" v-bind:key="index">
            <template #image><img :src="item.portada" class="card-img-top" alt="..."></template>
            <template #cardTitle>{{item.titulo}}</template>
            <template #cardText>{{item.puesto}}</template>
        </Card>
    </main>
</template>

<!--Script de vista-->
<script setup>
    // Componentes
    import Card from '/src/components/cards/card-01.vue'

    // Scripts
    import {ref} from 'vue'
    const data = ref([{
        titulo: "Título",
        puesto: "a",
        portada: "/src/assets/img/team-1.jpg"
    },
    {
        titulo: "Título",
        puesto: "a",
        portada: "/src/assets/img/team-2.jpg"
    },
    {
        titulo: "Título",
        puesto: "a",
        portada: "/src/assets/img/team-3.jpg"
    }
    ])
</script>

