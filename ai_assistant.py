import os
import sys

def simulate_ai_response(prompt, option):
    """Simulates an AI response if no API key is provided."""
    prompt_lower = prompt.lower()
    
    if option == "1": # General Chat
        if "hello" in prompt_lower or "hi" in prompt_lower:
            return "AI (Simulator): Hello! I am your AI assistant. How can I help you today?"
        elif "python" in prompt_lower:
            return "AI (Simulator): Python is a versatile, high-level programming language widely used in AI, data science, and web development."
        elif "calculator" in prompt_lower:
            return "AI (Simulator): I saw your calculator project! It looks great. Let me know if you want to optimize it."
        else:
            return f"AI (Simulator): That is an interesting prompt! ('{prompt}'). In a real setup, I would send this to the Gemini model and return its response."
            
    elif option == "2": # Summarization
        words = prompt.split()
        summary = " ".join(words[:min(10, len(words))]) + "..."
        return f"AI (Simulator) [Summary]: {summary}\n(Original length: {len(words)} words -> Summarized length: {len(summary.split())} words)"
        
    elif option == "3": # Sentiment Analysis
        positive_words = ["good", "great", "excellent", "happy", "love", "awesome", "amazing"]
        negative_words = ["bad", "sad", "angry", "hate", "terrible", "worst", "poor"]
        
        pos_count = sum(1 for w in positive_words if w in prompt_lower)
        neg_count = sum(1 for w in negative_words if w in prompt_lower)
        
        if pos_count > neg_count:
            sentiment = "POSITIVE 😊"
        elif neg_count > pos_count:
            sentiment = "NEGATIVE 😞"
        else:
            sentiment = "NEUTRAL 😐"
            
        return f"AI (Simulator) [Sentiment Analysis]:\nSentiment: {sentiment}\n(Confidence score based on keyword match: Pos={pos_count}, Neg={neg_count})"
        
    return "AI (Simulator): Unknown operation."

def main():
    print("=" * 55)
    print("       🚀 AI-POWERED PRODUCTIVITY ASSISTANT 🚀       ")
    print("=" * 55)
    print("This app supports the real Google Gemini API or a local simulator.")
    print("=" * 55)
    
    api_key = input("Enter your Gemini API Key (or press ENTER to use Simulator): ").strip()
    
    using_real_api = False
    model = None
    
    if api_key:
        try:
            print("\nInitializing Gemini API...")
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            using_real_api = True
            print("✅ Gemini API initialized successfully!")
        except Exception as e:
            print(f"❌ Failed to initialize Gemini API: {e}")
            print("Falling back to AI Simulator...")
    else:
        print("\nℹ️ No API key entered. Running in Simulator Mode.")
        
    while True:
        print("\n" + "=" * 40)
        print("          MAIN MENU          ")
        print("=" * 40)
        print("1. Chat with AI (General Assistant)")
        print("2. Summarize Long Text")
        print("3. Sentiment Analysis")
        print("4. Exit")
        print("=" * 40)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '4':
            print("\nThank you for using the AI Productivity Assistant! Goodbye! 👋")
            break
            
        if choice not in ['1', '2', '3']:
            print("\n❌ Invalid choice! Please select 1, 2, 3, or 4.")
            continue
            
        if choice == '1':
            print("\n--- 💬 Chat Mode ---")
            prompt = input("Ask anything: ").strip()
            if not prompt:
                continue
                
            if using_real_api:
                try:
                    print("Thinking...")
                    response = model.generate_content(prompt)
                    print(f"\n🤖 Gemini: {response.text}")
                except Exception as e:
                    print(f"\n❌ Error calling Gemini API: {e}")
            else:
                response = simulate_ai_response(prompt, choice)
                print(f"\n{response}")
                
        elif choice == '2':
            print("\n--- 📝 Summarization Mode ---")
            prompt = input("Paste the long text to summarize: ").strip()
            if not prompt:
                continue
                
            if using_real_api:
                try:
                    print("Summarizing...")
                    summarize_prompt = f"Provide a brief, clear summary of the following text:\n\n{prompt}"
                    response = model.generate_content(summarize_prompt)
                    print(f"\n📝 Summary:\n{response.text}")
                except Exception as e:
                    print(f"\n❌ Error calling Gemini API: {e}")
            else:
                response = simulate_ai_response(prompt, choice)
                print(f"\n{response}")
                
        elif choice == '3':
            print("\n--- 📊 Sentiment Analysis Mode ---")
            prompt = input("Enter text to analyze sentiment: ").strip()
            if not prompt:
                continue
                
            if using_real_api:
                try:
                    print("Analyzing...")
                    sentiment_prompt = f"Analyze the sentiment of this text. Respond with POSITIVE, NEGATIVE, or NEUTRAL and give a brief 1-sentence reason:\n\n{prompt}"
                    response = model.generate_content(sentiment_prompt)
                    print(f"\n📊 Sentiment Analysis:\n{response.text}")
                except Exception as e:
                    print(f"\n❌ Error calling Gemini API: {e}")
            else:
                response = simulate_ai_response(prompt, choice)
                print(f"\n{response}")
                
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
