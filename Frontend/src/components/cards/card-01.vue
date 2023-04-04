<template>
    <div class="card mb-4">
        <slot name="image"></slot>
        <div class="card-body">
            <h5 class="card-title"><slot name="cardTitle"></slot></h5>
            <p class="card-text"><slot name="cardText"></slot></p>
        </div>
    </div>
</template>

<style>
.card{
    width: 14rem;
}
</style>