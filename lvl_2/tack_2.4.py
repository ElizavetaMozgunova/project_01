# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
 new_string = ""
 for char in s:
    if char != "!":
            new_string += char
 return new_string
print(remove_exclamation_marks("Hi! Hello!"))  # "Hi Hello"
print(remove_exclamation_marks(""))  # ""
print(remove_exclamation_marks("Oh, no!!!"))  # "Oh, no"


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
     if len(s) == 0:
        return s
     last_char = s[-1]
     if last_char == "!":
        return s[:-1]
print(remove_last_em("Hi!"))  # "Hi"
print(remove_last_em("Hi!!!"))  # "Hi!!"
print(remove_last_em("!Hi"))  # "!Hi"



# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    words = s.split()
    new_words = []
    for word in words:
         exclamation_count = word.count("!")
         if exclamation_count != 1:
            new_words.append(word)
            new_string = " ".join(new_words)
            return new_string
print(remove_word_with_one_em("Hi!"))  # ""
print(remove_word_with_one_em("Hi! Hi!"))  # ""
print(remove_word_with_one_em("Hi! Hi! Hi!"))  # ""
print(remove_word_with_one_em("Hi Hi! Hi!"))  # "Hi"
print(remove_word_with_one_em("Hi! !Hi Hi!"))  # ""
print(remove_word_with_one_em("Hi! Hi!! Hi!"))  # "Hi!!"
print(remove_word_with_one_em("Hi! !Hi! Hi!"))  # "!Hi!"
