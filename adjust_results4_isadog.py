from classifier import classifier
from os import listdir
from get_pet_labels import get_pet_labels
from classify_images import classify_images

def adjust_results4_isadog(results_dic, dogfile):
    dognames_dic = dict()
    line_strip = list()
    value = "1"
    with open(dogfile, "r") as infile:
        lines = infile.readline()
        while lines != "":
            line_strip.append(lines.rstrip())
        
            lines = infile.readline()
    for idy in range (0, len(line_strip), 1):
        if line_strip[idy] not in dognames_dic:
            dognames_dic[line_strip[idy]] = value
    for key in results_dic:
        if results_dic[key][0] in dognames_dic:
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1, 1))
            else:
                results_dic[key].extend((1, 0))
        else:
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0, 1))
            else:
                results_dic[key].extend((0, 0))
    None
