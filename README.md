# Spam/Ham Classifier using NLP

This project is a web application that classifies emails as either "Spam" or "Ham" (not spam) using Natural Language Processing (NLP) techniques. The application is built with Streamlit, a framework for creating interactive web applications in Python.

## Features

- **Email Text Input:** Users can input email text directly into the web application.
- **Text Preprocessing:** The input text is preprocessed by converting it to lowercase, removing punctuation, and filtering out stopwords.
- **Spam/Ham Classification:** A trained machine learning model is used to classify the preprocessed text.
- **Interactive Interface:** The application provides an easy-to-use interface to enter email text and get instant classification results.

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Clone the Repository

```bash
git clone https://github.com/Aymn-Mohd/SpamNLP.git
cd SpamNLP
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Required Files

Ensure you have the following files in the project directory:
- `Vectorizer.pkl`: The trained TF-IDF vectorizer.
- `Model.pkl`: The trained classification model.

## Usage

To run the Streamlit application, use the following command:

```bash
streamlit run SpamNLP.py
```

This will start the application, and you can access it in your web browser at `http://localhost:8501`.

## Project Structure

- `main.py`: The main script to run the Streamlit application.
- `Vectorizer.pkl`: Pickle file containing the trained Count vectorizer.
- `Model.pkl`: Pickle file containing the trained machine learning model.
- `requirements.txt`: List of required Python packages.

## How It Works

1. **Input:** The user enters email text into the provided text area.
2. **Preprocessing:** The entered text is preprocessed:
   - Converted to lowercase.
   - Punctuation is removed.
   - Stopwords are filtered out.
   - Words are stemmed using the Porter Stemmer.
3. **Vectorization:** The preprocessed text is transformed using the CountVectorizer vectorizer.
4. **Prediction:** The transformed text is classified using the trained model.
5. **Output:** The classification result ("Spam" or "Ham") is displayed on the web interface.


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

---

This README provides a comprehensive overview of the project, including setup instructions, usage details, and an explanation of how the application works. Adjust the content as needed based on your specific project details.
