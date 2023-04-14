<!--Template de vista-->
<template>
    <main>
        <h2 class="mt-5 mb-4">Our team</h2>
        <div class="cards">
            <Card v-for="(item, index) in data" v-bind:key="index">
                <template #image><img :src="item.portada" class="card-img-top" alt="..."></template>
                <template #cardTitle>{{item.titulo}}</template>
                <template #cardText>{{item.puesto}}</template>
            </Card>
        </div>
        <h2 class="mt-5 mb-4">Spark Horizon team</h2>
        <table class="table table-striped">
        <thead>
            <tr>
            <th scope="col">ID</th>
            <th scope="col">Name</th>
            <th scope="col">Email</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th scope="row">A01735334</th>
                <td>María Fernanda Ramírez Romero</td>
                <td>A01735334@tec.mx</td>
            </tr>
            <tr>
                <th scope="row">A01730560</th>
                <td>Francisco Rocha Juárez</td>
                <td>A01730560@tec.mx</td>
            </tr>
            <tr>
                <th scope="row">A01732097</th>
                <td>Alan Eduardo Dávila Arellano</td>
                <td>A01732097@tec.mx</td>
            </tr>
            <tr>
                <th scope="row">A01660338</th>
                <td>Óscar Emiliano Ramírez Díaz</td>
                <td>A01660338@tec.mx</td>
            </tr>
            <tr>
                <th scope="row">A01730560</th>
                <td>Francisco Rocha Juárez</td>
                <td>A01730560@tec.mx</td>
            </tr>
            <tr>
                <th scope="row">A01734977</th>
                <td>Alejandro Alfonso Ubeto Yañez</td>
                <td>A01734977@tec.mx</td>
            </tr>
        </tbody>
        </table>
    </main>
</template>

<!--Script de vista-->
<script setup>
    // Componentes
    import Card from '/src/components/cards/card-01.vue'

    // Scripts
    import {ref} from 'vue'
    const data = ref([{
        titulo: "Fer", puesto: "SCRUM master",
        portada: "/src/assets/img/fer.png"
    },
    {
        titulo: "Ale", puesto: "Configuration manager",
        portada: "/src/assets/img/ale.jpg"
    },
    {
        titulo: "Omar", puesto: "Backend developer",
        portada: "/src/assets/img/team-3.jpg"
    },
    {
        titulo: "Oscar", puesto: "Frontend developer",
        portada: "/src/assets/img/oscar.jpg"
    },
    {
        titulo: "Alan", puesto: "Software developer",
        portada: "/src/assets/img/team-3.jpg"
    },
    {
        titulo: "Rocha", puesto: "Software developer",
        portada: "/src/assets/img/rocha.png"
    }
    ])
</script>

<style>
.cards{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}
</style>