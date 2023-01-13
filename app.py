from flask import Flask, render_template, request, send_file
import subprocess
import os, random
from png_tools import *

#####################
#   Source Directory!
#   no need to replace \ with \\ in raw strings
SOURCE_DIR = r""
if SOURCE_DIR == "":
    print("Add Source Directory in app.py\ncan copy paste directory into SOURCE_DIR raw string, C:\\Users\\foo\\bar")
    exit(1)
#
#####################

app = Flask(__name__)

@app.route('/')
def show_image():
    return render_template('image.html')

@app.route('/best')
def move_pic_best():
    source = request.args['image']
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" staticimg\\1best", shell = True)
    return "True"

@app.route('/mid')
def move_pic_mid():
    source = request.args['image']
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" staticimg\\2mid", shell = True)
    return "True"

@app.route('/bad')
def move_pic_bad():
    source = request.args['image']
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" staticimg\\3bad", shell = True)
    return "True"

@app.route('/worst')
def move_pic_worst():
    source = request.args['image']
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" staticimg\\4worst", shell = True)
    return "True"

@app.route('/next')
def next_image():
    value = random.choice([f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))])
    return value

@app.route('/png_info')
def png_info():
    img = request.args['img_name']
    pretty = png_print(SOURCE_DIR+"\\"+img)
    print("tried to get info on\n"+SOURCE_DIR+"\\"+img)
    print(pretty)
    return pretty

@app.route('/image')
def get_image():
    source = request.args['file']
    return send_file(SOURCE_DIR + "\\" + source)

if __name__ == '__main__':
    app.run()