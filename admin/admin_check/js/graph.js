var series = ["user1", "user2","user3"];
 
var dataset = [ 
    {'월':116, '화':159, '수':134, '목':27, '금':55, '토':24,  '일':45},
    {'월':17, '화':27, '수':37, '목':27, '금':17, '토':7,  '일':9}];

var keys = d3.keys(dataset[0]);
var data = [];

dataset.forEach(function(d, i) {
data[i] = keys.map(function(key) { return {x: key, y: d[key]}; })
});

var margin = {left: 20, top: 10, right: 10, bottom: 20};
var svg = d3.select("svg");
var width  = parseInt(svg.style("width"), 10) - margin.left - margin.right;
var height = parseInt(svg.style("height"), 10)- margin.top  - margin.bottom;
var svgG = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
var xScale = d3.scalePoint()//scaleBand() scaleOrdinal
    .domain(keys)
    .rangeRound([0, width]);
var yScale = d3.scaleLinear()
    .domain([0, d3.max(dataset, function(d) { return d3.max(keys, function(key) { return d[key];});})])
    .nice()
    .range([height, 0]);
var colors = d3.scaleOrdinal(d3.schemeCategory10);

svgG.append("g")
    .attr("class", "grid")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(xScale)
        .tickSize(-height)
    );

svgG.append("g")
    .attr("class", "grid")
    .call(d3.axisLeft(yScale)
        .ticks(5)
        .tickSize(-width)
       );

var line = d3.line()
    .x(function(d) { return xScale(d.x); })
    .y(function(d) { return yScale(d.y); });
var lineG = svgG.append("g")
    .selectAll("g")
    .data(data)
       .enter().append("g");

lineG.append("path")
    .attr("class", "lineChart")
    .style("stroke", function(d, i) { return colors( series[i]); })
    .attr("d", function(d, i) {return line(d); });

lineG.selectAll("dot")
    .data(function(d) {return d })
    .enter().append("circle")
        .attr("r", 3)
        .attr("cx", function(d) { return xScale(d.x) })
        .attr("cy", function(d) { return yScale(d.y);})
        .on("mouseover", function() { tooltip.style("display", null); })
        .on("mouseout",  function() { tooltip.style("display", "none"); })
        .on("mousemove", function(d) {
            tooltip.style("left", (d3.event.pageX+10)+"px");
            tooltip.style("top",  (d3.event.pageY-10)+"px");
            tooltip.html("month. " + d.x + "<br/>" + "data value : " + d.y);
        });

var tooltip = d3.select("body")
    .append("div")
    .attr("class", "toolTip")
    .style("display", "none");

var legend = svgG.append("g")
    .attr("text-anchor", "end")
    .selectAll("g")
    .data(series)
    .enter().append("g")
    .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

legend.append("rect")
      .attr("x", width - 20)
      .attr("width", 19)
      .attr("height", 19)
      .attr("fill", colors);
