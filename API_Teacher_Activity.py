from flask import Flask, render_template, url_for, request, jsonify
import tensorflow.keras
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('Boilerplate.html')
 
@app.route('/predict_emotion')
def predict_emotion():
 
    sentence= request.post["text_input"]

    # Tokenization

    tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
    tokenizer.fit_on_texts(sentence)

    # Create a word_index dictionary

    word_index = tokenizer.word_index

    sequence = tokenizer.texts_to_sequences(sentence)

    print(sequence[0:2])

    # Padding the sequence

    padded = pad_sequences(sequence, maxlen=100, 
                      padding='post', truncating='post')

    print(padded[0:2])

    # Define the model using .h5 file

    model=tensorflow.keras.models.load_model('Text_Emotion.h5')


   # Test the model

    result=model.predict(padded)

    print(result)

# Print the result

    predict_class = np.argmax(result, axis=1)

    print(predict_class)

    return(predict_class)

# {"anger": 0, "fear": 1, "joy": 2, "love": 3, "sadness": 4, "surprise": 5}

    return jsonify({'error' : 'Missing data!'})
     
     
if __name__ == '__main__':
    app.run(debug=True)