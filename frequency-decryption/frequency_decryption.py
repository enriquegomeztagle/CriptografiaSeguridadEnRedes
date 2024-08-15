from collections import Counter

alphabet = "abcdefghijklmnñopqrstuvwxyz"

def analyze_frequency(text):
    frequency = Counter([letter.lower() for letter in text if letter.lower() in alphabet])
    print("\nFrequency of the most common letters:")
    for letter, count in frequency.most_common(4):
        print(f"Letter: {letter}, Frequency: {count}")
    return frequency

def calculate_shift(frequency):
    most_frequent_letter = max(frequency, key=frequency.get)
    most_frequent_letter_position = alphabet.index(most_frequent_letter)
    e_position = alphabet.index('e')
    
    required_shift = (most_frequent_letter_position - e_position) % len(alphabet)
    print(f"\nShift found for -> ('{most_frequent_letter}') is: {required_shift}")
    return required_shift

def decrypt(text, shift):
    return ''.join(
        alphabet[(alphabet.index(letter.lower()) - shift) % 27].upper() if letter.isupper() 
        else alphabet[(alphabet.index(letter.lower()) - shift) % 27] if letter.lower() in alphabet 
        else letter
        for letter in text
    )

encrypted_text = """¡"Gnt ebtdtfge wtnpdfme", Pe pw wpxm op wm Gythpdetomo Bmymxpdtñmym. Bpda ¿Cgé etrytqtñm dpmwxpyfp? Xp dpñgpdom xgñsa m Rtadomya Ndgya, cgtpy etpyoa bdtetaypda umxáe ep bpdxtftó epyftdep fmw, bgpe eg pebídtfg k ñayhtññtóy qgpday wtndpe smefm cgp wm xgpdfp wp wtnpdó op eg bdabta ñgpdba, opuáyoa m eg pebídtfg wtnpdmd pw bpyemxtpyfa op wme rpypdmñtaype qgfgdme...”"""

frequencies = analyze_frequency(encrypted_text)

suggested_shift = calculate_shift(frequencies)

print(f"\nDecrypted text with shift -> ({suggested_shift}):\n\n{decrypt(encrypted_text, suggested_shift)}\n")
