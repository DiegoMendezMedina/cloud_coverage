import pytest
from PIL import Image
import numpy as np
from cloud_coverage import cloudiness
from cloud_coverage.coverage import cloudiness_index

@pytest.mark.parametrize(
        ['path', 'between'],
        [('img/segmented.png', (0,50)),
        ('img/empty.png', (0,0))]
)
def test_cloudiness_index(path, between):
    min, max = between
    image = np.asarray(Image.open(path))
    index = cloudiness_index(image)
    assert min <= index <= max


@pytest.mark.parametrize(
        ["path", "between"],
        [('img/easy_paint.png', (0.48,0.52)),
        ('img/easy_sky.png', (0.35,0.55))]
)
def test_cloudiness(path, between):
    min, max = between
    image = np.asarray(Image.open(path))
    image_output, index = cloudiness(image)
    assert min <= index <= max
