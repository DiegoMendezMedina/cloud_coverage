import numpy as np

def cloudiness(image: np.ndarray) -> tuple:
    """ Segment a sky image based on what is sky and what is a cloud
    and calculates the Cloudiness Index with that segmentation
    
    A fixed red/blue ratio is used as a threshold for faster segmentation

    Parameters
    ----------
    image: numpy.ndarray
        A third dimensional array which contains the red, green and blue
        channels of an image and the mask where the index will be calculated
    radious : int, optional
        The radious of the image, which will be useful to crop the image
        and stablish a limit to calculate the Cloudiness Index

    Returns
    -------
    tuple
        a tuple that contains the cloudiness index and a array with
        the segmented image
    """
    
    threshold = 0.95
    red_channel = image[:,:,0]
    blue_channel = image[:,:,2]
    mask = image[:,:,3]
    parameters = {"out": np.zeros(red_channel.shape, dtype= float), "where": blue_channel != 0}
    ratios = np.divide(red_channel, blue_channel, **parameters)
    segmentation = np.zeros_like(image[:,:,:2])
    segmentation[:,:,0] = (ratios >= threshold) * 1 
    segmentation[:,:,1] = mask 
    return makepng(segmentation), cloudiness_index(segmentation) 

def cloudiness_index(image: np.ndarray) -> float:
    """ Calculates the cloudiness index based on a segmented image
    
    Parameters
    ----------
    image: numpy.ndarray
        It's a third dimensional segmented array with the first layer the segmented image
        with values 0 to 1 for each pixel and the second layer a mask, where the area will be
        calculated

    Returns
    -------
    float
        the cloudiness index, which goes from 0 to 1
    """

    segmentation = image[:,:,0]
    mask = image[:,:,1] == 255
    cropped_image = segmentation[mask]
    cloud_pixels = np.sum(cropped_image == 1)
    return cloud_pixels / cropped_image.size 

def makepng(image: np.ndarray) -> np.ndarray:
    """ Makes a png image array with a segmented image, each layer
    will represent each RGBA channel

    Parameters
    ----------
    image: numpy.ndarray
        dd

    Returns
    -------
    numy.ndarray
        an array containing the RGBA channels of the image
    """

    width, height, _ = image.shape
    png = np.zeros((width, height, 4), dtype = np.uint8)
    # R,G,B channels
    png[:,:,0] = png[:,:,1] = png[:,:,2] = image[:,:,0] * 255
    # Alpha channel
    png[:,:,3] = image[:,:,1]
    return png
