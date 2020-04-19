<template>
  <div :class="className">
    <svg></svg>
  </div>
</template>

<script>
import * as d3 from 'd3'

export default {
  name: 'Chart',
  props: {
    msg: String,
    svg_width: Number,
    svg_height: Number,
    margin: Number,
    values: Array,
    className: String,
    min: Number,
    max: Number,
    centerAdjustment: Number
  },
  data () {
    return {
      chart: null
    }
  },
  mounted: function () {
    console.log(this.values)
    if (this.chart == null && this.values) this.renderChart(this.values)
  },
  methods: {
    renderChart (data) {
      const max = Math.max(...data)
      const chartWidth = this.svg_width - (2 * this.margin)
      const chartHeight = this.svg_height - (2 * this.margin)
      const lastValue = data[data.length - 1]
      let areaColor = 'black'

      if (lastValue <= this.min) {
        areaColor = 'red'
      } else if (lastValue >= this.max) {
        areaColor = '#ba0000'
      } else {
        areaColor = 'green'
      }

      console.log(areaColor)
      const x = d3.scaleLinear()
        .range([0, chartWidth])
        .domain([0, data.length - 1])

      const y = d3.scaleLinear()
        .range([chartHeight, 0])
        .domain([0, max])

      const xAxis = d3.axisBottom(x).tickFormat(function (d) { return d.x })

      const yAxis = d3.axisLeft(y)

      const line = d3.area()
        .x(function (d, i) { return x(i) })
        .y1(function (d) { return y(d) })
        .y0(chartHeight)
        .curve(d3.curveLinear)

      const svg = d3.select(`.${this.className} svg`)
        .attr('width', chartWidth + 60)
        .attr('height', chartHeight + 100)
        .append('g')
        .attr('transform', 'translate(50, 10)')

      svg.append('g')
        .attr('class', 'x axis')
        .attr('transform', 'translate(0,' + chartHeight + ')')
        .call(xAxis)

      svg.append('g')
        .attr('class', 'y axis')
        .call(yAxis)

      svg.append('path')
        .datum(data)
        .attr('class', 'line')
        .attr('fill', areaColor)
        .attr('d', line)

      svg.append('text')
        .attr('class', 'title')
        .attr('x', this.margin - this.centerAdjustment)
        .attr('y', chartHeight + 40)
        .attr('text-align', 'center')
        .text(this.msg + ':' + lastValue)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
