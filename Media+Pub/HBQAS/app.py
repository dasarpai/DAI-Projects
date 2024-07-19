!pip install -Uq transformers
!pip install -Uq evaluate
!pip install -Uq SentencePiece
!pip install -Uq sentence-transformers
!pip install rouge-score


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import ast
from tqdm import tqdm

import torch
import torch.nn as nn
from torch.optim import Adam
from torch.utils.data import Dataset, DataLoader, RandomSampler
from torch.nn.functional import cosine_similarity
import torch.nn.functional as F

from sentence_transformers import SentenceTransformer, util

import tensorflow as tf

# import spacy
# import string

from sklearn.model_selection import train_test_split

import transformers
from transformers import pipeline
import evaluate  # Bleu
from transformers import Trainer, TrainingArguments

import nltk
nltk.download('punkt')

import warnings
warnings.filterwarnings("ignore")



def load_model(predmodel_name):
    if predmodel_name=="t5":
        from transformers import T5Tokenizer, T5ForConditionalGeneration #,T5Model,  T5TokenizerFast
        model_name = "t5-small" #"t5-base"
        tokenizer = T5Tokenizer.from_pretrained(model_name)
        model = T5ForConditionalGeneration.from_pretrained(model_name, return_dict=True)
        model.to(DEVICE)
        optimizer = Adam(model.parameters(), lr=0.00001)
    return tokenizer, model
	

predmodel_name = "t5"
DEVICE = "cpu"
tokenizer, model = load_model(predmodel_name)

embmodel = SentenceTransformer(embmodelname)

=======================


from transformers import T5ForConditionalGeneration, T5Tokenizer
conf['MODEL_FOLDER'] = '/content/drive/MyDrive/HBQA/t5small-30epoch'

# Load the corresponding tokenizer
tokenizer = T5Tokenizer.from_pretrained( conf['MODEL_FOLDER'])

# Load the pre-trained T5 model
model = T5ForConditionalGeneration.from_pretrained(conf['MODEL_FOLDER'] )
model.to(DEVICE)




# @title Function: Predict Answer
def predict_answer(context, question, tokenizer, model):

    inputs = tokenizer(question, context, max_length= Q_LEN, padding="max_length", truncation=True, add_special_tokens=True)

    input_ids = torch.tensor(inputs["input_ids"], dtype=torch.long).to(DEVICE).unsqueeze(0)
    attention_mask = torch.tensor(inputs["attention_mask"], dtype=torch.long).to(DEVICE).unsqueeze(0)

    with torch.no_grad():
        outputs = model.generate(input_ids=input_ids, attention_mask=attention_mask, max_length=100)

    predicted_answer = tokenizer.decode(outputs.flatten(), skip_special_tokens=True)


    if len(predicted_answer)<3:
       predicted_answer="xxx"
    elif predicted_answer[0:5]=='[CLS]' or  predicted_answer[0:5]=='[SEP]' or predicted_answer[0:3]=='<s>' :
        predicted_answer="xxx"
    return predicted_answer

===
# @title Function: Predict Multipel Answer for Question and Corresponding Predicted Chunk
from IPython.display import clear_output
clear_output()

from IPython.display import display
from IPython.display import HTML

# Load file into dataframe for prediction.
#Get 5 answer from top 5 document for each question
tmpfilenm = "10.4-Predicted-DocumentId-for-Ques"+embmodelname1+".csv"
df = pd.read_csv( conf['RAAGS_FOLDER'] + tmpfilenm)

if predict_now:
  df_pred_answer = pd.DataFrame(columns=['Ques_Id','Question','Ref_Answer','Pred_FinalAns','Pred_Answer1','Pred_Answer2', 'Pred_Answer3', 'Pred_Answer4', 'Pred_Answer5'])

def predict_all_answers(df_pred, sample=True, verbose=False):
    import random
    if sample:
        ques_idx=random.sample( set(df.index),10)
    else:
        ques_idx = df.index

    total_items = len(ques_idx)

    for i  in ques_idx:

        ids = df.loc[i,"Pred_Chunk_Id"]
        ques_id = df.loc[i,"Ques_Id"]
        print ("Predicting for Question Id: ",ques_id)

        cond     = df_qa["Ques_Id"] == ques_id
        ques     = df_qa.loc[cond]["Question"].values[0]
        ref_ans  = df_qa.loc[cond]['Ref_Answer'].values[0]

        # print(ques)

        if len(ids)>3:
            ids = ast.literal_eval(ids)
        else:
            print("Sorry, No document")
            break

        if verbose:
            print('Question  :', ques)
            print("Ref Answer:", ref_ans)

        ans=[]
        for id in ids:
            # print(ques_id, id)
            cond  = df_chunk["Chunk_Id"]==id
            chunk = df_chunk.loc[cond]["Chunk"].values[0]

            # print(chunk[:20])
            pred_ans = predict_answer(chunk, ques, tokenizer, model)
            ans.append( pred_ans )

            if verbose:
                print("Pred Ans  :", pred_ans)


        # final prediction with all the joint answers.
        pred_finalans =  predict_answer(" ".join(ans), ques, tokenizer, model)

        if verbose:
            print("Final Pred Ans  :", pred_finalans)
            print('--------')

        df_pred_answer.loc[i] = ques_id, ques, ref_ans, pred_finalans, ans[0], ans[1], ans[2], ans[3], ans[4]






embmodelname, embmodelshort, embmodelname1 = 'multi-qa-mpnet-base-dot-v1', 'mpnet', '_multi-qa-mpnet-base-dot-v1'

embmodel = SentenceTransformer(embmodelname)

    Ans_Sentences = df_pred_answer1.Pred_FinalAns.tolist()
    Ans_Embeddings = embmodel.encode(Ans_Sentences)
	
	
