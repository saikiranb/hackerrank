def minion_game(string):
    # your code goes here
    string = str.upper(string)
    vowels = 'AEIOU'
    stuart = 0 #consonants 
    kevin = 0 #vowels
    length = len(string)
    for i in range(length):
        if(string[i] in vowels):
            kevin = kevin + (length - i);
        else:
            stuart = stuart + (length - i);
    if(kevin > stuart):
        print("Kevin "+str(kevin));
    elif(kevin < stuart):
        print("Stuart "+ str(stuart));
    else:
        print("Draw")

minion_game('saikiran')