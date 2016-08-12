# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:28:45 2016

@author: Monir Zaman

Script reads one line of text from a file at a time and computes the similarity score
between two fields of the line and writes back the line with similarity score appended
at the end
"""

from MatchingRoutines import similarity

#Setting params
inputFile='C:\\Users\\mmoniruz\\Documents\\MyProjects\\agencyProject\\TwoListAgencies_csv.csv'
outputFile='C:\\Users\\mmoniruz\\Documents\\MyProjects\\agencyProject\\TwoListAgencies_csv_score.csv'
quote='"'
fieldAIndx=0
fieldBIndx=1


def splitHandlingQuote(line,splitChar=','):
    """
    Split that considers quote surrounding a string. example: '"ZASLAVSKY, ELONA AND GREG", NSERC'
    will be splitted into two individual strings 'ZASLAVSKY, ELONA AND GREG' and 'NSERC'
    
    Args:
        line - String
        splitChar - line will be splitted based on splitChar
    Return:
        a list of strings resulted after split
    """
    
    words=[]
    while line.find(quote)>=0:
        firstQuote=line.find(quote)
        secondQuote=line.find(quote,firstQuote+1)
        #append the word inside the quote
        words.append(line[firstQuote:secondQuote+1].strip('"'))
        
        #update line
        line=line[:firstQuote]+line[secondQuote+1:]
    
    #split the rest of the line based on the split character
    for aword in line.split(splitChar):
        if aword not in ('',' '):
            words.append(aword)
    return words
        
    

def processALine(line,splitChar=','):
    """
    Computes similarity score between two fields in the line
    Args:
        line - string
        splitChar - a character based on which line is splitted
    Return:
        string with similarity score appended        
    """
    fields=splitHandlingQuote(line)

    fieldA=fields[fieldAIndx]
    fieldB=fields[fieldBIndx]

    #computing similarity when any of the fields are not null    
    score=similarity(fieldA,fieldB)
    if fieldA=='null' or fieldB=='null':
        score=0.0        

    return line.strip()+splitChar+str(score)       
    

def readProcessWrite(inputFileName, outputFileName, lineProcessMethod, header=True):
    """
    Reads from the inputFileName one line at a time, process the line using
    lineProcessMethod which returns a text that is written in the outputFileName
    
    Args:
        inputFileName, outputFileName : string giving the input and output filenames
        lineProcessMethod : Method that will be used to process line of text
        header : whether input file contains a heading

    Return:
        None        
    """

    with open(inputFileName) as fr:
        fw=open(outputFileName,'w')
        
        if header:
            #write header to the output if input file contains header
            heading=fr.readline().strip()
            fw.write(heading+',Similarity_score'+'\n')
    
        for aline in fr:
            outline=lineProcessMethod(aline.strip().lower())
            fw.write(outline+'\n')
        
        fw.close()
    
if __name__=='__main__':
    readProcessWrite(inputFile,outputFile,processALine)