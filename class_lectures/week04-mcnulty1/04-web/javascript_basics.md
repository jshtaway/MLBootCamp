# Javascript Basics


### Starting off

 * Let's make another index.html file within a new directory, and again launch the server from that directory via:
 
 ```
 # for Python 2
python -m SimpleHTTPServer 8000

# for Python 3
python -m http.server 8000
```

 * Using the JavaScript developer console in Google Chrome (option+command+i on Macs)
     * Clearing the javascript console is control+l
     * You can also pull up what you last entered, using the UP button
 * You can use the JavaScript console like a calculator

---

### Variables

Like Python, we can set integers to variable and treat them like integers. The difference in JavaScript is we have to explicitly state that they are variables, or "var." Arrays can also be variables, like `var Data = [1,2,3,4,5];`.

Let's make a few variables:

1. Make a variable called `numerator`, equal to 99.
2. Make a variable called `denominator`, equal to 100.
3. Make a variable called `percent`, equal to the numerator divided by the denominator.
4. Make an array called `dataset`, containing five numbers.

---

### Functions

Functions can have names, or not.

#### Named Functions

```javascript
function myFunction(x) { return x * 2; }
```

Try entering a value into `myFunction()`.

#### Anonymous Functions

```javascript
(function(x) { return x * 2; })(2);
```

This is also an "IIFE" (Immediately Invoked Function Expression).

Anonymous functions are commonly used as arguments, something like:

```javascript
var data = [1,2,3,4,5];

data.map( function(x) { return x * 2;} );
```

*This will be very important in D3, as we will often make functions on the fly. The difference in D3 is that we won't necessarily nest the function within a map() function.*

---

You can filter datasets with functions:

```javascript
var data = [1,2,3,4,5];

data.filter( function(x) { return x % 2 == 0; } );
```

Contrast this with `map`:

```javascript
var data = [1,2,3,4,5]

data.map( function(x) { return x % 2 == 0; } );
```

*Notice the difference in what those two return - the latter is what is more commonly used in D3.*

---

Let's make a few functions:

1. Make a function that adds 3 to any input.
2. Make a function that divides any input by three.
3. Make a function that takes an array and returns an array with only those elements that are less than 4.
4. Make a function that takes an array of numbers and returns their sum.
