from flask import Flask, render_template, request, send_file
import subprocess
import os, random
from png_tools import *
from png_analysis import get_dict_of_dicts
from user_constants import SOURCE_DIR
from user_constants import rank_dirs

last_mv_tuple = []
MAX_last_mv_len = 25

app = Flask(__name__)

@app.route('/')
def show_image():
    return render_template('image.html')

@app.route('/analysis')
def analysis():
    dict_of_dicts = get_dict_of_dicts("staticimg")
    return render_template('analysis.html', dict_of_dicts=dict_of_dicts)

@app.route('/best')
def move_pic_best():
    source = request.args['image']
    global last_mv_tuple
    last_mv_tuple = last_mv_tuple[1-MAX_last_mv_len:]
    last_mv_tuple.append((source, f"staticimg{rank_dirs[0]}"))
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" \"staticimg{rank_dirs[0]}\"", shell = True)
    return "moved last image to Best"

@app.route('/mid')
def move_pic_mid():
    source = request.args['image']
    global last_mv_tuple
    last_mv_tuple = last_mv_tuple[1-MAX_last_mv_len:]
    last_mv_tuple.append((source, f"staticimg{rank_dirs[1]}"))
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" \"staticimg{rank_dirs[1]}\"", shell = True)
    return "moved last image to Mid"

@app.route('/bad')
def move_pic_bad():
    source = request.args['image']
    global last_mv_tuple
    last_mv_tuple = last_mv_tuple[1-MAX_last_mv_len:]
    last_mv_tuple.append((source, f"staticimg{rank_dirs[2]}"))
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" \"staticimg{rank_dirs[2]}\"", shell = True)
    return "moved last image to Bad"

@app.route('/worst')
def move_pic_worst():
    source = request.args['image']
    global last_mv_tuple
    last_mv_tuple = last_mv_tuple[1-MAX_last_mv_len:]
    last_mv_tuple.append((source, f"staticimg{rank_dirs[3]}"))
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" \"staticimg{rank_dirs[3]}\"", shell = True)
    return "moved last image to Worst"

@app.route('/next')
def next_image():
    value = random.choice([f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))])
    return value

@app.route('/undo')
def undo_move():
    print("Undoing last move")
    if last_mv_tuple:
        moved_image, accidental_destination = last_mv_tuple.pop()
        print(f"move \"{accidental_destination}\\{moved_image}\" \"{SOURCE_DIR}\"")
        res = subprocess.call(f"move \"{accidental_destination}\\{moved_image}\" \"{SOURCE_DIR}\"", shell = True)
        return f"moved last img from \"{accidental_destination}\" back to \"{SOURCE_DIR}\""
    else:
        return "False"

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
