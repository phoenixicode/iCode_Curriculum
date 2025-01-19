# Dictionary of grammatical terms
grammar_terms = {
    "verbs": [
        "run", "walk", "jump", "eat", "sleep", "go", "play", "talk", "think", "work",
        "write", "sing", "dance", "is", "are", "was", "were", "have", "has", "do", "make", "give"
    ],
    "adverbs": [
        "quickly", "slowly", "happily", "sadly", "very", "well", "fast", "loudly", 
        "quietly", "carefully", "easily", "soon", "yesterday", "often", "sometimes", 
        "never", "always", "here", "there", "now"
    ],
    "adjectives": [
        "big", "small", "tall", "short", "happy", "sad", "fast", "slow", "bright", 
        "dark", "beautiful", "ugly", "easy", "difficult", "strong", "weak", "young", 
        "old", "new", "good", "bad"
    ],
    "prepositions": [
        "in", "on", "at", "over", "under", "through", "between", "behind", "before", 
        "after", "with", "without", "about", "around", "across", "against", "near", 
        "by", "for", "during"
    ],
    "nouns": [
        "dog", "cat", "house", "car", "book", "park", "computer", "phone", "apple", 
        "tree", "chair", "city", "water", "teacher", "student", "sky", "sun", 
        "table", "friend", "family"
    ],
    "pronouns": [
        "I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "them", 
        "us", "my", "your", "his", "her", "their", "its", "mine", "yours"
    ],
    "conjunctions": [
        "and", "but", "or", "so", "because", "although", "if", "when", "while", 
        "since", "though", "unless", "as", "yet", "nor"
    ],
    "determiners": [
        "a", "an", "the", "this", "that", "these", "those", "my", "your", "his", 
        "her", "its", "our", "their", "some", "any", "many", "few", "several"
    ],
    "interjections": [
        "wow", "oh", "ouch", "hey", "oops", "ah", "hmm", "yay", "ugh", "alas"
    ],
    "articles": [
        "a", "an", "the"
    ]
}
# Function to check if a word is in the dictionary
def is_word_in_dictionary(word):
    for key in grammar_terms:
        if word in grammar_terms[key]:
            return True, key
    return False, None
  
text = input("enter your desirable text: ").split()
sorted_dict = {}
print(text)

# sorting the input list in dictnory as per the grammar
for i in text:
  if is_word_in_dictionary(i)[0]:
    if is_word_in_dictionary(i)[1] in sorted_dict:
      sorted_dict[is_word_in_dictionary(i)[1]].append(i)
    else:
      sorted_dict[is_word_in_dictionary(i)[1]] = [i]
  else:
    #append the word to the grammer list as per user choice
      
    print(f"The word '{i}' does not exist in the dictionary.\nWould you like to add it to the dictionary? Please choose the appropriate category:")
    for k in grammar_terms.keys():
        print(k)
    category = input("Enter the category: ")
    if category in grammar_terms:
      grammar_terms[category].append(i)
      if category in sorted_dict:
        sorted_dict[category].append(i)
      else:
        sorted_dict[category] = [i]
      print(f"Word '{i}' added to {category} category successfully.")
    else:
      print("Invalid category entered.")
    



