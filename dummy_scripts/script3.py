import os
import sys
import glob
import time
import timeit
import argparse
import numpy as np
import multiprocessing as mp

usage = """
This CLI script is used for full reconstruction, editing the script to change 
default parameters of pre-processing methods (zinger removal, ring-artifact removal) 
or reconstruction methods.
"""

parser = argparse.ArgumentParser(description=usage)
parser.add_argument("-p", dest="proj_scan", help="Scan number of tomographic data",
                    type=int, required=True)
parser.add_argument("-d", dest="df_scan", help="Scan number of dark-flat data",
                    type=int, required=True)
parser.add_argument("-c", dest="center", help="Center of rotation", type=float,
                    required=False, default=0.0)
parser.add_argument("-r", dest="ratio", help="Ratio between delta and beta for phase filter",
                    type=float, required=False, default=0.0)
parser.add_argument("-f", dest="output_format", help="Output format: hdf or tif",
                    type=str, required=False, default="hdf")

parser.add_argument("--start", dest="start_slice", help="Start slice",
                    type=int, required=False, default=0)
parser.add_argument("--stop", dest="stop_slice", help="Stop slice", type=int,
                    required=False, default=-1)
parser.add_argument("--left", dest="crop_left", help="Crop left", type=int,
                    required=False, default=0)
parser.add_argument("--right", dest="crop_right", help="Crop right", type=int,
                    required=False, default=0)

parser.add_argument("--ring", dest="ring_removal", help="Select ring removal: 'sort', 'norm', 'all', 'none'",
                    type=str, required=False, default='all')
parser.add_argument("--zing", dest="zinger_removal", help="Enable/disable (1/0) zinger removal",
                    type=int, required=False, default=1)

parser.add_argument("--method", dest="method", help="Select a reconstruction method: 'fbp', 'gridrec', 'sirt'",
                    type=str, required=False, default='fbp')
parser.add_argument("--ncore", dest="num_core", help="Select number of CPU cores",
                    type=int, required=False, default=None)
parser.add_argument("--iter", dest="num_iteration", help="Select number of iterations for the SIRT method",
                    type=int, required=False, default=100)
parser.add_argument("--chunk", dest="slice_chunk", help="Select number of slices for reading in one go.",
                    type=int, required=False, default=30)
args = parser.parse_args()
print("-" * 30)
print("Run script 3")
print("-" * 30)
time.sleep(3)
print("-" * 30)
print("End script 3")
print("-" * 30)


