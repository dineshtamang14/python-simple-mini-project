from textblob import TextBlob


wrong_spell = input("Enter a Word to check spelling: ")
correct_spell = TextBlob(wrong_spell)
corrected_spell = correct_spell.correct()
print(f"The correct spelling of word {wrong_spell} is: {corrected_spell}")
