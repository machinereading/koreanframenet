
# coding: utf-8

# In[1]:


import json
from pprint import pprint
import conll2textae


# In[2]:


def get_tsv_data():
    fn_dir = '../data/'+str(version)+'/'
    with open(fn_dir+'training.tsv','r') as f:
        trn = f.readlines()
    with open(fn_dir+'dev.tsv','r') as f:
        dev = f.readlines()
    with open(fn_dir+'test.tsv','r') as f:
        tst = f.readlines()
        
    d = trn+dev+tst
        
    tokens, lus, frames, fes = [],[],[],[]
    
    sent = []
    result = {}
    for line in d:        
        line = line.strip()
        if line.startswith('#'):
            if 'anno-id' in line:
                anno_id = line.split('anno-id:')[-1]
            else:
                pass
        else:
            if line != '':
                line_list = line.split('\t')
                tokens.append(line_list[1])
                lus.append(line_list[2])
                frames.append(line_list[3])
                fes.append(line_list[4])
            else:
                sent.append(tokens)
                sent.append(lus)
                sent.append(frames)
                sent.append(fes)
                result[anno_id] = sent
                sent = []
                tokens, lus, frames, fes = [],[],[],[]
    return result


# In[3]:


version = '1.1'
fname = '../resource/'+str(version)+'/KFN_annotations.json'
with open(fname+'.bak','r') as f:
    annos = json.load(f)
tsv_data = get_tsv_data()


# In[4]:


print(len(annos))
print(len(tsv_data))


# In[5]:


print(len(tsv_data['0'][0]))
print(len(tsv_data['0'][1]))
print(len(tsv_data['0'][2]))
print(len(tsv_data['0'][3]))


# In[6]:


new_annos = {}
for anno_id in annos:
    anno = annos[anno_id]
    tsv = tsv_data[anno_id]
    new_anno = conll2textae.get_textae([tsv])[0]
    new_anno['tokens'] = tsv[0]
    new_anno['sent_id'] = anno['sent_id']
    new_anno['source'] = anno['source']
    new_annos[anno_id] = new_anno
    
print(len(annos))
print(len(new_annos))


with open(fname, 'w') as f:
    json.dump(new_annos, f, ensure_ascii=False, indent=4)
print(fname, 'is written')

