# SD PNG Sorter

This is a flask application that will help you sort PNGs in a given directory (intended to be used for pngs in a Stable Diffusion output directory)

Before running it, please edit the user_constants.py file to add:
your path\to\unsorted_png_directory as SOURCE_DIR
your folder output names and weights/values for each as rank_dirs and rank_dicts

How it works is it shows you a random image from the directory and lets you rate it from 1 to 4 (1 is best 4 is worst)

You may also press enter to skip

Once sorted, there are insights to be had regarding the best prompts, worst settings, and so on, for any given ckpt

The insights part is not yet implimented but has been started elsewhere

in cmd:
> pip install -r requirements.txt
> flask --debug run --host=0.0.0.0

--debug allows your changes in code to be registered whenever you refresh the page, no need to ctrl+c and start over
--host=0.0.0.0 will make the app available all over your network, so you can sort images on a laptop in a different room than your main SD machine