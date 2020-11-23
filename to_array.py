from PIL import Image
import numpy as np

def img_to_array(photo, v_flag):
    ''' Changes the photo size, to the intrested area '''

    photo_split = photo.split(".")
    photo_cad = photo_split[0]
    
    im = np.array(Image.open('samples/'+photo))
    im_trim = im[106:2806, 825:3525]
    
    mask = np.array(Image.open('samples/mask-1350-sq.png'))
    mask = mask.reshape(*mask.shape, 1)
    
    mask = mask / 255


    dst = im_trim * mask
    
    Image.fromarray(dst.astype(np.uint8)).save('samples/'+photo_cad+'.png')

    im_mask = np.array(Image.open('samples/'+photo_cad+'.png'))
    cad = im_mask.shape
    height = cad[0]
    width = cad[1]
    im_mask = np.dstack( (dst, np.zeros((width, height))))

    
    #im_mask = im_mask.astype(np.uint8)

    
    for i in range(width):
        for j in range(height):
            R, G, B, A = im_mask[i,j]
            if R+G+B > 0:
                im_mask[i, j] = (R, G, B, 255)
                
    return im_mask
    
    
