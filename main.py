import numpy
import json
import os
from io import StringIO
import sys


def print_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j])

def initialize():
    print("Initializing......")
    global json_text
    json_text = "jsondatas.txt"
    #init
    print("Done.")

def rotate_right(d):
    tmp = numpy.chararray((10, 10), unicode=True, itemsize=1000)
    c = len(d)-1
    for i in range(len(d)):
        for j in range(len(d[0])):
            tmp[j][c] = d[i][j]
        c -= 1
    print_array(tmp)
    return tmp

if __name__ == "__main__":
    initialize()
    global json_text
    datas = numpy.chararray((10, 10), unicode=True, itemsize=1000)
    print(len(datas))
    with open(json_text, "r") as fin:
        c = 0
        for list in fin:
            jsondata = json.loads(list.strip())
            for i in range(len(datas)):
                for j in range(len(datas[0])):
                    datas[i][j] = jsondata['mapChip'][c]
                    c += 1
    rotate_right(datas)
