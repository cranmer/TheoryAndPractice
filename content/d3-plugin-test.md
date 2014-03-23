Title: wp-d3 plugin test
Date: 2013-07-06 15:48
Author: cranmer
Category: Blog
Slug: d3-plugin-test

[d3-link]  
[data][]  
[/d3-link]

Trying to use the [wp-d3 plugin][]... and having problems. There should
be a pie chart here:

[d3-source canvas="chart"]  
var width = 960,  
height = 500,  
radius = Math.min(width, height) / 2;

var color = d3.scale.ordinal()  
.range(["\#98abc5", "\#8a89a6", "\#7b6888", "\#6b486b", "\#a05d56",
"\#d0743c", "\#ff8c00"]);

var arc = d3.svg.arc()  
.outerRadius(radius – 10)  
.innerRadius(0);

var pie = d3.layout.pie()  
.sort(null)  
.value(function(d) { return d.population; });

var svg = d3.select(".chart").append("svg")  
.attr("width", width)  
.attr("height", height)  
.append("g")  
.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

d3.csv("http://theoryandpractice.org/wp-content/uploads/2013/07/data.csv",
function(error, data)  
data.forEach(function(d) {  
d.population = +d.population;  
});

var g = svg.selectAll(".arc")  
.data(pie(data))  
.enter().append("g")  
.attr("class", "arc");

g.append("path")  
.attr("d", arc)  
.style("fill", function(d) { return color(d.data.age); });

g.append("text")  
.attr("transform", function(d) { return "translate(" + arc.centroid(d)
+ ")"; })  
.attr("dy", ".35em")  
.style("text-anchor", "middle")  
.text(function(d) { return d.data.age; });  
});  
[/d3-source]

Ok, well the piechart example above is not working, but here is some
success! I'm using a simple d3 example from this  
[tutorial][]. And I'm just putting the style right in the post instead
of an external .css file.

<style>
         .barchart rect {<br></br>
          stroke: white;<br></br>
          fill: steelblue;<br></br>
   text-align: right;<br></br>
   padding: 3px;<br></br>
   margin: 1px;<br></br>
   color: white;</p>
<p>}</p>
<p>.barchart div {<br></br>
   font: 10px sans-serif;<br></br>
   background-color: steelblue;<br></br>
   text-align: right;<br></br>
   padding: 3px;<br></br>
   margin: 1px;<br></br>
   color: white;<br></br>
 }</p>
</style>
[d3-source canvas="barchart"]  
var data = [4, 8, 15, 16, 23, 42];

var chart = d3.select(".barchart").append("svg")  
.attr("class", "barchart")  
.attr("width", 440)  
.attr("height", 140)  
.append("g")  
.attr("transform", "translate(10,15)");

var x = d3.scale.linear()  
.domain([0, d3.max(data)])  
.range([0, 420]);

chart.selectAll("rect")  
.data(data)  
.enter().append("rect")  
.attr("y", function(d, i) { return i \* 20; })  
.attr("width", x)  
.attr("height", 20);

var y = d3.scale.ordinal()  
.domain(data)  
.rangeBands([0, 120]);

chart.selectAll("rect")  
.data(data)  
.enter().append("rect")  
.attr("y", y)  
.attr("width", x)  
.attr("height", y.rangeBand());

chart.selectAll("text")  
.data(data)  
.enter().append("text")  
.attr("x", x)  
.attr("y", function(d) { return y(d) + y.rangeBand() / 2; })  
.attr("dx", -3) // padding-right  
.attr("dy", ".35em") // vertical-align: middle  
.attr("text-anchor", "end") // text-align: right  
.text(String);

chart.selectAll("line")  
.data(x.ticks(10))  
.enter().append("line")  
.attr("x1", x)  
.attr("x2", x)  
.attr("y1", 0)  
.attr("y2", 120)  
.style("stroke", "\#ccc");

chart.selectAll(".rule")  
.data(x.ticks(10))  
.enter().append("text")  
.attr("class", "rule")  
.attr("x", x)  
.attr("y", 0)  
.attr("dy", -3)  
.attr("text-anchor", "middle")  
.text(String);

chart.append("line")  
.attr("y1", 0)  
.attr("y2", 120)  
.style("stroke", "\#000");  
[/d3-source]

  [data]: http://theoryandpractice.org/wp-content/uploads/2013/07/data.csv
  [wp-d3 plugin]: http://figurebelow.com/2013/03/13/wp-d3-tutorial-adding-d3-snippet-into-a-wordpress-post/
  [tutorial]: http://mbostock.github.io/d3/tutorial/bar-1.html%20
