alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(text, shift):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    text_list = []
    number_list = []
    shift_list = []
    final_list = []
    for position in range(len(text)):
        letter = text[position]
        text_list.append(letter)

        num_alphabet = alphabet.index(text_list[position])
        number_list.append(num_alphabet)

        shift_position = number_list[position] + shift
        shift_list.append(shift_position)

        final_list.append(alphabet[shift_position])

        # if letter == text_list:
        #     new_position = position + shift
        #     letter = text[new_position]
        #

        # text_list.append(letter)
    print(text_list)
    print(number_list)
    print(shift_list)
    print(final_list)
    print(position)
    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


encrypt("hello", 5)
