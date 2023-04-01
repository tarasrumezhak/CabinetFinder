from typing import Dict, Any

import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from code.utils import process_image, prepare_templates


class CabinetFinder:
    """Finds cabinets in a query image using templates.

    Args:
        args: A dictionary containing parsed command line arguments.

    Attributes:
        args (Dict[str, Any]): A dictionary containing parsed command line arguments.
        templates (List[Dict[str, Any]]): A list of dictionaries containing template data.
        original_query (numpy.ndarray): The original query image.
        query (numpy.ndarray): The processed query image.
        coordinates (List[Dict[str, Union[str, int]]]): A list of dictionaries containing the coordinates of each cabinet.
    """

    def __init__(self, args: Dict[str, Any]) -> None:
        self.args = args
        self.templates = prepare_templates(args["templates"])
        self.original_query = cv2.imread(args["query"])
        self.query = process_image(self.original_query)
        self.coordinates = []

    def find(self) -> None:
        """Finds the cabinets in the query image, saves the visualization
        to a PNG file and the coordinates to a CSV file."""
        for template_data in self.templates:
            (temp_height, temp_width) = template_data["image"].shape[:2]
            result = cv2.matchTemplate(self.query, template_data["image"], cv2.TM_CCOEFF)
            result_normalized = cv2.normalize(result, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

            threshold = template_data["threshold"]
            loc = np.where(result_normalized >= threshold)

            for pt in zip(*loc[::-1]):
                br_coord = (pt[0] + temp_width, pt[1] + temp_height)
                self.coordinates.append(
                    {"type": template_data["type"], "x1": pt[0], "y1": pt[1], "x2": br_coord[0], "y2": br_coord[1]})
                color = tuple(template_data["color"]) if self.args["unique_colors"] else (255, 0, 0)
                cv2.rectangle(self.original_query, pt, br_coord, color, 2)

        if self.args["show_viz"]:
            plt.imshow(self.original_query)
            plt.show()

        cv2.imwrite(self.args["out_viz_path"], self.original_query)
        csv_data = pd.DataFrame.from_records(self.coordinates)
        csv_data.to_csv(self.args["out_csv_path"], index=False)
