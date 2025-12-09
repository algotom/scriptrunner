import os
import ast
import shutil
import sys
import time
import timeit
import argparse
import numpy as np

usage = """
This CLI script is used for find global min and global max of a reconstructed volume.
"""

parser = argparse.ArgumentParser(description=usage)
parser.add_argument("-p", dest="proj_scan", help="Scan number/name to full-reconstruction hdf data",
                    type=int, required=True)
parser.add_argument("-k", dest="hdf_key", help="Key to the dataset if input is in the hdf/nxs/h5 format. Optional. Default is entry/data/data",
                    required=False, default="entry/data/data")
parser.add_argument("--crop", dest="crop",
                    help="To crop the volume from the edges '(top, bottom, left, right, front, back)'. Default is (0, 0, 0, 0, 0, 0)",
                    type=str, required=False, default="(0, 0, 0, 0, 0, 0) ")
parser.add_argument("--skip", dest="skip",
                    help="Skipping step of images used for getting min-max values",
                    type=int, required=False, default=20)
args = parser.parse_args()

print("-" * 30)
print("Run script 5")
print("-" * 30)
time.sleep(5)
print("-" * 30)
print("End script 5")
print("-" * 30)