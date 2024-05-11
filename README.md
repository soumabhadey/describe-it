# Describe It

Describe It is a simple web application that uses a pre-trained image captioning model to describe images.

## Description

This web application allows users to input an image URL and get a description of the image. It uses a pre-trained image captioning model to generate descriptions for images.

## Features

- Input an image URL to describe the image.
- Uses a pre-trained image captioning model to generate descriptions.
- Provides a loading message while the description is being fetched.

## Technologies Used

- Flask: a micro web framework for Python.
- HTML: markup language for creating web pages.
- CSS: stylesheet language for styling web pages.
- Bootstrap: front-end framework for designing responsive websites.
- Transformers: library for natural language processing using deep learning.
- PIL (Python Imaging Library): library for opening, manipulating, and saving many different image file formats.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/describe-it.git
   ```

2. Install the required dependencies:

   ```
   pip install flask transformers pillow
   ```

3. Run the Flask web server:

   ```
   cd describe-it
   python app.py
   ```

4. Open your web browser and go to `http://localhost:5000` to use the application.

## Usage

1. Enter the URL of the image you want to describe in the input field.
2. Click on the "Describe Image" button.
3. Wait for the description to load.
4. Once the description is generated, it will be displayed below the image.

## Credits

- [Flask](https://flask.palletsprojects.com/) - Web framework for Python
- [Bootstrap](https://getbootstrap.com/) - Front-end framework
- [Transformers](https://huggingface.co/transformers/) - Natural language processing library
- [PIL](https://pillow.readthedocs.io/) - Python Imaging Library
