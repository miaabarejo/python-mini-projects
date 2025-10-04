import string
# import art
# print(art.logo)

#coding exercise
def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(56)

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}. What is it like in {location}?")

name = input("What is your name? ")
location = input("What is your location? ")
greet_with(name, location)
#or
# greet_with("Jack", "Nowhere")

#coding exercise
def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    # Calculate the score for "TRUE"
    true_score = 0
    true_score += combined_names.count('t')
    true_score += combined_names.count('r')
    true_score += combined_names.count('u')
    true_score += combined_names.count('e')

    # Calculate the score for "LOVE"
    love_score = 0
    love_score += combined_names.count('l')
    love_score += combined_names.count('o')
    love_score += combined_names.count('v')
    love_score += combined_names.count('e')

    # Combine the scores to form a 2-digit number
    final_score = int(str(true_score) + str(love_score))

    print(final_score)

calculate_love_score(name1="Angela Yu", name2="Jack Bauer")

#cipher, di nisdiscuss if hindi encode/decode ung itype
alphabet = list(string.ascii_lowercase)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter

        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet) #modulo
            output_text += alphabet[shifted_position]
    print(f"Here is your {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Thank you for playing!")
