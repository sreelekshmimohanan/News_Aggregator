from transformers import AutoModelWithLMHead, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-summarize-news")
model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-summarize-news")

def summarize(text, max_length=150):
  input_ids = tokenizer.encode(text, return_tensors="pt", add_special_tokens=True)

  generated_ids = model.generate(input_ids=input_ids, num_beams=2, max_length=max_length,  repetition_penalty=2.5, length_penalty=1.0, early_stopping=True)

  preds = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in generated_ids]

  return preds[0]
if __name__ == "__main__":
    sample_text = """The quick brown fox jumps over the lazy dog. This sentence is often used to demonstrate fonts and test typing skills. It contains every letter of the English alphabet, making it a pangram. The fox is known for its agility and cleverness, while the dog is typically seen as loyal and friendly. Together, they create a vivid image that has been used in various contexts, from educational materials to advertisements."""
    summary = summarize(sample_text)
    print("Original Text:\n", sample_text)
    print("\nSummary:\n", summary)