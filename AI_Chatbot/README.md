# 🤖 AI Chatbot - Rule-Based Customer Service Assistant

An intelligent, engaging rule-based chatbot designed to attract and assist humans, clients, and customers. Built with Python and Flask, featuring both CLI and web interfaces.

## ✨ Features

### 🎯 Core Capabilities
- **Enhanced Pattern Matching**: Advanced rule-based responses with fuzzy matching and keyword scoring
- **Intelligent Response Selection**: Multi-layered matching system for highly relevant responses
- **Multi-Purpose Support**: Handles greetings, product inquiries, pricing, support, and lead generation
- **Technology-Aware**: Recognizes and responds to specific technology questions (Python, React, databases, etc.)
- **Business Intelligence**: Understands business context and provides relevant solutions
- **Smart Fallbacks**: Provides helpful responses even for unclear or unrelated questions
- **Personality-Driven**: Friendly, professional, and engaging conversation style
- **Context Awareness**: Remembers user information throughout the conversation
- **Escalation Support**: Seamlessly connects users to human representatives when needed

### 🌟 Engagement Features
- **Personalized Responses**: Uses customer names and tailors responses
- **Emoji Integration**: Makes conversations more lively and human-like
- **Multiple Response Variations**: Prevents repetitive interactions
- **Lead Capture**: Intelligently collects contact information
- **24/7 Availability**: Always ready to assist customers

### 🖥️ Interfaces
- **Web Interface**: Beautiful, responsive chat UI with real-time messaging
- **CLI Interface**: Command-line version for testing and development
- **REST API**: Easy integration with existing systems

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   cd AI_Chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web interface**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to: `http://localhost:5000`

### CLI Testing
```bash
python chatbot.py
```

## 📁 Project Structure

```
AI_Chatbot/
├── chatbot.py          # Main chatbot engine
├── responses.py        # Response database and patterns
├── app.py             # Flask web application
├── config.py          # Configuration settings
├── requirements.txt   # Python dependencies
├── templates/
│   └── index.html     # Web interface template
└── README.md          # This file
```

## 🎨 Customization

### Modify Bot Personality
Edit `config.py` to customize:
- Bot name and company information
- Business hours and contact details
- Response behavior and personality traits

### Add New Response Patterns
In `responses.py`, add new patterns to the `patterns` dictionary:

```python
'new_category': {
    'patterns': [
        r'\bnew pattern\b',
        r'\banother pattern\b'
    ],
    'responses': [
        "Response 1 with emoji! 😊",
        "Alternative response 2! 🚀"
    ]
}
```

### Customize Web Interface
Modify `templates/index.html` to change:
- Colors and styling
- Layout and design
- Branding elements

## 🔧 Configuration Options

Key settings in `config.py`:

| Setting | Description | Default |
|---------|-------------|---------|
| `BOT_NAME` | Chatbot's name | "Alex" |
| `COMPANY_NAME` | Your company name | "TechSolutions Pro" |
| `USE_EMOJIS` | Enable emoji responses | `True` |
| `WEB_PORT` | Web interface port | `5000` |
| `MAX_RESPONSE_LENGTH` | Maximum response length | `200` |

## 🎯 Use Cases

### Customer Service
- Answer frequently asked questions
- Provide business information
- Handle support requests
- Escalate complex issues to humans

### Lead Generation
- Qualify potential customers
- Collect contact information
- Schedule consultations
- Provide product information

### Sales Support
- Explain services and products
- Provide pricing information
- Connect with sales team
- Answer pre-sales questions

## 🌐 API Endpoints

### POST `/api/chat`
Send a message to the chatbot
```json
{
  "message": "Hello, I need help with pricing"
}
```

### GET `/api/welcome`
Get the welcome message

### POST `/api/reset`
Reset the conversation

### GET `/api/stats`
Get conversation statistics

## 🧪 Testing

### Manual Testing
1. Start the web interface: `python app.py`
2. Open browser to `http://localhost:5000`
3. Test various conversation flows:
   - Greetings and basic chat
   - Service inquiries
   - Pricing questions
   - Support requests
   - Contact information requests

### CLI Testing
```bash
python chatbot.py
```

### Enhanced Testing
```bash
# Basic functionality test
python test_chatbot.py

# Enhanced response testing
python test_enhanced_chatbot.py

# Interactive demo
python interactive_demo.py
```

Try these test phrases to see improved relevance:
- **Technology**: "Can you build React websites?", "Do you work with Python?"
- **Business**: "Tell me about your company", "How experienced is your team?"
- **Solutions**: "I need an ecommerce website", "Can you build a CRM system?"
- **Process**: "What's your development process?", "How long does it take?"
- **Pricing**: "How much does a website cost?", "What are your rates?"
- **Random**: "What's the weather?", "I like pizza" (see smart fallbacks!)

## 🔮 Future Enhancements

- **Database Integration**: Store conversations and user data
- **Analytics Dashboard**: Track conversation metrics
- **Multi-language Support**: Support for different languages
- **Voice Integration**: Add speech-to-text capabilities
- **AI/ML Integration**: Hybrid rule-based and ML approach
- **CRM Integration**: Connect with customer management systems

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section below
2. Review the configuration settings
3. Test with the CLI interface first
4. Check the browser console for errors

### Common Issues

**Port already in use**: Change `WEB_PORT` in `config.py`
**Module not found**: Run `pip install -r requirements.txt`
**Web interface not loading**: Check if Flask is running and accessible

---

**Built with ❤️ for better customer engagement**
