from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="meta/llama-3.3-70b-instruct",
  messages=[{"role":"user","content":"Provide me an article on machine learning"}],
  temperature=0.34,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

