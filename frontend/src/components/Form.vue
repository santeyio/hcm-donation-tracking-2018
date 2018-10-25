<template>
  <div class="container-fluid text-center">
    <div class="col-md-8 offset-md-2">
      <form>
        <div class="text-left">
          <div class="form-group row">
            <label for="email" class="col col-form-label">Email</label>
            <div class="col">
              <input v-model="email" id="email" type="email" class="form-control" placeholder="Email"/>
            </div>
          </div>
          <div class="form-group row">
            <label for="first_name" class="col col-form-label">First Name</label>
            <div class="col">
              <input v-model="first_name" id="first_name" type="text" class="form-control" placeholder="John"/>
            </div>
          </div>
          <div class="form-group row">
            <label for="last_name" class="col col-form-label">Last Name</label>
            <div class="col">
              <input v-model="last_name" id="last_name" type="text" class="form-control" placeholder="Doe"/>
            </div>
          </div>
        </div>
        <hr/>
        <fieldset class="form-group">
          <legend class="col-form-laebl">Payment Method</legend>
          <div class="col-md-4 offset-md-5 text-left">
            <div class="form-check">
              <input v-model="payment_type" class="form-check-input" name="payment_type" type="radio" value="eft"/>
              <label for="eft">EFT</label>
            </div>
            <div class="form-check">
              <input v-model="payment_type" class="form-check-input" name="payment_type" type="radio" value="credit_card"/>
              <label for="eft">Credit Card</label>
            </div>
            <div class="form-check">
              <input v-model="payment_type" class="form-check-input" name="payment_type" type="radio" value="check"/>
              <label for="eft">Check</label>
            </div>
          </div>
        </fieldset>
        <hr/>
        <div class="form-group row">
          <div class="col">
            <label>One Time Donation</label>
          </div>
          <div class="col">
            <label>Monthly Donation</label>
          </div>
        </div>
        <div class="form-group row">
          <div class="col">
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text">$</span>
              </div>
              <input v-model="one_time_amount" id="one_time_amount" class="form-control" type="number" />
            </div>
          </div>
          <div class="col">
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text">$</span>
              </div>
              <input v-model="monthly_amount" id="monthly_amount" class="form-control" type="number" />
            </div>
          </div>
        </div>
      </form>
    </div>
    <button 
      type="button" 
      class="btn btn-primary"
      @click="submit"
    >
      Submit
    </button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Form',
  props: {
    msg: String
  },
  data: function() {
    return {
      payment_type,
      email,
      first_name,
      last_name,
      monthly_amount,
      one_time_amount
    }
  },
  methods: {
    submit: function submit() {
      console.log('submit happened!');
      console.log(this.payment_type, this.email, this.first_name, this.monthly_amount, this.one_time_amount);
      axios({
        url: `${this.$apiUrl}/api/user`,
        method: 'POST',
        data: {
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          payment_type: this.payment_type,
          one_time_amount: this.one_time_amount,
          monthly_amount: this.monthly_amount
        },
        headers: {
          'Content': 'application/json',
        }
      }).then(res => {
          console.log(res.status);
        }).catch(err => {
          console.log(err);
        });
    }
  },
  sockets: {
    donations: function donation_update(data) {
      console.log('socket event read: ', data);
      this.donations.push(data);
    }
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
