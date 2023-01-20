from flask import Flask, render_template, request, send_file
import subprocess
import os, random
from png_tools import *
from png_analysis import get_dict_of_dicts
from user_constants import SOURCE_DIR
from user_constants import rank_dirs

app = Flask(__name__)

@app.route('/')
def show_image():
    return render_template('image.html')

@app.route('/analysis')
def analysis():
    dict_of_dicts = get_dict_of_dicts("staticimg")
    return render_template('analysis.html', data=dict_of_dicts)

@app.route('/best')
def move_pic_best():
    source = request.args['image']
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" staticimg{rank_dirs[0]}", shell = True)
    return "True"

@app.route('/mid')
def move_pic_mid():
    source = request.args['image']
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" staticimg{rank_dirs[1]}", shell = True)
    return "True"

@app.route('/bad')
def move_pic_bad():
    source = request.args['image']
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" staticimg{rank_dirs[2]}", shell = True)
    return "True"

@app.route('/worst')
def move_pic_worst():
    source = request.args['image']
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" staticimg{rank_dirs[3]}", shell = True)
    return "True"

@app.route('/next')
def next_image():
    value = random.choice([f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))])
    return value

@app.route('/png_info')
def png_info():
    img = request.args['img_name']
    pretty = png_print(SOURCE_DIR+"\\"+img)
    return pretty

@app.route('/image')
def get_image():
    source = request.args['file']
    return send_file(SOURCE_DIR + "\\" + source)

if __name__ == '__main__':
    app.run()
