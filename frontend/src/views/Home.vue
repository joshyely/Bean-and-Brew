<script setup>
import { reactive, ref, provide } from 'vue';


const viewImage = '/src/assets/viewImages/home.png';



</script>

<template>
<div class="page-image-wrapper">
    <div class="image-container">
        <img src="../assets/pageImages/home.png" />
        <div class="overlay"></div>
    </div>
    <div class="cta">
        <h1 class="title">Bean and Brew</h1>
        <div class="cta-content">
            <div class="cta-left"></div>
            <div class="cta-right"></div>
        </div>
    </div>
</div>
</template>

<style scoped lang="scss">
.page-image-wrapper {
    height: 100vh;
    position:relative;
    width:100%;
    .image-container {
        position: relative;
        height:100%;
        overflow:hidden;
        img {
            position: absolute;
            object-fit: cover;
            min-height: 100%;
            width:100%;
        }
    }
    .cta {
        position:absolute;
        height: 85%;
        width:100%;
        color: white;
        bottom: 0;
        .cta-content{
            display:grid;
            grid-template-columns: 3fr 2fr;
            height:inherit;
            .cta-container{
                height:inherit;
                padding: 5%;
            }
        }
    }
    .overlay {
        background: linear-gradient(
            to top, 
            rgb(50, 50, 50, .98),
            rgb(50, 50, 50, .7),
            rgb(50, 50, 50, .65),
            rgb(50, 50, 50, .5),
            rgb(50, 50, 50, .3),
        );
        position:absolute;
        height: 100%;
        width: 100%;
        bottom: 0;
        display:flex;
        flex-direction: column;
        justify-content: end;
        
    }
}
.main-wrapper {
    padding: 0;
}
</style>
