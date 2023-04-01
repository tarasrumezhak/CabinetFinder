import glob
import json
import os
from typing import Union, List, Dict, Tuple

import cv2
import imutils


def process_image(image: str, canny_low: int = 100, canny_high: int = 200, scale: Union[int, float, None] = None) -> \
        Union[None, bytearray]:
    """
    This function takes an input image and applies the following image processing operations on it:
    1. Converts the image from BGR color space to grayscale using `cv2.cvtColor`.
    2. If a `scale` value is provided, resizes the image to that scale using `imutils.resize`.
    3. Applies the Canny edge detection algorithm to the image using `cv2.Canny`.

    Parameters:
    ----------
    image : str (required)
        Path to the input image.
    canny_low : int (optional)
        The lower threshold for the Canny edge detection algorithm (default: 100).
    canny_high : int (optional)
        The upper threshold for the Canny edge detection algorithm (default: 200).
    scale : int or float or None (optional)
        The scale to resize the image to (default: None).

    Returns:
    -------
    The processed image or None, if the image cannot be read or processed.
    """
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if scale:
            image = imutils.resize(image, width=int(image.shape[1] * scale))

        return cv2.Canny(image, canny_low, canny_high)
    except:
        print("Error while processing image.")
        return None


def prepare_templates(templates_path: str) -> List[Dict[str, Union[str, bytearray, int, Tuple[int, int, int]]]]:
    """
    This function loads a set of image templates data from a given path and prepares them for use in the CabinetFinder.

    Parameters:
    ----------
    templates_path : str (required)
        The path to the folder containing the templates.

    Returns:
    -------
    A list of dictionaries, where each dictionary contains the following keys:
    - `type`: The type of the template (as determined by the filename).
    - `image`: The processed image of the template (processed using the `process_image` function).
    - `threshold`: The threshold value for Template Matching (specified in a JSON file).
    - `color`: The color of the template (specified in a JSON file).
    """
    templates = []
    with open(os.path.join(templates_path, "parameters.json")) as f:
        parameters = json.load(f)["templates"]
    for template_path in glob.glob(os.path.join(templates_path, "images/*.png")):
        template = cv2.imread(template_path)
        temp_type = os.path.basename(template_path).split(".")[0]
        template_data = {"type": temp_type,
                         "image": process_image(template),
                         "threshold": parameters[temp_type]["threshold"],
                         "color": parameters[temp_type]["color"]}

        templates.append(template_data)

    return templates
