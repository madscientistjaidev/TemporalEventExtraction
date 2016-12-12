#!/usr/bin/env python

import os
import glob

'''
This file will act as a python module for Training CRF models using Stanford CRF classifiers and list of training files
'''
#output files
filepath = "stanford-ner-2015-12-09/data/TE3-platinum-test-text"
Testdir = "data/TE3-platinum-test-text/*.txt"
directory = "data/te3-platinum-col/inputCol"
targetdirectory = "data/TE3-platinum-test-output-final"

#Function to train model using files in directory
def run(fileName):
    os.chdir("stanford-ner-2015-12-09")
    #Classify Data
    os.system('java -mx4g -cp "stanford-ner.jar:lib/*" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -textFile '+fileName+ ' -outputFormat tsv > '+targetdirectory+'/'+tsvParse(fileName))
    os.chdir("..")

#Test Procedure
def test():
    if os.path.exists("stanford-ner-2015-12-09/ner-model.ser.gz"):
        #extract names of .txt files
        filenames = extractWriteNames(filepath)
        #create directory
        if not os.path.exists("stanford-ner-2015-12-09/"+targetdirectory):
            os.makedirs("stanford-ner-2015-12-09/"+targetdirectory)
        print("TESTING")
        #Run for each .txt file
        for file in filenames:
            run(file)
        stat()
    else:
        print ("FAILED :NO TRAINING MODEL FOUND")

#Test Data Statisitcs - Compare against Annotated Test Data
def stat():
    os.chdir("stanford-ner-2015-12-09")
    os.system('java -mx4g -cp "stanford-ner.jar:lib/*" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -testFile '+directory+'/' +' > '+'data/finalOutputAgainstActual.txt')
    os.chdir("..")
    
#Extract Filenames
def extractWriteNames(filepath):
    #extract names of files in folder
    allFiles = glob.glob("stanford-ner-2015-12-09/data/TE3-platinum-test-text/*.txt")
    
    #convert filePaths
    test_name = extract(allFiles)

    return test_name
    
#function to extract list
def extract(list):
    tokens = []
    i = 0
    for element in list:
        token = element.split("/")
        t = "data/TE3-platinum-test-text/"+token[3]
        tokens.append(t)
        i = i+1
    return tokens 
    
def tsvParse(filename):
    file = filename.split("/")
    file_tsv = file[2].split(".")
    file_tsv_name = file_tsv[0]+".tsv"
    return file_tsv_name
