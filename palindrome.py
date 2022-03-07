decoline = "**************************************************"
print(decoline)
print("Welcome to palindrome checker")
print(decoline)
word = input("Introduce your word: ")
word_len = len(word)
is_palindrome = True
p_index = 0
print("\n...")
print('Word Lenth: ' + str(word_len))
print("...")
for letter in word:
  p_index = p_index + 1
  print(letter.lower() + " - " + word[word_len - p_index].lower())
  if is_palindrome is True:
    if letter.lower() != word[word_len - p_index].lower(): is_palindrome = False
print("...\n")

if is_palindrome:
  print('BOOM!!! it is palindrome!!')
else:
  print('No no, it is NOT a palindrome!!')
