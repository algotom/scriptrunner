#!/nsls2/data/hex/shared/software/conda/hex_tomo/bin/python

import os
import time
import glob
import timeit
import argparse


usage = """
This CLI script is used to find the center of rotation manually:
https://algotom.readthedocs.io/en/latest/toc/section4/section4_5.html#finding-the-center-of-rotation
"""

parser = argparse.ArgumentParser(description=usage)
parser.add_argument("-p", dest="proj_scan",
                    help="Scan number of tomographic data", type=str,
                    required=True)
parser.add_argument("-d", dest="df_scan", help="Scan number of dark-flat data",
                    type=str, required=True)
parser.add_argument("-s", dest="slice_index",
                    help="Index of the reconstructed slice for visualization",
                    type=int, required=True)

parser.add_argument("--start", dest="start_center", help="Start center",
                    type=int, required=True)
parser.add_argument("--stop", dest="stop_center", help="Stop center", type=int,
                    required=True)
parser.add_argument("--step", dest="step_center", help="Searching step",
                    type=float, required=False, default=1.0)

parser.add_argument("--left", dest="crop_left", help="Crop left", type=int,
                    required=False, default=0)
parser.add_argument("--right", dest="crop_right", help="Crop right", type=int,
                    required=False, default=0)
parser.add_argument("--ring", dest="ring_removal",
                    help="Select ring removal: 'sort', 'norm', 'all', 'none'",
                    type=str, required=False, default='norm')
parser.add_argument("--method", dest="recon_method",
                    help="Select reconstruction method: 'fbp' or 'gridrec'",
                    type=str, required=False, default='gridrec')
parser.add_argument("-r", dest="ratio",
                    help="Ratio between delta and beta for denoising. Larger is stronger",
                    type=float, required=False, default=0.0)
parser.add_argument("-v", dest="view",
                    help="Select a sinogram-based method or a reconstruction-based method: 'sino', 'rec'",
                    type=str, required=False, default="rec")

args = parser.parse_args()

print("-" * 30)
print("Run script 2")
print("-" * 30)
print(f"Project Scan ID  : {args.proj_scan}")
time.sleep(1)
print(f"Dark/Flat ID     : {args.df_scan}")
print(f"Slice index  : {args.slice_index}")
print(f"Phase Ratio      : {args.ratio}")
print(f"Start center      : {args.start_center}")
time.sleep(2)
print(f"Stop center       : {args.stop_center}")
print(f"Step center       : {args.step_center}")
print(f"Crop Left        : {args.crop_left}")
time.sleep(1)
print(f"Crop Right       : {args.crop_right}")
print(f"Ring Removal     : {args.ring_removal}")
print(f"Recon Method     : {args.recon_method}")
print("-" * 30)
print("End script 2")
print("-" * 30)

