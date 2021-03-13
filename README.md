# Hand-written Mathematical Expression Recognization System
[![Build Status](https://staging.travis-ci.com/515handwritten-expression/515-handwritten-mathematical-expression.svg?branch=main)](https://staging.travis-ci.com/515handwritten-expression/515-handwritten-mathematical-expression)

Our handwritten mathmatical expression recognization system aims to take handwritten mathematical expressions as inputs, recognizes the expressions, generate a printed version, and performs the calculation. We build and train a deep learning model to recognize handwritten expressions and implement a function to perform the calculation. We deliver the user-provided expressions in a readable and print-friendly format using LaTeX, along with the results of the expressions. 

With our system, the pain of computing complex mathematical expressions by hand can be relifed. Our system is going to quickly convert the handwritten expressions to a machine-readable and generate the result.

### Directory Structure


### Tutorial for how to use the hand-written mathematical expression recognization system
#### Preperation and Installation
To run the system, you will need to begin by cloning axwx on your own computer by using the following command:
```
git clone https://github.com/515handwritten-expression/515-handwritten-mathematical-expression.git
```
Next, to install the package you will need to go into the directory and run the setup.py file:
```
cd 515-handwritten-mathematical-expression/
python setup.py install
```
Now you should be able to run the server in the index folder
```
cd handwritten_math_expression/index/
python3 index.py
```
Then, open the browser and go to the local host http://127.0.0.1:5000/, and you should see the webpage as the following

<img src="webpage.png"
     alt="webpage.png"/>


#### How to use the systme
To understand how to use the Hand-written Mathematical Expression Recognization System, please refer to the examples video demo.mov in the folder.
<ol>
<li>The users first hit the <b>Choose file</b> buttom, and upload a <b>.png</b> file for the mathematical expression they want to use the system on. Then hit the <b>upload</b> buttom to upload the image.</li>
<li>Once the image is uploaded, the website will show <b>calculating</b>, indicating the website is calculating.</li>
<li>Once the calculation is finished, a printed version will be shown one the webpage. If the expression is calculable (containing only number), a calculation result will appear on the website.</li>
</ol>


### User cases
#### User Case 1: Output print-friendly version of the uploaded math expression image.
Jane is a student studying AP Calculus. She has some handwritten math formulas in her notebook. She wishes to have a clearer version of these formulas for her exam review notes. She is not familiar with the typesetting systems such as Latex, so she wishes to have a tool that can generate a printed version of these formulas that she can take screenshots and paste onto her notes. 

To achieve her goal, Jane takes a clear picture of each math formula separately and uploads the picture to our website. Our website presents her a printed version of the uploaded math expression, produced using Latex. Jane takes screenshots of these expressions and uses them for her notes.

Procedure:
<ol>
<li>Take a photo of one expression. </li>
<li>Upload the photo to the website and hit the submit button.</li>
<li>A printed version of the expression appears on the website.</li>
</ol>

#### User Case 2: Produce result of the uploaded math expression
Jenny has a hand-written math function and she wishes to output the solution of the function. 
To achieve her goal, Jenny takes a clear picture of the math function and uploads the picture to our website. Our website presents her a printed version of the uploaded math function. If the function is solvable, the website will present the solution to the function. If the function is insolvable or has no meaning(such as dividing by 0), no solution will be present, and a message will be delivered. 

Procedure:
<ol>
<li>Take a photo of one expression. </li>
<li>Upload the photo to the website and hit the submit button.</li>
<li>A printed version of the expression appears on the website.</li>
<li>The result of the function or a message indicating that the function cannot be solved will appear on the website.</li>
</ol>

### Limitations



