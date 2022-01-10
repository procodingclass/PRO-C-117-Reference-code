from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import * 
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    print(request.json)
    input_text = request.json.get("text")  
    print(input_text)

    if not input_text:
        return jsonify({
            "status": "error",
            "message": "Please enter some text to predict emotion!"
        }), 400
    else:  
        predicted_emotion = predict(input_text)
        print(predicted_emotion)
        return jsonify({
            "data": {
                "predicted_emotion": predicted_emotion
            },
            "status": "success"
        }), 200
     
     
if __name__ == '__main__':
    app.run(debug=True)