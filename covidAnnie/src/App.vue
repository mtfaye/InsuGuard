<template>
  <div id="app">
    <div class="header"><img src="./assets/logo.png" height="60px"/></div>
    <h1 class="title">{{Title}}</h1>
    <Table :msg="Title" :customers="Customers" />
  </div>
</template>

<script>
import Table from './components/Table'
export default {
  name: 'App',
  components: {
    Table
  },
  data: function () {
    return {
      Title: 'Diabete Customer Monitor 0.02',
      Customers: [
        {
          id: 1,
          firstName: 'Robert',
          lastName: 'Casey',
          glucose: [
            {
              date: '2020-03-21T09:09:00',
              value: 5.6
            },
            {
              date: '2020-03-22T17:08:00',
              value: 6.6
            },
            {
              date: '2020-03-23T22:51:00',
              value: 6.8
            },
            {
              date: '2020-03-24T07:35:00',
              value: 12
            }
          ],
          insulin: [
            {
              date: '2020-03-21T09:09:00',
              value: 9
            },
            {
              date: '2020-03-22T17:08:00',
              value: 7
            },
            {
              date: '2020-03-23T22:51:00',
              value: 10
            },
            {
              date: '2020-03-24T07:35:00',
              value: 2
            }
          ],
          heartRate: [
            {
              date: '2020-03-21T09:09:00',
              value: 59
            },
            {
              date: '2020-03-22T17:08:00',
              value: 63
            },
            {
              date: '2020-03-23T22:51:00',
              value: 60
            },
            {
              date: '2020-03-24T07:35:00',
              value: 59
            }
          ],
          temperature: [
            {
              date: '2020-03-21T09:09:00',
              value: 37.2
            },
            {
              date: '2020-03-22T17:08:00',
              value: 37.1
            },
            {
              date: '2020-03-23T22:51:00',
              value: 37.4
            },
            {
              date: '2020-03-24T07:35:00',
              value: 37.1
            }
          ],
          sysPressure: [
            {
              date: '2020-03-21T09:09:00',
              value: 120
            },
            {
              date: '2020-03-22T17:08:00',
              value: 118
            },
            {
              date: '2020-03-23T22:51:00',
              value: 119
            },
            {
              date: '2020-03-24T07:35:00',
              value: 118
            }
          ],
          diaPressure: [
            {
              date: '2020-03-21T09:09:00',
              value: 100
            },
            {
              date: '2020-03-22T17:08:00',
              value: 95
            },
            {
              date: '2020-03-23T22:51:00',
              value: 99
            },
            {
              date: '2020-03-24T07:35:00',
              value: 94
            }
          ],
          oxygenLevel: [
            {
              date: '2020-03-21T09:09:00',
              value: 90
            },
            {
              date: '2020-03-22T17:08:00',
              value: 91
            },
            {
              date: '2020-03-23T22:51:00',
              value: 89
            },
            {
              date: '2020-03-24T07:35:00',
              value: 87
            }
          ],
          dateOfBirth: '1960-01-31',
          phone: '555-555-1234'
        },
        {
          id: 2,
          firstName: 'Haider',
          lastName: 'Cote',
          glucose: [
            {
              date: '2020-03-21T09:09:00',
              value: 11.7
            },
            {
              date: '2020-03-22T17:08:00',
              value: 14.3
            },
            {
              date: '2020-03-23T22:51:00',
              value: 7.2
            },
            {
              date: '2020-03-24T07:35:00',
              value: 13.3
            }
          ],
          insulin: [
            {
              date: '2020-03-21T09:09:00',
              value: 7
            },
            {
              date: '2020-03-22T17:08:00',
              value: 10
            },
            {
              date: '2020-03-23T22:51:00',
              value: 2
            },
            {
              date: '2020-03-24T07:35:00',
              value: 7
            }
          ],
          heartRate: [
            {
              date: '2020-03-21T09:09:00',
              value: 79
            },
            {
              date: '2020-03-22T17:08:00',
              value: 85
            },
            {
              date: '2020-03-23T22:51:00',
              value: 81
            },
            {
              date: '2020-03-24T07:35:00',
              value: 82
            }
          ],
          temperature: [
            {
              date: '2020-03-21T09:09:00',
              value: 35
            },
            {
              date: '2020-03-22T17:08:00',
              value: 36.4
            },
            {
              date: '2020-03-23T22:51:00',
              value: 36.4
            },
            {
              date: '2020-03-24T07:35:00',
              value: 36
            }
          ],
          sysPressure: [
            {
              date: '2020-03-21T09:09:00',
              value: 120
            },
            {
              date: '2020-03-22T17:08:00',
              value: 118
            },
            {
              date: '2020-03-23T22:51:00',
              value: 119
            },
            {
              date: '2020-03-24T07:35:00',
              value: 118
            }
          ],
          diaPressure: [
            {
              date: '2020-03-21T09:09:00',
              value: 100
            },
            {
              date: '2020-03-22T17:08:00',
              value: 95
            },
            {
              date: '2020-03-23T22:51:00',
              value: 99
            },
            {
              date: '2020-03-24T07:35:00',
              value: 94
            }
          ],
          oxygenLevel: [
            {
              date: '2020-03-21T09:09:00',
              value: 99
            },
            {
              date: '2020-03-22T17:08:00',
              value: 98
            },
            {
              date: '2020-03-23T22:51:00',
              value: 97
            },
            {
              date: '2020-03-24T07:35:00',
              value: 98
            }
          ],
          dateOfBirth: '1969-07-22',
          phone: '555-555-1234'
        },
        {
          id: 3,
          firstName: 'Allana',
          lastName: 'Goulding',
          glucose: [
            {
              date: '2020-03-21T09:09:00',
              value: 13.7
            },
            {
              date: '2020-03-22T17:08:00',
              value: 7.2
            },
            {
              date: '2020-03-23T22:51:00',
              value: 18.9
            },
            {
              date: '2020-03-24T07:35:00',
              value: 11.4
            }
          ],
          insulin: [
            {
              date: '2020-03-21T09:09:00',
              value: 10
            },
            {
              date: '2020-03-22T17:08:00',
              value: 4
            },
            {
              date: '2020-03-23T22:51:00',
              value: 9
            },
            {
              date: '2020-03-24T07:35:00',
              value: 4
            }
          ],
          heartRate: [
            {
              date: '2020-03-21T09:09:00',
              value: 80
            },
            {
              date: '2020-03-22T17:08:00',
              value: 85
            },
            {
              date: '2020-03-23T22:51:00',
              value: 97
            },
            {
              date: '2020-03-24T07:35:00',
              value: 97
            }
          ],
          temperature: [
            {
              date: '2020-03-21T09:09:00',
              value: 35
            },
            {
              date: '2020-03-22T17:08:00',
              value: 36.4
            },
            {
              date: '2020-03-23T22:51:00',
              value: 36.4
            },
            {
              date: '2020-03-24T07:35:00',
              value: 36
            }
          ],
          sysPressure: [
            {
              date: '2020-03-21T09:09:00',
              value: 144
            },
            {
              date: '2020-03-22T17:08:00',
              value: 140
            },
            {
              date: '2020-03-23T22:51:00',
              value: 149
            },
            {
              date: '2020-03-24T07:35:00',
              value: 150
            }
          ],
          diaPressure: [
            {
              date: '2020-03-21T09:09:00',
              value: 70
            },
            {
              date: '2020-03-22T17:08:00',
              value: 71
            },
            {
              date: '2020-03-23T22:51:00',
              value: 72
            },
            {
              date: '2020-03-24T07:35:00',
              value: 70
            }
          ],
          oxygenLevel: [
            {
              date: '2020-03-21T09:09:00',
              value: 99
            },
            {
              date: '2020-03-22T17:08:00',
              value: 98
            },
            {
              date: '2020-03-23T22:51:00',
              value: 97
            },
            {
              date: '2020-03-24T07:35:00',
              value: 98
            }
          ],
          dateOfBirth: '1945-01-20',
          phone: '555-555-1234'
        }
      ]
    }
  },
  methods: {
    getGlucose () {
      return this.Customers.map(cx => ({ id: cx.id, firstName: cx.firstName, lastName: cx.lastName, value: cx.glucose }))
    },
    getInsulin () {
      return this.Customers.map(cx => ({ id: cx.id, firstName: cx.firstName, lastName: cx.lastName, value: cx.insulin }))
    }
  }
}
</script>

<style lang="scss">
*{
   margin: 0;
   padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

.header{
  background-color: #6f5280;
  height: 60px;
  text-align: right;
}

.title{
  margin: 20px;
}
</style>
