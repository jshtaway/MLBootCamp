### Plan for Tuesday, October 17

#### Overview  

Today we'll continue with D3, and if we have time we'll go on to **Web Apps** with **Flask**.  This will conclude the data products portion of our course, so you can have a ball implementing a web app with a sweet D3 visualization for your Project McNulty.

#### Schedule

**9:15 am**: :coffee: up!

**9:30 am**: [Pair Problem](pair.md)

| Student 1 | Student 2 |
|---|---|
| Rebekah | Sufyan |
| Yanxi | Andre |
| Kenny | Carl |
| Laura | Michael |
| Jeff | Mike |
| Trent | Chuoran |
| Kalgi | Pradnya |

**10:15 am**: D3 Haberdashery: [Tailoring a d3 gallery example to fit your own data](d3_retrofit)

**11:15 am**: Web apps! With a Python Flask backend.

 * The simplest possible [example](app.py)
 * Defining a one-route prediction [API](predictor_app/)
 * Making a model-based [UI](cancer_app/)

**12:00 am**: Lunch

**1:30 pm**: Investigation Presentation: Kenny Leung on Computerized Essay Grading

**1:45 pm**: Viz Brainstorm: What visualization will complement your project?

 * Who is the audience?
 * What is the purpose of the visualization?
 * What data will be presented? Do you have it? Can you get it?

Draw your visualization! Draw before coding!


### Further Resources

If you are feeling uninspired, take a minute to read [this blog post](http://bost.ocks.org/mike/algorithms/) by Bostock about visualizing algorithms and come back when you feel super pumped.


 * Iterative local web development is more fun with an auto-reload tool like the [LivePage Chrome extension](https://github.com/MikeRogers0/LivePage).


#### D3 Basics

 * [D3 Example Library](https://github.com/mbostock/d3/wiki/Gallery)
 * [D3 API Reference](https://github.com/mbostock/d3/wiki/API-Reference)
 * [Mike Bostock's Website](http://bl.ocks.org/mbostock)
 * [Mike Bostock's Blocks](http://bost.ocks.org/mike/)
 * [Jason Davies](http://www.jasondavies.com/)


#### Additional D3 Tutorials

 * [Scott Murray's d3 Tutorials](http://alignedleft.com/tutorials/d3) (This guy wrote the book on D3. Literally.)
 * [Dashing d3](https://www.dashingd3js.com/) (Great set of tutorials by Sebastian Gutierrez.)
 * [D3 Site](http://d3js.org/)
 * [How to Make Your Own Block](http://bost.ocks.org/mike/block/)
 * [Making SVG Circles Tutorial](http://bost.ocks.org/mike/circles/)
 * [Thinking of Data Binding like Joins](http://bost.ocks.org/mike/join/)
 * [Bostock Deck on D3](http://bost.ocks.org/mike/d3/workshop/#0)
 * [O'Reilly](http://chimera.labs.oreilly.com/books/1230000000345/index.html)
 * [Manipulating Data in D3](http://www.jeromecukier.net/blog/2012/05/28/manipulating-data-like-a-boss-with-d3/)
 * [D3 MIXTAPES](http://enjalot.github.io/dot-enter/)
 * [A good explanation of how scales work](http://synthesis.sbecker.net/articles/2012/07/16/learning-d3-part-6-scales-colors)


#### On choosing colors

 * [A Less-Angry Rainbow](http://bl.ocks.org/mbostock/310c99e53880faec2434)
 * [Perceptual rainbox palette - the method](http://mycarta.wordpress.com/2013/02/21/perceptual-rainbow-palette-the-method/)


#### D3 Playgrounds

 * [Tributary](http://tributary.io/)
 * [JS Fiddle](http://jsfiddle.net/)


#### D3 Frameworks / Add-ins

 * http://nvd3.org/
 * https://square.github.io/cubism/
 * https://github.com/mbostock/queue
 * http://hughsk.io/colony/


#### Some math for visualizations with JavaScript

 * [Math for pictures](http://www.macwright.org/2013/03/05/math-for-pictures.html)


#### General Data Visualization

 * [Tufte](http://www.edwardtufte.com/tufte/)
 * [Image Quiltes](http://imagequilts.com/)
 * [Setosa](http://setosa.io/#/)


### D3 Examples

[Bostocks's Show Reel](http://bl.ocks.org/mbostock/1256572)

#### Line Charts

 * [Basic Line Chart](http://bl.ocks.org/mbostock/3883245)
 * [Line with Threshold Encoding](http://bl.ocks.org/mbostock/3970883)
 * [Line with Gradient Encoding](http://bl.ocks.org/mbostock/3969722)
 * [Difference Chart](http://bl.ocks.org/mbostock/3894205)
 * [Multi-Series Line Charts](http://bl.ocks.org/mbostock/3884955)
 * [It's a Table with a Line!](http://bl.ocks.org/llimllib/841dd138e429bb0545df)
 * [Slopechart](http://skedasis.com/d3/slopegraph/)


#### Area Charts

 * [Basic Area Chart](http://bl.ocks.org/mbostock/3883195)
 * [Basic Area Chart with Axis Component](http://bl.ocks.org/mbostock/1166403)
 * [Multiple Small Area Charts](http://bl.ocks.org/mbostock/9490313)
 * [Stacked Area Chart](http://bl.ocks.org/mbostock/3885211)
 * [Bivariate Chart](http://bl.ocks.org/mbostock/3884914)


#### Bar Charts

 * [Basic Bar Chart](http://bl.ocks.org/mbostock/3885304)
 * [Bar graph with tooltips](http://bl.ocks.org/Caged/6476579)
 * [Interactive Population Pyramid](http://bl.ocks.org/mbostock/4062085)
 * [Histogram](http://bl.ocks.org/mbostock/3048450)
 * [Diverging Stacked Bar](http://bl.ocks.org/wpoely86/e285b8e4c7b84710e463)
 * [Waterfall](http://bl.ocks.org/chucklam/f3c7b3e3709a0afd5d57)
 * [Sortable Bar Charts](http://bl.ocks.org/mbostock/3885705)


### Scatterplot

 * [Basic Scatterplot](http://bl.ocks.org/mbostock/3887118)
 * [Scatterplot Matrix with brushing](http://bl.ocks.org/mbostock/4063663)
 * [Small multiples](http://en.wikipedia.org/wiki/Small_multiple)


#### Venn Diagrams

 * [Basic Venn Diagram](http://bl.ocks.org/mbostock/1067616)


#### Timelines

 * [Cool Timeline Interpretation](http://bl.ocks.org/biovisualize/5609750)


#### Tables

 * [Sortable Tables with Bars](http://bl.ocks.org/mbostock/3719724)
 * [It's a Table with a Line!](http://bl.ocks.org/llimllib/841dd138e429bb0545df)
 * [Table with Cool Transitions](http://bost.ocks.org/mike/miserables/)


#### Trees

 * [Pedigree Tree](http://bl.ocks.org/mbostock/2966094)


#### Geometry

 * [Voronoi](http://bl.ocks.org/mbostock/3846051)
 * [Voronoi Clipping](http://bl.ocks.org/mbostock/4237768)
 * [Hexagonal Binning](http://bl.ocks.org/mbostock/4248145)
 * [Hexagonal Binning (Area)](http://bl.ocks.org/mbostock/4248146)
 * [Dynamic Hexabin](http://bl.ocks.org/mbostock/7833311)

#### Clocks

 * [Digital Clock](http://bl.ocks.org/mbostock/10685278)
 * [Spacetime](http://bl.ocks.org/clayzermk1/9142407)
 * [Polar Clock](http://bl.ocks.org/mbostock/1096355)


#### Random Cool Stuff

 * [Koalas to the Max](http://www.koalastothemax.com/) :koala:
 * [CSV Fingerprints](http://setosa.io/blog/2014/08/03/csv-fingerprints/)
 * [Jerome Cukier's simulation model gallery](http://www.jeromecukier.net/projects/models/models.html)
 * [Jim Vallandingham's visualizations](http://vallandingham.me/vis/)


##Data Viz In History

 * [William Playfair](http://en.wikipedia.org/wiki/William_Playfair)
 * [Charles Joseph Minard](http://en.wikipedia.org/wiki/Charles_Joseph_Minard)
 * [John Snow](http://en.wikipedia.org/wiki/John_Snow_(physician))



### Installing `flask`

```bash
# Most anywhere:
pip install flask

# On Ubuntu:
apt-get install python-flask
```

### More Resources

 * [How do websites work? What are web apps?](http://nilclass.com/courses/how-websites-work/#1): This neat little presentation starts very simple and step by step introduces every aspect of website infrastructure and it would be a good idea to read it before today's tutorial if this is new to you.
 * [What is an HTTP Request](http://rve.org.uk/dumprequest)
 * [Introduction to REST APIs](https://www.youtube.com/watch?v=YCcAE2SCQ6k): 14 minute video presentation by Google Developers. Very useful.
 * [HTTP Requests (GET and POST)](http://www.w3schools.com/tags/ref_httpmethods.asp)
 * [List of HTTP Response Status Codes](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
 * [Python requests documentation](http://docs.python-requests.org/en/latest/)
 * [Flask Documentation](http://flask.pocoo.org/)
