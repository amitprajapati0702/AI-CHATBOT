# AI-CHATBOT
# 🧠 AI Chatbot in Python (Limited Response Bot)

Welcome to the **AI Chatbot** project! This Python-based chatbot answers a limited set of predefined questions using simple AI logic. It’s designed for learning purposes, small-scale customer support, or demo prototypes. Lightweight, fast, and easy to understand!

## 🚀 Features

- Answers only a **limited set of known questions**
- Uses basic **Natural Language Processing (NLP) logic**
- **Keyword-matching** and **predefined response system**
- Command-line based chatbot
- Easy to extend with more Q&A pairs

## 🛠️ Technologies Used

- Python 3.x
- Basic NLP with string matching
- Optionally: `nltk` for word tokenization (optional and commented)

## 📂 Project Structure

ai_chatbot/
├── chatbot.py # Main script to run the chatbot
├── data.json # JSON file with predefined Q&A pairs
├── README.md # You are here!



## 🔧 How It Works

1. The chatbot loads predefined questions and answers from `data.json`.
2. It accepts user input and matches it with available questions.
3. If it finds a match (exact or partial), it responds.
4. Otherwise, it returns a fallback message like: “Sorry, I don’t understand that yet.”

## 💻 Usage

```bash
python chatbot.py

You: What is AI?
Bot: AI stands for Artificial Intelligence. It simulates human intelligence in machines.

{
  "What is AI?": "AI stands for Artificial Intelligence. It simulates human intelligence in machines.",
  "Who created you?": "I was created by a Python developer for demo purposes.",
  "How do you work?": "I match your question with a list of known answers."
}
```
email:- amitsprajapati123@gmail.com
Linkdin :- https://www.linkedin.com/in/amit-prajapati-b1b69032a/
