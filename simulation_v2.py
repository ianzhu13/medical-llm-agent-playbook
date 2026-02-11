import json
import time
import random
from typing import Dict, List, Optional
from dataclasses import dataclass

# --- 1. 定义知识结构 (Data Structures) ---
@dataclass
class ResearchPaper:
    title: str
    author: str
    year: int
    relevance: str

class MedicalKnowledgeBase:
    """
    Simulates a Vector Database (RAG) that holds expert knowledge and literature.
    """
    def __init__(self):
        self.papers = {
            "unet_plus": ResearchPaper("UNet++: A Nested U-Net Architecture", "Zhou et al.", 2018, "Segmentation"),
            "cyclegan": ResearchPaper("Unpaired Image-to-Image Translation", "Zhu et al.", 2017, "Domain Adaptation"),
            "focal_loss": ResearchPaper("Focal Loss for Dense Object Detection", "Lin et al.", 2017, "Class Imbalance"),
            "nnunet": ResearchPaper("nnU-Net: Self-adapting Framework", "Isensee et al.", 2021, "AutoML")
        }
        
        # 你的 Intalight 经验在这里变成了“规则”
        self.rules = [
            {
                "trigger": "30nm", 
                "warning": "Risk of structural layer thickening artifacts.",
                "recommendation": "Use CycleGAN with Structure-Consistency Loss.",
                "citation": "cyclegan"
            },
            {
                "trigger": "imbalance", 
                "warning": "Target class < 5% of volume.",
                "recommendation": "Switch to Focal Loss + Oversampling.",
                "citation": "focal_loss"
            },
            {
                "trigger": "quantification",
                "warning": "Potential affine projection errors.",
                "recommendation": "Verify Pixel-to-Physical mapping matrix.",
                "citation": "nnunet" # Just as a placeholder for robust pipelines
            }
        ]

    def retrieve_context(self, query_context: str) -> List[Dict]:
        """
        Simulate Retrieval-Augmented Generation (RAG).
        """
        hits = []
        for rule in self.rules:
            if rule["trigger"] in query_context.lower():
                hits.append(rule)
        return hits

# --- 2. 核心 Agent 逻辑 (The Brain) ---
class AdvancedMedicalAgent:
    def __init__(self):
        self.kb = MedicalKnowledgeBase()
        print(">>> [System] Medical AI Agent v2.0 Initialized (Knowledge Base Loaded)")

    def think(self, step: str):
        """Visualizing the Chain-of-Thought"""
        time.sleep(0.8) # Simulate processing time
        print(f"   [CoT] {step}")

    def generate_strategy(self, task: str, metadata: Dict) -> Dict:
        print(f"\n>>> [Input] Task: {task}")
        print(f">>> [Input] Metadata: {json.dumps(metadata)}")
        
        # Step 1: Safety Check
        self.think("Scanning for safety violations...")
        if "diagnose" in task.lower():
            return {"error": "REFUSAL: Agent cannot perform clinical diagnosis."}

        # Step 2: Context Retrieval (RAG)
        self.think("Retrieving relevant clinical protocols from Knowledge Base...")
        context_query = f"{task} {metadata.get('hardware', '')} {metadata.get('issue', '')}"
        retrieved_rules = self.kb.retrieve_context(context_query)
        
        if not retrieved_rules:
            self.think("No specific constraints found. Defaulting to baseline.")
            return {"strategy": "Standard UNet Baseline"}

        # Step 3: Reasoning & Synthesis
        self.think(f"Found {len(retrieved_rules)} critical constraints. Synthesizing strategy...")
        
        reasoning_trace = []
        citations = []
        final_config = {}

        for hit in retrieved_rules:
            print(f"      -> DETECTED: {hit['trigger'].upper()} issue.")
            reasoning_trace.append(f"Due to '{hit['trigger']}', we must address: {hit['warning']}")
            final_config[hit['trigger']] = hit['recommendation']
            
            # Link Citation
            paper = self.kb.papers.get(hit['citation'])
            if paper:
                citations.append(f"{paper.title} ({paper.author}, {paper.year})")

        # Step 4: Output Generation
        return {
            "status": "Success",
            "reasoning_trace": reasoning_trace,
            "recommended_stack": final_config,
            "supporting_evidence": citations
        }

# --- 3. 模拟运行 (Main Execution) ---
if __name__ == "__main__":
    agent = AdvancedMedicalAgent()

    # --- Scenario A: 你的 30nm 激光器痛点 ---
    print("\n" + "="*50)
    print("SCENARIO 1: Hardware Limitation (The 'Intalight' Case)")
    print("="*50)
    
    result = agent.generate_strategy(
        task="Retinal layer reconstruction",
        metadata={
            "hardware": "Low-bandwidth laser (30nm)",
            "resolution": "Low",
            "issue": "Blurry layers"
        }
    )
    print(json.dumps(result, indent=2))

    # --- Scenario B: 类别不平衡 ---
    print("\n" + "="*50)
    print("SCENARIO 2: Rare Pathology")
    print("="*50)
    
    result = agent.generate_strategy(
        task="Microaneurysm segmentation",
        metadata={
            "modality": "Fundus",
            "issue": "Extreme class imbalance (1:1000)"
        }
    )
    print(json.dumps(result, indent=2))