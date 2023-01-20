#####################
#   Source Directory!
#   no need to replace \ with \\ in raw strings
SOURCE_DIR = r""
if SOURCE_DIR == "":
    print("Add Source Directory in app.py\ncan copy paste directory into SOURCE_DIR raw string, i.e.:\nSOURCE_DIR = r\"C:\\Users\\foo\\bar\"")
    exit(1)
#
#####################

#####################
# RANKS: use the names of the output directories, and give values to each
# key = files, best to worst
# value = a number to mathematically give weight to things based on how it was ranked
rank_dirs = [
    "\\1best",
    "\\2mid",
    "\\3bad",
    "\\4worst"
]
rank_dict = {
    rank_dirs[0]    : 3,
    rank_dirs[1]    : 2,
    rank_dirs[2]    : -2,
    rank_dirs[3]    : -3
}