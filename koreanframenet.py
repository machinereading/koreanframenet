
# coding: utf-8

# In[7]:


import json
import os
from .src import dataio


# In[2]:


#print('### Korean FrameNet ###')
#print('\t# contact: hahmyg@kaist, hahmyg@gmail.com #')
#print('')


# In[11]:


dir_path = os.path.dirname(os.path.abspath(__file__))


# In[19]:


class interface():
    def __init__(self, version=1.0):
        self.version = str(version)
        file_path = dir_path+'/resource/'+self.version+'/'
        with open(file_path+'KFN_lus.json', 'r') as f:
            self.kfn_lus = json.load(f)
        with open(file_path+'KFN_annotations.json', 'r') as f:
            self.kfn_annos = json.load(f)
            
    def load_data(self):
        trn, dev, tst = dataio.load_framenet_data(self.version)
        return trn, dev, tst
    
    def lus_by_word(self, word):
        result = []
        for luid in self.kfn_lus:
            d = self.kfn_lus[luid]
            if word == d['lexeme']:
                item = {}
                item['lu'] = d['lexeme']+'.'+d['pos']
                item['frame'] = d['frame']
                item['lu_id'] = int(luid)
                result.append(item)
        return result
    
    def lus_by_token(self, token):
        result = []
        for luid in self.kfn_lus:
            d = self.kfn_lus[luid]
            if token in d['surface_forms']:
                item = {}
                item['lu'] = d['lexeme']+'.'+d['pos']
                item['frame'] = d['frame']
                item['lu_id'] = int(luid)
                result.append(item)
        return result
        
    
    def annotations_by_lu(self, luid):
        result = []
        luid = str(luid)
        anno_ids = self.kfn_lus[luid]['annotation_ids']
        for anno_id in anno_ids:
            anno_id = str(anno_id)
            anno = self.kfn_annos[anno_id]
            args = []
            for a in anno['denotations']:
                if a['role'] == 'ARGUMENT':
                    arg = a['text'] + ' ['+a['obj']+']'
                    args.append(arg)
            item = {}
            item['lu'] = anno['lu']
            item['text'] = anno['text']
            item['arguments'] = args
            result.append(item)
        return result
    
    

