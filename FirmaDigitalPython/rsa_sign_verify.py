import argparse
import sys
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature
from colorama import Fore, Style
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_key_pair():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def sign_message(message_bytes, private_key):
    return private_key.sign(
        message_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )


def save_bytes_to_file(data_bytes, file_name):
    with open(file_name, "wb") as f:
        f.write(data_bytes)


def load_bytes_from_file(file_name):
    with open(file_name, "rb") as f:
        return f.read()


def save_text_to_file(text, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(text)


def load_text_from_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()


def save_private_key(private_key, file_name):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    save_bytes_to_file(pem, file_name)


def save_public_key(public_key, file_name):
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    save_bytes_to_file(pem, file_name)


def load_public_key(file_name):
    public_key_pem = load_bytes_from_file(file_name)
    return serialization.load_pem_public_key(public_key_pem)


def verify_signature(message_bytes, signature, public_key):
    try:
        public_key.verify(
            signature,
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )
        return True
    except InvalidSignature:
        return False


def main():
    parser = argparse.ArgumentParser(description="Sign and verify messages using RSA.")
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    sign_parser = subparsers.add_parser("sign", help="Sign a message")
    sign_parser.add_argument("message", help="Message to sign")

    verify_parser = subparsers.add_parser("verify", help="Verify a signature")
    verify_parser.add_argument(
        "--message", default="text.txt", help="File containing the message"
    )
    verify_parser.add_argument(
        "--signature", default="sign.bin", help="File containing the signature"
    )
    verify_parser.add_argument(
        "--key", default="pub_key.pem", help="File containing the public key"
    )

    args = parser.parse_args()

    if args.action == "sign":
        private_key = generate_key_pair()
        public_key = private_key.public_key()

        message = args.message
        message_bytes = message.encode("utf-8")

        signature = sign_message(message_bytes, private_key)

        save_private_key(private_key, "priv_key.pem")
        save_public_key(public_key, "pub_key.pem")
        save_bytes_to_file(signature, "sign.bin")
        save_text_to_file(message, "text.txt")

        logger.info(Fore.GREEN + "\nFiles saved:" + Style.RESET_ALL)
        logger.info(Fore.YELLOW + "1. priv_key.pem" + Style.RESET_ALL)
        logger.info(Fore.YELLOW + "2. pub_key.pem" + Style.RESET_ALL)
        logger.info(Fore.YELLOW + "3. sign.bin" + Style.RESET_ALL)
        logger.info(Fore.YELLOW + "4. text.txt" + Style.RESET_ALL)

    elif args.action == "verify":
        try:
            public_key = load_public_key(args.key)
            signature = load_bytes_from_file(args.signature)
            message = load_text_from_file(args.message)
            message_bytes = message.encode("utf-8")

            is_valid = verify_signature(message_bytes, signature, public_key)
            print("\nOriginal message verification:")
            print(f"Message: {message}")
            print(f"Valid signature: {is_valid}")

            modified_message = input("\nEnter a modified message to verify: ")
            if modified_message:
                modified_message_bytes = modified_message.encode("utf-8")
                is_valid_mod = verify_signature(
                    modified_message_bytes, signature, public_key
                )
                print("\nModified message verification:")
                print(f"Message: {modified_message}")
                print(f"Valid signature: {is_valid_mod}")

        except FileNotFoundError as e:
            print(f"Error: File not found {e.filename}.")
            sys.exit(1)
        except Exception as e:
            print(f"Error during verification: {str(e)}")
            sys.exit(1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
