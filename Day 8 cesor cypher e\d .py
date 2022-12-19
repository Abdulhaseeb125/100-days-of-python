def encrypt(msg, c_list, shift):
    encrypted = ""
    for i in range(len(msg)):
        position = c_list.index(msg[i])
        position += shift
        position %= 27
        encrypted += c_list[position]
    return encrypted


def decrypt(messsege, ch_list, Shift):
    Decrypt = ""
    for i in range(len(messsege)):
        position = ch_list.index(messsege[i])
        position -= Shift
        Decrypt += ch_list[position]
    return Decrypt


char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', ' ']
decision = 'y'
while decision == 'y':
    mode = input("Chose a mode: Encrypt or Decrypt").lower()

    if mode == "encrypt":
        message = input("Enter your message:").lower()
        shifts = int(input("Number of shifts:"))
        encrypted = encrypt(message, char_list, shifts)
        print(encrypted)
    elif mode == "decrypt":
        message = input("Enter your message:").lower()
        shifts = int(input("Number of shifts:"))
        decrypted = decrypt(message, char_list, shifts)
        print(decrypted)
    else:
        print("invalid Command.")

    decision = input("do you want to run again. y/n")
    if decision == 'y':
        continue
    elif decision == 'n':
        break
    else:
        print("invalid command.")
