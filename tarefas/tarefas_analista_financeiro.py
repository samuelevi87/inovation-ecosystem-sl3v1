from crewai import Task


def criar_tarefa_analise_viabilidade(agente):
    return Task(
        description="Realizar uma análise detalhada de viabilidade financeira para as ideias selecionadas, considerando custos de desenvolvimento, potencial de mercado e retorno sobre investimento.",
        expected_output="Um relatório financeiro completo para cada ideia selecionada, incluindo análise de custos, projeções de receita e indicadores financeiros chave (ROI, VPL, TIR).",
        agent=agente
    )


def criar_tarefa_modelagem_negocios(agente):
    return Task(
        description="Desenvolver modelos de negócios robustos para as ideias mais promissoras, incluindo estratégias de monetização, estrutura de custos e projeções financeiras para os próximos 3-5 anos.",
        expected_output="Modelos de negócios detalhados para cada ideia promissora, incluindo canvas de modelo de negócios, projeções financeiras e análise de cenários.",
        agent=agente
    )


def criar_tarefa_recomendacoes_investimento(agente):
    return Task(
        description="Elaborar recomendações de investimento baseadas nas análises financeiras e modelos de negócios desenvolvidos, priorizando as ideias com melhor potencial de retorno e alinhamento estratégico.",
        expected_output="Um documento de recomendações de investimento, classificando as ideias por potencial financeiro e estratégico, com justificativas detalhadas para cada recomendação.",
        agent=agente
    )
