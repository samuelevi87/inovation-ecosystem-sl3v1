from crewai import Task


def criar_tarefa_plano_mestre(agente):
    return Task(
        description="Elaborar o plano mestre de inovação para o próximo trimestre, definindo objetivos claros, métricas de sucesso e principais marcos.",
        expected_output="Um documento detalhado contendo o plano mestre de inovação, incluindo objetivos, métricas de sucesso, cronograma e recursos necessários.",
        agent=agente
    )


def criar_tarefa_coordenacao(agente):
    return Task(
        description="Coordenar as atividades entre todos os agentes do ecossistema de inovação, garantindo alinhamento e sinergia entre as diferentes iniciativas.",
        expected_output="Um relatório de status detalhando as atividades coordenadas, pontos de alinhamento alcançados e próximos passos para cada iniciativa.",
        agent=agente
    )

# Adicione mais funções de criação de tarefas conforme necessário
