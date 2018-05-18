var data = ["static/df_savings_clean.csv", "static/df_current_clean.csv", "static/df_guarantees_clean.csv", "static/df_derivatives_clean.csv", "static/df_creditcard_clean.csv", "static/df_directdebit_clean.csv", "static/df_eacct_clean.csv", "static/df_funds_clean.csv", "static/df_guarantees_clean.csv", "static/df_homeacct_clean.csv", "static/df_junior_clean.csv", "static/df_loans_clean.csv", "static/df_ltdeposits_clean.csv", "static/df_mortgage_clean.csv", "static/df_mtdeposits_clean.csv", "static/df_payroll_clean.csv", "static/df_payroll2_clean.csv", "static/df_pensions_clean.csv", "static/df_savings_clean.csv", "static/df_securities_clean.csv", "static/df_specialacct1_clean.csv", "static/df_specialacct2_clean.csv", "static/df_specialacct3plus_clean.csv", "static/df_stdeposits_clean.csv", "static/df_taxes_clean.csv"];

var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var format = d3.format(",d");

var color = d3.scaleOrdinal(d3.schemeCategory20c);

var pack = d3.pack()
    .size([width, height])
    .padding(1.5);

function createGraph(newData) {	
	d3.csv(newData, function(d) {
	  d.value = +d.value;
	  if (d.value) return d;
	}, function(error, classes) {
	  if (error) throw error;

	  var root = d3.hierarchy({children: classes})
		  .sum(function(d) { return d.value; })
		  .each(function(d) {
			if (id = d.data.id) {
			  var id, i = id.lastIndexOf(".");
			  d.id = id;
			  d.package = id.slice(0, i);
			  d.class = id.slice(i + 1);
			}
		  });
	  
	  svg.selectAll(".node").remove()
	  
	  var node = svg.selectAll(".node")
		.data(pack(root).leaves())
		.enter().append("g")
		  .attr("class", "node")
		  .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

	  node.append("circle")
		  .attr("id", function(d) { return d.id; })
		  .attr("r", function(d) { return d.r; })
		  .style("fill", function(d) { return color(d.package); });

	  node.append("clipPath")
		  .attr("id", function(d) { return "clip-" + d.id; })
		.append("use")
		  .attr("xlink:href", function(d) { return "#" + d.id; });

	  
	  
	  node.append("text")
		  .attr("clip-path", function(d) { return "url(#clip-" + d.id + ")"; })
		.selectAll("tspan")
		.data(function(d) { return d.class.split(/(?=[A-Z][^A-Z])/g); })
		.enter().append("tspan")
		  .attr("x", 0)
		  .attr("y", function(d, i, nodes) { return 13 + (i - nodes.length / 2 - 0.5) * 10; })
		  .text(function(d) { return d; });

	  node.append("title")
		  .text(function(d) { return d.id + "\n" + format(d.value); });
});}
	
var select = d3.select('body')
  .append('select')
  	.attr('class','select')
	.attr("cx",20)
	.attr("cy",50)
    .on('change',onchange)

var options = d3.select('select')
  .selectAll('option')
	.data(data).enter()
	.append('option')
		.text(function (d) { return d; });

function onchange() {
	selectValue = d3.select('select').property('value')
	createGraph(selectValue)
};