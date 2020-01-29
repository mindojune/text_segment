import pympi
import glob     # Import glob to easily loop over files
import sys
import json
import csv
import random
from collections import Counter
import torch
from transformers import *
import spacy
import os
import argparse
import numpy as np
from sklearn import model_selection



def parse_args():
    """Parse command line arguments."""

    #eaf_path = "../data/annotations/"
    #json_path = "../data/json_data/"

    parser = argparse.ArgumentParser(description="K fold result report aggregate script")
    parser.add_argument("--chunk_length", default=128, type=int,
                        help="Chunk length. Choose from 128, 256, 512")
    parser.add_argument("--cuda", default=False, \
                       action = 'store_true',  help="Use CUDA.")

    return parser.parse_args()

def main():
    result_path = "./output_dir/level-"+str(level)+"/"
    
    #results = []
    total = Counter([])
    for i in range(k):
        with open(result_path+str(i)+"/metrics.json") as json_file:
            temp = json.load(json_file)       
            temp["training_duration"] = 0.0
            total = total + Counter(temp)
            #results.append(Counter(temp))
    
    total = { key:total[key]/float(k) for key in total }
    print(total)

    return

main()

