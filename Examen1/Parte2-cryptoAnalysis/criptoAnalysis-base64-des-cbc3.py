from base64 import b64decode
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

key_b64 = "c3Bpcml0dXM="

key = b64decode(key_b64).decode('utf-8')
print("Decoded key: ", key)

key = key.ljust(8, ' ').encode('utf-8')

cipher_text_base64 = """upa4z5/RUfCx1HVLFKLXOlIYSKb8a7zGn4D+dlPRATPbnz4N4CCBdKWr978T35iXCktj86og7M
+2Qv260qHwkhbpxM1lXXNFcT/v7cb3UFy/5Q9md49vA7I0o8XCsZyo7KOTgmRonpzXbHzwXVOimcfTnh2v9pdggxCumDQ5jVpGrF8S7agqo
+Ogts7I+xWHVtOqtlvtgkwXdypikfDuzZV9/NaQ
CmChulm1No/GnZtPnxYsu5hZcPJN8MRUOUs
s+C9q+oIZGxf04cBbSZnt9RCPFkZcjxRcHLyVn2TfsR7OJ0sbc4z19MqUxQvXPmb8CsRdgbs6QQ6fxtJWBvkm6Bu3Leuuu1cNOqHmtjdamc5
xUtpzi7Z4UVWNgk67FIuzQGDcTfThFNumpjIiS6A7jfQmxT+Y7cQqc4FyIz8+He4hQxCciwCu2XLtNOFk+GXpM7BKZ5g4rInvOoR24xfLsZ8FVU
CCDOJkWBZJq+LNKuP1p5cq3OXJfGDOTAjT7a/5pJXSarWTGuLMhrVDXLDLHc/QjOvphAqLbg1kjbgY76WFZug9iktesLlpdBqpb/+8n8mrkXq
# CYy0cZcGlbLMOqgOhcsKSkDzRo08J4dqpQjyKCQroTltDbw=="""

print(f"\nSize of the encrypted text in Base64: {len(cipher_text_base64)} characters")

cipher_text = b64decode(cipher_text_base64)
print(f"Decoded cipher text content: {cipher_text.hex()[:20]}...")

iv = bytes([0] * 8)

print(f"\nExtracted IV: {iv.hex()}")
print(f"Size of the IV: {len(iv)} bytes")
print(f"\nSize of the cipher data: {len(cipher_text) - len(iv)} bytes\n")

cipher_des = DES.new(key, DES.MODE_CBC, iv=iv)

try:
    decrypted_text = cipher_des.decrypt(cipher_text)
    
    decrypted_text = unpad(decrypted_text, DES.block_size).decode('utf-8')
    
    print("Decrypted text:\n", decrypted_text)

except (ValueError, KeyError) as e:
    print(f"Error while decrypting: {e}")
