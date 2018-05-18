

##  Html basics

- Start by making a folder however you like, however you want to organize things. Make a file called index.html in your local folder (outside of Metis Git Repo to avoid git conflicts).

- We can quickly create html 'structure', while using Atom editor (just type in <html (& tab complete))
You should see the following:  



```
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>

</body>
</html>
```

- Q: What is the 'DOCTYPE html' tag for?  
A little HTML review: a) the html tag is the root node of the HTML doc, where head & body are the children (again, we use indentation to illustrate the hierarchy).   He can create sibling as follows with h1 & p:

```
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<h1></h1>
	<p></p>

</body>
</html>
```

- Save your index.html file.  Fire up a local server and open the page in the Chrome development console. Test and see if your version loaded. Make sure you are in the new local folder where you created the index.html.

```
# for Python 2
python -m SimpleHTTPServer 8000

# for Python 3
python -m http.server 8000
```

- Take a few minutes to develop your front end skills by adding to your index.html file:
	* And text to your heading, paragraph etc.
	* And an image
	* Use CSS to change something. Do so by importing a CSS file, and then by adding CSS to index.html
	* Incorporate javascript into your front end design too.
	* Use JQuery to change something else

- A few words about:
	* HTML (Hypertext Markup Language): provides the structure for our page
	* CSS (Cascading Style Sheets) : provides the visual layout
	* HTML & CSS are concerned with how the information is displayed, whereas Javascript allows us to manipulate this display (tags etc,)
	(more about javascript later!)
	* jQuery is a collection of JavaScript libraries
	that are designed to simplify HTML document event
	handling, animation, & Ajax interactions (etc.)
