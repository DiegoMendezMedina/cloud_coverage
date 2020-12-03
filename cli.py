from pathlib import Path
from PIL import Image
import numpy as np
from cloud_coverage import cloudiness

def read_terminal():
    ''' Reads the program input and validates it '''
    
    entry = input()
    txt = entry.split(" ")
    
    if len(txt) < 1: 
        return
    
    photo = txt[0]
    flag =  "none"
    v_flag = False
    if len (txt) > 1:
        flag = txt[1]
        v_flag = True

    v_photo = check_photo_existance(photo)
    
    if flag != "none":
        v_flag = valid_flag(flag)
               
    if v_photo:
        img_masked = to_nparray(photo)
        img_result, index = cloudiness(img_masked)
        if v_flag:
            Image.fromarray(img_result.astype(np.uint8)).save('111.png')
        print(index)
    else :
        return

def check_photo_existance(photo):
    ''' Returns True if the photo exists on the sample directory;
    Otherwhise returns False'''
    
    fileName = r"./"+photo
    fileObj = Path(fileName)
    return fileObj.is_file()


def valid_flag(flag):
    ''' Returns True if the flag is 'S' or 's'; 
    Otherwhise prints a "invalid flag" message and returns False.'''

    if flag.upper() != 'S':
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
    
    im = np.array(Image.open('./'+photo))
    im_trim = im[106:2806, 825:3525]
    im_mask = im_trim
    height, width, _= im_trim.shape
        
    
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

if __name__ == '__main__':
    read_terminal()
