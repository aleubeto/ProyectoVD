<template>
    <div class="card mb-5">
        <div class="cardImageContainer">
            <slot name="image"></slot>
        </div>
        <div class="card-body">
            <h5 class="card-title"><slot name="cardTitle"></slot></h5>
            <p class="card-text"><slot name="cardText"></slot></p>
            <slot></slot>
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
    border-radius: 5px 5px 0px 0px;
}
.card .cardImageContainer img{
    object-fit: cover;
    height: 100%;
    transition: all 0.5s ease-out
}
.cardImageContainer img:hover{
    scale: 1.1;
}
</style>