alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]
def encryption(plain_text,shift_key):
    ciper_text=""
    for char in plain_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift_key)%26
            ciper_text+=alphabets[new_position]
        else :
            ciper_text+=char
    print(f"Cipher Text: {ciper_text}")




def decryption(ciper_text,shift_key):
    plain_text=""
    for char in ciper_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position-shift_key)%26
            plain_text+=alphabets[new_position]
        else :
            plain_text+=char
    print(f"plane text: {plain_text}")




wanna_end=False
while not wanna_end:
    what_to_do=input("Type 'encrypt' for encryption or 'decrypt' for decryption")
    text=input("Type your message:\n")
    shift=int(input("Type the shift number:\n"))
    what_to_do.lower()
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(text,shift)

    play_again=input("Type 'yes' or 'no':\n")
    if play_again=="no":
        wanna_end=True
        print("Thank you for using Caesar_Cipher")