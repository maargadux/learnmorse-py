morse_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}

def morse_parser(txt):
    txt = txt.lower()
    morsetxt = ''
    #char for character 
    #txt for text
    #morsetxt for morse text
    #mose_dict for morse dictionary
    #morse_dict[char] for call the morse dictionary and put the character in the morse dictionary
    for char in txt:
        if char == ' ':
            morsetxt += ' '  # keep spaces between words
        elif char in morse_dict:
            morsetxt += morse_dict[char] + ' '  # add a space between letters
        else:
            morsetxt += '?'  # unknown character
    print(morsetxt)
morse_parser(input('Write your massage: '))
        

