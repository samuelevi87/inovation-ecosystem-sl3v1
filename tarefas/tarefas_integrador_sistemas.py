from crewai import Task


def criar_tarefa_analise_arquitetura_atual(agente):
    return Task(
        description="""Realize uma análise abrangente da arquitetura de sistemas atual da empresa. Esta análise deve incluir:
        1. Mapeamento dos principais sistemas e suas interconexões
        2. Identificação de tecnologias legadas e suas limitações
        3. Avaliação da escalabilidade e flexibilidade da arquitetura existente
        4. Análise de pontos de integração existentes e potenciais gargalos

        Utilize a ferramenta de busca para identificar as melhores práticas atuais em arquitetura de sistemas empresariais e compare com a estrutura existente.""",
        expected_output="Um relatório detalhado da arquitetura de sistemas atual, destacando pontos fortes, fracos e oportunidades de melhoria.",
        agent=agente
    )


def criar_tarefa_plano_integracao_inovacoes(agente):
    return Task(
        description="""Com base nas inovações propostas e na análise da arquitetura atual, desenvolva um plano detalhado de integração. Este plano deve:
        1. Identificar os pontos de integração necessários para cada inovação
        2. Propor soluções para superar limitações dos sistemas legados
        3. Sugerir tecnologias e frameworks de integração adequados
        4. Delinear uma estratégia de migração de dados, se necessário
        5. Abordar questões de segurança e conformidade

        Use o Analisador de Compatibilidade de Sistemas para avaliar a viabilidade das integrações propostas.""",
        expected_output="Um plano de integração abrangente para cada inovação, incluindo abordagens técnicas, cronograma estimado e análise de riscos.",
        agent=agente
    )


def criar_tarefa_prototipo_integracao(agente):
    return Task(
        description="""Desenvolva um protótipo ou prova de conceito para a integração mais crítica ou desafiadora identificada no plano. Este protótipo deve:
        1. Demonstrar a viabilidade técnica da integração proposta
        2. Utilizar tecnologias e padrões de integração modernos (ex: APIs RESTful, GraphQL, ou arquitetura de microserviços)
        3. Abordar questões de desempenho e escalabilidade
        4. Incluir considerações de segurança e manipulação de erros

        Documente o processo de desenvolvimento do protótipo, destacando desafios encontrados e soluções aplicadas.""",
        expected_output="Um protótipo funcional da integração crítica, acompanhado de documentação técnica e lições aprendidas durante o desenvolvimento.",
        agent=agente
    )


def criar_tarefa_recomendacoes_arquitetura_futura(agente):
    return Task(
        description="""Com base em todas as análises e no trabalho de prototipagem realizados, desenvolva um conjunto de recomendações para a evolução da arquitetura de sistemas da empresa. Estas recomendações devem:
        1. Propor uma visão de arquitetura futura que acomode as inovações planejadas e futuras
        2. Sugerir tecnologias e padrões arquiteturais a serem adotados (ex: arquitetura em nuvem, edge computing, IA/ML integrados)
        3. Delinear um roadmap de transformação arquitetural
        4. Identificar competências e treinamentos necessários para a equipe de TI
        5. Abordar considerações de governança de TI e gerenciamento de mudanças

        Utilize a ferramenta de busca para identificar tendências futuras em arquitetura de sistemas empresariais e incorpore insights relevantes às suas recomendações.""",
        expected_output="Um documento estratégico de recomendações para a evolução da arquitetura de sistemas, incluindo visão de longo prazo, roadmap de implementação e considerações de mudança organizacional.",
        agent=agente
    )
