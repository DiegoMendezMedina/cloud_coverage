import pytest
from PIL import Image
import numpy as np
from cloud_coverage import cloudiness

@pytest.mark.parametrize(
        ["path", "between"],
        [('img/easy_paint.png', (0.48,0.52)),
        ('img/easy_sky.png', (0.35,0.55))]
)
def test_cloudiness_without_radious(path, between):
    min, max = between
    image = np.asarray(Image.open(path))
    image_output, cloudiness_index = cloudiness(image)
    assert min <= cloudiness_index <= max
