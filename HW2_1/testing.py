#Import all the required libraries
import sys
import json
import model
import torch
import pickle
import training
import bleu_eval
from torch.utils.data import DataLoader

test_data=sys.argv[1]
test_json="MLDS_hw2_1_data/testing_label.json"
model_path="Model/modelarch.h5"
outputfile_path=sys.argv[2]

modelIP = torch.load(model_path)
files_dir = test_data
i2w,w2i,dictonary =training.dictonaryFunc(4)
test_dataset = training.test_dataloader(files_dir)
test_dataloaderr =training.DataLoader(dataset = test_dataset, batch_size=1, shuffle=True, num_workers=8)
model = modelIP

ss =training.testfun(test_dataloaderr, model, i2w)

try:
    with open(outputfile_path, 'w') as f:
        for id, s in ss:
            f.write('{},{}\n'.format(id, s))
        print('File updated successfully!')
except FileNotFoundError:
    with open(file_path, 'x') as f:
        for id, s in ss:
            f.write('{},{}\n'.format(id, s))
        print('File created and updated successfully!')

test = json.load(open(test_json,'r'))
output =outputfile_path
result = {}


with open(output,'r') as f:
    for line in f:
        line = line.rstrip()
        comma = line.index(',')
        test_id = line[:comma]
        caption = line[comma+1:]
        result[test_id] = caption
bleu=[]


for item in test:
    score_per_video = []
    captions = [x.rstrip('.') for x in item['caption']]
    score_per_video.append(bleu_eval.BLEU(result[item['id']],captions,True))
    bleu.append(score_per_video[0])
average = sum(bleu) / len(bleu)

print("Average bleu score is " + str(average))