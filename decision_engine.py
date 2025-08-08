import json

def parse_verdict(response_str):
    # Strip markdown code block formatting if present
    response_str = response_str.strip()

    if response_str.startswith("```"):
        # Remove surrounding ```json ... ```
        response_str = re.sub(r"^```(?:json)?\s*", "", response_str)
        response_str = re.sub(r"\s*```$", "", response_str)

    try:
        verdict = json.loads(response_str)
        return verdict.get("verdict"), verdict.get("reason")
    except json.JSONDecodeError as e:
        print("JSON parsing failed:", e)
        print("Raw LLM output:", response_str)
        return None, "Could not parse LLM output"
