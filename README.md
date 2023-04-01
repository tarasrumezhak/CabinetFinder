# Cabinet Finder

Cabinet Finder is a Python script that uses classical computer vision to detect cabinets in an image and output their coordinates as a CSV file. It also produces a visual representation of the detection.

## Usage

To use Cabinet Finder, run the following command:

```
python main.py -t /path/to/templates/folder -q /path/to/query/image
```

For example:

```
python .\main.py --templates data/templates/wall_cabinet --query data/query/interior.png
```

### Required arguments:

- `-t` or `--templates`: Path to the folder with templates
- `-q` or `--query`: Path to the query image

### Optional arguments:

- `-csv` or `--out_csv_path`: Path where to save the CSV file with coordinates of each cabinet (default: "result.csv")
- `-viz` or `--out_viz_path`: Path where to save the visualization (default: "result.png")
- `-show` or `--show_viz`: Flag indicating whether or not to show the visualization (default: True)
- `-colors` or `--unique_colors`: Flag indicating whether or not to separate different types of cabinets with different colors (default: True)

## Requirements

- Python 3.6+
- OpenCV
- imutils
- pandas
- matplotlib
- numpy

## How it works

Cabinet Finder uses a set of templates to detect cabinets in an image. The templates are processed using the Canny edge detection algorithm. The script then reads in the query image, processes it using the same algorithm, and matches it with the templates using OpenCV's `matchTemplate` function. Cabinets are detected where the normalized result of the template matching exceeds a certain threshold. The coordinates of each detected cabinet are saved in a CSV file, and a visualization of the detection is saved as an image.
