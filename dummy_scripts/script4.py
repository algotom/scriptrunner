import os
import ast
import shutil
import sys
import time
import timeit
import argparse
import numpy as np

usage = """
This CLI script is used for data reduction of a reconstructed volume: 
rescaling, downsampling, cropping, reslicing.
"""

parser = argparse.ArgumentParser(description=usage)
parser.add_argument("-p", dest="proj_scan", help="Scan number/name to full-reconstruction hdf data",
                    type=int, required=True)
parser.add_argument("-k", dest="hdf_key", help="Key to the dataset if input is in the hdf/nxs/h5 format. Optional. Default is entry/data/data",
                    required=False, default="entry/data/data")
parser.add_argument("--crop", dest="crop",
                    help="To crop the volume from the edges '(top, bottom, left, right, front, back)'. Default is (0, 0, 0, 0, 0, 0)",
                    type=str, required=False, default="(0, 0, 0, 0, 0, 0) ")
parser.add_argument("--rescale", dest="rescale",
                    help="Rescale to a 8/16-bit data-type. Default is 8",
                    type=int, required=False, default=8)
parser.add_argument("--gmin", dest="gmin",
                    help="To set global min for recaling data to 8-or 16-bit data. Default is None (for automated calculation)",
                    type=float, required=False, default=None)
parser.add_argument("--gmax", dest="gmax",
                    help="To set global max for recaling data to 8-or 16-bit data. Default is None (for automated calculation)",
                    type=float, required=False, default=None)
parser.add_argument("--downsample", dest="downsample", help="Downsample. e.g, 2x2x2. Default is 1x1x1",
                    type=int, required=False, default=1)
parser.add_argument("--axis", dest="axis", help="Axis for slicing the volume (only 2 options: 0 (z-slice) or 1 (y-slice)). Default is 1",
                    type=int, required=False, default=1)
parser.add_argument("--rotate", dest="rotate", help="Rotate the volume (degree) if reslicing is enabled. Optional. Default is 0.0",
                    type=float, required=False, default=0.0)
args = parser.parse_args()

print("-" * 30)
print("Run script 4")
print("-" * 30)
time.sleep(5)
print("-" * 30)
print("End script 4")
print("-" * 30)
