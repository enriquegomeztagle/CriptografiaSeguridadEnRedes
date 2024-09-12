def caesar_cipher(text, shift):
    return ''.join(
        chr((ord(char) - base + shift) % 26 + base)
        if char.isalpha() else char
        for char in text
        for base in [ord('A') if char.isupper() else ord('a')]
    )


text = """
Qyyn zsvqbsw, iye ny
gbyxq iyeb rkxn dyy wemr,
Grsmr wkxxobvi nofydsyx
crygc sx drsc;
Pyb cksxdc rkfo rkxnc
drkd zsvqbswc’ rkxnc ny
dyemr,
Kxn zkvw dy zkvw sc ryvi
zkvwobc’ uscc.
"""

# Desplazar con k=-10 al restarle letras, que es lo mismo que sumarle 16 por ser un alfabeto de 26 letras
shift = 16
decrypted_text = caesar_cipher(text, shift)
print("Decrypted text with k={0}:".format(shift), decrypted_text)

shift = -10
decrypted_text = caesar_cipher(text, shift)
print("Decrypted text with k={0}:".format(shift), decrypted_text)
