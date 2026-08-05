from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

prompt = """
Write a 1500-word SEO-friendly HTML blog article.

Topic: Best Amazon Products

Include:
- H1 Title
- Introduction
- Features
- Pros
- Cons
- FAQ
- Conclusion

Return only valid HTML.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

with open("article.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Article generated successfully!")
