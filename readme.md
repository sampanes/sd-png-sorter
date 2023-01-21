# SD PNG Sorter

This is a flask application that will help you sort PNGs in a given directory (intended to be used for pngs in a Stable Diffusion output directory)

Before running it, please edit the user_constants.py file to add:
your path\to\unsorted_png_directory as SOURCE_DIR
your folder output names and weights/values for each as rank_dirs and rank_dicts
the file user_constants.py is ignored but IDK if it should be, it certainly should be skipped like the command
git update-index --skip-worktree <file>
we'll see if things blow up

How it works is it shows you a random image from the directory and lets you rate it from 1 to 4 (1 is best 4 is worst)

You may also press enter to skip
Press backspace to revert a change, this can undo a history of recent file moves, up to MAX_last_mv_len which is defined in user_constants.py

Once sorted, there are insights to be had regarding the best prompts, worst settings, and so on, for any given ckpt

The insights part is not yet implimented but has been started elsewhere

in cmd:
> .venv\Scripts\activate.bat
> pip install -r requirements.txt
> flask --debug run --host=0.0.0.0

--debug allows your changes in code to be registered whenever you refresh the page, no need to ctrl+c and start over
--host=0.0.0.0 will make the app available all over your network, so you can sort images on a laptop in a different room than your main SD machine


(as a note
we want d_of_d to have prompts, neg prompts, and settings ranked from high to low
dictionary of dictionaries is currently formatted as follows (no ranks present)
```
d_of_d =
	{
		"123hash":
			{
				"Prompts":
					[
						"perfect vector art of (mykeyword) at night, in the style...",
						"minimalistic symmetric painting of (mykeyword) at sunrise, in the style of Afshar".
						...
					],
				"Negative Prompts":
					[
						"((((watermark)))), (((copywrite))), ((istock)), ((stock image)), [out of frame]...",
						"((((ugly)))), (((disfigured))), ((gross)), ((mutated)), [out of frame]...",
						...
					],
				"Settings":
					[
						{"Steps": "50", "Model hash": "123hash", "Denoising strength": "0.25", ...},
						{"Steps": "75", "Model hash": "123hash", "Sampler": "Euler A", ...},
						...
					]
			}
		"abchash":
			{
				"Prompts":
					["ipsum lorem",...],
				"Negative Prompts":
					["no ipsum, oxi lorem",...],
				"Settings":
					[
						{"Steps": ..., "Model hash": ...},
						{...},
						...
					]
			}
	}
```
)