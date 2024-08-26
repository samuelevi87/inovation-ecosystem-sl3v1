from crewai import Task
from config.config import obter_config

def criar_tarefa_definir_criterios(agente):
    return Task(
        description="Definir e refinar os critérios de avaliação para as ideias inovadoras, considerando o contexto atual da empresa e as tendências de mercado.",
        expected_output="Uma lista detalhada de critérios de avaliação, com descrições claras e métricas associadas para cada critério.",
        agent=agente
    )

def criar_tarefa_avaliacao_ideias(agente):
    config = obter_config()
    criterios = config['criterios_avaliacao']
    return Task(
        description=f"Avaliar cada ideia gerada durante o brainstorming utilizando os seguintes critérios: {', '.join(criterios)}. Atribuir uma pontuação de 1 a 10 para cada critério e calcular a pontuação total.",
        expected_output="Uma planilha ou documento contendo todas as ideias avaliadas, com pontuações detalhadas para cada critério e pontuação total calculada.",
        agent=agente
    )

def criar_tarefa_relatorio_avaliacao(agente):
    return Task(
        description="Elaborar um relatório detalhado da avaliação, destacando as ideias mais promissoras, justificando as pontuações e fornecendo recomendações para o desenvolvimento futuro de cada ideia selecionada.",
        expected_output="Um relatório completo de avaliação, incluindo análises das ideias top-ranking, justificativas para as pontuações e recomendações específicas para cada ideia selecionada.",
        agent=agente
    )