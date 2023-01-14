import os

##############
#
#   Assume directory structure:
'''
    > /ignore/
    > /images/
        |----    > 1best
        |----    > 2mid
        |----    > 3nogood
        |----    > 4worst
    > ignore.x
'''
#
##############

path = os.getcwd()

def get_list_of_dirs(my_root=''):
    ret_l = []
    d = os.path.join(path, my_root)
    for objname in os.listdir(d):
        f = os.path.join(my_root,objname)
        if os.path.isfile(f):
            #objname is a file
            #print("ignoring file: ",f)
            pass
        if os.path.isdir(f):
            #objname is a directory
            #print("adding directory: ",f)
            ret_l.append(f)
    return ret_l

def get_list_of_files(my_root=''):
    ret_l = []
    d = os.path.join(path, my_root)
    for objname in os.listdir(d):
        f = os.path.join(my_root,objname)
        if os.path.isfile(f):
            #objname is a file
            #print("adding file: ",f)
            ret_l.append(f)
        if os.path.isdir(f):
            #objname is a directory
            #print("ignoring directory: ",f)
            pass
    return ret_l