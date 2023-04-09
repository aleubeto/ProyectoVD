<template>
    <main>
        <div class="row flex-column flex-md-row justify-content-between mt-5" id="joinus">
            <div class="col-md-5 mb-4 mb-md-0">
                <h2 class="mb-4">Join Us</h2>
                <p>Thank you for visiting Spark Horizon's informative webpage!
                    If you're interested in learning more about job openings available at our company,
                    we invite you to fill out our form to receive exclusive information.
                    <br><br> Don't miss the opportunity to join our team and be part of a company in constant growth.
                    We look forward to your registration!
                </p>
            </div>
            <div class="col-md-6">
                <form>
                    <!--Nombre-->
                    <div class="mb-3">
                        <label for="userName" class="form-label">Your name</label>
                        <input type="text" class="form-control" id="userName">
                    </div>
                    <!--Email-->
                    <div class="mb-3">
                        <label for="userEmail" class="form-label">Email</label>
                        <input type="email" class="form-control" id="userEmail" aria-describedby="emailHelp">
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
            </div>
        </div>
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

<style>
form{
    background-color: #d6d6d6;
    padding: 15px;
    border-radius: 10px;
}
</style>