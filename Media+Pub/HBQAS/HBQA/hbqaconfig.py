
import configparser
config = configparser.ConfigParser()

env_list=['colab','local','kaggle'] 
def setEnv(env):
    if env=='colab': 
        apipath = r'/content/drive/MyDrive/config/hbqa.txt'
        config.read(apipath)
        conf = {
            "DATA_FOLDER" :  config['colab']['DATA_FOLDER'],
            "PE_FOLDER" : config['colab']['PE_FOLDER'],
            "QAGS_FOLDER" : config['colab']['QAGS_FOLDER'],
            "DRS_FOLDER" : config['colab']['DRS_FOLDER'],
            "AGS_FOLDER" : config['colab']['AGS_FOLDER'],
            "RAAGS_FOLDER" : config['colab']['RAAGS_FOLDER'],
            "REPORT_FOLDER" :  config['colab']['REPORT_FOLDER'],
            "CORPUS_SECTIONS_FOLDER" :  config['colab']['CORPUS_SECTIONS_FOLDER'],
            "CORPUS_CHAPTER_FOLDER" :  config['colab']['CORPUS_CHAPTER_FOLDER'],
            
            "OPENAI_KEY" : config['common']['OPENAI_KEY'],
            "PINECONE_API_KEY" : config['common']['PINECONE_KEY'],
            "PINECONE_ENV" : config['common']['PINECONE_ENV'],
            "CHATPDF_KEY" : config['common']['CHATPDF_KEY'],
        }
 
    elif env=="local":
        apipath = r'H:\My Drive\config\hbqa.txt'
        config.read(apipath)
        conf = {
            "DATA_FOLDER" :  config['local']['DATA_FOLDER'],
            "PE_FOLDER" : config['local']['PE_FOLDER'],
            "QAGS_FOLDER" : config['local']['QAGS_FOLDER'],
            "DRS_FOLDER" : config['local']['DRS_FOLDER'],
            "AGS_FOLDER" : config['local']['AGS_FOLDER'],
            "RAAGS_FOLDER" : config['local']['RAAGS_FOLDER'],
            "REPORT_FOLDER" :  config['local']['REPORT_FOLDER'],
            "CORPUS_SECTIONS_FOLDER" :  config['local']['CORPUS_SECTIONS_FOLDER'],
            "CORPUS_CHAPTER_FOLDER" :  config['local']['CORPUS_CHAPTER_FOLDER'],

            "OPENAI_KEY" : config['common']['OPENAI_KEY'],
            "PINECONE_API_KEY" : config['common']['PINECONE_KEY'],
            "PINECONE_ENV" : config['common']['PINECONE_ENV'],
            "CHATPDF_KEY" : config['common']['CHATPDF_KEY'],
        }
    elif env=="kaggle":
        conf = {
            "DATA_FOLDER" :  "",
            "PE_FOLDER" : "",
            "QAGS_FOLDER" : "",
            "DRS_FOLDER" : "",
            "AGS_FOLDER" : "",
            "REPORT_FOLDER" :  "",
            "CORPUS_SECTIONS_FOLDER" :  "",
            "CORPUS_CHAPTER_FOLDER" :  ""
        }
    return conf


