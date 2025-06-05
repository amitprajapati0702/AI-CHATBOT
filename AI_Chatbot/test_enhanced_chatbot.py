"""
Enhanced Test script for the improved AI Chatbot
Tests various types of questions to show improved relevance
"""

from chatbot import create_chatbot
from config import BOT_NAME

def test_enhanced_responses():
    """Test the enhanced chatbot with diverse inputs"""
    print(f"🚀 Testing Enhanced {BOT_NAME} Chatbot")
    print("=" * 60)
    print("Testing improved pattern matching and relevance...")
    print("=" * 60)
    
    bot = create_chatbot()
    
    # Enhanced test cases covering various scenarios
    test_cases = [
        # Technology questions
        ("I need a Python web application", "Technology-specific"),
        ("Can you build React websites?", "Technology-specific"),
        ("Do you work with databases like MySQL?", "Technology-specific"),
        
        # Business questions
        ("Tell me about your company", "Business inquiry"),
        ("How experienced is your team?", "Business inquiry"),
        ("What's your portfolio like?", "Business inquiry"),
        
        # Specific solutions
        ("I need an ecommerce website", "Solution-specific"),
        ("Can you build a CRM system?", "Solution-specific"),
        ("I want a booking system", "Solution-specific"),
        
        # Process questions
        ("What's your development process?", "Process inquiry"),
        ("How long does development take?", "Process inquiry"),
        ("What methodology do you use?", "Process inquiry"),
        
        # Random/unclear questions
        ("What about the weather?", "Unrelated question"),
        ("I like pizza", "Random statement"),
        ("Can you help me with my homework?", "Unclear request"),
        
        # Mixed questions
        ("I need help building a mobile app for my business", "Complex inquiry"),
        ("What technologies do you recommend for a startup?", "Advisory question"),
        ("How much would a simple website cost?", "Pricing with context"),
    ]
    
    print(f"Welcome Message: {bot.get_welcome_message()}\n")
    
    for i, (test_input, category) in enumerate(test_cases, 1):
        print(f"Test {i} ({category}): {test_input}")
        
        # Extract user info if present
        bot.extract_user_info(test_input)
        
        # Get response
        response = bot.process_input(test_input)
        print(f"Response: {response}\n")
        print("-" * 50)
    
    # Show conversation summary
    print("\n📊 Enhanced Conversation Summary:")
    summary = bot.get_conversation_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")

def test_keyword_matching():
    """Test keyword-based matching specifically"""
    print(f"\n🔍 Testing Keyword Matching")
    print("=" * 40)
    
    bot = create_chatbot()
    
    keyword_tests = [
        "software development services",
        "pricing information needed",
        "contact details please",
        "business hours inquiry",
        "technical support required",
        "interested in solutions"
    ]
    
    for test in keyword_tests:
        response = bot.process_input(test)
        print(f"Input: {test}")
        print(f"Response: {response[:100]}...\n")

if __name__ == "__main__":
    test_enhanced_responses()
    test_keyword_matching()
