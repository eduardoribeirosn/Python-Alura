# Desafio -> Python: Inteligência Artificial Aplicada > 03 (Temp) > 04 (Ep)

# for numero, email in enumerate(lista_de_emails): -> FOR COM INDICES

import json
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# -----
emails_resumidos = []

emails_gerados = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="""
    Gere 5 Emails com assuntos aleatórios sobre anime. em formato JSON:
    
    {
        "emails": [
            "...",
            "...",
            "..."
        ]
    }
    """
)

def resumindo_email_com_ia(lista_de_emails):
    data = json.loads(lista_de_emails.strip("```json").strip("```"))
    emails = data["emails"]
    for email_grande in emails:
        response_email_current_summarized = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"""
            Resuma este email em 1 linha, definindo o que essa pessoa quer no email.
            
            EMAIL: 
            {email_grande}
            """
        )

        emails_resumidos.append(response_email_current_summarized.text)


resumindo_email_com_ia(emails_gerados.text)

print(f"Esses são os resumos de Emails gerados pela IA:\n\n")
for email_atual in emails_resumidos:
    print(email_atual)