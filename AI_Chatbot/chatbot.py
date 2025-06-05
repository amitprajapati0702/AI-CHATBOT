"""
Main Chatbot Engine - Rule-based AI Chatbot
"""

import re
import json
import datetime
import random
from responses import ResponseDatabase
from config import *

class AIChatbot:
    def __init__(self):
        self.response_db = ResponseDatabase()
        self.conversation_history = []
        self.user_data = {}
        self.conversation_count = 0
        self.session_start = datetime.datetime.now()

    def process_input(self, user_input):
        """Process user input and generate appropriate response"""
        self.conversation_count += 1

        # Log the conversation
        if ENABLE_LOGGING:
            self.log_conversation(user_input, "user")

        # Check for escalation keywords
        if self.check_escalation(user_input):
            response = self.response_db.get_escalation_response()
        else:
            # Get response from pattern matching
            response = self.response_db.find_response(user_input)

            # Add personalization if user data exists
            response = self.personalize_response(response)

        # Log bot response
        if ENABLE_LOGGING:
            self.log_conversation(response, "bot")

        # Store in conversation history
        self.conversation_history.append({
            'user': user_input,
            'bot': response,
            'timestamp': datetime.datetime.now().isoformat()
        })

        return response

    def check_escalation(self, user_input):
        """Check if user wants to escalate to human support"""
        user_input_lower = user_input.lower()
        return any(keyword in user_input_lower for keyword in ESCALATION_KEYWORDS)

    def personalize_response(self, response):
        """Add personalization to responses based on user data"""
        if 'name' in self.user_data:
            # Add user's name to some responses
            if random.choice([True, False]):  # 50% chance to add name
                response = f"{self.user_data['name']}, {response}"

        return response

    def extract_user_info(self, user_input):
        """Extract user information from input"""
        # Simple email extraction
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, user_input)
        if emails:
            self.user_data['email'] = emails[0]

        # Simple name extraction (basic implementation)
        name_patterns = [
            r'my name is (\w+)',
            r'i\'m (\w+)',
            r'call me (\w+)',
            r'i am (\w+)'
        ]

        for pattern in name_patterns:
            match = re.search(pattern, user_input.lower())
            if match:
                self.user_data['name'] = match.group(1).title()
                break

    def log_conversation(self, message, sender):
        """Log conversation for analytics"""
        log_entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'sender': sender,
            'message': message,
            'session_id': id(self)
        }

        # In a real application, you'd save this to a database
        # For now, we'll just print it if in debug mode
        if DEBUG_MODE:
            print(f"[LOG] {sender.upper()}: {message[:50]}...")

    def get_conversation_summary(self):
        """Get summary of current conversation"""
        return {
            'total_messages': len(self.conversation_history),
            'session_duration': str(datetime.datetime.now() - self.session_start),
            'user_data': self.user_data,
            'conversation_count': self.conversation_count
        }

    def reset_conversation(self):
        """Reset conversation state"""
        self.conversation_history = []
        self.user_data = {}
        self.conversation_count = 0
        self.session_start = datetime.datetime.now()

    def get_welcome_message(self):
        """Get initial welcome message"""
        welcome_messages = [
            f"🌟 Welcome to {COMPANY_NAME}! I'm {BOT_NAME}, your AI assistant. I'm here to help you with information about our services, answer questions, and connect you with our team. How can I assist you today?",
            f"Hello! 👋 I'm {BOT_NAME} from {COMPANY_NAME}. I'm excited to help you discover how our technology solutions can benefit you. What brings you here today?",
            f"Hi there! 🚀 Welcome to {COMPANY_NAME}! I'm {BOT_NAME}, and I'm here to make your experience amazing. Whether you need information, support, or want to explore our services, I've got you covered!"
        ]
        return random.choice(welcome_messages)

# Utility functions for the chatbot
def clean_input(user_input):
    """Clean and normalize user input"""
    # Remove extra whitespace
    user_input = user_input.strip()

    # Remove special characters that might interfere with processing
    user_input = re.sub(r'[^\w\s@.-]', '', user_input)

    return user_input

def format_response(response):
    """Format response for better display"""
    # Ensure response isn't too long
    if len(response) > MAX_RESPONSE_LENGTH:
        response = response[:MAX_RESPONSE_LENGTH-3] + "..."

    return response

# Main chatbot instance
def create_chatbot():
    """Factory function to create a new chatbot instance"""
    return AIChatbot()

if __name__ == "__main__":
    # Simple CLI interface for testing
    bot = create_chatbot()
    print(bot.get_welcome_message())
    print("\n" + "="*50)
    print("Type 'quit' to exit the chat")
    print("="*50 + "\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ['quit', 'exit', 'bye']:
            print(f"\n{BOT_NAME}: " + bot.process_input("goodbye"))
            break

        if user_input:
            # Extract user info
            bot.extract_user_info(user_input)

            # Clean input
            cleaned_input = clean_input(user_input)

            # Get response
            response = bot.process_input(cleaned_input)

            # Format and display response
            formatted_response = format_response(response)
            print(f"\n{BOT_NAME}: {formatted_response}\n")
        else:
            print(f"\n{BOT_NAME}: I didn't catch that. Could you please say something?\n")
