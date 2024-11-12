#Select Model Function

# https://www.sbert.net/docs/pretrained_models.html

#250MB, multi-qa-distilbert-cos-v1',  Max Sequence Length:	512, Dimensions:768, Normalized Embeddings:	true
#80MB, all-MiniLM-L6-v2, Max Sequence Length:	256, Dimensions:	384, Normalized Embeddings:	true
#290MB, all-distilroberta-v1, Max Sequence Length:	512, Dimensions:	768, Normalized Embeddings:	true
#420MB, all-mpnet-base-v2, Max Sequence Length:	384, Dimensions:	768, Normalized Embeddings:	true
#1.36GB, all-roberta-large-v1, Max Sequence Length:	256, Dimensions: 1024, Normalized Embeddings:	true

def select_embmodel(num, verbose=True):
    emb_modelshortlist = ['distilbert','minilm','distilroberta','mpnet','roberta']

    emb_modellist = ['multi-qa-distilbert-cos-v1',
                'all-MiniLM-L6-v2',
                'all-distilroberta-v1',
                'multi-qa-mpnet-base-dot-v1',
                'all-roberta-large-v1']

    embmodelname = emb_modellist[num]
    embmodelshort = emb_modelshortlist[num]
    embmodelname1 = "_" + embmodelname
    if verbose:
        print (embmodelname,'\t',embmodelshort,'\t', embmodelname1)
        
    return embmodelname, embmodelshort, embmodelname1

def describe(df):
    import pandas as pd
    summary = df.describe()
    sum_row = df.sum().to_frame().T
    sum_row.index = ['sum']
    summary = pd.concat([summary, sum_row])
    return pd.DataFrame(summary)

def select_predmodel(n):
    predmodels_list = {"0" :"T5:t5", "1" : "Flan-T5:flant5", "2":"GPT2:gpt2","3":"DistilBERT:distilbert",
                   "4":"RoBERTa:roberta","5":"Llama2:llama2", "6":"BERTSquad:bert", 
                   "7":"LongFormer:longformer", "8":"DistilBERT512:distilbert512"}
    predmodel_name = predmodels_list['2'].split(':')[n]
    return predmodel_name

def convert_to_int(values):
    v1=[]
    for v in values:
        v1.append(int(v))
    return v1

def convert_to_float(values,n=2):
    v1=[]
    for v in values:
        v1.append( round(float(v),n))
    return v1
