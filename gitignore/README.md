# SMS Spam Classifier

This project is an SMS spam classifier built using machine learning techniques. The model is trained using a dataset of SMS messages labeled as \"spam\" or \"ham\". 

## Project Structure

\`\`\`
spam-classifier/
├── data/
│   └── spam.csv
├── models/
│   ├── svm_spam_classifier.pkl
│   └── tfidf_vectorizer.pkl
├── notebooks/
│   └── data_preparation_and_model_training.ipynb
├── app/
│   ├── app.py
│   └── requirements.txt
├── .gitignore
└── README.md
\`\`\`

## Setup

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/yourusername/spam-classifier.git
cd spam-classifier
\`\`\`

### 2. Create and Activate Virtual Environment

\`\`\`bash
conda create -n spam-classifier python=3.8
conda activate spam-classifier
\`\`\`

### 3. Install Requirements

\`\`\`bash
pip install -r app/requirements.txt
\`\`\`

### 4. Run the Flask App

\`\`\`bash
cd app
python app.py
\`\`\`

## Usage

Send a POST request to the \`/classify\` endpoint with a JSON body containing the message to classify:

\`\`\`bash
curl -X POST http://127.0.0.1:5000/classify -H "Content-Type: application/json" -d '{"message": "Your message here"}'
\`\`\`

The response will be a JSON object with the classification result.

## License

This project is licensed under the MIT License.