from pathlib import Path
from PIL import Image
import numpy as np

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
            img_masked = to_nparray(photo)

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

def to_nparray(photo):
    '''
    Given the direction of the file, this method changes 
    the img file to a numpy array with four channels.
    
    
    Parameters
    ----------
    String
    Direction of the photo.

    Returns
    ---------
    numpy array masked 255 in the fourth channel only on the intrested 
    area.
    '''
    photo_split = photo.split(".")
    photo_cad = photo_split[0]
    
    im = np.array(Image.open('samples/'+photo))
    im_trim = im[106:2806, 825:3525]
    im_mask = im_trim
    cad = im_trim.shape
    height = cad[0]
    width = cad[1]
        
    Image.fromarray(im_mask.astype(np.uint8)).save('samples/'+photo_cad+'.png')
    im_mask = np.array(Image.open('samples/'+photo_cad+".png"))
    
    a = np.zeros((width, height))
    a.fill(255)
    
    im_mask = np.dstack((im_trim, a))

    mask = create_circular_mask(width, height, 1350)
    im_mask[~mask] = 0

    return im_mask


def create_circular_mask(h, w,  radius):
    '''
    Creates a circular mask given the height, width of the file and area
    of the zone you want to mask.
    
    Takes the middle point as the center of the file. 
    
    Parameters
    ----------
    int h: height
    int w: width
    int radius: radius of the intrested area.
    '''
    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - 1350)**2 + (Y-1350)**2)
    mask = dist_from_center <= radius
    return mask
