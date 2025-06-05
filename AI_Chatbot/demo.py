"""
Interactive Demo for AI Chatbot
Showcases the chatbot's capabilities with guided examples
"""

import time
from chatbot import create_chatbot
from config import BOT_NAME, COMPANY_NAME

def print_slowly(text, delay=0.03):
    """Print text with typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def demo_conversation():
    """Run an interactive demo conversation"""
    print("🎭" + "="*60 + "🎭")
    print_slowly(f"   Welcome to the {BOT_NAME} AI Chatbot Demo!")
    print_slowly(f"   Powered by {COMPANY_NAME}")
    print("🎭" + "="*60 + "🎭\n")
    
    bot = create_chatbot()
    
    # Demo scenarios
    scenarios = [
        {
            "title": "🌟 Greeting & Introduction",
            "inputs": ["Hello!", "What services do you offer?"]
        },
        {
            "title": "💰 Pricing Inquiry",
            "inputs": ["How much does it cost?", "I need a quote for my project"]
        },
        {
            "title": "🕒 Business Information",
            "inputs": ["What are your business hours?", "How can I contact you?"]
        },
        {
            "title": "🆘 Support Request",
            "inputs": ["I need help with a problem", "My application is not working"]
        },
        {
            "title": "🎯 Lead Generation",
            "inputs": ["I'm interested in learning more", "My name is Sarah Johnson and my email is sarah@company.com"]
        },
        {
            "title": "👥 Human Escalation",
            "inputs": ["Can I speak to a human agent?", "I want to talk to a representative"]
        }
    ]
    
    print_slowly("🚀 Starting Demo Conversation...\n")
    
    # Welcome message
    welcome = bot.get_welcome_message()
    print_slowly(f"🤖 {BOT_NAME}: {welcome}\n")
    
    for scenario in scenarios:
        print_slowly(f"\n{scenario['title']}")
        print("-" * 40)
        
        for user_input in scenario['inputs']:
            print_slowly(f"👤 User: {user_input}")
            
            # Extract user info and get response
            bot.extract_user_info(user_input)
            response = bot.process_input(user_input)
            
            print_slowly(f"🤖 {BOT_NAME}: {response}\n")
            time.sleep(1)  # Pause between exchanges
    
    # Show final statistics
    print_slowly("\n📊 Demo Conversation Summary:")
    print("-" * 40)
    summary = bot.get_conversation_summary()
    for key, value in summary.items():
        print_slowly(f"• {key.replace('_', ' ').title()}: {value}")
    
    print_slowly(f"\n✨ Demo completed! {BOT_NAME} is ready to engage with your customers!")

def interactive_mode():
    """Run interactive chat mode"""
    print("\n🎮 Interactive Mode")
    print("="*40)
    print_slowly("You can now chat directly with the bot!")
    print_slowly("Type 'demo' to run the demo again, or 'quit' to exit.\n")
    
    bot = create_chatbot()
    
    while True:
        user_input = input("👤 You: ").strip()
        
        if user_input.lower() == 'quit':
            print_slowly(f"🤖 {BOT_NAME}: " + bot.process_input("goodbye"))
            break
        elif user_input.lower() == 'demo':
            demo_conversation()
            continue
        elif user_input:
            bot.extract_user_info(user_input)
            response = bot.process_input(user_input)
            print_slowly(f"🤖 {BOT_NAME}: {response}\n")

def main():
    """Main demo function"""
    print_slowly("Welcome to the AI Chatbot Demo! 🤖\n")
    
    while True:
        print_slowly("Choose an option:")
        print_slowly("1. 🎭 Run Guided Demo")
        print_slowly("2. 🎮 Interactive Chat")
        print_slowly("3. 🌐 Web Interface Info")
        print_slowly("4. ❌ Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            demo_conversation()
        elif choice == '2':
            interactive_mode()
        elif choice == '3':
            print_slowly("\n🌐 Web Interface Information:")
            print_slowly("The web interface is available at: http://localhost:5000")
            print_slowly("To start the web server, run: python app.py")
            print_slowly("The web interface provides a beautiful chat UI with:")
            print_slowly("• Real-time messaging")
            print_slowly("• Responsive design")
            print_slowly("• Session management")
            print_slowly("• Typing indicators")
            print_slowly("• Conversation reset functionality\n")
        elif choice == '4':
            print_slowly("Thank you for trying the AI Chatbot! 👋")
            break
        else:
            print_slowly("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
