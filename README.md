# Document Analysis Using LLMs

This project demonstrates how to analyze documents using **Large Language Models (LLMs)** in Python. It combines the power of Natural Language Processing (NLP) and Transformer-based models to extract text from PDFs, summarize content, generate questions, and perform question answering – all in an automated pipeline.

---

## Key Features

- **Text Extraction**: Extract raw text from PDF files using `pdfplumber`.
- **Text Summarization**: Use the `t5-small` model to create concise summaries.
- **Question Generation**: Automatically generate questions from the summarized content using `valhalla/t5-base-qg-hl`.
- **Question Answering**: Answer questions using `deepset/roberta-base-squad2` by searching within the original document.

---

## Tech Stack
- Python 
- Hugging Face Transformers 
- pdfplumber 
- nltk 

---

## Installation

**Make sure you have Python 3.7+ installed, then run:**

```bash
pip install pdfplumber transformers nltk
```

**For first-time use of `nltk`, download the tokenizer models:**
```bash
import nltk
nltk.download('punkt')
```

**Add reference doc:**

Download the doc from `google_terms_of_service_en_in.pdf` given in the repo.


**Run the jupyter notebook:**
```bash
jupyter document_analysis_llm.ipynb
```

**Run the main file:**
```python
python main.py
```

---

## License
This project is licensed under [MIT License](https://github.com/veydantkatyal/doc-analysis/blob/main/LICENSE)

