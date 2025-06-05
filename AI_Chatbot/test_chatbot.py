"""
Test script for the AI Chatbot
"""

from chatbot import create_chatbot
from config import BOT_NAME

def test_chatbot():
    """Test the chatbot with various inputs"""
    print(f"🧪 Testing {BOT_NAME} Chatbot")
    print("=" * 50)
    
    # Create chatbot instance
    bot = create_chatbot()
    
    # Test cases
    test_cases = [
        "Hello",
        "What services do you offer?",
        "How much does it cost?",
        "What are your business hours?",
        "I need help with a problem",
        "I'm interested in learning more",
        "My name is John and my email is john@example.com",
        "Can I speak to a human?",
        "Thank you, goodbye"
    ]
    
    print(f"Welcome Message: {bot.get_welcome_message()}\n")
    
    for i, test_input in enumerate(test_cases, 1):
        print(f"Test {i}: {test_input}")
        
        # Extract user info if present
        bot.extract_user_info(test_input)
        
        # Get response
        response = bot.process_input(test_input)
        print(f"Response: {response}\n")
        print("-" * 30)
    
    # Show conversation summary
    print("\n📊 Conversation Summary:")
    summary = bot.get_conversation_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    test_chatbot()
