from pathlib import Path

def run():
    read_terminal()

def read_terminal():
    entry = input()
    txt = entry.split(" ")
    program = txt[0]
    photo = txt[1]
    flag =  "none"
    if len (txt) >2:
        flag = txt[2]
    #valid_program()
    v_photo = check_photo_existance(photo)
    v_flag = valid_flag(flag)

def check_photo_existance(photo):
    fileName = r"resources/"+photo
    fileObj = Path(fileName)
    return fileObj.is_file()


def valid_flag(flag):
    if flag.upper() == 'S':
        return True
    return False
