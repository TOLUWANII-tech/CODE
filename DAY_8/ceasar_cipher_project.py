alphabet= ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    
    for character in start_text:
        if character in alphabet:
            index = alphabet.index(character)
            if cipher_direction =='encode':
                new_index = (index+shift_amount)%26
            elif cipher_direction =='decode':
                new_index = (index+26-shift_amount)%26
            end_text+=alphabet[new_index]
        else:
            end_text += character

    print(f"The {cipher_direction}d text is {end_text}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text= input("Type your message:\n").lower()
    shift = int(input('Type the shift number:\n'))


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again, type 'no' if you want to quit")
    if restart =='no':
        should_continue = False




