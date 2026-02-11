# Evaluation Framework

To ensure the `Medical-LLM-Agent` provides reliable and safe recommendations, we propose the following multi-dimensional evaluation metrics.

## 1. Safety & Compliance Metrics
* **Refusal Rate (RR):** Percentage of non-medical/unsafe queries correctly refused.
    * *Target:* > 99% for direct diagnosis requests.
* **Jailbreak Resistance:** Robustness against prompts trying to bypass safety guardrails (e.g., "Imagine you are a doctor...").

## 2. Technical Validity (Code Correctness)
* **Executability Score:** Can the generated Python config/code run without syntax errors?
* **Parameter Consistency:** Does the generated loss function match the output layer activation?
    * *Example:* If `Sigmoid` is used, Loss must not be `CrossEntropy` (expecting logits).

## 3. Domain Alignment (Expert Review)
* **Rationale Rating:** A panel of senior algorithm engineers rates the "Reasoning" field on a 1-5 scale.
    * *Criteria:* Does the agent correctly identify that low-bandwidth OCT requires specific GAN losses? [Based on Intalight experience]
* **Hallucination Rate:** Frequency of recommending non-existent libraries or model layers.

## 4. Benchmark Dataset
We are compiling a test set of **50 diverse OCT scenarios**, covering:
* Low-quality / Noisy data
* Rare pathologies (e.g., Microaneurysms)
* Hardware-specific constraints (30nm vs 100nm bandwidth)