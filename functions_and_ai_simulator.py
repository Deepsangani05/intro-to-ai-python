# ==============================================================================
# Functions and AI Simulator in Python
# ==============================================================================
# This program demonstrates modular programming with functions:
# - Defining functions (def keyword)
# - Positional, Keyword, and Default arguments
# - Return values and type hinting
# - Standard docstrings for documentation
# - It implements a simple text-based Rule-Based AI Customer Support Simulator.
# ==============================================================================

# Define a dictionary of mock responses for our chatbot
KNOWLEDGE_BASE = {
    "hello": "Hello! I am Codex, your AI assistant. How can I help you today?",
    "hi": "Hi there! How can I assist you with your Python or AI learning?",
    "python": "Python is an interpreted, high-level programming language known for its readability and major role in AI/ML.",
    "ai": "Artificial Intelligence is the simulation of human intelligence processes by machines, especially computer systems.",
    "ml": "Machine Learning is a subset of AI that allows software applications to learn from data and improve accuracy without explicit programming.",
    "dl": "Deep Learning is a specialized subfield of ML based on artificial neural networks with multiple layers (hence 'deep').",
    "help": "You can ask me about: 'AI', 'ML', 'DL', 'Python', or type 'exit' to quit.",
}

# 1. Defining a function with arguments and default parameter values
def get_bot_response(user_query: str, fallback: str = "I'm sorry, I don't understand that yet. Type 'help' to see what I know!") -> str:
    """
    Search the query in the knowledge base and return the matching response.
    
    Parameters:
        user_query (str): The cleaned text query from the user.
        fallback (str): The response returned if no keywords match. Default is generic help message.
        
    Returns:
        str: Response from chatbot knowledge base.
    """
    # Convert query to lowercase to ensure case insensitivity
    cleaned_query = user_query.strip().lower()
    
    # Simple keyword matching algorithm
    for key, response in KNOWLEDGE_BASE.items():
        if key in cleaned_query:
            return response
            
    return fallback


# 2. Defining a function with multiple return types and parameter validation
def register_customer(name: str, email: str, plan: str = "Free") -> dict:
    """
    Registers a customer profile and returns a structured dictionary.
    """
    # Example of variables and dictionary creation
    profile = {
        "customer_name": name,
        "email_address": email,
        "service_plan": plan,
        "is_active": True
    }
    return profile


def run_chatbot_simulation(user_name: str):
    """
    Runs the main interactive loop for the customer chatbot.
    """
    print(f"\n[AI Simulator] Starting chat session with {user_name}...")
    print("Codex AI: Hello! Type 'help' to see options or 'exit' to quit.")
    
    while True:
        user_input = input(f"{user_name}: ")
        
        # Check for exit condition
        if user_input.strip().lower() == 'exit':
            print("Codex AI: Thank you for chatting! Happy coding!")
            break
            
        # Get response using our custom function
        bot_response = get_bot_response(user_input)
        print(f"Codex AI: {bot_response}\n")


def main():
    print("==================================================")
    print("Python Functions & AI Simulator Demonstration")
    print("==================================================")
    
    # Prompt user for their name and email
    print("Let's set up your profile for the session:")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    
    # Register customer using keyword arguments
    customer_profile = register_customer(name=name, email=email, plan="Enterprise Student")
    
    print("\n--- User Profile Registered ---")
    # Print dictionary elements
    for key, value in customer_profile.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")
    
    # Run the interactive simulator
    run_chatbot_simulation(customer_profile["customer_name"])
    
    print("==================================================")

if __name__ == "__main__":
    main()
