
# Final Year Project: DNA-Based Steganography Desktop Application
**Completion Date**: December 2022

## Project Description

This project was completed as part of my final year in December 2022. This project is a desktop application for encoding and decoding messages using DNA-based cryptography and image steganography. The application provides a triple layer of security to ensure the confidentiality, integrity, and availability of the data.


## Table of Content

- Introduction
- Features
- Motivation
- Methodology
- Setup
- Usage
- Contributing
- Acknowledgements
## Introduction

As cyber-attacks become increasingly common, it is crucial to protect sensitive information from unauthorized access. This project aims to develop a covert communication app for secure data transmission using DNA cryptography and steganography techniques.

## Features

- Encode and decode messages using DNA-based cryptography.
- Embed encrypted messages into images using steganography.
- Triple layer of security: DNA cryptography, DNA steganography, and image steganography.
- User-friendly graphical interface for easy interaction.
- Fullscreen mode

## Motivation

In Pakistan, 68% of people use smartphones, making them vulnerable to cyber-attacks. There is a need for secure communication applications to protect sensitive information. This project aims to address this gap by providing a highly secure messaging application.
## Methodology

1. **Analysis of Algorithm**: Understanding and improving the DNA-based encryption algorithm.
2. **Development of Basic App Structure**: Creating the core structure of the desktop application.
3. **Integration of Encryption Algorithm**: Embedding the DNA-based encryption algorithm into the app.
4. **Testing, Debugging, and Deployment**: Ensuring the application functions correctly and securely.
## Setup
To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/dna-steganography-app.git
    cd dna-steganography-app
    ```

2. **Install the required dependencies**:
   Make sure you have the following libraries installed on your local machine before running this code:
   - **tkinter**: For the GUI (this is included in the Python standard library, so it doesn't need to be installed).
   - **Pillow**: For image handling.
   - **numpy**: For numerical operations and handling image data.
   - **requests**: For HTTP requests.
   - **webbrowser**: For opening web pages (this is included in the Python standard library, so it doesn't need to be installed).

3. **Run the application**:
    ```sh
    python main.py
    ```

## Usage

1. **Encoding a Message**: 
- Enter the message you want to encode in the provided text field.
- Select an image file using the "Browse" button.
- Click the "Encode" button to embed the encoded message into the image.
2. **Decoding a Message**:
- Select the image file containing the encoded message using the "Browse" button.
- Click the "Decode" button to extract and display the decoded message.
3. **Sharing**:
- Click the "Share" button to open a web browser (WhatsAPP web) and send the encoded message through a web application.
## Contributions

Contributions are always welcome!
Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Acknowledgements

This project was developed as part of my Bachelor's final year project at Eletronics Engineering Department at Mehran University of Engineering and Technology Jamshoro. I would like to thank my supervisors, Dr. Fahim Aziz Umrani and Engr. Khuhed Memon, and Dr Azam Memon for their guidance and support.
