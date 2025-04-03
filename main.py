# Extract text from pdf
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    text = ''.join([page.extract_text() for page in pdf.pages])

# Summarize extracted text
from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")
summary = summarizer(text[:1000], max_length=150, min_length=30, do_sample=False)[0]['summary_text']

# Generate questions from summary
qg = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")
questions = qg(f"generate questions: {summary}")[0]['generated_text'].split("<sep>")

# Answer generated questions
qa = pipeline("question-answering", model="deepset/roberta-base-squad2")

for question in questions:
    result = qa(question=question, context=text)
    print(f"Q: {question}")
    print(f"A: {result['answer']}\n")
