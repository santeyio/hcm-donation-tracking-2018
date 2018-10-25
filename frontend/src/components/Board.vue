<template>
  <div class="col-md-8 text-center" id="scoreboard">
    <h1>Total: ${{ formatWithCommas(total) }}</h1>
    <h2>Goal: ${{ formatWithCommas(goal) }}</h2>
    <div class="col">
      <b-progress variant="success" :value="counter" :max="max" show-progress animated></b-progress>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Form',
  props: {
  },
  data: function() {
    return {
      donations_to_display: [],
      donations_displayed: [],
      time_offset: 0,
      running_notifications: false,
      goal: this.$goalAmount,
    }
  },
  beforeCreate: function() {
    axios.get(`${this.$apiUrl}/api/donations`)
      .then(res => {
        this.donations_to_display = res.data;
      }).catch(err => {
        console.log(err);
      });
  },
  mounted: function() {
    if (!this.running_notifications) {
      this.runNotifications();
    }
  },
  updated: function() {
    if (!this.running_notifications) {
      this.runNotifications();
    }
  },
  methods: {
    runNotifications() {
      this.running_notifications = true;
      var s = setInterval(() => {
        if (this.donations_to_display.length) {
          var donation = this.donations_to_display.pop();
          donation.displayed = true;
          this.donations_displayed.push(donation);
          this.$notify({
            group: 'donations',
            title: 'New Donation!',
            text: '$' + String((Number(donation.monthly_amount) * 12) + Number(donation.one_time_amount)) ,
            duration: 30000,
          });
        } else {
          console.log('clear setInterval');
          clearInterval(s);
          this.running_notifications = false;
        }
      }, 6000);
    },
    formatWithCommas(x) {
      var parts = x.toString().split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    },
  },
  computed: {
    total() {
      var donations = this.donations_displayed.reduce((total, donation) => {
        return total + (Number(donation.monthly_amount) * 12) + Number(donation.one_time_amount);
      }, 0);
      return donations;
    },
    counter() {
      return Number(this.total) / (this.goal / 100);
    }
  },
  sockets: {
    donations: function donation_update(data) {
      console.log('socket event read: ', data);
      this.donations_to_display.push(data);
      if (!this.running_notifications) {
        this.runNotifications();
      }
    }
  }
}
</script>

<style>
h1 {
  font-size: 200px;
}
h2 {
  font-size: 80px;
}
#scoreboard {
  margin-top: 3%;
}
</style>
