"""
Enhanced Response database and pattern matching for the AI Chatbot
"""

import re
import random
import difflib
from collections import defaultdict
from config import BOT_NAME, COMPANY_NAME, BUSINESS_HOURS, CONTACT_EMAIL, CONTACT_PHONE, USE_EMOJIS

class ResponseDatabase:
    def __init__(self):
        self.patterns = {
            # Greetings and basic conversation
            'greeting': {
                'patterns': [
                    r'\b(hi|hello|hey|good morning|good afternoon|good evening|greetings|howdy|sup)\b',
                    r'\bhow are you\b',
                    r'\bwhat\'s up\b',
                    r'\bhow\'s it going\b',
                    r'\bnice to meet you\b',
                    r'\bpleasure to meet\b'
                ],
                'keywords': ['hello', 'hi', 'hey', 'morning', 'afternoon', 'evening', 'greetings', 'howdy'],
                'responses': [
                    f"Hello! 👋 I'm {BOT_NAME}, your friendly AI assistant from {COMPANY_NAME}. How can I help you today?",
                    f"Hi there! 😊 Welcome to {COMPANY_NAME}! I'm here to assist you. What can I do for you?",
                    f"Hey! Great to see you! I'm {BOT_NAME}, and I'm excited to help you with anything you need. What's on your mind?",
                    f"Good to meet you! 🤝 I'm {BOT_NAME}, and I'm here to make your experience with {COMPANY_NAME} amazing. How can I assist you?"
                ]
            },

            # Product/Service inquiries
            'services': {
                'patterns': [
                    r'\b(services|products|what do you offer|solutions|capabilities|offerings)\b',
                    r'\bwhat can you do\b',
                    r'\btell me about\b',
                    r'\bwhat kind of\b',
                    r'\bwhat type of\b',
                    r'\bshow me\b',
                    r'\blist.*services\b',
                    r'\bwhat.*available\b'
                ],
                'keywords': ['services', 'products', 'solutions', 'offerings', 'capabilities', 'software', 'development', 'AI', 'technology'],
                'responses': [
                    f"🚀 {COMPANY_NAME} offers cutting-edge technology solutions including:\n• Custom software development\n• AI & Machine Learning solutions\n• Cloud services\n• Digital transformation consulting\n\nWhich area interests you most?",
                    f"We specialize in innovative tech solutions! 💡 Our main services include software development, AI implementation, and digital consulting. Would you like details about any specific service?",
                    f"Great question! We're experts in:\n✅ Custom applications\n✅ AI chatbots (like me!)\n✅ Cloud migration\n✅ Tech consulting\n\nWhat project are you working on?",
                    f"Here's what we can help you with! 🎯\n• Web & Mobile App Development\n• AI/ML Implementation\n• Cloud Solutions\n• Database Design\n• API Development\n• System Integration\n\nWhat's your specific need?"
                ]
            },

            # Pricing inquiries
            'pricing': {
                'patterns': [
                    r'\b(price|cost|pricing|how much|budget|quote|rates|fees|charges)\b',
                    r'\baffordable\b',
                    r'\bexpensive\b',
                    r'\bmoney\b',
                    r'\bdollar\b',
                    r'\bcheap\b',
                    r'\bfree\b'
                ],
                'keywords': ['price', 'cost', 'pricing', 'budget', 'quote', 'money', 'affordable', 'expensive', 'rates'],
                'responses': [
                    f"💰 Our pricing is competitive and tailored to your needs! Each project is unique, so I'd love to understand your requirements better. Can you tell me more about what you're looking for?",
                    f"Great question about pricing! 📊 We offer flexible packages starting from basic solutions to enterprise-level implementations. Would you like me to connect you with our sales team for a personalized quote?",
                    f"We believe in transparent, value-based pricing! 💎 Costs vary depending on project scope and complexity. Let me gather some details to provide you with accurate information. What's your project about?",
                    f"I understand budget is important! 💵 Our pricing is competitive and we offer various packages. To give you accurate pricing, I'd need to know more about your specific requirements. What kind of solution are you looking for?"
                ]
            },

            # Contact and support
            'contact': {
                'patterns': [
                    r'\b(contact|phone|email|address|location)\b',
                    r'\bhow to reach\b',
                    r'\bget in touch\b'
                ],
                'keywords': ['contact', 'phone', 'email', 'address', 'location', 'reach', 'touch'],
                'responses': [
                    f"📞 You can reach us at:\n• Phone: {CONTACT_PHONE}\n• Email: {CONTACT_EMAIL}\n• Business Hours: {BUSINESS_HOURS}\n\nI'm also here 24/7 to help! What would you like to know?",
                    f"Here's how to connect with us! 📧\n{CONTACT_EMAIL} | {CONTACT_PHONE}\n\nOur team is available during {BUSINESS_HOURS}. For immediate assistance, I'm your go-to bot! How can I help?",
                    f"Let's get you connected! 🤝\n• Email us: {CONTACT_EMAIL}\n• Call us: {CONTACT_PHONE}\n• Chat with me anytime!\n\nWhat's the best way to assist you right now?"
                ]
            },

            # Business hours
            'hours': {
                'patterns': [
                    r'\b(hours|open|closed|when|schedule|time)\b',
                    r'\bwhat time\b',
                    r'\bavailable\b'
                ],
                'keywords': ['hours', 'open', 'closed', 'when', 'schedule', 'time', 'available'],
                'responses': [
                    f"🕒 Our business hours are: {BUSINESS_HOURS}\n\nBut here's the good news - I'm available 24/7 to help you! What can I assist you with right now?",
                    f"We're open {BUSINESS_HOURS} ⏰\n\nThough our human team has set hours, I'm always here to help! What questions do you have?",
                    f"Our office hours: {BUSINESS_HOURS} 🏢\n\nI never sleep though! 😄 Feel free to ask me anything anytime. How can I help you today?"
                ]
            },

            # Technical support
            'support': {
                'patterns': [
                    r'\b(help|support|problem|issue|bug|error)\b',
                    r'\bnot working\b',
                    r'\btrouble\b'
                ],
                'keywords': ['help', 'support', 'problem', 'issue', 'bug', 'error', 'trouble', 'broken', 'fix'],
                'responses': [
                    f"🛠️ I'm here to help! Can you describe the issue you're experiencing? The more details you provide, the better I can assist you.",
                    f"No worries, let's get this sorted out! 💪 What specific problem are you facing? I'll do my best to help or connect you with our technical team.",
                    f"Support is what we do best! 🎯 Please tell me:\n• What were you trying to do?\n• What happened instead?\n• Any error messages?\n\nI'm here to help!"
                ]
            },

            # Lead generation
            'interested': {
                'patterns': [
                    r'\b(interested|want to know more|tell me more|sign up)\b',
                    r'\bget started\b',
                    r'\bhow to begin\b'
                ],
                'keywords': ['interested', 'want', 'know', 'more', 'tell', 'sign', 'up', 'started', 'begin'],
                'responses': [
                    f"That's fantastic! 🎉 I'd love to learn more about your needs. Could you share:\n• Your name\n• Your email\n• What type of solution you're looking for?\n\nThis helps us provide the best assistance!",
                    f"Excellent! Let's get you started! 🚀 To provide personalized recommendations, I'll need:\n• Your name\n• Contact email\n• Brief description of your project\n\nWhat's your name?",
                    f"Perfect timing! 💫 We'd love to help you succeed. Can you tell me your name and email so our team can follow up with tailored solutions?"
                ]
            },

            # Goodbye
            'goodbye': {
                'patterns': [
                    r'\b(bye|goodbye|see you|thanks|thank you|that\'s all)\b',
                    r'\bhave a good\b',
                    r'\btalk later\b'
                ],
                'keywords': ['bye', 'goodbye', 'thanks', 'thank you'],
                'responses': [
                    f"Thank you for chatting with me! 😊 It was great helping you today. Feel free to reach out anytime - I'm always here! Have a wonderful day! 🌟",
                    f"Goodbye! 👋 Thanks for visiting {COMPANY_NAME}. Remember, I'm available 24/7 whenever you need assistance. Take care! 💙",
                    f"It was a pleasure talking with you! 🤗 Don't hesitate to come back if you have more questions. Wishing you success with your projects! ✨"
                ]
            },

            # Technology specific questions
            'technology': {
                'patterns': [
                    r'\b(python|javascript|react|node|java|php|database|mysql|mongodb)\b',
                    r'\b(web development|mobile app|android|ios|flutter)\b',
                    r'\b(cloud|aws|azure|google cloud|hosting)\b',
                    r'\b(api|rest|graphql|microservices)\b'
                ],
                'keywords': ['python', 'javascript', 'react', 'node', 'java', 'web', 'mobile', 'cloud', 'api', 'database'],
                'responses': [
                    f"Great choice of technology! 💻 We have extensive experience with that stack. Our team specializes in modern development practices and can help you build robust, scalable solutions. What specific project are you working on?",
                    f"Excellent! 🚀 We're experts in that technology. Whether you need development, consulting, or migration services, we can help. What's your current challenge or goal?",
                    f"Perfect! 🎯 That's right in our wheelhouse. We've delivered many successful projects using those technologies. Would you like to discuss your specific requirements?"
                ]
            },

            # Business questions
            'business': {
                'patterns': [
                    r'\b(company|business|team|experience|portfolio|clients)\b',
                    r'\bhow long\b',
                    r'\bwho are you\b',
                    r'\babout.*company\b',
                    r'\byour background\b'
                ],
                'keywords': ['company', 'business', 'team', 'experience', 'portfolio', 'about'],
                'responses': [
                    f"Great question! 🏢 {COMPANY_NAME} is a leading technology solutions provider with years of experience helping businesses transform digitally. We've worked with startups to enterprises across various industries. What would you like to know specifically?",
                    f"We're a passionate team of tech experts! 👥 Our company specializes in delivering innovative solutions that drive business growth. We pride ourselves on quality, reliability, and customer satisfaction. How can we help your business?",
                    f"Thanks for asking! 🌟 {COMPANY_NAME} has been at the forefront of technology innovation, helping companies leverage cutting-edge solutions to achieve their goals. We'd love to learn about your business needs!"
                ]
            },

            # Process and methodology
            'process': {
                'patterns': [
                    r'\b(process|methodology|how do you work|timeline|steps)\b',
                    r'\bhow long does it take\b',
                    r'\bwhat.*process\b',
                    r'\bhow do you\b'
                ],
                'keywords': ['process', 'methodology', 'timeline', 'steps', 'work', 'approach'],
                'responses': [
                    f"Great question about our process! 📋 We follow agile methodologies with these key steps:\n• Discovery & Requirements\n• Design & Planning\n• Development & Testing\n• Deployment & Support\n\nTimelines vary by project complexity. What type of project are you considering?",
                    f"We believe in transparent, collaborative processes! 🤝 Our approach includes regular communication, milestone reviews, and iterative development. This ensures you're always in the loop and get exactly what you need. What's your project scope?",
                    f"Our methodology is designed for success! ✅ We start with understanding your needs, then plan, build, test, and deploy with continuous feedback. Most projects take 2-12 weeks depending on complexity. What are you looking to build?"
                ]
            },

            # Specific solutions
            'solutions': {
                'patterns': [
                    r'\b(ecommerce|e-commerce|online store|shopping)\b',
                    r'\b(crm|customer management|sales)\b',
                    r'\b(inventory|warehouse|logistics)\b',
                    r'\b(booking|appointment|scheduling)\b',
                    r'\b(payment|billing|subscription)\b'
                ],
                'keywords': ['ecommerce', 'store', 'crm', 'inventory', 'booking', 'payment', 'management'],
                'responses': [
                    f"Perfect! 🛒 We specialize in that type of solution. We've built many successful systems with features like user management, secure payments, analytics, and more. What specific functionality do you need?",
                    f"Excellent choice! 💼 That's exactly the kind of solution we excel at building. We can create custom features tailored to your business needs. What's your main business challenge we can solve?",
                    f"Great idea! 🎯 We have extensive experience building those types of systems. From basic functionality to advanced features, we can create something perfect for your needs. What's your vision?"
                ]
            },

            # Default/fallback responses
            'default': {
                'patterns': [],
                'responses': [
                    f"That's an interesting question! 🤔 While I might not have the perfect answer right now, I'd love to help you find what you're looking for. Could you rephrase or tell me more?",
                    f"I want to make sure I understand you correctly! 💭 Could you provide a bit more detail about what you're looking for? I'm here to help!",
                    f"Great question! 🌟 I'm still learning, but I'm eager to assist. Can you tell me more about what you need help with? Or would you like to speak with our human team?"
                ]
            }
        }

    def find_response(self, user_input):
        """Find the best response for user input using enhanced matching"""
        user_input = user_input.lower().strip()

        # Score each category
        category_scores = defaultdict(int)

        for category, data in self.patterns.items():
            if category == 'default':
                continue

            # Pattern matching score
            pattern_score = 0
            for pattern in data['patterns']:
                if re.search(pattern, user_input, re.IGNORECASE):
                    pattern_score += 10  # High score for regex match

            # Keyword matching score
            if 'keywords' in data:
                keyword_score = 0
                for keyword in data['keywords']:
                    if keyword.lower() in user_input:
                        keyword_score += 5  # Medium score for keyword match
                    # Fuzzy matching for similar words
                    for word in user_input.split():
                        similarity = difflib.SequenceMatcher(None, keyword.lower(), word).ratio()
                        if similarity > 0.8:  # 80% similarity threshold
                            keyword_score += 3

                category_scores[category] += keyword_score

            category_scores[category] += pattern_score

        # Find the best matching category
        if category_scores:
            best_category = max(category_scores, key=category_scores.get)
            if category_scores[best_category] > 0:
                return random.choice(self.patterns[best_category]['responses'])

        # Enhanced fallback - try to give helpful response based on keywords
        return self._get_smart_fallback(user_input)

    def _get_smart_fallback(self, user_input):
        """Provide intelligent fallback responses based on input analysis"""
        # Check for question words
        question_words = ['what', 'how', 'when', 'where', 'why', 'who', 'which', 'can', 'do', 'does', 'is', 'are']
        has_question = any(word in user_input for word in question_words)

        # Check for technology terms
        tech_terms = ['app', 'website', 'software', 'system', 'code', 'programming', 'development', 'tech', 'digital']
        has_tech = any(term in user_input for term in tech_terms)

        # Check for business terms
        business_terms = ['business', 'company', 'project', 'solution', 'help', 'need', 'want', 'looking']
        has_business = any(term in user_input for term in business_terms)

        if has_question and has_tech:
            return f"That's a great technical question! 💻 While I'd love to give you the perfect answer, I want to make sure you get the most accurate information. Could you tell me more about your specific situation? Or would you like me to connect you with our technical team?"

        elif has_question and has_business:
            return f"Excellent question about our business solutions! 🏢 I want to make sure I understand your needs correctly. Could you provide a bit more detail about what you're looking for? This will help me give you the most relevant information."

        elif has_tech:
            return f"I can see you're interested in technical solutions! 🚀 {COMPANY_NAME} has extensive experience in that area. Could you tell me more about your specific requirements or challenges? I'd love to help you find the right solution."

        elif has_business:
            return f"It sounds like you have a business need we might be able to help with! 💼 {COMPANY_NAME} specializes in helping businesses grow through technology. What specific challenge or goal are you working on?"

        else:
            # Generic helpful fallback
            fallback_responses = [
                f"That's interesting! 🤔 I want to make sure I give you the most helpful response. Could you tell me a bit more about what you're looking for? I'm here to help with information about our services, pricing, or any questions you might have.",
                f"I appreciate you reaching out! 😊 To better assist you, could you help me understand what you need? Whether it's about our services, technical questions, or business solutions - I'm here to help!",
                f"Thanks for your message! 🌟 I want to make sure I provide you with the most relevant information. Could you share more details about what you're interested in? I'm excited to help you find what you need!"
            ]
            return random.choice(fallback_responses)

    def get_escalation_response(self):
        """Response for escalating to human support"""
        return f"I understand you'd like to speak with a human representative! 👥 Let me connect you with our team. Please provide your name and email, and someone will reach out to you within 2 hours during business hours ({BUSINESS_HOURS})."
