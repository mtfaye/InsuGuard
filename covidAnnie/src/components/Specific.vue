<template>
  <div class="specific">
    <div class="header"></div>
    <h1 class="name">
      {{customer.firstName + ' ' + customer.lastName + ', ' + getAge(customer.dateOfBirth)}}
    </h1>
    <div class="charts">
      <Chart msg="Glucose"  :min=3.9 :max=8.1 :svg_width=300 :svg_height=250 :margin=60 :centerAdjustment=25 className="glucose" :values="getRawValue(customer.glucose)"/>
      <Chart msg="Insulin"  :min=3.9 :max=8.1 :svg_width=300 :svg_height=250 :margin=60 :centerAdjustment=10 className="insulin" :values="getRawValue(customer.insulin)"/>
      <Chart msg="Heart rate" :min=59 :max=100 :svg_width=300 :svg_height=250 :margin=60 :centerAdjustment=8 className="heartRate" :values="getRawValue(customer.heartRate)"/>
      <Chart msg="Temperature" :min=36 :max=37.3 :svg_width=300 :svg_height=250 :margin=60 className="temperature" :values="getRawValue(customer.temperature)"/>
      <Chart msg="Diastolic pressure" :min=79 :max=90 :svg_width=300 :svg_height=250 :margin=60 className="diaPressure" :values="getRawValue(customer.diaPressure)"/>
      <Chart msg="Systolic pressure" :min=119 :max=140 :svg_width=300 :svg_height=250 :margin=60 className="sysPressure" :values="getRawValue(customer.sysPressure)"/>
       <Chart msg="Oxygen saturation" :min=94 :max=100 :svg_width=300 :svg_height=250 :margin=60 className="oxygenLevel" :values="getRawValue(customer.oxygenLevel)"/>
    </div>
    <div class="call">
      <div>Call patient</div>
      <div>Call doctor</div>
    </div>
  </div>
</template>

<script>
import * as moment from 'moment/moment'
import Chart from './Chart'
export default {
  name: 'Specific',
  props: {
    customer: Object
  },
  components: {
    Chart
  },
  methods: {
    getRawValue (rawValues) {
      return rawValues.map(val => val.value)
    },
    getAge (birthDate) {
      const today = moment()
      const birth = moment(birthDate)
      return Math.floor(moment.duration(today.diff(birth)).asYears())
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.specific{
 font-family: Avenir, Helvetica, Arial, sans-serif;
}
.header{
  background-color: #6f5280;
  height: 10px;
}

.name{
  text-align: center;
  margin-top: 10px;
}

.charts{
  margin-top: 20px;
  display: flex;
  flex-wrap: wrap;
}

.call{
  bottom: 0px;
  font-size: 40px;
  width: 100%;
  display: flex;
  justify-content: space-around;
  text-transform: uppercase;

  div{
     background-color: #6f5280;
     padding: 10px;
  }
}
</style>
