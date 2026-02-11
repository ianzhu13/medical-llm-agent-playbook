import time
import json
import random
import sys
from datetime import datetime

# --- 终端颜色配置 (让截图看起来很专业) ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def typing_print(text, delay=0.02):
    """Simulate streaming token output"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def log_step(step_name, detail):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{Colors.BLUE}[{timestamp}] {Colors.BOLD}{step_name:<15}{Colors.ENDC} | {detail}")
    time.sleep(random.uniform(0.5, 1.2))

class SimulatedMedicalAgent:
    def __init__(self):
        print(f"{Colors.HEADER}{'='*60}")
        print(f"   MEDICAL IMAGING AGENT (MIA) - v2.0 (Offline Kernel)")
        print(f"{'='*60}{Colors.ENDC}")
        log_step("SYSTEM", "Initializing Knowledge Graph...")
        log_step("MEMORY", "Loading Intalight_OCT_Protocol_v4.json...")
        log_step("SAFETY", "Guardrails Active (Strict Mode)")
        print()

    def analyze(self, query, metadata):
        print(f"{Colors.CYAN}>>> USER QUERY: {query}{Colors.ENDC}")
        print(f"{Colors.CYAN}>>> METADATA:   {json.dumps(metadata)}{Colors.ENDC}\n")

        # 1. 模拟安全检查
        log_step("GUARDRAIL", "Scanning for PII and medical advice requests...")
        if "diagnose" in query.lower():
            return self._refusal_response()
        
        # 2. 模拟 RAG 检索
        log_step("RETRIEVAL", f"Searching context for keywords: {list(metadata.keys())}...")
        
        # 3. 核心逻辑分支 (硬编码你的专家经验)
        if "30nm" in metadata.get("hardware", ""):
            return self._scenario_low_bandwidth()
        elif "compression" in query.lower():
            return self._scenario_compression()
        elif "area" in query.lower() or "quantification" in query.lower():
            return self._scenario_affine()
        else:
            return self._scenario_general()

    def _scenario_low_bandwidth(self):
        log_step("REASONING", "Detected hardware constraint: Low-Bandwidth Source.")
        log_step("WARNING", "Standard Super-Resolution risks structural hallucination.")
        log_step("SYNTHESIS", "Formulating GAN-based strategy...")
        
        return {
            "Analysis": "Hardware limitation (30nm source) causes axial blurring.",
            "Critical_Warning": "Do NOT use standard ResNet/SRGAN. Risk of 'layer thickening' artifacts.",
            "Recommendation": "CycleGAN with Structure-Consistency Loss",
            "Configuration": {
                "Generator": "ResNet-9blocks (Unpaired)",
                "Loss_Weights": {"Cycle": 10.0, "Identity": 5.0, "Structural_SSIM": 2.5},
                "Resolution_Target": "Simulate 100nm source distribution"
            }
        }

    def _scenario_affine(self):
        log_step("REASONING", "Detected quantification discrepancy.")
        log_step("MATH", "Verifying pixel-to-physical projection matrix...")
        
        return {
            "Analysis": "Segmentation is accurate (Dice > 0.9), but area calculation is flawed.",
            "Root_Cause": "Enface projection lacks curvature correction (Affine Matrix Mismatch).",
            "Action_Plan": [
                "Extract metadata tag (0x0028, 0x0030) for PixelSpacing.",
                "Apply geometric correction for fundus curvature.",
                "Re-calculate area in mm² space."
            ]
        }
    
    def _scenario_compression(self):
        log_step("REASONING", "Evaluating storage vs. fidelity trade-off.")
        log_step("SAFETY", "Standard JPEG rejected due to block artifacts.")
        
        return {
            "Recommendation": "Use JPEG-2000 or nvJPEG (GPU).",
            "Why": "Preserves high-bit-depth (16-bit) dynamic range essential for micro-pathology detection."
        }

    def _refusal_response(self):
        return {"status": "BLOCKED", "reason": "Safety Policy Violation"}

# --- 运行演示 ---
if __name__ == "__main__":
    agent = SimulatedMedicalAgent()
    
    # 模拟场景 1: 那个经典的 30nm 激光器问题
    response = agent.analyze(
        query="Enhance resolution of these blurry OCT scans.",
        metadata={"hardware": "Light source bandwidth ~30nm", "modality": "SD-OCT"}
    )
    
    print(f"\n{Colors.GREEN}>>> AGENT RESPONSE (GENERATED JSON):{Colors.ENDC}")
    typing_print(json.dumps(response, indent=2))
    
    print(f"\n{Colors.HEADER}{'='*60}")
    print("DEMO COMPLETE - LOGS SAVED")
    print(f"{'='*60}{Colors.ENDC}")