import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




print(logo.logo)
running = True
while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

    

    #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

    def encodeDecode(text,shift,direction):
        final_text = ""
        if direction == 'decode':
                shift *= -1
        for letter in  text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift
                final_text += alphabet[new_position]
            else:
                final_text += letter

        print(f"The decoded text is {final_text}")




    shift = shift % len(alphabet)
    encodeDecode(text, shift,direction)
    restart = input('Do you want to continue?? (y = yes, n = no)')

    if restart == 'y':
        running = True
    elif restart == 'n':
        running = False
        print('Bye')