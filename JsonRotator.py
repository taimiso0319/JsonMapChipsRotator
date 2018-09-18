import numpy
import json
import copy
import math
import os
from io import StringIO
import sys

class EventTypeInfo:
    def __init__(self, event_type, hl_type):
        self.event_type = event_type
        self.hl_type = hl_type

def print_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j])

def initialize():
    path = os.path.dirname(sys.argv[0]) + "/"
    global json_text
    global output_text
    if len(path) == 1:
        path = ""
    json_text = path + "jsondatas.txt"
    output_text = path + "output.txt"

def randomize_endpointchip(jsondata):
    arr_eti = [EventTypeInfo(0,0)]
    for i in range(len(jsondata['mapChip'])):
        if 'mapChipType' in jsondata['mapChip'][i]:
            if jsondata['mapChip'][i]['mapChipType'] == 1:
                tmp_etype = jsondata['mapChip'][i]['mapEventType']
                tmp_hltype = jsondata['mapChip'][i]['hlType'] if 'hlType' in jsondata['mapChip'][i] else -1
                if len(arr_eti) == 1:
                    arr_eti[0].event_type = tmp_etype
                    arr_eti[0].hl_type = tmp_hltype
                else:
                    arr_eti.append(EventTypeInfo(tmp_etype,tmp_hltype))
                print()
                #print(jsondata['mapChip'][i])
                pass

def print_trapskill(jasondata):
    for i in range(len(jsondata['eventInfo'])):
        print(jasondata['eventInfo'][i]['trapSkillId'])

def rotate_right(jsondata):
    array_size=math.sqrt(len(jsondata['mapChip']))
    if not array_size.is_integer():
        return
    s = int(array_size)
    tmp_data = copy.deepcopy(jsondata)
    for i in range(len(jsondata['mapChip'])):
        a = (len(jsondata['mapChip']) - 1) - (i + ((s * (s-1)) - ((i%s) * (s+1)) - ((i // s) * (s-1))))
        jsondata['mapChip'][a] = tmp_data['mapChip'][i]
        if len(tmp_data['mapChip'][i]) > 0:
            jsondata['mapChip'][a]['addrId'] ='mapChipAdr_'+ str(s - (i//s)) +'-'+ str(i%s+2)
            jsondata['mapChip'][a]['mapDirectionType'] =  (tmp_data['mapChip'][i]['mapDirectionType'] + 90) % 360

def print_enmGrIds(jsondata):
    for i in range(len(jsondata['mapChip'])):
        if 'enmGrId' in jsondata['mapChip'][i]:
            print(jsondata['mapChip'][i]['enmGrId'])

if __name__ == "__main__":
    global json_text
    global output_text
    initialize()
    output = ""
    if sum(1 for line in open(json_text)) > 5000:
        print("too much lines for input, please make sure that has less than 5000 lines.")
        sys.exit(main())
    with open(json_text, "r") as fin:
        c = 0
        for list in fin:
            jsondata = json.loads(list.strip())
            #randomize_endpointchip(jsondata)
            #print_enmGrIds(jsondata)
            #print_trapskill(jsondata)
            output += str(jsondata)+'\n'
            for times in range(3):
                rotate_right(jsondata)
                output += str(jsondata)+'\n'
    output = output.replace("'",'"')
    if os.path.exists(output_text):
        with open(output_text, "w") as fout:
            fout.write(output)
    else:
        with open(output_text, "x") as fout:
            fout.write(output)
