import CaesarCipherArt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

misc = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', ' ', '?', '<', '>', ',', '.']

# Using index.
def caesar(cipher_direction, plain_text, shift_amount):
  cipher_text = ""
  if cipher_direction == 'decode' or cipher_direction == 'd':
    shift_amount *= -1
  for char in plain_text:
    if char in misc:
      cipher_text += char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      if new_position > 25:
        new_position %= 26
      elif new_position < 0:
        new_position %= -26
      cipher_text += alphabet[new_position]
  print(f"The {cipher_direction}d text is {cipher_text}.")



# # Using enumerate.
# def caesar(cipher_direction, plain_text, shift_amount):
#   cipher_text = ""
#   if cipher_direction == 'decode' or cipher_direction == 'd':
#     shift_amount *= -1
#   for char in plain_text:
#     if char in misc:
#       cipher_text += char
#     for position, alpha_letter in enumerate(alphabet):
#       if alpha_letter == char:
#         shift_amount % 26
#         new_position = position + shift_amount
#         if new_position > 25:
#           new_position %= 26
#         elif new_position < 0:
#           new_position %= -26
#         cipher_text += alphabet[new_position]
#   print(f"The {cipher_direction}d text is {cipher_text}.")



print(CaesarCipherArt.logo)
continues = True

while continues:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)

  answer = input("\nWould you like to restart the cipher program?\nYes (Y) - No (N)\n").lower()

  if answer == "no" or answer == "n":
    continues = False
    print("Goodbye")