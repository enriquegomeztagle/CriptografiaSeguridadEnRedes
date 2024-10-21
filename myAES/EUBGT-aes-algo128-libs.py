from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from colorama import Fore, Style, init
import logging
import sys

# Initialize colorama
init(autoreset=True)

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AESCipher:
    def __init__(self, key: str):
        """
        Initializes the AESCipher instance with a given key.

        Args:
            key (str): The encryption key, must be exactly 16 characters.

        Raises:
            ValueError: If the key is not 16 characters long.
        """
        if len(key) != 16:
            logger.error("The key must be exactly 16 characters.")
            raise ValueError("The key must be exactly 16 characters.")
        self.key = key.encode()
        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def encrypt(self, text: str) -> bytes:
        """
        Encrypts the given text using AES in ECB mode.

        Args:
            text (str): The text to be encrypted.

        Returns:
            bytes: The encrypted text in bytes.
        """
        text_padded = pad(text.encode(), AES.block_size)
        return self.cipher.encrypt(text_padded)

    def decrypt(self, encrypted_text: bytes) -> str:
        """
        Decrypts the given encrypted text using AES in ECB mode.

        Args:
            encrypted_text (bytes): The encrypted text in bytes.

        Returns:
            str: The decrypted text.
        """
        decrypted_padded = self.cipher.decrypt(encrypted_text)
        return unpad(decrypted_padded, AES.block_size).decode()

def get_key() -> str:
    """
    Prompts the user to enter the encryption key and validates its length.

    Returns:
        str: The encryption key provided by the user.

    Raises:
        ValueError: If the key is not 16 characters long.
    """
    key = input(Fore.CYAN + "Enter an encryption key (16 characters): ")
    if not key:
        logger.info("No input provided, using default key.")
        key = "default_key_1234"
        print(Fore.YELLOW + "No input provided, using default key: 'default_key_12345'")
    return key

def get_text_to_encrypt() -> str:
    """
    Prompts the user to enter the text to be encrypted and validates its length.

    Returns:
        str: The text to be encrypted.

    Raises:
        ValueError: If the text exceeds 16 characters.
    """
    text = input(Fore.CYAN + "Enter the text to encrypt (maximum 16 characters): ")
    if not text:
        logger.info("No input provided, using default text.")
        text = "default_text_"
        print(Fore.YELLOW + "No input provided, using default text: 'default_text_'")
    elif len(text) > 16:
        logger.error("The text must be a maximum of 16 characters.")
        raise ValueError("The text must be a maximum of 16 characters.")
    return text

def main():
    try:
        key = get_key()
        aes_cipher = AESCipher(key)

        text_to_encrypt = get_text_to_encrypt()
        encrypted_text = aes_cipher.encrypt(text_to_encrypt)

        logger.info("Text encrypted successfully.")
        print(Fore.GREEN + "Encrypted text in hexadecimal format:")
        print(Fore.YELLOW + encrypted_text.hex())

        decrypted_text = aes_cipher.decrypt(encrypted_text)
        logger.info("Text decrypted successfully.")
        print(Fore.GREEN + "Decrypted text:")
        print(Fore.YELLOW + decrypted_text)

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        print(Fore.RED + f"Error: {e}")
    except Exception as e:
        logger.critical(f"An unexpected error occurred: {e}")
        print(Fore.RED + f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
