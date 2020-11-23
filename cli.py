from pathlib import Path
from to_array import img_to_array

def read_terminal():
    ''' Reads the program input and validates it '''
    
    entry = input()
    txt = entry.split(" ")
    
    if len(txt) < 2:
        print("Invalid input size");
        return;
    
    program = txt[0]
    photo = txt[1]
    flag =  "none"
    if len (txt) > 2:
        flag = txt[2]
        
    v_program = valid_program(program)
    v_photo = check_photo_existance(photo)
    v_flag = False
    
    if flag != "none":
        v_flag = valid_flag(flag)
    
    if v_program:
        if v_photo:
            img = img_to_array(photo, v_flag)
        else :
            print("Photo not found on sample");
            return;
    else:
        print("Wrong execute call")
        return;

def check_photo_existance(photo):
    ''' Returns True if the photo exists on the sample directory;
    Otherwhise returns False'''
    
    fileName = r"samples/"+photo
    fileObj = Path(fileName)
    return fileObj.is_file()


def valid_flag(flag):
    ''' Returns True if the flag is 'S' or 's'; 
    Otherwhise prints a "invalid flag" message and returns False.'''

    if flag.upper() != 'S':
        print("Invalid flag")
        return False
    return True

def valid_program(exe):
    ''' Returns True if the string received is "CCI";
    Otherwhise returns False.'''
    
    if exe != "CCI" :
        return False
    return True
