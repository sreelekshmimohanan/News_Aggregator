from transformers import pipeline

def generate_summary(article_text):
    """
    Generate a summary of the given article text using Facebook BART model.
    """
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn", model_kwargs={"cache_dir": "./ML/facebook_bart_large_cnn"})
        summary_result = summarizer(article_text, max_length=200, min_length=100, do_sample=False)
        return summary_result[0]['summary_text']
    except Exception as e:
        print(f"Error generating summary: {e}")
        return ""