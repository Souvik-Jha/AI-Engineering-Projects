from openai import OpenAI 
from dotenv import load_dotenv
from scraper import summarize_website_contnet

load_dotenv()
client = OpenAI()
system_prompt = """You analyze the contents of a website and
give a short, friendly summary. Ignore navigation menus.
Respond in markdown."""


def summarize(url):
    website = summarize_website_contnet(url)
    responce = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[{
            "role":"system","content": system_prompt},
            {"role":"user", "content" :f"summarize this website: /n/n {website}"
        }]
    )
    return responce.choices[0].message.content