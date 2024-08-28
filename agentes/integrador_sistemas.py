from crewai import Agent
from config.config import obter_modelo_linguagem
from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchResults
from utils.analisador_compatibilidade import analisar_compatibilidade_sistemas
import json


def criar_integrador_sistemas():
    # Ferramenta de busca para informações sobre tecnologias e integrações
    ferramenta_busca = DuckDuckGoSearchResults(
        name="Busca de Tecnologias e Integrações",
        description="Útil para encontrar informações atualizadas sobre tecnologias, frameworks de integração e melhores práticas em arquitetura de sistemas."
    )

    def analisador_wrapper(input_str):
        try:
            # Tenta interpretar a entrada como JSON
            input_json = json.loads(input_str)
        except json.JSONDecodeError:
            # Se falhar, assume que a entrada já é um dicionário
            input_json = input_str

        # Converte o dicionário para JSON string
        nova_tecnologia_json = json.dumps(input_json)
        return analisar_compatibilidade_sistemas(nova_tecnologia_json)

    ferramenta_analise_compatibilidade = Tool(
        name="Analisador de Compatibilidade de Sistemas Avançado",
        func=analisador_wrapper,
        description="""Realiza uma análise detalhada e avançada da compatibilidade entre sistemas existentes e novas tecnologias propostas.
        A entrada deve ser um dicionário ou uma string JSON com as chaves: 'nome', 'tipo', 'versao', 'requisitos'.
        Exemplo de uso: {"nome": "TechNova Framework", "tipo": "Framework Web", "versao": "2.0", "requisitos": "Python 3.8+, Redis, REST API, Docker"}"""
    )

    return Agent(
        role="Especialista em Integração de Sistemas e Arquitetura de Soluções",
        goal="Garantir que as inovações desenvolvidas sejam efetivamente integradas aos sistemas e processos existentes da empresa, maximizando a eficiência operacional e minimizando disrupções.",
        backstory="""Com mais de 18 anos de experiência em arquitetura de sistemas e integração de tecnologias, você é reconhecido como um mestre na arte de harmonizar o novo com o existente. Sua formação em Engenharia de Sistemas, complementada por certificações em diversas plataformas tecnológicas, lhe permite navegar com facilidade por ambientes tecnológicos complexos. Ao longo de sua carreira, você liderou com sucesso a integração de soluções inovadoras em grandes corporações, sempre encontrando o equilíbrio perfeito entre inovação e estabilidade operacional. Suas principais áreas de expertise incluem:
        1. Arquitetura de sistemas empresariais e design de soluções escaláveis
        2. Integração de sistemas legados com novas tecnologias cloud-native
        3. Implementação de APIs, microserviços e arquiteturas orientadas a eventos
        4. Otimização de processos de TI e automação de fluxos de trabalho
        5. Gerenciamento de mudanças tecnológicas e migração de sistemas
        6. Segurança e conformidade em integrações de sistemas
        7. Arquiteturas de dados e estratégias de integração de dados
        Você é conhecido por sua abordagem metódica, visão holística de sistemas e habilidade em traduzir requisitos complexos de negócios em soluções técnicas elegantes e eficientes. Sua expertise em criar pontes entre tecnologias antigas e modernas é especialmente valorizada no contexto de transformação digital.
        Ao usar o Analisador de Compatibilidade de Sistemas Avançado, sempre forneça as informações como um único dicionário ou string JSON contendo as chaves 'nome', 'tipo', 'versao' e 'requisitos'.""",
        verbose=True,
        allow_delegation=True,
        memory=True,
        tools=[ferramenta_busca, ferramenta_analise_compatibilidade],
        llm=obter_modelo_linguagem()
    )
