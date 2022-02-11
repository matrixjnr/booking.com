#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'awardTopKHotels' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING positiveKeywords
#  2. STRING negativeKeywords
#  3. INTEGER_ARRAY hotelIds
#  4. STRING_ARRAY reviews
#  5. INTEGER k
#

def awardTopKHotels(positiveKeywords, negativeKeywords, hotelIds, reviews, k):
    # Write your code here
    pwords = positiveKeywords.split(" ")
    nwords = negativeKeywords.split(" ")
    
    hscore = {}
    
    for i in range(len(reviews)):
        hid = hotelIds[i]
        hscore[hid] = 0
        
        review = reviews[i].split(" ")
        
        p = 0
        n = 0
        
        for x in review:
            # print(x)
            if "." in x:
                x[0:len(x)-1]
            if x in pwords:
                p += 1
            if x in nwords:
                n += 1
        
        hscore[hid] = 3 * p - n
        
    new_data = dict(sorted(hscore.items(), key=lambda k: k[1], reverse=True))
    
    print(new_data)
        
    return new_data.keys()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    positiveKeywords = input()

    negativeKeywords = input()

    hotelIds_count = int(input().strip())

    hotelIds = []

    for _ in range(hotelIds_count):
        hotelIds_item = int(input().strip())
        hotelIds.append(hotelIds_item)

    reviews_count = int(input().strip())

    reviews = []

    for _ in range(reviews_count):
        reviews_item = input()
        reviews.append(reviews_item)

    k = int(input().strip())

    result = awardTopKHotels(positiveKeywords, negativeKeywords, hotelIds, reviews, k)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
