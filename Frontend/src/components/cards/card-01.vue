<template>
    <div class="card mb-5">
        <div class="cardImageContainer">
            <slot name="image"></slot>
        </div>
        <div class="card-body">
            <h5 class="card-title"><slot name="cardTitle"></slot></h5>
            <p class="card-text"><slot name="cardText"></slot></p>
        </div>
    </div>
</template>

<style>
.card{
    width: 18rem;
}
.cardImageContainer{
    height: 200px;
    overflow: hidden;
}
</style>