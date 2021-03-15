# Hand-written Mathematical Expression Recognization System
[![Build Status](https://staging.travis-ci.com/515handwritten-expression/515-handwritten-mathematical-expression.svg?branch=main)](https://staging.travis-ci.com/515handwritten-expression/515-handwritten-mathematical-expression)

Our Handwritten Mathmatical Expression Recognization System aims to take handwritten mathematical expressions as inputs, recognize the expressions, perform the calculation, and generate a printed version of the results. We build and train a deep learning model to recognize handwritten expressions and implement a function to perform the calculation. We deliver the user-provided expressions in a readable and print-friendly format using LaTeX, along with the results of the expressions. 

With our system, the pain of computing complex mathematical expressions by hand can be relifed. Our system is going to quickly convert the handwritten expressions to a machine-readable version and generate the calculation result.

### Directory Structure
```
.
├── README.md
├── data
│   ├── TestData
│   │   ├── predPNG
│   │   │   ├── test_1.png
...
│   │   ├── testPNG
│   │   │   ├── easy_1.png
│   │   │   ├── hard_1.png
│   │   │   ├── median_1.png
...
│   │   └── testPNGSeg
│   │       ├── easy_1
│   │       │   ├── 01.png
│   │       │   └── easy_1.pkl
...
│   ├── TrainData
│   │   ├── (
│   │   │   ├── (_100.png
...
│   │   ├── )
│   │   │   ├── )_100.png
...
│   │   ├── +
│   │   │   ├── +_100.png
...
│   │   ├── -
│   │   │   ├── -_100.png
...
│   │   ├── 0
│   │   │   ├── 0_100.png
...
│   │   ├── 1
│   │   │   ├── 1_100.png
...
│   │   ├── 2
│   │   │   ├── 2_100.png
...
│   │   ├── 3
│   │   │   ├── 3_100.png
...
│   │   ├── 4
│   │   │   ├── 4_100.png
...
│   │   ├── 5
│   │   │   ├── 5_100.png
...
│   │   ├── 6
│   │   │   ├── 6_100.png
...
│   │   ├── 7
│   │   │   ├── 7_100.png
...
│   │   ├── 8
│   │   │   ├── 8_100.png
...
│   │   ├── 9
│   │   │   ├── 9_100.png
...
│   │   ├── =
│   │   │   ├── =_100.png
...
│   │   ├── [
│   │   │   ├── [_1.png
...
│   │   ├── ]
│   │   │   ├── ]_1.png
...
│   │   ├── div
│   │   │   ├── div_1.png
│...
│   │   ├── e
│   │   │   ├── e_1.png
...
│   │   ├── geq
│   │   │   ├── geq_1.png
...
│   │   ├── gt
│   │   │   ├── gt_1.png
...
│   │   │   └── gt_174.png
│   │   ├── leq
│   │   │   ├── leq_1.png
...
│   │   │   └── leq_433.png
│   │   ├── lt
│   │   │   ├── lt_1.png
...
│   │   │   └── lt_249.png
│   │   ├── neq
│   │   │   ├── neq_1.png
...
│   │   │   └── neq_294.png
│   │   ├── pi
│   │   │   ├── pi_1.png
...
│   │   │   └── pi_320.png
│   │   ├── pm
│   │   │   ├── pm_1.png

│   │   │   └── pm_430.png
│   │   ├── times
│   │   │   ├── times_1.png

│   │   │   └── times_342.png
│   │   ├── x
│   │   │   ├── x_1.png
...
│   │   │   └── x_291.png
│   │   ├── {
│   │   │   ├── {_1.png
...
│   │   │   └── {_160.png
│   │   └── }
│   │       ├── }_1.png
...
│   │       └── }_99.png
│   └── testimg
│       ├── testimg_1
│       │   ├── 1.png
...
│       │   ├── 4.png
│       │   ├── testReadAndConvert_1.png
│       │   └── testimg_1.pkl
│       ├── testimg_1.png
│       ├── testimg_2
│       │   ├── 1.png
...
│       │   ├── 12.png
│       │   ├── testReadAndConvert_2.png
│       │   └── testimg_2.pkl
│       ├── testimg_2.png
│       ├── testimg_3
│       │   ├── 1.png
...
│       │   ├── 6.png
│       │   ├── testReadAndConvert_3.png
│       │   └── testimg_3.pkl
│       ├── testimg_3.png
│       ├── testinkml_1.inkml
│       ├── testinkml_2.inkml
│       └── testinkml_3.inkml
├── demo.mov
├── docs
│   └── FunctionalSpec.docx
├── handwritten_math_expression
│   ├── ImagePreprocessing.py
│   ├── LeNetModel_v3.h5
│   ├── __pycache__
│   │   ├── ImagePreprocessing.cpython-38.pyc
│   │   ├── generateStrForLatexAndTree.cpython-38.pyc
│   │   ├── stringCalculation.cpython-38.pyc
│   │   └── stringMathJaxConverter.cpython-38.pyc
│   ├── generateStrForLatexAndTree.py
│   ├── index
│   │   ├── __pycache__
│   │   │   └── myscript.cpython-37.pyc
│   │   ├── index.py
│   │   ├── myscript.py
│   │   ├── results
│   │   │   ├── MathJaxResult.txt
│   │   │   └── calculationResult.txt
│   │   ├── templates
│   │   │   ├── index.html
│   │   │   ├── result.html
│   │   │   └── wait.html
│   │   └── uploads
│   │       ├── hard_8
│   │       │   ├── 01.png
...
│   │       │   ├── 08.png
│   │       │   └── hard_8.pkl
│   │       └── hard_8.png
│   ├── label_map_v3.npy
│   ├── main.py
│   ├── stringCalculation.py
│   ├── stringMathJaxConverter.py
│   └── tools
│       ├── LoadData.py
│       └── train_model.py
├── requirements.txt
├── setup.py
├── testTravisci
├── tests
│   ├── LeNetModel_v3.h5
│   ├── __init__.py
│   ├── label_map_v3.npy
│   ├── test_1
│   │   └── imgseg
│   │       ├── 01.png
...
│   │       ├── 05.png
│   │       └── test_1.pkl
│   ├── test_GenerateStrForLatexAndTree.py
│   ├── test_ImagePreprocessing.py
│   ├── test_stringCalculation.py
│   ├── test_stringMathJaxConverter.py
│   └── train_model.ipynb
└── webpage.png
```


### Tutorial for how to use the hand-written mathematical expression recognization system
#### Preperation and Installation
Our system require python3.5-python3.7 pre-installed.

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
To understand how to use the Hand-written Mathematical Expression Recognization System, please refer to the example video demo.mov in the folder.
<ol>
<li>The users first hit the <b>Choose file</b> buttom, and upload a <b>.png</b> file for the mathematical expression they want to use the system on. Then hit the <b>upload</b> buttom to upload the image.</li>
<li>Once the image is uploaded, the website will show <b>calculating</b>, indicating that the website is calculating.</li>
<li>Once the calculation is finished, a printed version of the expression will be shown on the webpage. If the expression is calculable (containing only numbers and calculable operations), a calculation result will appear on the website.</li>
</ol>


### Limitations
Currently, our system can only recognize the following symbols:

-, (, ), [, ], {, }, +, =, , ., 
<img src="https://render.githubusercontent.com/render/math?math=\frac{}{}">,
e
<img src="https://render.githubusercontent.com/render/math?math=\geq">,
<img src="https://render.githubusercontent.com/render/math?math=\gt">,
<img src="https://render.githubusercontent.com/render/math?math=\leq">,
<img src="https://render.githubusercontent.com/render/math?math=\lt">,
<img src="https://render.githubusercontent.com/render/math?math=\neq">,
<img src="https://render.githubusercontent.com/render/math?math=\pi">,
<img src="https://render.githubusercontent.com/render/math?math=\pm">,
<img src="https://render.githubusercontent.com/render/math?math=\times">,
<img src="https://render.githubusercontent.com/render/math?math=\x">,
and integers (0-9)

Our system can only perform calculation on numbers. Our system cannot solve functions that contain variables like <img src="https://render.githubusercontent.com/render/math?math=\x">.

For power, our system can only identify the first digit after the power sign. For example, if the target image is <img src="https://render.githubusercontent.com/render/math?math=2^{213}">, our system can only identify <img src="https://render.githubusercontent.com/render/math?math=2^2">
