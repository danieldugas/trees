from __future__ import print_function

import numpy as np
from scipy.misc import imread
import os
import matplotlib.pyplot as plt

def ensure_dir_exists(path):
    import os
    dir_ = path.rsplit('/',1)[0]
    if not os.path.exists(dir_):
        print("Directory",dir_, "created.")
        os.makedirs(dir_)
        return 1
    return 0

def write_trunks(trunks, path):
    ensure_dir_exists(path)
    with open(path, 'w') as file_handler:
        for item in trunks:
            file_handler.write("{}\n".format(item))
    print(len(trunks), " trunks written to", path)

def read_trunks(path):
    trunks = []
    with open(path, 'r') as file_handler:
        for line in file_handler:
            trunks.append(int(line.strip()))
    return trunks


in_dir = "./undistorted/"
out_dir = "./trunks_undistorted/"

import sys
script_path = sys.argv[0]
if len(sys.argv) == 3:
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
print("Input directory:", in_dir)
print("Output directory:", out_dir)

# List filenames
filenames = os.listdir(in_dir)
filenames = sorted(filenames)
print(len(filenames), "input files found.")

# Find if trunk data already exists
try: 
    already_existing_trunks = os.listdir(out_dir)
except FileNotFoundError:
    already_existing_trunks = []
    print("No pre-existing trunk data found")
for name in already_existing_trunks:
    corresponding_image_name = name[7:].split('.')[0]+'.'+filenames[0].split('.')[1]
    if corresponding_image_name in filenames:
        print("Trunk data found for", corresponding_image_name, ", will be skipped.")
        filenames.remove(corresponding_image_name)


plt.close("all")
plt.ion()
for name in filenames:
    image = imread(in_dir+name, flatten=True)
    plt.figure(1)
    plt.cla()
    plt.imshow(image, cmap="gray")
    plt.axhline(image.shape[0]/2, color='r')
    plt.title(name)
    trunks = []
    print("Click all visible tree trunk positions")
    while True:
        click = plt.ginput()
        if len(click) > 0:
            cut_x = click[0][0]
            plt.axvline(cut_x, color='g')
            plt.title(name+" [confirm position]")
            click2 = plt.ginput()
            if len(click2) > 0:
                plt.axvline(cut_x, color='lime')
                trunks.append(cut_x)
            else:
                plt.cla()
                plt.imshow(image, cmap="gray")
                plt.axhline(image.shape[0]/2, color='r')
                for x in trunks:
                    plt.axvline(x, color='lime')
            plt.title(name)
        else:
            break
    write_trunks(trunks, out_dir+"trunks_"+name.split('.')[0]+".txt")

plt.close("all")
