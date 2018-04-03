from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    text_string = text_string.replace('\n'," ")
    #after importing document text as a string, remove new line and replace with space
    text_list = text_string.split(" ")
    #split the words at the space
    chains = {}
    #create empty dictionary
  
    for i in range(len(text_list)-2):
    #create a key and value pair for the dictionary from the text list
    #loop through per index from beginning of list excepting the last two indicies
        value_list = []  
        first_two_key = (text_list[i], text_list[i+1])
        #create key tuple with first and second item from text list
        value_list.append(text_list[i+2])
        #create a value by appending the third item from the text list
        chains[first_two_key] = value_list
        #add key tuple and value into the dictionary

    return chains, text_string


def make_text(chains, text_string):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    
  #  for i in len(text_string)-1:
    text_string = text_string.rstrip()
    last_words_list = text_string.split(" ")[-2:]
    last_words_tuple = (last_words_list[0], last_words_list[1])

    for key in chains:
        while key != last_words_tuple:
            print "first", key
            random_word = choice(chains[key])
            #generate a random word from the value list
            text = text + key[0] + " " + key[1] + " " + random_word + " "
            #add to text string the tuple and random word
            second_two_key = (key[1], random_word)
            key = second_two_key
            print "new", key
            #set second key as the new key and reinitiate loop
        break
    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains, text_string = make_chains(input_text)
#print text_string
# Produce random text
random_text = make_text(chains, text_string)

print random_text
