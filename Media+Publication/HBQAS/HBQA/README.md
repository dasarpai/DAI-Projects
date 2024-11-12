# Unveiling the Past: AI Powered Historical Book Question Answering (HBQA) System

## Introduction

In the recent past, various approaches, datasets, and models, including large language models (LLMs), have been employed for question-answering. While the outcomes of these initiatives are promising, challenges persist in generating questions from historical documents, particularly when translations involve different scripts and spelling variations. Addressing these challenges involves tackling the generation of descriptive answers, evaluating their correctness, measuring model performance, and extracting answers from a large corpus without context. 

This work explores techniques for creating questions and answers for a historical book corpus, focusing on ChatGPT and other available methods. Additionally, it involves fine-tuning the transformers and large language models for answer generation (AGS), retrieving relevant documents for answering questions (DRS), and developing a system capable of answering history questions without context (RAAGS). The Mahabharata book serves as the corpus for this study.

### Methodology & Sub-systems

**HBQAS Overall Approach**

images\projects\hbqas\HBQA-PPT+Images

![HBQAS Overall Approach](https://dasarpai.com/assets/images/projects/hbqas/HBQA-PPT+Images/Ch3.20-HBQA-Approach.png)

**HBQAS has four subsystems as mentioned below.**

**QAGS (Question-Answer Generation System):** Techniques for generating question-answer pairs using ChatGPT and other methods.

![Question-Answer Generation System](https://dasarpai.com/assets/images/projects/hbqas/HBQA-PPT+Images/Ch3.30-QAGS.png) 

**AGS (Answer Generation System):** Fine-tuning the t5 and flan-t5 models for creating an answer generation system.

![Answer Generation System](https://dasarpai.com/assets/images/projects/hbqas/HBQA-PPT+Images/Ch3.50-AGS.png)

**DRS (Document Retrieval System):** Retrieving relevant documents to answer specific questions.

![Document Retrieval System](https://dasarpai.com/assets/images/projects/hbqas/HBQA-PPT+Images/Ch3.40-DRS.png)

**RAAGS (Context-less Question Answering System):** Creating and evaluating a system that answers historical questions without any context.

![RAAGS](https://dasarpai.com/assets/images/projects/hbqas/HBQA-PPT+Images/Ch3.60-RAAGS.png)

### Evaluation Metrics

To evaluate the different sub-systems, various metrics have been employed, including:
- BLEU
- ROUGE
- Accuracy
- Recall
- R@n
- P@n
- F1@n
- Cosine

![HBQA-Evaluation-Metrics](https://dasarpai.com/assets/images/projects/hbqas/HBQA-PPT+Images/Ch3.70-HBQA-Evaluation-Metrics.png)

Text embedding is performed using SentenceTransformer, and the approach is designed to be domain-agnostic, script-agnostic, and language-agnostic. Manual feature engineering is not required.

### Results

- **QAGS:** Cosine between answer & question, answer & chunk is 0.91.
- **DRS:** Mean Reciprocal Rank (MRR) metric is 0.55, and Mean Average Precision (MAP) is 0.25.
- **AGS:** The Cosine between the reference answer and the predicted answer is 0.827.
- **RAAGS:** Cosine between the reference answer and the predicted answer is 0.763.

### Transformer Models Explored
- Text embedding is performed using SentenceTransformer, and the focus is to design domain-agnostic, script-agnostic, and language-agnostic. Manual feature engineering is not required.
- State-of-the-art transformers such as T5, distilBERT, RoBERTa, BLOOM, BERT, and BigBird from Hugging Face were explored for zero-shot learning.
- T5, Flan-T5 were used for model finetuning
---

[Link to the HBQAS GitHub Repository](https://github.com/dasarpai/HBQA)
