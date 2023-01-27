from os_tools import *
from png_tools import *
import nltk
from user_constants import rank_dict
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder

dict_keys = ["Prompts","Negative Prompts","Settings"]

def get_dict_of_dicts(MY_ROOT):
    #example test code just gets all the stuff as dicts from each hash, then a dicts of hash,dict
    d_of_d={}
    for dir in get_list_of_dirs(MY_ROOT):
        dir_stripped = dir.replace(MY_ROOT,"")
        if dir_stripped in rank_dict:
            for file in get_list_of_files(dir):
                prompts, neg_prompts, settings = get_binary_png_info(file)
                if settings:
                    settings_dict = extract_individual_settings(settings)
                    if settings_dict['Model hash'] in d_of_d:
                        # d_of_d[settings_dict['Model hash']].update_obj(rank_dict[dir_stripped], prompts, neg_prompts, settings)
                        d_of_d[settings_dict['Model hash']][dict_keys[0]].append(prompts)
                        d_of_d[settings_dict['Model hash']][dict_keys[1]].append(neg_prompts)
                        d_of_d[settings_dict['Model hash']][dict_keys[2]].append(settings)
                    else:
                        temp_dict = {
                            "rating":0,
                            "count":0,
                            dict_keys[0]:[prompts],
                            dict_keys[1]:[neg_prompts],
                            dict_keys[2]:[settings]
                            }
                        d_of_d[settings_dict['Model hash']] = temp_dict.copy()
                d_of_d[settings_dict['Model hash']]["rating"]+=rank_dict[dir_stripped]
                d_of_d[settings_dict['Model hash']]["count"]+=1

        else:
            print("dir error:\nMY_ROOT {}\ndir_stripped\t{}\ndir\t{}".format(MY_ROOT,dir_stripped,dir))
            
    return d_of_d

def gpt_get_collocations_and_ratings(d_of_d):
    return False

def generate_hash_dict(MY_ROOT):
    for dir in get_list_of_dirs(MY_ROOT):
        print(dir)
    return "FOOBAR"