#function to punctuate and capitalize
def sentence_maker(phrase):
    interrogatives = ("what", "where", "why", "how")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

#empty list to append to
results = []

#while loop to interate through the user input until \end
while True:
    user_input = input("Say Something: ")
    if user_input ==  "\end":
        break
    else:
        results.append(sentence_maker(user_input))

#add a space and join the user input together
print(" ".join(results))
