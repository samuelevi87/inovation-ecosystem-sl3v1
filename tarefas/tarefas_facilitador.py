from crewai import Task


def criar_tarefa_planejamento_sessao(agente):
    return Task(
        description="Planejar uma sessão de brainstorming inovadora, definindo metodologias, ferramentas e dinâmicas que serão utilizadas para maximizar a geração de ideias criativas.",
        expected_output="Um plano detalhado da sessão de brainstorming, incluindo agenda, metodologias selecionadas e materiais necessários.",
        agent=agente
    )


def criar_tarefa_conducao_sessao(agente):
    return Task(
        description="Conduzir a sessão de brainstorming, garantindo a participação ativa de todos os membros, estimulando o pensamento divergente e mantendo o foco nos objetivos estabelecidos.",
        expected_output="Um relatório da sessão de brainstorming, incluindo lista de participantes, ideias geradas e observações sobre a dinâmica do grupo.",
        agent=agente
    )


def criar_tarefa_documentacao_ideias(agente):
    return Task(
        description="Documentar de forma estruturada e detalhada todas as ideias geradas durante a sessão de brainstorming, categorizando-as e preparando-as para a fase de avaliação.",
        expected_output="Um documento organizado com todas as ideias geradas, categorizadas e com descrições detalhadas para facilitar a avaliação posterior.",
        agent=agente
    )
