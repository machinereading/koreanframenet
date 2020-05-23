
# coding: utf-8

# In[7]:


import json
import os
from .src import dataio

nltk = False
try:
    from nltk.corpus import framenet as fn
    nltk = True
except KeyboardInterrupt:
    raise
except:
    pass


# In[2]:


# print('### Korean FrameNet ###')
# print('\t# contact: hahmyg@kaist, hahmyg@gmail.com #')
# print('')


# In[11]:


dir_path = os.path.dirname(os.path.abspath(__file__))


# In[19]:


class interface():
    def __init__(self, version=1.1, info=True):
        self.version = str(version)
        file_path = dir_path+'/resource/'+self.version+'/'
        with open(file_path+'KFN_lus.json', 'r') as f:
            self.kfn_lus = json.load(f)
        with open(file_path+'KFN_annotations.json', 'r') as f:
            self.kfn_annos = json.load(f)
        with open(dir_path+'/resource/info/kfn'+self.version+'_lufrmap.json', 'r') as f:
            self.lufrmap = json.load(f)   
        with open(dir_path+'/resource/info/fn1.7_frame2idx.json', 'r') as f:
            self.fn17_idx = json.load(f)
        with open(file_path+'frame2luid.json','r') as f:
            self.frame2luid = json.load(f)
        self.info = info
            
    def load_data(self):
        trn, dev, tst = dataio.load_framenet_data(self.version, info=self.info)
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
    
    def lus_by_frame(self, frame):
        result = []
        luids = self.frame2luid[frame]
        for luid in luids:
            d = self.kfn_lus[str(luid)]
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
    
    def frames(self):
        result = []                   
        frames = []
        for lu in self.lufrmap:
            frame = self.lufrmap[lu]
            frames += frame
        frames = list(set(frames))
        for f in self.fn17_idx:
            if self.fn17_idx[f] in frames:
                result.append(f)
        return result
    
    def get_trans(self, luid):
        luid = str(luid)
        trans = self.kfn_lus[luid]['edef']
        return trans
    
    def get_trans_by_word(self, word):
        result = []
        kfn_interface = interface(version=self.version)
        lus = kfn_interface.lus_by_word(word)
        for lu_item in lus:
            lu, frame, luid = lu_item['lu'],lu_item['frame'],lu_item['lu_id']
            trans = kfn_interface.get_trans(luid)
            item = {}
            item['lu'] = lu
            item['frame'] = frame
            item['trans'] = trans
            result.append(item)
        return result
    
    def get_frame_definition(self, frame):
        if nltk == True:
            frame_idx = self.fn17_idx[frame]
            f = fn.frame(frame_idx)
            definition = f.definition
            return definition            
        else:
            print('please install nltk FrameNet first. refer: http://www.nltk.org/howto/framenet.html')
            return False
        
    def get_frames_by_trans(self, trans):
        if nltk == True:
            lemma = trans
            frames = fn.frames_by_lemma(lemma)
            if len(frames) == 0:
                lemma = r'(?i)'+str(trans)
                frames = fn.frames_by_lemma(lemma)
            frames = [i.name for i in frames]
            return frames
            
        else:
            print('please install nltk FrameNet first. refer: http://www.nltk.org/howto/framenet.html')
            return False
        
            
                      
    
    

