#getting the 20 percent from the sentence 

# class for reapiting 20 percent words in the sentence 
def repeat():
    number = len(wordList)
    numb = int(number*0.20)
    for x in range(numb):
        wordList.insert((random.randint(1,len(wordList))-1),wordList[random.randint(1,len(wordList))-1])
        #print(len(wordList))
        #print(wordList)
        return wordList
    
# class for droping(deleting) 20 percent words in the sentence 
def drop():
    number = len(wordList)
    numb = int(number*0.20)
    for x in range(numb):
        num = (random.randint(1,len(wordList))-1)
        wordList.remove(wordList[num])
        #print(len(wordList))
        #print(wordList)
        return wordList
    
# class for swapping 20 percent words in the sentence 
def swap():
    def swapPositions(list, pos1, pos2): 
        list[pos1],list[pos2] = list[pos2],list[pos1] 
        return list
    
    number = len(wordList)
    numb = int(number*0.20)
    for x in range(numb):
        
        num1 = (random.randint(1,len(wordList))-1)
        num2 = (random.randint(1,len(wordList))-1)
        swapPositions(wordList, num1, num2)
        #wordList[num]
        
        #print(len(wordList))
        #print(wordList)
        return wordList



import pandas as pd
import numpy as np
import random
import re

df = pd.read_csv('/Users/ankitsaharkar/Desktop/brown-corpus/brown.csv')
df2 = df['tokenized_text'].str.split()
#df2 = df1.head(56340)     # training the model 
#df3 = df1.tail(1000)      # testing 

##############adding 20% noise to the dataset#########
noisy_dataset = []

for i in range(len(df2)):
    aa = df2.iloc[i]
    mystr = str(aa)
    wordList = re.sub("[^\w]", " ",  mystr).split()
    for x in range(1):
        choose_operation = random.randint(1,3)
        if choose_operation == 1:
            repeat()
            noisy_dataset.append(wordList)
            
        if choose_operation == 2:
            drop()
            noisy_dataset.append(wordList)
            
        if choose_operation == 3:
            swap()
            noisy_dataset.append(wordList)
            
    
df5 = pd.DataFrame(noisy_dataset)    
df5['ColumnA'] = df5[df5.columns[1:]].apply(
    lambda x: ' '.join(x.dropna().astype(str)),
    axis=1
)
noissy_dataset = df5['ColumnA']  
label = df[['label']]
label_tr = label

final_noisy_dataset = pd.concat([noissy_dataset, label_tr.reindex(label_tr.index)], axis=1)


#############testing ############
final_noisy_test = final_noisy_dataset.tail(1000)
final_noisefree_test = final_noisefree_dataset.tail(1000)

###############train ###############
final_noisy_train = final_noisy_dataset.head(50000)
final_noisefree_train = final_noisefree_dataset.head(50000)


###############validation ###############

final_noisy_dataset = final_noisy_dataset.head(56340)
final_noisefree_dataset = final_noisefree_dataset.head(56340)
final_noisy_valid = final_noisy_dataset.tail(6340)
final_noisefree_valid = final_noisefree_dataset.tail(6340)


####description ##########
i have wrote this code for adding the noise in the brown corpus dataset for training dataset i took first 50,000 sentence and 
validation i took next 6340 sentense and for testiong i took 1000 sentenses
