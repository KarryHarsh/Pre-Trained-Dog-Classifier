from classifier import classifier
from os import listdir
from get_pet_labels import get_pet_labels

def classify_images(images_dir, results_dic, model):
    for key in results_dic:
        model_label = ""
        model_lab = ""
        model_label = classifier(images_dir + key, model)
        model_lab = model_label.lower().strip()
    
        truth = results_dic[key][0]
        if truth in model_lab:
            results_dic[key].extend((model_lab, 1))
        else:
            results_dic[key].extend((model_lab, 0))
    None
