### Pair Problem
For pairing this morning you can put away your Python.  Instead, open up [this page](http://www.w3schools.com/html/default.asp) in your browsers and use it as a reference.

HTML stands for Hyper Text Markup Language. It is the language used to create World Wild Web documents (aka. webpages). HTML uses various tags to create different elements for a webpage. Today you will try out a few tags and create a basic webpage.

Download and save this file [`home.html`](./home.html) in your working directory and open it with a text editor to examine its content. In another window, open this same file with a web browser (eg. Chrome). We'll start adding to the file, you can see the changes in action when you refresh the browser page.

**IMPORTANT:** We are aware that some of you may have significantly more web experience than others.  This is okay.  Remember the ideals of Pair Problems, if you're more experienced than your partner than you should take it upon yourself to help them get to the same understanding (it will reinforce your own understanding too).  If you're the other side of the coin, don't check out--you will **need** to understand how simple HTML works in web pages to be able to get through Project 2, so use your more experienced partner liberally to learn and stay engaged.  If you're both struggling, then help each other!  And if you're both masters, then make us something cool!

If you are unsure about any syntax, use google liberally.

1. #### Title
Add a title to your webpage. Where should the title tag go?  
Refresh your page, what do you see?  

	```
hint: use the <title>my_awesome_webpage</title>
	```  
1. #### Text and paragraphs
Add two paragraphs of text. Make sure you include some line breaks in your text, too. Feel free to style your text.  

	```
	hint: use the <p></p> tag for paragraphs
	```
1. #### Links
Create a new div with `<div id = 'linkdiv'></div>` and add a link to your favorite website in it.

 	```
 hint: use the <a href=""></a> tag
 	```

1. #### Images
Create a new div `<div id = 'imgdiv'></div>` and add your favorite image in this div.  
	```
hint: images tags are self-closing, like this
<img src="replace with url of your image" alt="the hovering text"/>
	```
1. #### Tables
Create a new div `<div id = 'tbldiv'></div>` and add this table about you and your classmates in the div. Feel free to create more rows / columns for your table

	|   | Last Name | First Name | Spirit Animal | Quote |
	|---|-----------|------------|-------|-------|
	| 1 (you)|           |            |       |       |
	| 2 (your partner)|           |            |       |       |


	```
	hint: create the table using the <table></table> tag.
  Then add <tr></tr>, <th></th>, and <td></td> tags appropriately.
  Can you make a table cell that spans multile rows or columns?
	```

1. #### Lists
Create one **Ordered list** and list three of your favorite movies in order  
Create one **Unordered list** and list three git commands that you've used

	```
hint: use <ol></ol> and <ul></ul>
	```

### Extras:
 * Style your page. Test out different combinations of font-color, font-style, font-size, background-color etc. You could find some color templates [here](http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3)
  * You can also try looking at [css](http://www.w3schools.com/css/default.asp)
 * Add a horizontal line between the divs, can you specify the line width?
 * Add a `favicon` to your webpage.
 * Add a comment to your html.

### Take an image of your webpage and share in the slack channel!
