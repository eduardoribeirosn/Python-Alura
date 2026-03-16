# Criar ambiente virtual = python -m venv .venv -> o ".venv" é o nome do ambiente
# Para ativar o ambiente = .venv/Scripts/activate.ps1
# Para desativar o ambiente = deactivate
# Instalar dependências = pip install -q openai -> o "-q" é para não vir um monte de textos
from openai import OpenAI

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

resposta_do_llm = client_openai.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[
        {
            "role": "user",
            "content": "Quando lança o próximo filme de homem aranha de animação?"
        }
    ],
    temperature=1.0
)

print(resposta_do_llm.choices[0].message.content)