import json

def get_token_span(token_ids, text):
    text = text.split(' ')
    d = {}
    cid = -1
    for i in range(len(text)):
        if i == 0:
            d[i] = (0, len(text[i]))
            cid = len(text[i]) +1
        else:
            d[i] = (cid, cid+len(text[i]))
            cid =  cid+len(text[i]) +1
    start = True
    for i in token_ids:
        if start == True:
            begin = d[i][0]
            start = False
        end = d[i][1]
    span = {}
    span['begin'] = begin
    span['end'] = end
    return span

def get_relations(denos):
    relations = []
    for i in denos:
        if i['role'] == 'ARGUMENT':
            did = i['id']
            relation = {}
            relation['subj'] = 1
            relation['obj'] = did
            relation['pred'] = 'arg'
            relations.append(relation)
    return relations

def get_textae(conll):
    result = []
    for item in range(len(conll)):
        anno = conll[item]
        tokens, targets, frames, args = anno[0], anno[1], anno[2], anno[3]        
        text = ' '.join(tokens)
        
        tgt_list = []
        tgt_span = []
        for idx in range(len(targets)):
            if targets[idx] != '_':
                lu = targets[idx]
                frame = frames[idx]
                tgt_span.append(idx)
                tgt_list.append(tokens[idx])
        tgt_text = ' '.join(tgt_list)
        
        denos = []
        deno = {}
        deno['id'] = 1
        deno['obj'] = frame
        span = get_token_span(tgt_span, text)
        deno['span'] = span
        deno['token_span'] = tgt_span
        deno['role'] = 'TARGET'
        deno['text'] = tgt_text
        denos.append(deno)
        
        deno_id = 2
        for idx in range(len(args)):
            arg = args[idx]
            if arg.startswith('B'):
                arg_tokens, arg_span = [],[]
                arg_tokens.append(tokens[idx])
                arg_span.append(idx)
                arg_tag = arg.split('-')[1]
                next_idx = idx +1
                while next_idx <= len(args) and args[next_idx] == 'I-'+arg_tag:
                    arg_tokens.append(tokens[next_idx])
                    arg_span.append(next_idx)
                    next_idx +=1                
                    
                arg_text = ' '.join(arg_tokens)
                deno = {}
                deno['id'] = deno_id
                deno['obj'] = arg_tag
                span = get_token_span(arg_span, text)
                deno['span'] = span
                deno['token_span'] = arg_span
                deno['role'] = 'ARGUMENT'
                deno['text'] = arg_text
                denos.append(deno)
                deno_id += 1
        relations = get_relations(denos)
        d = {}
        d['text'] = text
        d['lu'] = lu+'.'+frame
        d['frame'] = frame
        d['denotations'] = denos
        d['relations'] = relations
        
        result.append(d)
        
    return result