
We're going to use this template to plot info from our tiny brooklyn biz data set
(our d3 template: https://bl.ocks.org/dhoboy/ccafe73e24cf9c36353f2641a4469314)     
(our data source: http://www.businessinsider.com/coolest-new-small-businesses-in-brooklyn-2014-9)

 - Save the D3 teaswarm viz as index.html    
 - Find 'data' within your viz: redefine with your new data source as follows: 

original:
```
d3.csv("song_scatter.csv", function(data) {
  tea.song = data;
  if (!--remaining) draw();
});

d3.csv("redblossom_scatter.csv", function(data) {
  tea.redblossom = data;
  if (!--remaining) draw();
});

function draw() {
  teaKeys.forEach(function(company) {
    tea[company] = tea[company].map(function(d) {
      return {
        company: company,
        tea_name: d.tea,
        brewing_amount: +d["brewing_amount(g)"],
        brewing_temp: +d["brewing_temp(F)"],
        brewing_time: +d["brewing_time(minutes)"] * 60,
        brewing_volume: +d["brewing_volume(ml)"],
        price_per_ounce: +d["price_per_oz($)"],
        type: d.type,
        location: d.location,
        imgUrl: d.imgUrl
      };
    });
  });
```

update to:
```                 
// load data, we're going to use all of data columns, so we will add them all here 
// What's this = + for?
// It's just to explicity state that these items are treated like numbers


d3.csv("bk_data.csv", function(error,data) {

data.forEach(function(d) {
    d.name = d.name;
    d.add = d.add;
    d.long = +d.long;
    d.lat = +d.lat;
    d.yelp=+d.yelps;
    d.what = d.what;
    d.img = d.img;

});
```

Also make sure you have the update the end of your file to:   
```
});
```


</script>

 - Update Axis: 

original: 
```
var xAxis = d3.axisBottom(x)
    .ticks(10, "$")

var yAxis = d3.axisLeft(y)
    .ticks(5, "%")
```

update to:
```
// note: var x & var y look good as they are  
var xAxis = d3.axisBottom(x)
    .ticks(10);

var yAxis = d3.axisLeft(y)
    .ticks(5);
    
// this also works: 
var xAxis = d3.axisBottom(x)
    .scale(x)

var yAxis = d3.axisLeft(y)
    .scale(y)
   
```
 - Update domain:

original:

```
 x.domain([0, d3.max(tea, function(d) { return d[dimensions.x]; } )]);
 y.domain(d3.extent(tea, function(d) { return d[dimensions.y]/d["brewing_volume"]; }));
 r.domain(d3.extent(tea, function(d) { return d[dimensions.r]; }));
 ```
 
 update to:
 
 ```
  // Setting the x & y domain to the min and max of the features we're using
  // .nice() function makes a domain start and end on nice values (helps with formatting)
  x.domain(d3.extent(data, function(d) { return d.long; })).nice();
  y.domain(d3.extent(data, function(d) { return d.lat; })).nice();
  
  ```
  
-  Update var node:   
   - Change data source from 'tea' to 'data'   
   - update return values for x,y & r
   - update fill to a specific color
  
  ```
  var node = svg.selectAll("g")
    .data(data)
    .enter()
    .append("g")
    .attr("class", "node")
    
  node
    .append("circle")
    .attr("cx", function(d) { return x(d.long); })
    .attr("cy", function(d) { return y(d.lat); })
    .attr("r", function(d) { return 1.75*(d.yelps); })
    .style("fill", "#6a3d9a")
 
 ```
 
 - Update .text(d.tea_name) to .text(d.name)
 - Update "img" attribute
 - Update tooltip.select()
 
 
 ```
 .on("mouseover", function(d) {
       tooltip.html("");
       tooltip.append("h3").attr("class", "tooltip_title");
       tooltip.append("img").attr("class", "tooltip_img");
       tooltip.append("pre").attr("class", "tooltip_body");
       tooltip.select(".tooltip_title")
         .text(d.name)

       tooltip.select("img")
         .attr("src", d.img);

       tooltip.select(".tooltip_body")
         .text( 
           "company: " + d.name + "\n" + 
           "address: " + d.add + "\n" +
           "what it is: " + d.what 
          );
```
- Update Axis Labels: 
```
x_axis = svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis)
    .append("text")
    .attr("transform", "translate(655,50)")
      .attr("class", "axis_title")
      .text("Longitude")

  y_axis = svg.append("g")
    .attr("class", "y axis")
    .attr("transform", "translate(0" + ",0)")
    .call(yAxis)
    .append("text")
    .attr("transform", "translate(-60,170) rotate(-90)")
      .attr("class", "axis_title")
      .text("Latitude") 
      
 });
  ```
  
- Add a title: 

```
svg.append("text")
        .attr("x", (width / 2))             
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")  
        .style("font-size", "16px") 
        .style("text-decoration", "underline")  
        .text("Small Biz in Brooklyn");
```

- Add a legend: 

```
var legend = svg.selectAll(".legend")
      .data(color.domain())
    .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

  legend.append("rect")
      .attr("x", width - 18)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", color);

  legend.append("text")
      .attr("x", width - 24)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return d; });
      
``` 

- Update 'teaKeys' as follows: 

```
var teaKeys = ["yelp ratings"];
```

- Run your local server to see how things look! 
```
# for Python 2
python -m SimpleHTTPServer 8000

# for Python 3
python -m http.server 8000
```
