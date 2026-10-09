
import pandas as pd

df = pd.read_csv("dataset/llm_responses.csv")

df["response_length"] = df["response"].astype(str).str.len()

df["response_status"] = df["response"].apply(
    lambda x: "Error" if str(x).startswith("Error:") else "Success"
)

df.to_csv("dataset/response_comparison.csv", index=False)

print("Response comparison saved successfully!")
print("Total responses:", len(df))