# write a program to correct hte speling of the single wrong word 

from textblob import TextBlob 

mylist = ["frst" , "secnd"] 

correct_list = []

for word in mylist:
   correct_list.append(TextBlob(word))


for item in correct_list:
    print(item.correct())