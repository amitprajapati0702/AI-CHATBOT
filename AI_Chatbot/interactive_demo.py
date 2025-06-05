"""
Interactive Demo showing the enhanced chatbot capabilities
"""

from chatbot import create_chatbot
from config import BOT_NAME

def interactive_demo():
    """Run an interactive demo to showcase improvements"""
    print("🎯" + "="*60 + "🎯")
    print(f"   Enhanced {BOT_NAME} Chatbot - Interactive Demo")
    print("   Now with MUCH better question understanding!")
    print("🎯" + "="*60 + "🎯\n")
    
    bot = create_chatbot()
    
    print("🤖 " + bot.get_welcome_message())
    print("\n" + "="*60)
    print("Try asking me different types of questions:")
    print("• Technology: 'Can you build React apps?'")
    print("• Business: 'Tell me about your company'")
    print("• Solutions: 'I need an ecommerce website'")
    print("• Process: 'What's your development process?'")
    print("• Pricing: 'How much does a website cost?'")
    print("• Random: 'What's the weather like?'")
    print("\nType 'quit' to exit, 'examples' to see more examples")
    print("="*60 + "\n")
    
    conversation_count = 0
    
    while True:
        user_input = input("👤 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print(f"\n🤖 {BOT_NAME}: " + bot.process_input("goodbye"))
            break
        
        elif user_input.lower() == 'examples':
            show_examples()
            continue
        
        elif user_input.lower() == 'stats':
            show_stats(bot)
            continue
        
        elif user_input:
            conversation_count += 1
            
            # Extract user info
            bot.extract_user_info(user_input)
            
            # Get response
            response = bot.process_input(user_input)
            
            print(f"\n🤖 {BOT_NAME}: {response}\n")
            
            # Show helpful hints every few interactions
            if conversation_count % 5 == 0:
                print("💡 Tip: Try asking about specific technologies, business questions, or solutions!")
                print("    Type 'examples' for more ideas or 'stats' for conversation stats.\n")
        
        else:
            print(f"\n🤖 {BOT_NAME}: I didn't catch that. Could you please say something?\n")

def show_examples():
    """Show example questions users can try"""
    print("\n📝 Example Questions to Try:")
    print("-" * 40)
    
    examples = {
        "Technology Questions": [
            "Do you work with Python?",
            "Can you build mobile apps?",
            "What about React development?",
            "Do you use cloud services like AWS?"
        ],
        "Business Questions": [
            "How experienced is your team?",
            "What's your company background?",
            "Who are your typical clients?",
            "What industries do you serve?"
        ],
        "Solution Questions": [
            "I need a booking system",
            "Can you build an online store?",
            "I want a customer management system",
            "Do you create inventory systems?"
        ],
        "Process Questions": [
            "How do you work with clients?",
            "What's your development timeline?",
            "What methodology do you follow?",
            "How do you handle project management?"
        ],
        "Random Questions": [
            "What's the weather like?",
            "I like coffee",
            "Tell me a joke",
            "What's your favorite color?"
        ]
    }
    
    for category, questions in examples.items():
        print(f"\n🎯 {category}:")
        for q in questions:
            print(f"   • {q}")
    
    print("\n" + "-" * 40)
    print("Try any of these or ask your own questions!\n")

def show_stats(bot):
    """Show conversation statistics"""
    print("\n📊 Conversation Statistics:")
    print("-" * 30)
    
    summary = bot.get_conversation_summary()
    for key, value in summary.items():
        formatted_key = key.replace('_', ' ').title()
        print(f"• {formatted_key}: {value}")
    
    if bot.user_data:
        print(f"\n👤 User Information Collected:")
        for key, value in bot.user_data.items():
            print(f"• {key.title()}: {value}")
    
    print("-" * 30 + "\n")

if __name__ == "__main__":
    interactive_demo()
