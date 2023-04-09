<template>
    <main>
        <h2 class="mt-4 mb-4">Join Us</h2>
        <form>
            <!--Nombre-->
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Your name</label>
                <input v-model="mensaje" type="text" class="form-control" id="exampleInputTest">
            </div>
            <!--Email-->
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email</label>
                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            </div>
            <!--Terms & conditions-->
            <div class="mb-3">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="terms&conditions" v-model="checkboxValue" @click="acceptTermsAndConditions">
                  <label class="form-check-label" for="terms&conditions">
                    I've read and accept the terms & conditions
                  </label>
                </div>
            </div>
            <!--Submit button-->
            <Button1 :disabled="disabledRequest">Send my request</Button1>
          </form>
    </main>
</template>

<!--Script de vista-->
<script>
    import Button1 from '/src/components/buttons/button-01.vue';
    export default {
        components: {
            Button1
        },
        data() {
            return {
                checkboxValue: false,
                disabledRequest: true
            }
        },
        methods: {
            acceptTermsAndConditions() {
                this.disabledRequest = !this.disabledRequest;
            }
        }
    }
</script>