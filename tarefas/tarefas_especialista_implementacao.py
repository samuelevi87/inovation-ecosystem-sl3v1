from crewai import Task


def criar_tarefa_plano_implementacao(agente):
    return Task(
        description="Desenvolver um plano detalhado de implementação para as ideias inovadoras selecionadas, incluindo cronograma, alocação de recursos, marcos e estratégias de mitigação de riscos.",
        expected_output="Um documento abrangente de plano de implementação para cada ideia selecionada, detalhando todas as fases do projeto, desde o início até a conclusão.",
        agent=agente
    )


def criar_tarefa_analise_impacto_organizacional(agente):
    return Task(
        description="Realizar uma análise completa do impacto organizacional das inovações selecionadas, identificando mudanças necessárias em processos, estruturas e culturas.",
        expected_output="Um relatório detalhado de análise de impacto organizacional, destacando áreas-chave de mudança e recomendações para uma transição eficaz.",
        agent=agente
    )


def criar_tarefa_estrategia_gestao_mudancas(agente):
    return Task(
        description="Elaborar uma estratégia abrangente de gestão de mudanças para facilitar a adoção das inovações em toda a organização, incluindo planos de comunicação e treinamento.",
        expected_output="Um documento estratégico de gestão de mudanças, detalhando abordagens para superar resistências, promover engajamento e garantir a adoção bem-sucedida das inovações.",
        agent=agente
    )
