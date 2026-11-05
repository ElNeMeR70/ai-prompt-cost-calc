"""LLM Prompt Token & Cost Calculator"""

RATES = {
    "gpt-4o": {"in": 0.005 / 1000, "out": 0.015 / 1000},
    "claude-3-5-sonnet": {"in": 0.003 / 1000, "out": 0.015 / 1000},
    "gemini-1-5-flash": {"in": 0.000075 / 1000, "out": 0.0003 / 1000}
}

def estimate_cost(model, in_tokens, out_tokens):
    r = RATES.get(model, RATES["gpt-4o"])
    return (in_tokens * r["in"]) + (out_tokens * r["out"])

if __name__ == "__main__":
    print("[RUN] LLM Prompt Cost Calculator...")
    cost = estimate_cost("gpt-4o", 12000, 800)
    print(f"[OK] Estimated Cost for 12k prompt + 800 completion: ${cost:.6f}")
