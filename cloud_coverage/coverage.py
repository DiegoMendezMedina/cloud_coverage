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

    parameters = {"out": np.zeros(red_channel.shape, dtype= float), "where": blue_channel != 0}
    ratios = np.divide(red_channel, blue_channel, **parameters)
    
    segmentation = np.copy(image)
    segmentation[:,:,0] = segmentation[:,:,1] = segmentation[:,:,2] = (ratios >= threshold) * 255 
    return segmentation, cloudiness_index(segmentation) 

def cloudiness_index(image: np.ndarray) -> float:
    """ Calculates the cloudiness index based on a segmented image
    
    Parameters
    ----------
    image: numpy.ndarray
        It's a third dimensional segmented array with the first three layers are the segmented image
        with values 0 or 255 for each pixel and the second layer a mask, where the area will be
        calculated

    Returns
    -------
    float
        the cloudiness index, which goes from 0 to 1
    """

    segmented_layer = image[:,:,0]
    mask = image[:,:,3] == 255
    cropped_image = segmented_layer[mask]
    if cropped_image.size == 0:
        return 0

    cloud_pixels = np.sum(cropped_image == 255)
    return cloud_pixels / cropped_image.size 

