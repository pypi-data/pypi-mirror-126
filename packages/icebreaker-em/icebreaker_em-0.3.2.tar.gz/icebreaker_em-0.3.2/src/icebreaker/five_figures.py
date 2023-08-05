import sys
import numpy as np

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
import mrcfile

# import cv2
# import os
# import seaborn as sns
from pathlib import Path


def main(grouped_mic_dir):
    with open("five_figs_test.csv", "w") as f:
        files = [
            str(filename)
            for filename in Path(grouped_mic_dir).glob("**/*.mrc")
        ]
        r = 10000

        f.write("path,min,q1,q2=median,q3,max\n")
        for img_path in sorted(files):
            with mrcfile.open(img_path, "r", permissive=True) as mrc:
                img = mrc.data
                if not np.isnan(np.sum(img)):
                    path = img_path[:-4]
                    min = int(np.min(img) * r)
                    q1 = int(np.quantile(img, 0.25) * r)
                    median = int(np.median(img) * r)
                    q3 = int(np.quantile(img, 0.75) * r)
                    max = int(np.max(img) * r)
                    f.write(f"{path},{min},{q1},{median},{q3},{max}\n")


if __name__ == "__main__":
    grouped_mic_dir = sys.argv[1]
    main(grouped_mic_dir)
