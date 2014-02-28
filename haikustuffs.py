# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:32:02 2014

@author: dmichael
"""
from random import *

def sort_by_syllable(tweetsraw):
    tweets1=[]
    tweets2=[]
    tweets3=[]
    tweets4=[]
    tweets5=[]
    tweets6=[]
    tweets7=[]
    for i in len(tweetsraw):    
        if num_syllables(tweetsraw[i]) == 1:
            tweets1.append(tweetsraw[i])
        elif num_syllables(tweetsraw[i]) == 2:
            tweets2.append(tweetsraw[i])
        elif num_syllables(tweetsraw[i]) == 3:
            tweets3.append(tweetsraw[i])
        elif num_syllables(tweetsraw[i]) == 4:
            tweets4.append(tweetsraw[i])
        elif num_syllables(tweetsraw[i]) == 5:
            tweets5.append(tweetsraw[i])
        elif num_syllables(tweetsraw[i]) == 6:
            tweets6.append(tweetsraw[i])
        elif num_syllables(tweetsraw[i]) == 7:
            tweets7.append(tweetsraw[i])
    tweets = {1:tweets1,2:tweets2,3:tweets3,4:tweets4,5:tweets5,6:tweets6,7:tweets7}
    return tweets
    
def build_haiku(depth,tweets):
    # your doc string goes here
    """ creates a sudorandom function of a deapth between the min and max which you imput as an int"""
    # your code goes here
    if depth == 0:
        break
    if depth == 1:
        end = tweets[1]
        haiku = end[randint(0,len(end)-1)]
        return haiku
    
    y = randint(1,depth)    
    x = build_haiku(depth-y,tweets)


    if depth > 1:
        notend = tweets[y]
        haiku = [notend(randint(0,len(notend)-1)),x]
        return haiku
        
if __name__ == "__main__":
    tweets = sort_by_syllable(tweetsraw)
    line1 = build_haiku(5,tweets)
    line2 = build_haiku(7,tweets)
    line3 = build_haiku(5,tweets)
    