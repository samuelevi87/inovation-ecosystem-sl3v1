from crewai import Task


def criar_tarefa_identificar_tendencias(agente):
    return Task(
        description="""Realize uma pesquisa abrangente para identificar as tendências emergentes mais relevantes nos próximos 2-5 anos. 
        Foque em tendências tecnológicas, comportamentais e de mercado que possam impactar significativamente nosso setor. 
        Utilize a ferramenta de busca DuckDuckGo para obter informações atualizadas.

        Apresente um relatório com:
        1. Lista das top 10 tendências identificadas
        2. Breve descrição de cada tendência
        3. Potencial impacto em nosso setor
        4. Fontes confiáveis que suportam cada tendência""",
        expected_output="Um relatório detalhado listando e descrevendo as top 10 tendências emergentes, seu potencial impacto e fontes de referência.",
        agent=agente
    )


def criar_tarefa_analisar_impacto_tendencias(agente):
    return Task(
        description="""Com base nas tendências identificadas, realize uma análise aprofundada do potencial impacto em nosso negócio.
        Para cada tendência:
        1. Avalie o nível de disrupção (baixo, médio, alto)
        2. Identifique oportunidades específicas para nossa empresa
        3. Aponte possíveis ameaças ou desafios
        4. Sugira áreas de inovação que podemos explorar

        Priorize as tendências com base em seu potencial de impacto e relevância para nossa estratégia de negócios.""",
        expected_output="Uma análise detalhada do impacto de cada tendência, incluindo oportunidades, ameaças e sugestões de áreas para inovação, com uma lista priorizada das tendências mais relevantes.",
        agent=agente
    )


def criar_tarefa_recomendar_acoes(agente):
    return Task(
        description="""Com base na análise de impacto das tendências, desenvolva um conjunto de recomendações acionáveis para nossa empresa.
        Para cada recomendação:
        1. Descreva a ação específica a ser tomada
        2. Explique como ela se alinha com as tendências identificadas
        3. Estime o prazo para implementação (curto, médio, longo prazo)
        4. Sugira métricas para medir o sucesso da implementação

        Priorize as recomendações com base em seu potencial de impacto, viabilidade e alinhamento estratégico.""",
        expected_output="Um conjunto priorizado de recomendações acionáveis, detalhando ações específicas, alinhamento com tendências, prazos e métricas de sucesso.",
        agent=agente
    )
