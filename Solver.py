from random import randint

import english_words

five_letter_words = [word for word in list(english_words.english_words_lower_alpha_set) if len(word) == 5]

answer = five_letter_words[randint(0, len(five_letter_words) - 1)]
print("Answer is", answer)

for i in range(1, 7):
    guess = five_letter_words[randint(0, len(five_letter_words) - 1)]
    print("Guess ", i, "is", guess)
    if guess == answer:
        print("FOUND", answer)
        break
    else:
        for j in range(5):
            if guess[j] == answer[j]:
                five_letter_words = [word for word in five_letter_words if word[j] == answer[j]]
            elif guess[j] in answer:
                five_letter_words = [word for word in five_letter_words if guess[j] in word and guess[j] != word[j]]
            else:
                five_letter_words = [word for word in five_letter_words if guess[j] not in word]
            print("Length of words list after", guess[j], len(five_letter_words))
