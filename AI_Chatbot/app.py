"""
Flask Web Application for AI Chatbot
"""

from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
import uuid
from chatbot import create_chatbot
from config import WEB_PORT, DEBUG_MODE, BOT_NAME

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'
CORS(app)

# Store chatbot instances for each session
chatbot_sessions = {}

@app.route('/')
def index():
    """Main chat interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        # Get or create session ID
        if 'session_id' not in session:
            session['session_id'] = str(uuid.uuid4())
        
        session_id = session['session_id']
        
        # Get or create chatbot for this session
        if session_id not in chatbot_sessions:
            chatbot_sessions[session_id] = create_chatbot()
        
        bot = chatbot_sessions[session_id]
        
        # Get user message
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Extract user info
        bot.extract_user_info(user_message)
        
        # Process message and get response
        bot_response = bot.process_input(user_message)
        
        return jsonify({
            'response': bot_response,
            'session_id': session_id,
            'bot_name': BOT_NAME
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/welcome', methods=['GET'])
def welcome():
    """Get welcome message"""
    try:
        # Get or create session ID
        if 'session_id' not in session:
            session['session_id'] = str(uuid.uuid4())
        
        session_id = session['session_id']
        
        # Get or create chatbot for this session
        if session_id not in chatbot_sessions:
            chatbot_sessions[session_id] = create_chatbot()
        
        bot = chatbot_sessions[session_id]
        welcome_message = bot.get_welcome_message()
        
        return jsonify({
            'message': welcome_message,
            'bot_name': BOT_NAME,
            'session_id': session_id
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/reset', methods=['POST'])
def reset_chat():
    """Reset chat session"""
    try:
        if 'session_id' in session:
            session_id = session['session_id']
            if session_id in chatbot_sessions:
                chatbot_sessions[session_id].reset_conversation()
        
        return jsonify({'message': 'Chat reset successfully'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get conversation statistics"""
    try:
        if 'session_id' not in session:
            return jsonify({'error': 'No active session'}), 400
        
        session_id = session['session_id']
        
        if session_id not in chatbot_sessions:
            return jsonify({'error': 'No chatbot session found'}), 400
        
        bot = chatbot_sessions[session_id]
        stats = bot.get_conversation_summary()
        
        return jsonify(stats)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print(f"🚀 Starting {BOT_NAME} Web Interface...")
    print(f"🌐 Open your browser to: http://localhost:{WEB_PORT}")
    print("💬 Ready to chat!")
    
    app.run(host='0.0.0.0', port=WEB_PORT, debug=DEBUG_MODE)
