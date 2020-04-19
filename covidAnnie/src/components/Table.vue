<template>
  <div class="hello">
    <table class="customer">
      <thead>
        <tr>
          <th class="name"></th>
          <th class="dataCell">Glucose (mmol/L)</th>
          <th class="dataCell">Insulin (unit)</th>
          <th class="dataCell">Heart rate (BPM)</th>
          <th class="dataCell">Temperature (℃)</th>
          <th class="dataCell">Systolic pressure (mm Hg)</th>
          <th class="dataCell">Diastolic pressure (mm Hg)</th>
          <th class="dataCell">Oxygen saturation (%)</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="cx in customers" :key="cx.id" @click="showModal(cx)">
          <td class="name"><div>{{cx.firstName + ' ' + cx.lastName + ', ' + getAge(cx.dateOfBirth)}}</div></td>
          <td class="dataCell"><div :class="evalValue(cx.glucose, 3.9, 8.1)">{{getLatestValue(cx.glucose)}}</div></td>
          <td class="dataCell"><div :class="evalValue(cx.insulin, 3.9, 8.1)">{{getLatestValue(cx.insulin)}}</div></td>
          <td class="dataCell"><div :class="evalValue(cx.heartRate, 59, 100)">{{getLatestValue(cx.heartRate)}}</div></td>
          <td class="dataCell"><div :class="evalValue(cx.temperature, 36, 37.3)">{{getLatestValue(cx.temperature)}}</div></td>
          <td class="dataCell"><div :class="evalValue(cx.diaPressure, 79, 90)">{{getLatestValue(cx.diaPressure)}}</div></td>
          <td class="dataCell"><div :class="evalValue(cx.sysPressure, 119, 140)">{{getLatestValue(cx.sysPressure)}}</div></td>
          <td class="dataCell"><div :class="evalValue(cx.oxygenLevel, 94, 100)">{{getLatestValue(cx.oxygenLevel)}}</div></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import * as moment from 'moment/moment'
import specific from './Specific'
export default {
  name: 'Table',
  props: {
    msg: String,
    customers: Array
  },
  methods: {
    getLatestValue (values) {
      return values[values.length - 1].value
    },
    evalValue (rawValue, min, max) {
      const value = this.getLatestValue(rawValue)
      if (value <= min) {
        return 'low'
      } else if (value >= max) {
        return 'high'
      } else {
        return 'normal'
      }
    },
    getAge (birthDate) {
      const today = moment()
      const birth = moment(birthDate)
      return Math.floor(moment.duration(today.diff(birth)).asYears())
    },
    showModal (cx) {
      this.$modal.show(specific, { customer: cx }, { draggable: true, reset: true, width: '90%', height: '90%' })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  .customer{
    border-collapse: separate;
    border-spacing: 0px;
    margin-left: auto;
    margin-right: auto;

    & td, & th{
      padding: 5px;
      text-align: left;
    }

    & th{
      font-size: 12px;
      width: 180px;
    }

    & td .low, & td .high, & td .normal{
      padding: 10px;
      border-radius: 4px;
      font-weight: bold;
    }

    & .low{
      background: red;
    }

     & .high{
      background: #ba0000;
    }

    & .normal{
      background: green;
    }

    & tr{
      cursor: pointer;
    }
  }
</style>
