<script setup>
import { reactive, ref, provide } from 'vue';
import Card from '@/components/Card.vue';
import Grid from '@/components/Grid.vue';
import Accordion from '../components/Accordion.vue';
import Article from '@/components/Article.vue';
import TextButton from '@/components/buttons/TextButton.vue';

const viewImage = '/src/assets/viewImages/home.png';



</script>

<template>
    <div class="page-image-wrapper">
        <div class="image-container">
            <img src="../assets/pageImages/home.png" />
            <div class="overlay"></div>
        </div>
        <div class="cta">
            <div class="container">
                <h1 class="title">Bean and Brew</h1>
            </div>
            <div class="cta-content">
                <div class="cta-left container">
                    <Article heading="Lorem ip sum">
                        <p>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque, molestias ex. Optio commodi
                            ducimus,
                            animi dignissimos beatae nesciunt cumque aspernatur, quos aut et exercitationem voluptate
                            velit
                            fugit blanditiis illo eligendi.
                        </p>
                    </Article>
                </div>
                <div class="cta-right container">
                    <Article heading="Create an Account">
                        <p>
                            Create an account to get exclusive access to some of our features,
                            as well as rewards!
                        </p>
                        <br>
                        <TextButton style="margin-left: 8%; width: 40%;">
                            Register
                        </TextButton>
                    </Article>
                </div>
            </div>
        </div>
    </div>
    <section class="full">
        <div class="flex">
            <Card></Card>
            <Card></Card>
            <Card></Card>
        </div>
    </section>

</template>

<style scoped lang="scss">
.page-image-wrapper {
    height: 100vh;
    position: relative;
    width: 100%;

    .image-container {
        position: relative;
        height: 100%;
        overflow: hidden;

        img {
            position: absolute;
            object-fit: cover;
            min-height: 100%;
            width: 100%;
        }
    }

    .cta {
        position: absolute;
        min-height: 85%;
        width: 100%;
        color: white;
        bottom: 0;

        .container {
            padding: 0 3%;
        }

        .cta-content {
            display: flex;
            height: inherit;
            padding: 8vh 0;

            .cta-left {
                height: inherit;
                width: 60%;
            }

            .cta-right {
                height: inherit;
                width: 40%;
            }
        }
    }

    .overlay {
        background: linear-gradient(to top,
                rgb(50, 50, 50, .98),
                rgb(50, 50, 50, .7),
                rgb(50, 50, 50, .65),
                rgb(50, 50, 50, .5),
                rgb(50, 50, 50, .3),
            );
        position: absolute;
        height: 100%;
        width: 100%;
        bottom: 0;
        display: flex;
        flex-direction: column;
        justify-content: end;

    }
}

.content {
    display: flex;
    width: 100%;
    justify-content: center;
}



.main-wrapper {
    padding: 0;
}
</style>
