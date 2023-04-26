<!--Script de vista-->
<script setup>
    // Componentes
    import Card from '/src/components/cards/card-01.vue'
    import CustomButton from '/src/components/buttons/CustomButton.vue'

    // Scripts
    import {onMounted, ref} from 'vue'
    import axios from 'axios'

    const data = ref([
        {
            id: '',
            titulo: '',
            sinopsis: '',
            autores: '',
            calificacion: '',
            calificaciones: '',
            fecha_publicacion: '',
            genero: '',
            num_pag: '',
            portada: '',
        }
    ]);

    onMounted(
        axios.get('http://localhost:8000/api/posts')
        .then((result) => {
            console.log(result.data);
            data.value = result.data;
        })
        .catch((error) => {
            console.log(error)
        })
    )
    /*const data = ref([{
        titulo: "Bootstrap, crea sitios responsivos facilmente", portada: "/src/assets/img/bootstrap.png"
    },
    {
        titulo: "La magia de SCRUM, el secreto de su metodología", portada: "/src/assets/img/scrum.jpg"
    },
    {
        titulo: "Vue vs React, la guerra de los frameworks", portada: "/src/assets/img/vue-vs-react.png"
    },
    ])*/
</script>

<!--Template de vista-->
<template>
    <main>
        <h2 class="mt-5 mb-4">Blog</h2>
        <div class="cards">
            <Card v-for="(item, index) in data" v-bind:key="index">
                <template #image><img :src="item.portada" class="card-img-top" alt="..."/></template>
                <template #cardTitle>{{item.titulo}}</template>
                <CustomButton>Check this out</CustomButton>
            </Card>
        </div>
    </main>
</template>

<style>
.cards{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}
</style>