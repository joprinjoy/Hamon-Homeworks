import random
from urllib.request import urlopen
import sys

# URL to fetch words for the exercise
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# Dictionary with code snippets
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# Check if there two arguments and second argument is english
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# loop throgh the line from word_url
for word in urlopen(WORD_URL).readlines():
    #trimming the white spaces from word and append the string to WORDS
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    # Generating class names 
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    # Generate other names from the WORDS list
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    # Generate parameter lists for functions
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    # Process the snippet and phrase to replace placeholders
    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# Main loop to run the quiz
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")