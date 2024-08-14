from ollama import generate

prompt = '''Translate a given piece of text from English to
Spanish 
text:Do you speak spanish?'''

response = generate(
  model="gemma2:2b",
  prompt=prompt,
  options={
    'num_predict': 128,
    'temperature': 0
  },
)

print(response['response'])