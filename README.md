
# ComplyFinder
This project consists of two models working on eCFR dataset of Federal Banking Regulations of United States. One is a multi-label text classifcation model categorizing the regulations into labels--Money Laundering, Enforcement, Financial Reporting,Consumer Protection, Risk Management, Operational Integrity, Market Conduct. Second model is a basic semantic search engine based on setence transformers and BM-25 function for getting five relevant regulations based on a query from user in form of a keyword or statements. 

Hello !!! All the passionate studnets,Data Science and Machine Learning students. You are welcomed to use this project, modify it, reproduce and imporve it.

Feel free to modify and imporve the code. Message us if you have any doubts !!!

## Before Starting

I have used windows lapotp and commands might vary as operating system chnages. Install my project with jypter notebooks and all the requirements are present under requirements.txt

We installed Prodigy application for annotating and creating models which helps us to create models easily in less time !!

First download the dataset, explore it and make sure to clean and preprocess it for any application.

Dataset: https://huggingface.co/datasets/wesslen/ecfr-title-12

If you want to learn more about cleaning and preprocessing 
https://www.freecodecamp.org/news/data-cleaning-and-preprocessing-with-pandasbdvhj/

Prerequisites:

Sentence Transformers and Semantic Search: https://www.sbert.net/examples/applications/semantic-search/README.html

BM-25: https://www.rdocumentation.org/packages/superml/versions/0.5.7/topics/bm_25

Prodigy: https://prodi.gy/doc

Python: https://www.python.org/
(Touch with Json, Pandas etc modules is recommneded)

Jypter Notebook: https://jupyter.org/

Not compulsory but recommneded,

Visual Studio Code: https://code.visualstudio.com/

Google Colaboratory: https://colab.research.google.com/

## Installation

Simply start by installing Prodigy 

Steps:
1. Go to teriminal of Visual Studio Code or just powershell
2. Create a seperate folder
4. Then open the folder from in terminal.
5. Make sure to install python
6. If already installed then verify version with py --version
7. Then check the version of the pip: "pip --version" or "python -m pip --version".
8. If it is not installed then install it 
9. Install virtual environmnet using command "python -m pip install virtualenv".
10. Go with creating a random virtual environment name (lets say virtual environmnet name to be created is venv) using the command "python -m virtualenv venv"
11. Activate the virtual environment using the command ".\venv\Scripts\activate"
12. If you face any problem here, then go to windows powershell> open as adminstrator > type "Get-ExecutionPolicy" > change 'Restricted' to 'RemoteSigned' by using "Set-ExecutionPolicy RemoteSigned" command.
13. Then you are going to get name of virtual environment on left side bracket before path. Then activation done sucessfully and proceed to other steps.
14. Then check prodigy is installed or not using the command "python -m prodigy stats" command.
15. If prodigy does not exist go with installing it using python command "python -m pip install prodigy -f https://XXXX-XXXX-XXXX-XXXX@download.prodi.gy " using your license recieved to your mail from 'Explosion' 
16. Now you will get some results about sessions and datasets.

And you are good to go.

## Steps Documentation - Text classification model

1. Once prodigy is installed, go donwload the dataset.
2. You can start annotations for multi-label text classification model.

Refer Prodigy documents for any clartiy: https://prodi.gy/docs

3. After annotations, save them by clicking on save button on top left side and clicking ctrl+c
4. Then go with splitting the dataset with a code or manually. Splitting it with code is recommeded. Refer to Jypter notebook for more clarity.
4. Train the model using prodigy train or spacy train. 

Spacy Train: https://spacy.io/api/doc
Prodigy Train: https://prodi.gy/docs

5. Run the model and get stats.
6. You can fine tune with other models or train it further

## Steps Documentation - Semantic Search Engine

Just follow the jypter notebook code

