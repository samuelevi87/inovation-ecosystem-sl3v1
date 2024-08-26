from crewai import Task

def criar_tarefa_planejamento_prototipo(agente):
    return Task(
        description="Elaborar um plano de prototipagem para as ideias selecionadas, definindo as técnicas mais adequadas, recursos necessários e cronograma para cada protótipo.",
        expected_output="Um documento detalhado de planejamento de prototipagem, incluindo metodologias selecionadas, lista de recursos necessários, cronograma e orçamento estimado para cada protótipo.",
        agent=agente
    )

def criar_tarefa_desenvolvimento_prototipo(agente):
    return Task(
        description="Desenvolver protótipos funcionais ou conceituais para as ideias selecionadas, utilizando as técnicas mais apropriadas para cada caso (e.g., mockups digitais, impressão 3D, prototipagem de software).",
        expected_output="Um conjunto de protótipos desenvolvidos, acompanhados de documentação técnica detalhando o processo de criação, especificações e instruções de uso para cada protótipo.",
        agent=agente
    )

def criar_tarefa_teste_inicial(agente):
    return Task(
        description="Conduzir testes iniciais dos protótipos desenvolvidos, coletando feedback preliminar e identificando áreas para refinamento e iteração.",
        expected_output="Um relatório de testes contendo os resultados dos testes iniciais, feedback coletado, análise de desempenho dos protótipos e recomendações para melhorias e iterações futuras.",
        agent=agente
    )