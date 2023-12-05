def word_frequency(sentence):
    value = sentence.split(" ")
    words = [word.replace(".", "") for word in value]   
    my_dictionary = {}

    for i in words:
        my_dictionary[i] = words.count(i)
    return(my_dictionary)
    

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)