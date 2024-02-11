# Map calls a function on each value of an iterable

def main():
    yell("Hello", "Little", "World")
    
def yell(*words):
    #call str.upper for each word
    uppercased_words = map(str.upper, words)
    #unpack the words from the list
    print (*uppercased_words)
    
if __name__ == "__main__":
    main()

