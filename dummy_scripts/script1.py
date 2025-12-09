import os
import time
import glob
import argparse

usage = "This CLI script is used to reconstruct a few slices across image height"

parser = argparse.ArgumentParser(description=usage)
parser.add_argument("-p", dest="proj_scan", help="Scan number of tomographic data", type=int, required=True)
parser.add_argument("-d", dest="df_scan", help="Scan number of dark-flat data", type=int, required=True)
parser.add_argument("-c", dest="center", help="Center of rotation", type=float, required=False, default=0.0)
parser.add_argument("-r", dest="ratio", help="Ratio between delta and beta for phase filter", type=float, required=False, default=0.0)

parser.add_argument("--start", dest="start_slice", help="Start slice", type=int, required=False, default=0)
parser.add_argument("--stop", dest="stop_slice", help="Stop slice", type=int, required=False, default=-1)
parser.add_argument("--step", dest="step_slice", help="Step slice", type=int, required=False, default=100)

parser.add_argument("--left", dest="crop_left", help="Crop left", type=int,required=False, default=0)
parser.add_argument("--right", dest="crop_right", help="Crop right", type=int, required=False, default=0)
parser.add_argument("--ring", dest="ring_removal", help="Select ring removal: 'sort', 'norm', 'all', 'none'",
                    type=str, required=False, default='norm')
parser.add_argument("--method", dest="recon_method", help="Select reconstruction method: 'fbp', 'gridrec', 'sirt'",
                    type=str, required=False, default='gridrec')
parser.add_argument("--iter", dest="num_iteration", help="Select number of iterations for the SIRT method",
                    type=int, required=False, default=100)
args = parser.parse_args()

print("-" * 30)
print("Run script 1")
print("-" * 30)
print(f"Project Scan ID  : {args.proj_scan}")
time.sleep(1)
print(f"Dark/Flat ID     : {args.df_scan}")
print(f"Rotation Center  : {args.center}")
print(f"Phase Ratio      : {args.ratio}")
print(f"Start Slice      : {args.start_slice}")
time.sleep(2)
print(f"Stop Slice       : {args.stop_slice}")
print(f"Step Slice       : {args.step_slice}")
print(f"Crop Left        : {args.crop_left}")
time.sleep(2)
print(f"Crop Right       : {args.crop_right}")
print(f"Ring Removal     : {args.ring_removal}")
print(f"Recon Method     : {args.recon_method}")
print(f"Iterations       : {args.num_iteration}")
print("-" * 30)
print("End script 1                      ")
print("-" * 30)

