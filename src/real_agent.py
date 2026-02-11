import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

# 1. Load Environment Variables (API Key)
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API Key not found! Please check your .env file.")

genai.configure(api_key=api_key)

class RealMedicalAgent:
    def __init__(self, model_name="gemini-2.0-flash-lite-001"):
        """
        Initializes the agent with the specific system prompt from your Intalight experience.
        """
        self.model_name = model_name
        self.system_prompt = self._load_system_prompt()
        
        # Configure the model architecture
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=self.system_prompt, # Injecting your expert persona
            generation_config={
                "response_mime_type": "application/json", # FORCE JSON output
                "temperature": 0.2, # Low temperature for deterministic/rigorous answers
            }
        )
        print(f">>> [System] Real Agent initialized with {model_name}")

    def _load_system_prompt(self) -> str:
        """Reads the markdown prompt file we created earlier."""
        # Assuming the script is run from project root
        prompt_path = Path("prompts/system_prompt_v1.md") 
        
        if not prompt_path.exists():
            # Fallback check if running from src folder
            prompt_path = Path("../prompts/system_prompt_v1.md")
            
        if not prompt_path.exists():
            raise FileNotFoundError("Could not find system_prompt_v1.md. Did you create it?")
            
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()

    def analyze_case(self, user_query: str):
        """
        Sends the user query to the live model and returns the parsed JSON.
        """
        print(f"\n>>> [Input] Querying Expert Agent: {user_query[:60]}...")
        
        try:
            # The actual API call
            response = self.model.generate_content(user_query)
            
            # Parse the text response into a Python dictionary
            result_json = json.loads(response.text)
            return result_json
            
        except Exception as e:
            return {"error": f"API Error: {str(e)}"}

# --- Execution Block ---
if __name__ == "__main__":
    agent = RealMedicalAgent()

    # ---------------------------------------------------------
    # Test Case: The "30nm Laser" Problem (Your real experience)
    # ---------------------------------------------------------
    query = (
        "I am working with a custom OCT device that has a limited bandwidth source (30nm). "
        "The retinal layers look very blurry. "
        "My manager wants to use a standard ResNet-based Super-Resolution model to fix it. "
        "Is this a good idea?"
    )

    result = agent.analyze_case(query)

    # Pretty print the real AI response
    print("\n" + "="*60)
    print("  REAL-TIME AGENT RESPONSE")
    print("="*60)
    print(json.dumps(result, indent=2))