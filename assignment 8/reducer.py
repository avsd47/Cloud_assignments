#!/usr/bin/python3
import sys
current_word=None
current_count=0
for line in sys.stdin:
    line=line.strip().split(',')
    word,count=line[0],int(line[1])
    #print(f'{word}') #uncomment for part a
    if current_word == None:
        current_word=word
        current_count=count
    elif current_word == word:
        current_count+=count
    else:
        print(f'{current_word},{current_count}') #comment for part a
        current_word=word
        current_count=count
print(f'{current_word},{current_count}') #comment for part a
