# Local LLM Inference

## Project Description

This project uses Ollama to run a local Large Language Model (LLM) and generate responses to prompts using the Llama 3.2 model.

## Objectives

* Run a language model locally using Ollama.
* Read prompts from a CSV dataset.
* Generate responses using Python.
* Store generated responses in CSV files.
* Compare response lengths and statuses.

## Technologies Used

* Python
* Ollama
* Llama 3.2
* Pandas
* CSV

## Project Structure

```text
OLLAMA_LOCAL_INTERFACE/
├── dataset/
│   ├── prompts.csv
│   ├── llm_responses.csv
│   ├── response_comparison.csv
│   └── conversation_history.csv
├── notebook/
│   └── Week8_Local_LLM_Inference.ipynb
├── local_llm.py
├── compare_responses.py
├── README.md
└── requirements.txt
```

## How to Run

1. Install Ollama and download the Llama 3.2 model.
2. Install Python dependencies using `pip install -r requirements.txt`.
3. Start Ollama and run `ollama run llama3.2` if needed.
4. Execute `python local_llm.py`.
5. Execute `python compare_responses.py`.

## Output

The generated responses are saved in `dataset/llm_responses.csv`. The comparison results are saved in `dataset/response_comparison.csv`.

## Conclusion

This project demonstrates how to run a local language model, generate responses from prompts, and store and compare the results using Python.
