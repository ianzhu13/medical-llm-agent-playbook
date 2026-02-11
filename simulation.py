import json
import time
from typing import Dict, List

class MedicalAgent:
    """
    A simulated wrapper for the Medical LLM Agent.
    Demonstrates the intended I/O structure and safety checks.
    """
    
    def __init__(self, model_name: str = "gemini-1.5-pro"):
        self.model_name = model_name
        print(f"[System] Initializing Medical Agent with {self.model_name}...")
        # In a real scenario, API keys and LangChain tools would be loaded here.

    def _safety_check(self, query: str) -> bool:
        """
        Simulated Guardrail: Blocks direct clinical diagnosis requests.
        """
        forbidden_terms = ["diagnose me", "do I have", "treatment for"]
        for term in forbidden_terms:
            if term in query.lower():
                print(f"[Guardrail] BLOCKED unsafe query containing: '{term}'")
                return False
        return True

    def generate_strategy(self, task_description: str, data_meta: Dict) -> Dict:
        """
        Simulates the Chain-of-Thought reasoning process.
        """
        print(f"\n[Input] Analyzing Task: {task_description}")
        print(f"[Input] Data Meta: {json.dumps(data_meta)}")
        
        if not self._safety_check(task_description):
            return {"error": "Safety violation. This agent does not provide medical diagnosis."}

        print("[Agent] Thinking... (Retrieving OCT domain knowledge)")
        time.sleep(1.5) # Simulate inference latency
        
        # MOCK RESPONSE (Based on your Intalight experience)
        # This matches the System Prompt logic we defined earlier.
        mock_response = {
            "status": "success",
            "reasoning_trace": [
                "Target is 'Intraretinal Fluid' (variable scale).",
                "Data has class imbalance (fluid is < 5% of pixels).",
                "Standard CrossEntropy will fail."
            ],
            "recommendation": {
                "architecture": "UNet++ with Deep Supervision",
                "loss_function": "Generalized Dice Loss + Focal Loss",
                "augmentation": ["RandomRotate90", "ElasticDeform", "IntensityShift"]
            }
        }
        
        return mock_response

if __name__ == "__main__":
    # 1. Define a Mock Context (Low-resource OCT task)
    user_task = "Segment intraretinal fluid in SD-OCT scans."
    dataset_stats = {
        "modality": "SD-OCT",
        "num_samples": 300,
        "resolution": "512x512",
        "class_balance": "Heavily imbalanced"
    }

    # 2. Run the Agent
    agent = MedicalAgent()
    result = agent.generate_strategy(user_task, dataset_stats)

    # 3. Output the JSON
    print("\n>>> FINAL AGENT OUTPUT >>>")
    print(json.dumps(result, indent=2))
