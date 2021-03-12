# -*- coding: utf-8 -*-

import os, shutil
from os import walk
from flask import Flask, render_template, request, redirect, url_for, current_app, flash
from werkzeug.utils import secure_filename
import jinja2
import sys
import myscript as ms
# import myscript

# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


cwd = os.getcwd()
app.config['UPLOAD_FOLDER'] = cwd + '/uploads/'  # '/Users/stlp/Desktop/index/uploads/'
# need to  be modified on different machines


@app.route('/')
def upload_f():
   return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])  # uploader
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
      # return 'file uploaded successfully, we will redirect you to the page once your result ready'
      
      # call another script
      # myscript.my_func()
      return render_template('wait.html')

RESULT_FOLDER = '/Users/stlp/Desktop/index/results/' # os.path.join('static', 'people_photo')
app.config['RESULT_FOLDER'] = RESULT_FOLDER


@app.route('/result', methods=['GET', 'POST'])
def show_result():
    # full_filename =  os.path.join(app.config['RESULT_FOLDER'], 'res.jpg')  # os.path.join(app.config['RESULT_FOLDER'], 'res.jpg')
    # print(full_filename)

    h = open('results/calculationResult.txt', 'r') 
  
    # Reading from the file 
    content = h.readlines() 

    # Varaible for storing the sum 
    mynum = "No result available"

    # Iterating through the content 
    # Of the file 
    for line in content: 
        mynum = line # int(line) 


    f = open('results/MathJaxResult.txt', 'r') 
  
    # Reading from the file 
    cont = f.readlines() 

    # Varaible for storing the sum 
    mylatex = "No latex output available"

    # Iterating through the content 
    # Of the file 
    for line in cont: 
        mylatex = line # int(line) 

    return render_template("result.html", user_number = mynum, user_latex = mylatex)


@app.route('/reset')
def remove():
    output_path =  cwd + '/results/' # '/Users/stlp/Desktop/index/results/'
    prefix = os.path.abspath(output_path) 
    file_list = [os.path.join(prefix, f) for f in os.listdir(prefix) if f.endswith('.txt')]
    
    input_path =  cwd + '/uploads/' # '/Users/stlp/Desktop/index/uploads/'
    pr = os.path.abspath(input_path) 
    in_list = [os.path.join(pr, f) for f in os.listdir(pr) if (f.endswith('.png'))  or (f.endswith('.jpg')) or (f.endswith('.jpeg'))]
  
    try:
        # os.remove(input_filename)
        # also delete two txt files

        for file in in_list:
          os.remove(file)

        # os.remove(output_filename)
        # os.remove(output_filename1)
        for file in file_list:
          os.remove(file)
        # return filename
        return render_template("index.html")
    except Exception as e:
        return f"Error in deleting files: {e}"


@app.route("/trigger-python", methods=['GET', 'POST'])
def print_something():
    print("Successful line print")
    ms.my_func()
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
