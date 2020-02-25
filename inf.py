#!/usr/bin/env python3

from PIL import Image
from coremltools.models import MLModel
import numpy as np
import os

def infer(inp_model_path, images):
    model =  MLModel(inp_model_path)
    for (path, image) in images:
        predictions = model.predict({'input.1': image})
        predictions = predictions['470'].reshape(-1)
        predictions = np.array2string(predictions, max_line_width=np.inf)
        print(path, predictions)

if __name__ == '__main__':
    ims_dir = '/Users/pete/Downloads/ims'
    images = sorted([i for i in os.listdir(ims_dir) if i.endswith(".png")])
    images = [(i,Image.open(os.path.join(ims_dir, i))) for i in images]
    mls_dir = '/Users/pete/Downloads'
    for p in sorted(os.listdir(mls_dir)):
        if not p.endswith(".mlmodel"):
            continue
        print(p)
        infer(os.path.join(mls_dir,p), images)
        print()
