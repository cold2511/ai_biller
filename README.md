# ai_biller

A Flask-based web application for image-based product identification, user authentication, and cost calculation.

## Features

- User Signup and Login
- Image-based text extraction and object recognition
- Storing extracted data in MongoDB
- Calculating total cost of identified objects
- Viewing and managing user data

## Prerequisites

- Python 3.7+
- MongoDB
- Tesseract OCR
- EasyOCR

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/cold2511/ai_biller.git
    cd ai_biller
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up MongoDB:**

    Ensure MongoDB is installed and running on your machine. By default, the app connects to a local MongoDB instance:

    ```plaintext
    mongodb://localhost:27017/
    ```

6. **Set up Tesseract OCR:**

    Install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).

7. **Set up environment variables:**

    Create a `.env` file in the project root directory and add the following:

    ```env
    SECRET_KEY=your_secret_key
    ```

## Running the Application

1. **Start the Flask application:**

    ```bash
    python app.py
    ```

2. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

### User Signup

- Navigate to `/register` to create a new user account.

### User Login

- Navigate to `/login` to log in with your username and password.

### Upload Image for Object Recognition

- After logging in, go to `/index` to upload an image for text extraction and object recognition.

### Calculate Total Cost

- Go to `/calculate` to view the total cost of identified objects.

### View Data

- Go to `/view_data` to manage your data.

### Thank You

- Go to `/thank_you` to clear your data.

## Project Structure

- `app.py`: Main application file
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript, images)

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or suggestions, feel free to open an issue or contact the repository owner.
