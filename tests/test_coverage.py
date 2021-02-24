import pytest
from PIL import Image
import numpy as np
from cloud_coverage.cci.index_calculator.coverage import cloudiness
from cloud_coverage.cci.index_calculator.coverage import cloudiness_index

''' 
path: Image black and white, expected cci value belongs to 
      the range represented in between.

between: Range of the image's cci located on the path.
'''
@pytest.mark.parametrize(
        ['path', 'between'],
        [('img/segmented.png', (0,50)), 
        ('img/empty.png', (0,0))]
)

def test_cloudiness_index(path, between):
    '''
    Function to test cloudiness_index function.
    
    The cloud coverage index of the image is know. 

    Parameters:
    -----------
    path, String. Location of an image we already know de 
                  cloud coverage index.

    between, Tuple. (a,b) where a is lower than the image's cci (cloud coverage
                                                                 index).
                           And b is greather than the image's cci.

    Returns:
    --------
    True if the first element in between is lower or equals than the image's 
                 cci and the second element in the tuple is greater or equal
                 than the image's cci.

    False otherwhise.
    '''
    min, max = between
    image = np.asarray(Image.open(path))
    index = cloudiness_index(image)
    assert min <= index <= max


    
''' 
path: Image black and white, expected cci value belongs to 
     the range represented in between.

between: Range of the image's cci located on the path.
'''
@pytest.mark.parametrize(
        ["path", "between"],

        [('img/easy_paint.png', (0.48,0.52)), 
        ('img/easy_sky.png', (0.35,0.55))]
)

def test_cloudiness(path, between):
    ''' 
    Function to test the cloudiness function. 

    Parameters:
    -----------
    path, String. Location of an image we already know de 
                  cloud coverage index.

    between, Tuple. (a,b) where a is lower than the image's cci (cloud coverage
                                                                 index).
                           And b is greather than the image's cci.
    Returns:
    --------
    True if the first element in between is lower or equals than the image's 
                 cci and the second element in the tuple is greater or equal
                 than the image's cci.

    False otherwhise.
    '''
    min, max = between
    image = np.asarray(Image.open(path))
    image_output, index = cloudiness(image)
    assert min <= index <= max
