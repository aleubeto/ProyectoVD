<script setup>
    import {ref} from 'vue'
    const data = ref([{
        titulo: "Título",
        autor: "Semana 1",
        portada: "/src/assets/img/team-1.jpg"
    },
    {
        titulo: "Título",
        autor: "Semana 3",
        portada: "/src/assets/img/team-2.jpg"
    },
    {
        titulo: "Título",
        autor: "Semana 5",
        portada: "/src/assets/img/team-3.jpg"
    }
    ])
</script>

<template>
    <main>
        <h2>Galería</h2>
        <div v-for = "(item,i) in data" v-bind:key="i" class="card" style="width: 18rem;">
        <img :src="item.portada" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{{item.titulo}}</h5>
                <p class="card-text">Autor: {{item.autor}}</p>
                <a href="#" class="btn btn-primary">Check this out</a>
            </div>
        </div>
    </main>
</template>
