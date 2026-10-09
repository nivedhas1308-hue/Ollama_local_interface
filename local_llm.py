import pandas as pd
import ollama

# Load prompts from CSV
prompts = pd.read_csv("dataset/prompts.csv")

# Remove rows with empty prompts
prompts = prompts.dropna(subset=["prompt"])
prompts["prompt"] = prompts["prompt"].astype(str).str.strip()
prompts = prompts[prompts["prompt"] != ""]

# Select the local LLM model
model = "llama3.2"

# Store generated responses
responses = []

# Process each prompt
for index, row in prompts.iterrows():

    prompt = row["prompt"]

    print(f"\nProcessing prompt {index + 1}: {prompt}")

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response["message"]["content"]

        print("Response:", answer)

        responses.append({
            "prompt_id": row["prompt_id"],
            "domain": row["domain"],
            "prompt": prompt,
            "response": answer
        })

    except Exception as e:
        print("Error generating response:", e)

        responses.append({
            "prompt_id": row["prompt_id"],
            "domain": row["domain"],
            "prompt": prompt,
            "response": f"Error: {e}"
        })

# Convert responses to a DataFrame
result = pd.DataFrame(
    responses,
    columns=["prompt_id", "domain", "prompt", "response"]
)

# Save generated responses
result.to_csv(
    "dataset/llm_responses.csv",
    index=False
)

print("\nResponses saved successfully.")
print("Output file: dataset/llm_responses.csv")
print("Total prompts processed:", len(result))


