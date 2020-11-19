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


def load_data_by_source(source, info=True):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    fname = dir_path+'/../data/split_by_source/'
    
    if info:
        print('\n### loading Korean FrameNet (from', source, ')')
    
    if source == 'efn':
        # for training data
        trn_fname = fname+'ekfn_trn.tsv'
        with open(fname, 'r') as f:
            fn_d = f.readlines()
        trn_data = conll2data(fn_d)
        
        # for test data
        tst_fname = fname+'ekfn_tst.tsv'
        with open(fname, 'r') as f:
            fn_d = f.readlines()
        tst_data = conll2data(fn_d)
        
        result = (trn_data, tst_data)
        
        if info:
            print('tuples: (trn, tst)')
            print(len(trn_data), len(tst_data))
        
    elif source == 'jfn':
        # for training data
        trn_fname = fname+'jkfn_trn.tsv'
        with open(fname, 'r') as f:
            fn_d = f.readlines()
        trn_data = conll2data(fn_d)
        
        # for test data
        tst_fname = fname+'jkfn_tst.tsv'
        with open(fname, 'r') as f:
            fn_d = f.readlines()
        tst_data = conll2data(fn_d)
        
        result = (trn_data, tst_data)
        
        if info:
            print('tuples: (trn, tst)')
            print(len(trn_data), len(tst_data))
            
    elif source == 'probank':
        # for training data
        trn_fname = fname+'pkfn_trn.tsv'
        with open(fname, 'r') as f:
            fn_d = f.readlines()
        trn_data = conll2data(fn_d)
        
        # for unlabel data
        unlabel_fname = fname+'pkfn_unlabel.tsv'
        with open(fname, 'r') as f:
            fn_d = f.readlines()
        unlabel_data = conll2data(fn_d)
        
        # for test data
        tst_fname = fname+'pkfn_tst.tsv'
        with open(fname, 'r') as f:
            fn_d = f.readlines()
        tst_data = conll2data(fn_d)
        
        result = (trn_data, unlabel_data, tst_data)
        
        if info:
            print('tuples: (trn, unlabel_data, tst)')
            print(len(trn_data), len(unlabel_data), len(tst_data))
            
    elif source == 'sejong':
        # for training data
        trn_fname = fname+'skfn_trn.tsv'
        with open(fname, 'r') as f:
            fn_d = f.readlines()
        trn_data = conll2data(fn_d)
        
        # for unlabel data
        unlabel_fname = fname+'skfn_unlabel.tsv'
        with open(fname, 'r') as f:
            fn_d = f.readlines()
        unlabel_data = conll2data(fn_d)
        
        # for test data
        tst_fname = fname+'skfn_tst.tsv'
        with open(fname, 'r') as f:
            fn_d = f.readlines()
        tst_data = conll2data(fn_d)
        
        result = (trn_data, unlabel_data, tst_data)
        
        if info:
            print('tuples: (trn, unlabel_data, tst)')
            print(len(trn_data), len(unlabel_data), len(tst_data))
            
    else:
        print('input source: {efn, jfn, propbank, sejong}')
        
        
        
#     elif source == 'efn_test':
#         fname = fname+'ekfn_tst.tsv'
#     elif source == 'jfn':
#         fname = fname+'jkfn.tsv'
#     elif source == 'propbank':
#         fname = fname+'pkfn.tsv'
#     elif source == 'sejong':
#         fname = fname+'skfn.tsv'
    
#     else:
#         print('input source: {efn, jfn, propbank, sejong}')
    
#     with open(fname, 'r') as f:
#         fn_d = f.readlines()
        
#     fn_data = conll2data(fn_d)
    
#     if info:
#         print('\n### loading Korean FrameNet (from', source, ')')
#         print('\t# of instances :', len(fn_data))
    
    return result