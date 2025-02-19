# steganography

 Secure Data Hiding in Images Using Steganography


*Project Description*

This project provides a secure and user-friendly method for hiding secret messages inside images using steganography and password-protected encryption. It ensures that confidential information can be safely embedded within an image and retrieved only by authorized users with the correct password.

Using AES encryption, the message is first encrypted with a user-provided password, making it unreadable without decryption. The encrypted message is then embedded into an image using steganography, ensuring that the presence of hidden data remains undetectable.

A Graphical User Interface (GUI) built with Tkinter makes the tool accessible to users without requiring technical expertise. The project is useful for secure communication, data protection, and cybersecurity applications.

*Key Features:*

- Password-Protected Encryption – Ensures only authorized users can decrypt the message

- Steganography – Hides the message inside an image without altering its appearance

- User-Friendly GUI – No need for command-line operations, just select an image, enter text & password

- Offline & Secure – Works locally on your computer, no internet connection required

- Cross-Platform – Compatible with Windows, Mac, and Linux

This project is perfect for cybersecurity professionals, journalists, developers, and privacy-conscious users who need a safe and efficient method for secure communication. 

## Requirements

Make sure you have the following dependencies installed before running the scripts:

```sh
pip install opencv-python
```

## Usage

### 1. Encryption Process (Hiding the Message)

To hide a secret message in an image:

```sh
python encrypt.py
```

#### Steps:

## Run the Encryption Script (Encrypt.py)

python Encrypt.py

## Select an Image

Choose a cover image (PNG format recommended)
This image will store the hidden message

## Enter the Secret Message & Password

Type the message you want to hide
Set a password for encryption

## Encryption & Steganography

The message is encrypted using AES encryption
The encrypted message is embedded into the image

## Save the New Image

A new stego-image (image with hidden message) is generated
This image looks the same but contains hidden data


### 2.  Decryption Process (Retrieving the Message)

To retrieve the hidden message from the encrypted image:

```sh
python decrypt.py
```

#### Steps:

## Run the Decryption Script (Decrypt.py)

python Decrypt.py

## Select the Stego-Image

Choose the image containing the hidden message

## Enter the Password

Type the correct password used during encryption

## Decryption & Message Extraction

The program extracts the hidden encrypted message
It decrypts the message using the provided password

## View the Secret Message

If the password is correct, the original message is displayed
If incorrect, decryption fails

## File Descriptions

- **encrypt.py** - Script to embed a secret message into an image.
- **decrypt.py** - Script to extract the secret message from the image.
- **sample_image.png** - Original image used for encryption.
- **key.txt** - Stores the password required for decryption.
- **output_image.jpg** - Image containing the hidden message.



## Notes

- The encryption process replaces pixel values with message bytes.
- The message length should not exceed the image size.
- A NULL (`\0`) byte is used as an end marker to detect the message termination.


## Conclusion

-This project safeguards confidential messages by embedding them in images with password-protected encryption. 
-It is an efficient and secure way to transmit sensitive data without raising suspicion.

