from transformers import pipeline

# Download and save the model in the current directory
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", model_kwargs={"cache_dir": "./facebook_bart_large_cnn"})

ARTICLE = """ After the sound and the fury, weeks of demonstrations and anguished calls for racial justice, the man whose death gave rise to an international movement, and whose last words — “I can’t breathe” — have been a rallying cry, will be laid to rest on Tuesday at a private funeral in Houston.George Floyd, who was 46, will then be buried in a grave next to his mother’s.The service, scheduled to begin at 11 a.m. at the Fountain of Praise church, comes after five days of public memorials in Minneapolis, North Carolina and Houston and two weeks after a Minneapolis police officer was caught on video pressing his knee into Mr. Floyd’s neck for nearly nine minutes before Mr. Floyd died. That officer, Derek Chauvin, has been charged with second-degree murder and second-degree manslaughter. His bail was set at $1.25 million in a court appearance on Monday. The outpouring of anger and outrage after Mr. Floyd’s death — and the speed at which protests spread from tense, chaotic demonstrations in the city where he died to an international movement from Rome to Rio de Janeiro — has reflected the depth of frustration borne of years of watching black people die at the hands of the police or vigilantes while calls for change went unmet.
"""
print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))
