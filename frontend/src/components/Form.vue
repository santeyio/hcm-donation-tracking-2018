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
            <label for="firstName" class="col col-form-label">First Name</label>
            <div class="col">
              <input v-model="firstName" id="firstName" type="text" class="form-control" placeholder="John"/>
            </div>
          </div>
          <div class="form-group row">
            <label for="lastName" class="col col-form-label">Last Name</label>
            <div class="col">
              <input v-model="lastName" id="lastName" type="text" class="form-control" placeholder="Doe"/>
            </div>
          </div>
        </div>
        <hr/>
        <fieldset class="form-group">
          <legend class="col-form-laebl">Payment Method</legend>
          <div class="col-md-4 offset-md-5 text-left">
            <div class="form-check">
              <input v-model="paymentType" class="form-check-input" name="paymentType" type="radio" value="EFT"/>
              <label for="eft">EFT</label>
            </div>
            <div class="form-check">
              <input v-model="paymentType" class="form-check-input" name="paymentType" type="radio" value="Credit or Debit Card"/>
              <label for="eft">Credit or Debit Card</label>
            </div>
            <div class="form-check">
              <input v-model="paymentType" class="form-check-input" name="paymentType" type="radio" value="Cash or Check"/>
              <label for="eft">Cash or Check</label>
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
              <input v-model="oneTimeAmount" id="oneTimeAmount" class="form-control" type="number" />
            </div>
          </div>
          <div class="col">
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text">$</span>
              </div>
              <input v-model="monthlyAmount" id="monthlyAmount" class="form-control" type="number" />
            </div>
          </div>
        </div>
      </form>
    </div>
    <button 
      type="button" 
      class="btn btn-primary"
      v-b-modal.submitModal
    >
      Continue
    </button>
    <b-modal ref="submitModal" hide-footer id="submitModal" title="Please Verify Your Information">
      <div class="col">
        <span class="text-muted">First Name:</span> {{ firstName }}<br/>
        <span class="text-muted">Last Name:</span> {{ lastName }}<br/>
        <span class="text-muted">Email:</span> {{ email }}<br/>
        <span class="text-muted">Monthly Donation:</span> {{ monthlyAmount }}<br/>
        <span class="text-muted">One Time Donation:</span> {{ oneTimeAmount }}<br/>
        <span class="text-muted">Payment Type:</span> {{ paymentType }}<br/>
      </div><br/>
      <div id="footer" class="modal-footer">
        <b-button @click="hideModal" id="info-button" variant="info">Edit</b-button>
        <b-button @click="submit" variant="primary">Submit</b-button>
      </div>
    </b-modal>
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
      paymentType: "",
      email: "",
      firstName: "" ,
      lastName: "",
      monthlyAmount: null,
      oneTimeAmount: null
    }
  },
  methods: {
    submit: function submit() {
      console.log('submit happened!');
      axios({
        url: `${this.$apiUrl}/api/user`,
        method: 'POST',
        data: {
          first_name: this.firstName,
          last_name: this.lastName,
          email: this.email,
          payment_type: this.paymentType,
          one_time_amount: this.oneTimeAmount,
          monthly_amount: this.monthlyAmount
        },
        headers: {
          'Content': 'application/json',
        }
      }).then(res => {
          console.log(res.status);
          this.$router.push('/success');
          window.open('https://www.hartfordcitymission.org/donate.html', '_parent')
        }).catch(err => {
          alert('Whoops! Something went wrong, please try again');
          console.log(err);
        });
    },
    hideModal() {
      this.$refs.submitModal.hide();
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
#info {
  margin-bottom: 3%;
}
#footer {
  padding-bottom: 0;
}
#info-button {
  margin-right: 3%;
}
</style>
