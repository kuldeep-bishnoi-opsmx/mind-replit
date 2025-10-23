import openai
import os
from dotenv import load_dotenv
from typing import List, Dict, Optional
import asyncio
import httpx

load_dotenv()

# Initialize OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Sentiment analysis is disabled (transformers library not installed to reduce dependencies)
sentiment_analyzer = None

class AIService:
    def __init__(self):
        self.system_prompt = """You are a compassionate and empathetic AI mental wellness coach. Your role is to:

1. Provide supportive, non-judgmental responses
2. Help users process their emotions and thoughts
3. Offer gentle guidance and coping strategies
4. Encourage self-reflection and mindfulness
5. Suggest healthy habits and wellness practices
6. NEVER provide medical advice or diagnose conditions
7. Always encourage users to seek professional help when needed

Guidelines:
- Be warm, understanding, and encouraging
- Use active listening techniques
- Ask thoughtful follow-up questions
- Validate the user's feelings
- Offer practical, actionable suggestions
- Keep responses concise but meaningful
- If someone expresses thoughts of self-harm, immediately encourage them to contact emergency services or a crisis helpline

Remember: You are a supportive companion, not a replacement for professional mental health care."""

    async def generate_chat_response(self, messages: List[Dict[str, str]], user_context: Optional[Dict] = None) -> str:
        """Generate AI response using OpenAI GPT-4o."""
        try:
            # Prepare messages with system prompt
            formatted_messages = [{"role": "system", "content": self.system_prompt}]
            
            # Add user context if available
            if user_context:
                context_msg = f"User context: Recent mood trends show {user_context.get('mood_trend', 'stable emotions')}. "
                if user_context.get('recent_topics'):
                    context_msg += f"Recent conversation topics: {', '.join(user_context['recent_topics'])}."
                formatted_messages.append({"role": "system", "content": context_msg})
            
            # Add conversation history
            formatted_messages.extend(messages)
            
            # Make API call to OpenAI
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {openai.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "gpt-4o",
                        "messages": formatted_messages,
                        "max_tokens": 500,
                        "temperature": 0.7,
                        "presence_penalty": 0.1,
                        "frequency_penalty": 0.1
                    },
                    timeout=30.0
                )
                
                if response.status_code == 200:
                    result = response.json()
                    return result["choices"][0]["message"]["content"].strip()
                else:
                    raise Exception(f"OpenAI API error: {response.status_code}")
                    
        except Exception as e:
            print(f"Error generating AI response: {e}")
            return "I'm sorry, I'm having trouble connecting right now. Please try again in a moment. Remember, if you need immediate support, please reach out to a mental health professional or crisis helpline."

    def analyze_sentiment(self, text: str) -> float:
        """Analyze sentiment of text and return score (-1 to 1)."""
        if not sentiment_analyzer:
            return 0.0
        
        try:
            results = sentiment_analyzer(text)
            
            # Convert to single score (-1 to 1)
            # Assuming the model returns NEGATIVE, NEUTRAL, POSITIVE scores
            if not results or len(results) == 0 or not isinstance(results[0], (list, tuple)):
                return 0.0
            scores = {result['label']: result['score'] for result in results[0]}
            
            # Calculate weighted sentiment score
            sentiment_score = 0.0
            if 'LABEL_0' in scores:  # NEGATIVE
                sentiment_score -= scores['LABEL_0']
            if 'LABEL_2' in scores:  # POSITIVE
                sentiment_score += scores['LABEL_2']
            
            return max(-1.0, min(1.0, sentiment_score))
            
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return 0.0

    def generate_journal_prompt(self, user_mood: Optional[str] = None, recent_topics: Optional[List[str]] = None) -> str:
        """Generate AI-powered journal prompts."""
        prompts = [
            "What are three things you're grateful for today, and why do they matter to you?",
            "Describe a moment today when you felt most like yourself. What were you doing?",
            "What emotion have you been carrying lately? Write it a letter.",
            "If your future self could send you a message right now, what would it say?",
            "What's one small act of kindness you could do for yourself today?",
            "Write about a challenge you're facing. What would you tell a friend in the same situation?",
            "What does your ideal day look like? What elements can you incorporate into tomorrow?",
            "Reflect on a recent conversation that made you think. What insights did you gain?",
            "What's something you've learned about yourself this week?",
            "Describe your current mood as if it were weather. What would help clear the skies?"
        ]
        
        # Customize based on mood if provided
        if user_mood:
            if "sad" in user_mood.lower() or "😢" in user_mood:
                return "You seem to be going through a tough time. What's one small thing that brought you even a moment of peace today? Sometimes the tiniest lights matter most in the darkness."
            elif "happy" in user_mood.lower() or "😊" in user_mood:
                return "You're feeling good today! What contributed to this positive mood? How can you carry this energy forward?"
            elif "anxious" in user_mood.lower() or "😰" in user_mood:
                return "When anxiety visits, it often brings important messages. What is your anxiety trying to tell you? What would help you feel more grounded right now?"
        
        # Return a random prompt
        import random
        return random.choice(prompts)

# Create singleton instance
ai_service = AIService()
