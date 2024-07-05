from flask import Flask, request, jsonify
import joblib

# Load model and vectorizer
model = joblib.load('../models/svm_spam_classifier.pkl')
vectorizer = joblib.load('../models/tfidf_vectorizer.pkl')

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify_message():
    data = request.get_json()
    message = data['message']
    message_tfidf = vectorizer.transform([message])
    prediction = model.predict(message_tfidf)
    result = 'spam' if prediction[0] == 1 else 'ham'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
