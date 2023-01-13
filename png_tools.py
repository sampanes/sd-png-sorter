import png

def get_binary_png_info(my_png):
    if ".png" in my_png:
        f=open(my_png, 'rb')
        r=png.Reader(file=f)

        g=r.chunks()

        t=[b"",b""]
        while b"tEXt" not in t[0]:
            t=next(g)

        if b"tEXt" not in t[0]:
            return False, False, False
            
        ret = t[1]
        lines = ret.split(b'\n')

        if len(lines) == 2:
            prompts, settings = lines
            prompts = prompts.decode().replace('parameters\x00','')
            neg_prompts = ""
            settings = settings.decode()
        if len(lines) == 3:
            prompts, neg_prompts, settings = lines
            prompts = prompts.decode().replace('parameters\x00','')
            neg_prompts = neg_prompts.decode().replace('Negative prompt: ','')
            settings = settings.decode()
        if len(lines) <= 1 or len(lines) >= 4:
            print("\n\n\nBROKEN CODE PLEASE ADDRESS THIS IMMEDIATELY\n\n\n")
            return False, False, False

        f.close()
        return prompts, neg_prompts, settings
    return False, False, False

def extract_individual_settings(settings):
    set_list = [set.strip() for set in settings.split(',')]

    set_dict = {line.split(': ')[0]: line.split(': ')[1] for line in set_list}

    return set_dict

def png_print(my_png):
    p, n, s = get_binary_png_info(my_png)
    if p or n or s:
        retstr = ""
        if p:
            retstr+="<br><b><u>Prompts</b></u>: "+p+"<br>"
        if n:
            retstr+="<br><b><u>Negative Prompts</b></u>: "+n+"<br>"
        if s:
            retstr+="<br><b><u>Settings</b></u>: "+s+"<br>"
        return retstr
    else:
        return "No png info available for this item<br> check in Stable Diffusion if this has any"