# Korean FrameNet

## About
Korean FrameNet is a lexical database that has rich annotations to represent the meaning of text using semantic frames.

## prerequisite
* `python 3`
* `nltk` (optional)

## How to use
**Install**
`git clone https://github.com/machinereading/koreanframenet.git`

**Import Korean FrameNet (in your python code)**
```
from koreanframenet import koreanframenet
version = 1.1 
kfn = koreanframenet.interface(version=version)
```

**Load dataset**
`training_data, dev_data, test_data = kfn.load_data()`
Each data is a list for a sentence and its FrameNet annotations. Each sentence consists of four lists: tokens, target, frame, and its arguments. For example, a sentence '이 도시는 대중교통수단이 잘 구비되어 있어 시민생활이 매우 편리하다' is shown in following four lists:
* TOKENS: ['이', '도시는', '대중교통수단이', '잘', '구비되어', '있어', '시민생활이', '매우', '편리하다.']
* TARGET: ['_', '_', '_', '_', '구비되다.v', '_', '_', '_', '_']
* FRAME: ['_', '_', '_', '_', 'Possession', '_', '_', '_', '_']
* ARGUMENTS: ['B-Owner', 'I-Owner', 'B-Possession', 'B-Manner', 'O', 'O', 'O', 'O', 'O']

TARGET list provides target annotation. The tag `_` means that the token is not target word and other tag is target word. For above example, the lexeme `구비되다.v` is annotated for the target word `구비되어` (5th token in TOKEN list). In this case, the lexeme `구비되다.v` is annotated with the frame `Possession`. In terms of FrameNet, arguments is annotated with frame element tags of the frame `Possession` with BIO scheme. For above example, the word '이 도시는' is annotated with `Owner`, the word '대중교통수단이' is with `Possession`, and the word '잘' is with `Manner`. 


## Licenses
* `CC BY-NC-SA` [Attribution-NonCommercial-ShareAlike](https://creativecommons.org/licenses/by-nc-sa/2.0/)
* If you want to commercialize this resource, [please contact to us](http://mrlab.kaist.ac.kr/contact)

## Publisher
[Machine Reading Lab](http://mrlab.kaist.ac.kr/) @ KAIST

## Acknowledgement
This work was supported by Institute for Information & communications Technology Promotion(IITP) grant funded by the Korea government(MSIT) (2013-0-00109, WiseKB: Big data based self-evolving knowledge base and reasoning platform)
