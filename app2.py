from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image
from io import BytesIO
import pymongo
import pytesseract
import easyocr
from werkzeug.security import generate_password_hash, check_password_hash

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

app.secret_key = 'your_secret_key'

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
#db = client["image_identification"]
#db2=client['h2']
#collection = db["identified_objects"]
#collection2=db["h22"]
db = client.mydatabase
collection = db.collection
collection2 = db.collection2


user_name='hr'
key=generate_password_hash("password123")
text='na'
name='na'
price=0
# Load pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

reader = easyocr.Reader(['en'])



def extext2(image_path):
    result = reader.readtext(image_path)
    #extracted_text = [text[1] for text in result]

    # Initialize variables to store the text with the highest confidence
    #highest_confidence_text = ''
    #highest_confidence_score = 0

    # Iterate through the result list
    #for box, text, confidence in result:
        # Check if the confidence score of the current text is higher than the highest recorded confidence score
        #if confidence > highest_confidence_score:
            # Update the highest confidence text and score
            #highest_confidence_text = text
            #highest_confidence_score = confidence

    # Return the text with the highest confidence
    #return highest_confidence_text
    tallest_text = ''
    largest_height = 0

    # Iterate through the result list
    for box, text, confidence in result:
        # Calculate the height of the current bounding box
        box_height = abs(box[3][0] - box[1][0])

        # Check if the height of the current bounding box is taller than the largest recorded height
        if box_height > largest_height:
            # Update the tallest text and height
            tallest_text = text
            largest_height = box_height

    # Return the text with the largest height
    return tallest_text

def extext(image_path):
    result = reader.readtext(image_path)
    extracted_text = [text[1] for text in result]

    # Initialize variables to store the text with the highest confidence
    #highest_confidence_text = ''
    #highest_confidence_score = 0

    # Iterate through the result list
    #for box, text, confidence in result:
        # Check if the confidence score of the current text is higher than the highest recorded confidence score
        #if confidence > highest_confidence_score:
            # Update the highest confidence text and score
            #highest_confidence_text = text
            #highest_confidence_score = confidence

    # Return the text with the highest confidence
    #return highest_confidence_text
    #tallest_text = ''
    #largest_height = 0

    # Iterate through the result list
    #for box, text, confidence in result:
        # Calculate the height of the current bounding box
        #box_height = abs(box[3][0] - box[1][0])

        # Check if the height of the current bounding box is taller than the largest recorded height
        #if box_height > largest_height:
            # Update the tallest text and height
            #tallest_text = text
            #largest_height = box_height

    # Return the text with the largest height
    return extracted_text




# Function to process image and identify objects
def process_image(image_bytes):
    img = Image.open(BytesIO(image_bytes))
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)[0]
    return decoded_predictions



def update_dic(user_name, s):
    query = {
    'user_name': user_name,  # Filter by username
    'text': s           # Filter by text
    }


# Execute the query and fetch the results
    result = collection.find_one(query)
    #result = collection.find_one({"name": name})
    #result2 = collection.find_one({"text": s})
    if result:
        
        te=result.get("text2")
        cost2=result.get("price")
        db.collection.delete_one({"user_name":user_name,"text":s,"price":cost2})
        db.collection2.insert_one({
            "user_name": user_name,
            "price": cost2,
            "text":s,
            "text2":te
        })
        
    



# Function to save data to MongoDB
def save_to_mongodb(name, price, text,user_name,key,text2):
    db.collection.insert_one({
        "name": name,
        "price": price,
        "text": text,
        "user_name":user_name,
        "key":key,
        "text2":text2
    })


@app.route('/index', methods=['GET', 'POST'])
def index():
    user_name = session.get('user_name')
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        file.seek(0)
        image_path='temp_image.jpg'
        file.save(image_path)
        #s='na'
        extracted_text =extext(image_path)
        file.seek(0)
        extracted_texts =extext2(image_path)
        file.seek(0)


        price = request.form['price']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file:
            # Extract text from the image
            #image = Image.open(file2)
            #extracted_text = pytesseract.image_to_string(image)
            s=extracted_text
            ss=extracted_texts

            filename = secure_filename(file.filename)
            file_bytes = file.read()
            identified_objects = process_image(file_bytes)
            object_name = identified_objects[0][1]

            save_to_mongodb(object_name, price,s,user_name,key,ss)

            return render_template('index.html', objects=object_name, filename=filename, price=price,s=s)

    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = collection.find_one({'user_name': username})
        if user and check_password_hash(user["key"], password):
            # Successful login
            # Redirect to the index page or any other page you want
            #user_name=username
            session['user_name'] = username
            return redirect(url_for('index'))
        else:
            flash('Invalid username/password')
            return redirect(url_for('login'))
    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        user_name=username
        key=hashed_password
        text2='na'
        save_to_mongodb(name,price,text,username,key,text2)

        #user_data = {'username': username, 'password': hashed_password}
        #coll.insert_one(user_data)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/calculate', methods=['GET'])
def calculate():
    #ans=sum(dict.values)
    user_name=session.get('user_name')
    cut=collection2.find({'user_name':user_name})
    ans=0
    data = []
    #for collection2 in db.list_collection_names():
        #collection3 = db[collection2]
        #documents = collection3.find({}, {"_id": 0, "name": 1, "price": 1})  # Exclude _id field
        #data.extend(documents)
    for doc in cut:
        ans+=int(doc["price"])
        #ans=1
    documents = collection2.find({'user_name':user_name}, {"_id": 0, "text2": 1,"price":1})  # Exclude _id field
    data.extend(documents)
    
    
    return render_template('calculate.html',data=data,ans=ans)

@app.route('/thank_you', methods=['GET'])
def thank_you():
    user_name=session.get('user_name')
    #db.collection.delete_many({})
    db.collection2.delete_many({'user_name':user_name})
    return render_template('thank_you.html')

@app.route('/view_data', methods=['GET','POST'])
def view_data():
    #dict={'na':'0'}
    object_j='hh'
    ans=0
    user_name = session.get('user_name')
    if request.method == 'POST':
        file = request.files['file']
        
        
        if file:
            filename = secure_filename(file.filename)
            image_path='temp_image.jpg'
            file.save(image_path)
        #s='na'
            extracted_text =extext(image_path)
            s=extracted_text
            file.seek(0)
            file_bytes = file.read()
            #image = cv2.imdecode(np.fromstring(file_bytes, np.uint8), cv2.IMREAD_GRAYSCALE)
            #_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
            #num_labels, labeled_image = cv2.connectedComponents(binary_image)
            #num_objects = num_labels
            identified_object = process_image(file_bytes)
            object_j=identified_object[0][1]
            update_dic(user_name,s)
            #result = collection2.find_one({"name": object_j})
            
                #if result: 
                    #ans=1

            #result = collection.find_one({"name": object_j})
            #return render_template('view_data.html',object_j=object_j)
            return render_template('view_data.html')
                
    return render_template('view_data.html')


if __name__ == '__main__':
    app.run(debug=True)
