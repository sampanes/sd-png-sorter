from flask import Flask, render_template, request, send_file
import subprocess
import os, random
from png_tools import *
from png_analysis import get_dict_of_dicts
from user_constants import SOURCE_DIR
from user_constants import rank_dirs
from user_constants import last_mv_tuple
from user_constants import MAX_last_mv_len

app = Flask(__name__)

def append_history(old_source, old_destination_idx):
    global last_mv_tuple
    last_mv_tuple = last_mv_tuple[1-MAX_last_mv_len:]
    last_mv_tuple.append((old_source, f"staticimg{rank_dirs[old_destination_idx]}"))

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
    append_history(source,0) # rank_dirs[0], so idx is 0
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" \"staticimg{rank_dirs[0]}\"", shell = True)
    return "moved last image to Best"

@app.route('/mid')
def move_pic_mid():
    source = request.args['image']
    append_history(source,1) # rank_dirs[1], so idx is 1
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" \"staticimg{rank_dirs[1]}\"", shell = True)
    return "moved last image to Mid"

@app.route('/bad')
def move_pic_bad():
    source = request.args['image']
    append_history(source,2) # rank_dirs[2], so idx is 2
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" \"staticimg{rank_dirs[2]}\"", shell = True)
    return "moved last image to Bad"

@app.route('/worst')
def move_pic_worst():
    source = request.args['image']
    append_history(source,3) # rank_dirs[3], so idx is 3
    res = subprocess.call(f"move \"{SOURCE_DIR}\\{source}\" \"staticimg{rank_dirs[3]}\"", shell = True)
    return "moved last image to Worst"

@app.route('/next')
def next_image():
    value = random.choice([f for f in os.listdir(SOURCE_DIR) if f.endswith('.png') and os.path.isfile(os.path.join(SOURCE_DIR, f))])
    return value

@app.route('/undo')
def undo_move():
    print("Undoing last move")
    global last_mv_tuple
    if last_mv_tuple:
        moved_image, accidental_destination = last_mv_tuple.pop()
        print(f"move \"{accidental_destination}\\{moved_image}\" \"{SOURCE_DIR}\"")
        res = subprocess.call(f"move \"{accidental_destination}\\{moved_image}\" \"{SOURCE_DIR}\"", shell = True)
        if res == 0:
            return str(len(last_mv_tuple))+f": moved last img from \"{accidental_destination}\" back to \"{SOURCE_DIR}\""
        else:
            return str(len(last_mv_tuple))+f": FAILED! last img not in \"{accidental_destination}\" or \"{SOURCE_DIR}\" invalid"
    else:
        return "No more history to undo, back button does nothing now"

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
