import argparse

from code.finder import CabinetFinder

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-t", "--templates", required=True, help="Path to the folder with templates")
    arg_parser.add_argument("-q", "--query", required=True, help="Path to the query image")
    arg_parser.add_argument("-csv", "--out_csv_path", default="result.csv",
                            help="Path where to save the csv file with coordinates of each cabinet")
    arg_parser.add_argument("-viz", "--out_viz_path", default="result.png",
                            help="Path where to save the visualization")
    arg_parser.add_argument("-show", "--show_viz", default=True,
                            help="Flag indicating whether or not to show the visualization")
    arg_parser.add_argument("-colors", "--unique_colors", default=True,
                            help="Flag indicating whether or not to separate different type of cabinets")
    args = vars(arg_parser.parse_args())

    cabinet_finder = CabinetFinder(args)
    cabinet_finder.find()
