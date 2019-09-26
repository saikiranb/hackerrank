from collections import OrderedDict
def merge_the_tools(string, k):
    length = len(string)
    
    parts = [string[i:i+k] for i in range(0, length, k)]

    for j in parts:
        sub = "".join(OrderedDict.fromkeys(j))
        print(sub)
merge_the_tools('AABCAAADA',3)