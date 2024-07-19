# This project is part of my M.Sc Thesis.

### Abstract 
Hindi is third most spoken language on our planet. Like English which is written in Roman script, Hindi also does not have its own script but almost all the Hindi speaking people write Hindi in Devanagari script. Hinglish is a mix language and it is spoken by Hindi speaking, English educated people and they can add words from other Indian languages during their conversation. Unlike Hindi Hinglish has its own script and this script is called Hinglish script. This script has characters borrowed characters from Roman and Devanagari scripts. [Demographics of india - wikipedia](https://en.wikipedia.org/wiki/Demographics_of_India) states that 65\% of Indian population is under 35 years age. Several disruptions like low cost mobile phone, extremely cheap data, digital India initiatives by government of India has caused huge surge in Hinglish language content. Hinglish language content is available in audio, video, images, and text format. We can find Hinglish content in comment box of online product, news articles, service feedback, WhatsApp messages, social media like YouTube, Facebook, twitter etc. With the increasing number of educated people in Indian society it is obvious that people do not say negative things directly even when they want to say. Generally, an educated mind is more diplomatic than less educated. In this paper we are demonstrating a system which can help in automatic sarcasm detection in Hinglish language. In this work no word, either Indian language words written in Roman or English word written in Devanagari is translated or transliterated. We developed our dataset with the help of 3 Hinglish language speakers. In this work we used ten classification libraries for classification work and developed 109 classification models, including 4 classification models developed using neural network. We analysed the performance of those models against the embedding and classifier used. Our best model with fastTextWiki embedding and Naïve Bayesian classifier gives 76\% accuracy, 78\% recall, 75\% precision, 76\% F1 score and 80\% AUC.	
   
   
### Aim and Objective of the Project
The aim of this research is to propose a model and embedding, which can predict sarcasm in a given Hinglish language sentence with highest possible accuracy. Based on the this primary goal, objectives of this research are as following.

<OL style="A">
<LI> To create Hinglish language dataset with minimum 2000 sentences, which can be used for training and testing a sarcasm detection model of Hinglish Language</li>
<LI> To develop a sarcasm detection models</li>
<LI> To check the effectiveness of Transfer learning for our work.</li>
<LI> To understand which embedding works best for Hinglish language.</li>
<LI> To understand which classifier performs best this proble</li>
</OL>

### Research Question of this Project are
<OL style="A">
<LI> To study how sarcasm detection is done by other researchers for English or any other Indian languages?
<LI> To determine which word embedding & linguistic features works best for sarcasm detection in our Hinglish dataset?
<LI> Is transfer learning useful for our work?
</OL>

### Scope of the Study
<OL style="A">
<LI>  This research is not related to any specific domain like philosophy, politics, history, current affair new etc. Rather it is trying to detect sarcasm in day to day informal conversation.
<LI> Sarcasm in our communication can be expressed and experienced at Visual (facial express, body language), Vocal (tone, pace of speech, emphasis on certain word) and text (book, newspaper, articles, social media tweets, comments and feedback box on internet. Visual sarcasm is more universal than vocal and written, because voice uses language and there are 7000+ languages on the earth so there is no universal vocal language of expressing sarcasm. But pause, pitch, pace, modulation between words, while speaking, are more universal like Visual. In this paper we are deal only with textbased sarcasm.
<LI>  Only Roman and Devanagari scripts are considered.
<LI>  Only Hindi and English language words are considered. If we find sentence using words from other languages, then we will not consider those sentences for our dataset.
<LI>  No analysis of degree of sarcasm.
<LI>  We know to understand the context datetime plays a critical role. Our base dataset does not have datetime. And lots of the text in the dataset is coming from nontweet sources which does not have datetime chronology of communication. Therefore, we ignored context which is coming from datetime.
</OL>

# Other Related Reports
- [SDSHL-An_Introduction_of_Sarcasm_Detection_In_Hinglish_(SDH)_and_Challenges.pdf](https://github.com/dasarpai/SDSHL/tree/main/docs/share/SDSHL-An_Introduction_of_Sarcasm_Detection_In_Hinglish_(SDH)_and_Challenges.pdf)

- [SDSHL-Dataset_Cleaning_Steps_for_Hinglish_Language_Corpus.pdf](https://github.com/dasarpai/SDSHL/tree/main/docs/share/SDSHL-Dataset_Cleaning_Steps_for_Hinglish_Language_Corpus.pdf)

- [SDSHL-ElsevierFormat](https://github.com/dasarpai/SDSHL/tree/main/docs/share/SDSHL-ElsevierFormat.pdf)

- [SDSHL-Performance_of_Various_Embedding_and_Classifers.pdf](https://github.com/dasarpai/SDSHL/blob/main/docs/share/SDSHL-Performance_of_Various_Embedding_and_Classifers.pdf)

- [SHSHL-Literature_Review_on_Sarcasm_Detection_In_Hinglish.pdf](https://github.com/dasarpai/SDSHL/blob/main/docs/share/SHSHL-Literature_Review_on_Sarcasm_Detection_In_Hinglish.pdf)


## Folder Structure
### Data folder has 4 folders 
- External - Here I kept the raw data which I acquired from scrapping twitter/blogs etc.
- Internal - After web scrapping I cleaned the data and put in excel file so that it can given to different annotators for the annotation. We need to annotate a sentence is sarcastic or not. This folder has data which I received from annonators.
- Processed - A final dataset was cleaned after considering inputs from annotators. Some classifers like FastText need data in certain format. That formatting was done and the files were kept in the folder. To ensure different classifier, different embedding have same data in train and test we created train and test and put in separate file in this folder.
- Results - After creating 109 models we evaluated the perform performance of each model against the test data. What prediction a model has done for a sentence is kept in the folder.

### Notesbooks
- 1-Exploration : All technical research related work done in this folder.
- 2-Experiments:  All the experiments are kept in this folder. Some of these were consider for final tuning and other left in this folder.
- 3-PoC : Final code of the project is in the folder. Files are number in the way they are processed in pipeline.

### Docs 
- 0-TopicSelection - All the work before project is finalized is kept in this folder.
- 1-Proposal - Proposal and related docs of this project is kept in this folder.
- 2-InterimReport - During the project, when Literature Review was complete, a report was subjected to LJMU. Files related to internal reports are kept in this folder.
- 3-Dissertation - Final dissertation and other documents created in this folder.
- 4-LaTex - To submit the work to Journal this was converted into latext format. All the related work is kept in this folder.
- 5-final - Journals cannot publish full thesis or dissertation so it need to be compressed. In this process I created some other reports and article which can be used for public consumption.
- 6-share - Articles, which I shared with professionals, researchers, interested parties are kept in this folder.

