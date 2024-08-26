from crewai import Crew
from agentes.gerente_inovacao import criar_gerente_inovacao
from agentes.facilitador_brainstorming import criar_facilitador_brainstorming
from agentes.avaliador_ideias import criar_avaliador_ideias
from agentes.prototipador import criar_prototipador
# Importe os outros agentes...

from tarefas.tarefas_gerente import criar_tarefa_plano_mestre, criar_tarefa_coordenacao
from tarefas.tarefas_facilitador import criar_tarefa_planejamento_sessao, criar_tarefa_conducao_sessao, \
    criar_tarefa_documentacao_ideias
from tarefas.tarefas_avaliador import criar_tarefa_definir_criterios, criar_tarefa_avaliacao_ideias, \
    criar_tarefa_relatorio_avaliacao
from tarefas.tarefas_prototipador import criar_tarefa_planejamento_prototipo, criar_tarefa_desenvolvimento_prototipo, \
    criar_tarefa_teste_inicial
# Importe as outras tarefas...

from config.config import obter_config
from utils.helpers import salvar_resultado, formatar_ideias, gerar_grafico_avaliacoes, calcular_metricas_inovacao


def criar_equipe_inovacao():
    gerente = criar_gerente_inovacao()
    facilitador = criar_facilitador_brainstorming()
    avaliador = criar_avaliador_ideias()
    prototipador = criar_prototipador()
    # Crie os outros agentes...

    tarefas = [
        criar_tarefa_plano_mestre(gerente),
        criar_tarefa_coordenacao(gerente),
        criar_tarefa_planejamento_sessao(facilitador),
        criar_tarefa_conducao_sessao(facilitador),
        criar_tarefa_documentacao_ideias(facilitador),
        criar_tarefa_definir_criterios(avaliador),
        criar_tarefa_avaliacao_ideias(avaliador),
        criar_tarefa_relatorio_avaliacao(avaliador),
        criar_tarefa_planejamento_prototipo(prototipador),
        criar_tarefa_desenvolvimento_prototipo(prototipador),
        criar_tarefa_teste_inicial(prototipador),
        # Adicione as outras tarefas...
    ]

    return Crew(
        agents=[gerente, facilitador, avaliador, prototipador],  # Adicione todos os agentes
        tasks=tarefas,
        verbose=True
    )


def main():
    config = obter_config()
    equipe_inovacao = criar_equipe_inovacao()

    print("Iniciando o processo de inovação...")
    resultado = equipe_inovacao.kickoff()

    print("\nResultado do processo de inovação:")
    print(resultado)

    # Processamento e visualização dos resultados
    ideias_geradas = resultado.get('ideias_geradas', [])
    ideias_avaliadas = resultado.get('ideias_avaliadas', [])

    print(f"\nTotal de ideias geradas: {len(ideias_geradas)}")
    print("Top 5 ideias avaliadas:")
    for i, ideia in enumerate(ideias_avaliadas[:5], 1):
        print(f"{i}. {ideia['nome']} - Pontuação: {ideia['pontuacao']}")

    # Gerar gráfico das avaliações
    gerar_grafico_avaliacoes(ideias_avaliadas)

    # Calcular e exibir métricas de inovação
    metricas = calcular_metricas_inovacao(resultado)
    print("\nMétricas de Inovação:")
    print(f"Total de ideias geradas: {metricas['total_ideias']}")
    print(f"Ideias aprovadas para prototipagem: {metricas['ideias_aprovadas']}")
    print(f"Taxa de aprovação: {metricas['taxa_aprovacao']:.2f}%")

    # Salvar o resultado em um arquivo
    salvar_resultado(resultado)


if __name__ == "__main__":
    main()
