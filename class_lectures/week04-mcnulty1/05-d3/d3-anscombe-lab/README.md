# LAB - Building Anscombe's Quartet with D3

Now that you've seen the power and functionality of D3, we hope you're itching to start coding your own visualizations! This lab serves to provide a guided tour of D3 scatterplots with [Anscombe's famous dataset](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=0ahUKEwifnsTwqLbVAhUH1oMKHcr1AI4QFgg2MAM&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FAnscombe%2527s_quartet&usg=AFQjCNENdnbdVDRwG4-kd6q_9ddVeDMBAA)

### Objectives
- Build D3 viz from scratch
- Understand HTML, CSS, and JS language interactions and organization
- Practice hosting interactive Python servers locally

## Part I

1. We'll start by creating a new folder for our index.html file.

2. When using D3, we can create our HTML template as follows:

  ```
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">

    <style type="text/css">
      /*css to go here*/
    </style>
  </head>
  <body>

    <script src="https://d3js.org/d3.v4.min.js"></script>
    <script>
      //JS to go here
    </script>
  </body>
  </html>
  ```

3. Fire up a local server and open the page in the console. Test and see if your version loaded.  Make sure you are in the new local folder where you created the index.html.

  ```
  # for Python 2
  python -m SimpleHTTPServer 8000

  # for Python 3
  python -m http.server 8000
  ```


4. Open `index.html` in a text editor, and append an `h1` to the page via d3.select("body").append("h1").text("some text")

5. Let's also add some styles and a class to it.

6. More efficiently, D3 lets you "chain" your code. Handy!

7. Now do a data join. Make an array called parts and create a new `p` element for each.

  ```
    var parts = ["This is", "my first", "data join!"]

    var sentence = d3.select("body").selectAll("p")
        .data(parts)
      .enter()
        .append("p")
        .text(function(d) { return d; });
  ```

  That's a data join! Selecting elements you haven't created yet is a little strange, and we'll discuss it (and get plenty more experience in the next six weeks), but we won't linger for now. For more details, Scott Murray has [a great explanation](http://alignedleft.com/tutorials/d3/binding-data) and Mike Bostock Goes charactistically deep in [Thinking With Joins](http://bost.ocks.org/mike/join/).

8. As mundane as that was, that's the building block of every D3 chart you see on the internet.

## Part II
We're going to make the famous Anscombe plot using D3:

1. Clear out or start a new `index.html`.

2. Make a Javascript object out of your tabular data in (quartet.tsv) and make sure you know how to manipulate it. (This is an annoying but useful exercise in getting useful in a text editor.) Choose One Group Data only (I, II, III or IV).  There are only 11 data rows per group, so this will build the muscle memory in writing Javascript Object arrays.  You only need X, Y attribute values in this data variable.

  ```
  // Group I data
  var data = [
  { x: 10, y: 8.04},
  ...
  ]

  ```

3. Now let's try to code this using D3 and produce the same Scatter plot. Add an SVG element of width 600 and height 400.

4. Using a data join, add a circle for every element of our array. Give it a radius 5 and a class, `anscombe-circle'. Inspect it in the browser. To start, I like to put a pink border around the SVG to make sure I knew it drew:

    ```
    /* Add CSS Styles in Header section of the html */
    svg {
      border: 1px solid #f0f;
    }
    ```

5. Position the circles based on their `x` and `y` attributes. How does SVG interpret these positions?

6. We need a [scale](https://github.com/mbostock/d3/wiki/Quantitative-Scales#linear-scales). Let's add one. (There's a trick.)    Checkpoint is [here](03-enter-append-scatter.html).

7. Let's label the coordinate positions of each using text. Is another data join really necessary?

 - Redo the original join, using groups first, then appending circles and text. Note SVG [transformation](http://www.w3.org/TR/SVG/coords.html) documentation, which is not that fun. Scott Murray [does better](http://chimera.labs.oreilly.com/books/1230000000345/ch08.html#_cleaning_it_up).

  Checkpoint is [here](04-add-scales.html).

8.  Maybe [axes](https://github.com/mbostock/d3/wiki/SVG-Axes) are in order? The built-in components are a little clunky, and [Gregor](https://twitter.com/driven_by_data) prefers not to use them at all, but you have to know the rules before you break them, so let's use them for now.

 - We might need to move our axes around. We'll go through the math. Also, it looks horrible unstyled. Let's inspect it and fix, using CSS.

  Checkpoint is [here](05-axes.html)

9. Let's add a bit more style: 

  Final checkpoint is [here](06-styling-anscombe.html).

Congratulations, your D3 journey has only begun!

### Objectives
- Build D3 viz from scratch
- Understand HTML, CSS, and JS language interactions and organization
- Practice hosting interactive Python servers locally
