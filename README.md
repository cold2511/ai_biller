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

## How to Run

### 🧠 Prerequisites

- Python 3.8+
- pip
- MongoDB installed locally
- `mongosh` for shell interaction
- Git

### 📦 Clone Repository

```bash
git clone https://github.com/your-username/scanner-less-biller.git
cd scanner-less-biller

🐍 Create Virtual Environment & Install Requirements
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt

⚙️ Set Up MongoDB Replica Set
MongoDB must be in replica set mode to allow transactions.

Stop any existing MongoDB service:
sudo systemctl stop mongod

Start a single-node replica set manually:
mongod --dbpath /data/db --replSet "rs0"


Make sure /data/db exists or create it with sudo mkdir -p /data/db

Open a new terminal and initiate replica set:
mongosh

Then inside mongosh:

rs.initiate()

You should see: "ok" : 1 in the result.

Optionally, check replica set status:

rs.status()

Now your MongoDB is replica-set enabled.

🚀 Run the App
python app2.py

Navigate to http://127.0.0.1:5000 in your browser.


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
