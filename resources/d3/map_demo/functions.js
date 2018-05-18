function fillMap(selection, color, data) {
    selection
    .attr("fill", function(d) 
    { return typeof data[d.id] === 'undefined' ? color_na :
                          d3.rgb(color(data[d.id])); });
}

function updateMap(color, data) {
  d3.selectAll("svg#map path").transition()
    .delay(100)
    .call(fillMap, color, data);
  d3.select("h3").text(d3.select("#year").node().value);
}


function calcColorScale(data) {
  let data_values = Object.values(data).sort(function(a, b){ return a-b; });
  var scale = d3.scaleThreshold()
      .domain([1, 50, 100])
      .range(d3.schemeReds[3]);
  return scale;
}
