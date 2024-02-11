# List comprehension 

def main():
    yell("Hello", "Little", "World")
    
def yell(*words):
    uppercased_words = [word.upper() for word in words]
    #unpack the words from the list
    print (*uppercased_words)
    
if __name__ == "__main__":
    main()

