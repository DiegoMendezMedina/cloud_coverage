from PIL import Image
import numpy as np

def img_to_array(photo, v_flag):
    ''' Changes the photo size, to the intrested area '''
    
    im = np.array(Image.open('samples/'+photo))
    im_trim = im[106:2806, 825:3525]
    cad = im_trim.shape
    height = cad[0]
    width = cad[1]

    return im_trim
    #Image.fromarray(im_trim).save('samples/output/save.jpg')
    
