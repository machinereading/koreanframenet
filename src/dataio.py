import json
import os

def lines2tsv(lines):
    tsv = []
    sent = []
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            pass
        else:
            if line != '':
                token = line.split('\t')
                sent.append(token)
            else:
                tsv.append(sent)
                sent = []
    return tsv

def conll2data(conll):
    tsv = lines2tsv(conll)    
    data = []
    for sent in tsv:     
        tok_str, tok_lu, tok_frame, tok_fe= [],[],[],[]
        for token in sent:
            tok_str.append(token[1])
            tok_lu.append(token[2])
            tok_frame.append(token[3])
            if token[4].startswith('S'):
                token[4] = token[4].replace('S-','B-')
            tok_fe.append(token[4])
        sent_list = []
        sent_list.append(tok_str)
        sent_list.append(tok_lu)
        sent_list.append(tok_frame)
        sent_list.append(tok_fe)
        data.append(sent_list)
    return data     

def load_framenet_data(version, info=True):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    fname = dir_path+'/../data/'+version+'/'
    with open(fname+'training.tsv','r') as f:
        trn_data = f.readlines()
    with open(fname+'dev.tsv','r') as f:
        dev_data = f.readlines()
    with open(fname+'test.tsv','r') as f:
        tst_data = f.readlines()
        
    trn = conll2data(trn_data)
    dev = conll2data(dev_data)
    tst = conll2data(tst_data)
    
    if info:
        print('\n### loading Korean FrameNet', version, 'data...')
        print('\t# of instances in training data:', len(trn))
        print('\t# of instances in dev data:', len(dev))
        print('\t# of instances in test data:', len(tst))
    
    return trn, dev, tst