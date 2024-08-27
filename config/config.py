from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente de um arquivo .env
load_dotenv()

def obter_modelo_linguagem():
    return ChatOpenAI(
        model_name="gpt-4o-mini",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.7
    )

# Configurações globais do projeto
CONFIG = {
    "max_iteracoes": 5,
    "tempo_limite_sessao": 120,  # em minutos
    "numero_minimo_ideias": 20,
    "criterios_avaliacao": [
        "Viabilidade técnica",
        "Potencial de mercado",
        "Alinhamento estratégico",
        "Inovação",
        "Sustentabilidade"
    ]
}

def obter_config():
    return CONFIG