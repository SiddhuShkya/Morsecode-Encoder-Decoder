# A Morse code encoder/decoder
import os

MORSE_CODE = (("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..","D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-","K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.","R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--","Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---","2"), ("...--", "3"), ("....-", "4"), (".....", "5"),
    ("-....", "6"), ("--...", "7"), ("---..","8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.",";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-","$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!"))
# converting tuple into dictionary
morse_code = dict(MORSE_CODE)
# this function is ued to introduce the program

def print_intro():
    return "Welcome to Wolmorse\nThis program encodes and decodes Morse code."
# this fuction is used to get all the required inputs needed for the program

def get_input():
    global mode  # globalizing mode to use it on other functions
    mode = input("Would you like to encode(e) or decode(d) : ").lower()
    i = 0
    if mode == "e" or mode == "d":
        # Asks if the user wants to read from a file or not
        input_file = input(
            "Would you like to read from a file (f) or the console(c) : ").lower()
        if input_file == "f":
            print(get_filename_input())
        else:
            # if user enters "e" or "E" then it encodes the message
            if mode == "e":
                encode_message = input(
                    "What message would you like to encode : ").upper()
                print(encode(encode_message))
            # if user enters "d" or "D" then it encodes the message
            elif mode == "d":
                decode_message = input(
                    "What message would you like to decode : ")
                print(decode(decode_message))
        i = i+1
    # if user typer values other than "e" and "d" then the program keeps asking until their input is valid.
    else:
        print(f"Invalid Mode")
        get_input()
    if i == 1:
        # This function asks the user if he wants to run the entire program again or not
        again = input(
            "Would you like to encode/decode another message? (y/n) : ").lower()
        if again == "y" or again == "yes":
            get_input()
        # When the the user enters "n" it ends the program
        elif again == "n" or again == "no":
            print("Thanks for using the program, goodbye!")
            quit()
# This function converts or encrypts the message from English to morse code.

def encode(message):
    global cipher
    new_morse_code_dict = {}
    for pair in morse_code.items():
        # creates another dictionary (new_morse_code_dict) that has its position of keys and values interchanged.
        new_morse_code_dict[pair[1]] = pair[0]
    cipher = ''
    for letter in message:
        # Adds the corresponding morse code along with a space to separate the codes for different characters
        if letter != ' ':
            cipher = cipher + new_morse_code_dict[letter] + ' '
        else:
            # 1 space indicates 1 character while 2 space indicates new words.
            cipher += ' '
    return cipher

# This function converts or decrypts the message from morse code to english

def decode(message):
    global decipher
    message += ' '
    decipher = ''
    ci_text = ''
    for letter in message:
        if letter != ' ':  # checks for space
            i = 0  # keeps tracks for space
            ci_text += letter  # stores the morse code of a single character
        else:
            i += 1  # keeps on indicating a new character
            if i == 2:  # keeps on indicating a new word
                decipher += ' '  # adds space to seperate different words
            else:
                # accesing the values using their keys
                decipher += list(morse_code.values()
                                 )[list(morse_code.keys()).index(ci_text)]
                ci_text = ''
    return decipher

# ---------- Challenge Functions (Optional) ----------
# reads the contents of the given text file and also converts all the characters to uppercase

def process_lines(filename, mode):
    file = open(filename, 'r')
    file = file.read().upper()
    if mode == "e":
        encode(file)
        write_lines(cipher)
    elif mode == "d":
        decode(file)
        write_lines(decipher)
# this function creates a new text file that stores the output result


def write_lines(lines):
    empty_string = ''
    in_file = open(input_file, 'r')
    output_file = open("result.txt", 'w')
    line = in_file.readline()
    while line != empty_string:
        output_file.write(lines)
        line = in_file.readline()
    in_file.close()
    output_file.close()
# This fuction checks whether the filename given by the user exists or not

def check_file_exists(filename):
    if os.path.isfile(filename):
        process_lines(filename, mode)
# keeps on asking the user the filename until the user inputs the correct filename
    else:
        print("Invalid Filename")
        get_filename_input()
# This function asks the user to enter the name of the text file

def get_filename_input():
    global input_file
    input_file = input("Enter a filename : ")
    check_file_exists(input_file)

# main function of the program

def main():
    print(print_intro())
    get_input()

# Program execution begins here
if __name__ == '__main__':
    main()