import numpy
import json
import copy
import math
import os
from io import StringIO
import sys


def print_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j])

def initialize():
    global json_text
    global output_text
    json_text = "jsondatas.txt"
    output_text = "output.txt"

def rotate_right(jsondata):
      
    array_size=math.sqrt(len(jsondata['mapChip']))
    if not array_size.is_integer():
        return
    s = int(array_size) 
    tmp_data = copy.deepcopy(jsondata)
    for i in range(len(jsondata['mapChip'])):
        a = 99 - (i + ((s * (s-1)) - ((i%s) * (s+1)) - ((i // s) * (s-1))))
        jsondata['mapChip'][a] = tmp_data['mapChip'][i]
        if len(tmp_data['mapChip'][i]) > 0:
            jsondata['mapChip'][a]['addrId'] ='mapChipAdr_'+ str(s - (i//s)) +'-'+ str(i%s+2)
            jsondata['mapChip'][a]['mapDirectionType'] =  (tmp_data['mapChip'][i]['mapDirectionType'] + 90) % 360

    


def appry(data_edited, jsondata):
    c = 0
    for i in range(len(datas)):
        for j in range(len(datas)):
            jsondata['mapChip'][c] = datas[i][j]
            c += 1

if __name__ == "__main__":
    initialize()
    global json_text
    global output_text
    output = ""
    if sum(1 for line in open(json_text)) > 5000:
        print("too much lines for input, please make sure that has less than 5000 lines.")
        sys.exit(main())
    with open(json_text, "r") as fin:
        c = 0
        for list in fin:
            jsondata = json.loads(list.strip())
            for times in range(3):
                rotate_right(jsondata)
                output += str(jsondata)+'\n'
    if os.path.exists(output_text):
        with open(output_text, "w") as fout:
            fout.write(output)
    else:
        with open(output_text, "x") as fout:
            fout.write(output)
    
