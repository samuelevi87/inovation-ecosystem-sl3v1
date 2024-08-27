from crewai import Task


def criar_tarefa_avaliar_etica_ideias(agente):
    return Task(
        description="""Realize uma avaliação ética abrangente das ideias inovadoras propostas. Para cada ideia:
        1. Identifique potenciais dilemas éticos ou áreas de preocupação
        2. Avalie o impacto social e ambiental
        3. Verifique a conformidade com regulamentações existentes e emergentes
        4. Sugira modificações ou salvaguardas para mitigar riscos éticos

        Utilize a ferramenta de busca para verificar as últimas regulamentações e melhores práticas em ética na inovação.
        Use o Analisador de Impacto Ético para uma avaliação detalhada de cada ideia.""",
        expected_output="Um relatório detalhado para cada ideia inovadora, destacando considerações éticas, impactos potenciais, conformidade regulatória e recomendações para mitigação de riscos.",
        agent=agente
    )


def criar_tarefa_desenvolver_diretrizes_eticas(agente):
    return Task(
        description="""Desenvolva um conjunto abrangente de diretrizes éticas para o processo de inovação da empresa. Estas diretrizes devem:
        1. Abordar os principais dilemas éticos identificados nas ideias propostas
        2. Incorporar princípios de inovação responsável e sustentável
        3. Ser práticas e acionáveis para as equipes de desenvolvimento
        4. Alinhar-se com os valores da empresa e as expectativas dos stakeholders

        Baseie-se em casos de estudo de empresas líderes em inovação ética e adapte as melhores práticas ao nosso contexto específico.""",
        expected_output="Um documento de diretrizes éticas para inovação, incluindo princípios fundamentais, exemplos práticos e um framework para tomada de decisões éticas no processo de inovação.",
        agent=agente
    )


def criar_tarefa_plano_treinamento_etica(agente):
    return Task(
        description="""Elabore um plano de treinamento em ética e inovação responsável para todos os envolvidos no processo de inovação. O plano deve:
        1. Cobrir os princípios básicos de ética em inovação
        2. Incluir estudos de caso relevantes para nossa indústria
        3. Fornecer ferramentas práticas para avaliação ética no dia a dia
        4. Propor métodos de avaliação para medir a eficácia do treinamento

        O objetivo é criar uma cultura de inovação ética em toda a organização.""",
        expected_output="Um plano detalhado de treinamento em ética e inovação responsável, incluindo currículo, metodologias de ensino, recursos necessários e métricas de avaliação.",
        agent=agente
    )
