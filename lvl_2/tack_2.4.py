# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
 return s.replace("!", "")


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    pass


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
    pass



def _test_remove_comments():
  """
  Unit test for L{_remove_comments}.
  """
  s = '/*d s kjlsdf */*//*/*//**/**/*//**/a' * 50
  assert len(_remove_comments(s)) == len(s)
  s = '/**/' * 50 + '/*5845*/*/*//*/**/dfd'+'/*//**//'
  assert len(_remove_comments(s)) == len(s)
  s = 'a/**/' * 50 + '/**//**/////***/****/*//**//*/' * 5
  assert len(_remove_comments(s)) == len(s)
  s = 'hi /* foo */ hello /* bar!!!!! \n\n */ there!'
  assert _remove_comments(s) ==                                     \
         'hi           hello                   there!'