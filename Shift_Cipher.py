import sys

#global variables for the imported text and dictionary
textIn = ""
dict = ""

#array of lowercase alphabet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def main():
    global dict
    global textIn
    args = sys.argv #array of args from terminal
    if len(args) == 5: #correct amount of args detected for program run, proceeding
        try:
                inFile = open(args[2], "r") #open the file to read at path specified
                textIn = inFile.read()
        except :
            print("\nIssue opening input file, check path provided or permissions.\n")
            help()
            sys.exit()

        if args[1] == "-e" or args[1] == "-d": #checking if the file will be shifted
            
            try:
                outFile = open(args[4], "w") #open (create if not found) file to write output
            except :
                print("\nIssue opening output file, check path provided or permissions.\n")
                help()
                sys.exit()
            try:
                key = int(args[3]) #get the key specified as an integer
            except :
                print("\nIssue importing key, make sure given key is an integer.\n")
                help()
                sys.exit()
                
            if args[1] == "-e": #shifting, encrypting specifically
                textOut = shift(key%26)
            if args[1] == "-d": #shifting, decrypting specifically (notice inverted key input)
                textOut = shift(26-(key%26))
            
            outFile.write(textOut) #writing to the file with name provided at runtime
            outFile.close()
            inFile.close()

                
        elif args[1] == "-c": #checking for the cracking arg
            try:
                dictFile = open("dictionary.txt", "r") #import dictionary for use in cracking
                dict = dictFile.read().split()
            except :
                print("\nIssue importing dictionary, make sure dictionary.txt is in the same folder as Shift_Cipher.py.\n")
                help()
                sys.exit()
            try:
                crack(float(args[4])) #calling the crack method with the threshold value provided
            except ValueError:
                print("\nInvalid threshold value, make sure to enter a decimal.\n")
                help()
                sys.exit()
        else: #if no -e, -d, or -c found
            print("\nIncorrect values of arguments in command line.\n")
            help()
            sys.exit()

    else: #more or less than 5 args detected, invalid command line, exiting
        print("\nIncorrect number of arguments in command line.\n")
        help()
        sys.exit()
    
def shift(key): #function to shift the alphabet for a text by a given number (used for both encrypt and decrypt)
    output = ""
    for character in textIn.lower(): #looping through each character in input text
        if character.isalpha(): #checking if character is in alphabet
            output += alphabet[(alphabet.index(character) + key)%26] #appends the single shifted letter to the output string
        else: #character not in alphabet, goes to output unchanged
            output += character
    return output

def crack(threshold): #function for cracking, calls analyze() 25 times, for numbers 1-25, then prints if analyze returns acceptability at or above threshold.
    maxAcceptability = 0.0 #placeholder for highest threshold found
    for i in range(25):
        acceptability = analyze(shift(26-(i+1)%26)) #analyze call, happens 25 times, once for each possible alphabet shift. NOTE: This assumes it is not operating on the plaintext.
        if acceptability > maxAcceptability:
            maxAcceptability = acceptability
        if acceptability >= threshold:
            print("\nKey found!")
            print("Key is", i+1)
            print("Below is the cracked text.\n")
            print(shift(26-(i+1)%26))
            return

    print("\nNo possible key with the proportion of acceptable words above given threshold was found, sorry.")
    print("The highest threshold of the text tested was", str(maxAcceptability) + ", try slightly less than that value as threshold input.")
    return



def analyze(textToCompare): #takes a text, processes it and gives an acceptability value in a range from 0 to 1
    wordList = textToCompare.split() #splitting input text into a list of individual words
    countMatches = 0 #initialization of tally of acceptable words to calculate acceptability value
    acceptability = 0.0
    for word in wordList: #looping over each word in the text
        if dict.count(word) != 0: #if word in the shift is found in dictionary, increment match count by 1
            countMatches += 1
    try:
        acceptability = countMatches/len(wordList) #calculate how many words in the text had a match in the dictionary
    except :
        pass
        
    return acceptability

def help(): #print options for running the program, this method is called when some sort of user error causes the program to close
    print("Here are the options for running this command:")
    print("-e\t: specifies that the file will be encrypted.")
    print("-d\t: specifies that the file will be decrypted.")
    print("-c\t: specifies that the file will be cracked by brute force. Followed by -t.")
    print("-t\t: follows the filename used with -c, prefaces")
    print("\nBelow are some examples")
    print("python Shift_Cipher.py -e foo.txt 20 oof.txt")
    print("python Shift_Cipher.py -d foo.txt 7 oof.txt")
    print("python Shift_Cipher.py -c foo.txt -t .75")

if __name__ == "__main__": #main method call
    main()