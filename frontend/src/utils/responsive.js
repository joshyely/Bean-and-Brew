import { useWindowSize } from "@vueuse/core";
import { ref, watch, reactive } from "vue";

export const mobile = ref(true);

const { width, height } = useWindowSize()

const checkScreenWidth = () => {
    if(width.value < 1024) {
        mobile.value = true;
    } else {
        mobile.value = false;
    }
}

watch(
    () => width.value,
    () => checkScreenWidth()
);
checkScreenWidth()

