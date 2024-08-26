import argparse
import logging
from crewai import Crew
from agentes.gerente_inovacao import criar_gerente_inovacao
from agentes.facilitador_brainstorming import criar_facilitador_brainstorming
from agentes.avaliador_ideias import criar_avaliador_ideias
from agentes.prototipador import criar_prototipador
from agentes.analista_financeiro import criar_analista_financeiro
from agentes.especialista_implementacao import criar_especialista_implementacao

from tarefas.tarefas_gerente import criar_tarefa_plano_mestre, criar_tarefa_coordenacao
from tarefas.tarefas_facilitador import criar_tarefa_planejamento_sessao, criar_tarefa_conducao_sessao, \
    criar_tarefa_documentacao_ideias
from tarefas.tarefas_avaliador import criar_tarefa_definir_criterios, criar_tarefa_avaliacao_ideias, \
    criar_tarefa_relatorio_avaliacao
from tarefas.tarefas_prototipador import criar_tarefa_planejamento_prototipo, criar_tarefa_desenvolvimento_prototipo, \
    criar_tarefa_teste_inicial
from tarefas.tarefas_analista_financeiro import criar_tarefa_analise_viabilidade, criar_tarefa_modelagem_negocios, \
    criar_tarefa_recomendacoes_investimento
from tarefas.tarefas_especialista_implementacao import criar_tarefa_plano_implementacao, \
    criar_tarefa_analise_impacto_organizacional, criar_tarefa_estrategia_gestao_mudancas

from config.config import obter_config
from utils.helpers import salvar_resultado, formatar_ideias, gerar_grafico_avaliacoes, calcular_metricas_inovacao, \
    obter_ultimo_resultado, carregar_resultado, gerar_markdown, salvar_markdown

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def criar_equipe_inovacao():
    gerente = criar_gerente_inovacao()
    facilitador = criar_facilitador_brainstorming()
    avaliador = criar_avaliador_ideias()
    prototipador = criar_prototipador()
    analista_financeiro = criar_analista_financeiro()
    especialista_implementacao = criar_especialista_implementacao()

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
        criar_tarefa_analise_viabilidade(analista_financeiro),
        criar_tarefa_modelagem_negocios(analista_financeiro),
        criar_tarefa_recomendacoes_investimento(analista_financeiro),
        criar_tarefa_plano_implementacao(especialista_implementacao),
        criar_tarefa_analise_impacto_organizacional(especialista_implementacao),
        criar_tarefa_estrategia_gestao_mudancas(especialista_implementacao),
    ]

    return Crew(
        agents=[gerente, facilitador, avaliador, prototipador, analista_financeiro, especialista_implementacao],
        tasks=tarefas,
        verbose=True
    )


def executar_processo_inovacao():
    try:
        config = obter_config()
        equipe_inovacao = criar_equipe_inovacao()

        logging.info("Iniciando o processo de inovação...")
        resultado = equipe_inovacao.kickoff()

        logging.info("Processo de inovação concluído. Processando resultados...")

        # Formatar e exibir ideias geradas
        ideias_geradas = resultado.get('ideias_geradas', [])
        ideias_formatadas = formatar_ideias(ideias_geradas)
        logging.info(f"Ideias geradas:\n{ideias_formatadas}")

        # Calcular e exibir métricas
        metricas = calcular_metricas_inovacao(resultado)
        logging.info("Métricas de Inovação:")
        logging.info(f"Total de ideias geradas: {metricas['total_ideias']}")
        logging.info(f"Ideias aprovadas para prototipagem: {metricas['ideias_aprovadas']}")
        logging.info(f"Taxa de aprovação: {metricas['taxa_aprovacao']:.2f}%")

        # Salvar o resultado em um arquivo JSON
        nome_arquivo_json = salvar_resultado(resultado)

        # Gerar gráfico das avaliações
        nome_arquivo_grafico = gerar_grafico_avaliacoes(resultado.get('ideias_avaliadas', []))

        # Gerar e salvar o relatório Markdown
        markdown = gerar_markdown(resultado, nome_arquivo_grafico)
        nome_arquivo_md = salvar_markdown(markdown)

        logging.info(f"Resultado salvo em JSON: {nome_arquivo_json}")
        logging.info(f"Relatório Markdown gerado: {nome_arquivo_md}")
        logging.info("Processo de inovação finalizado com sucesso.")

        return resultado

    except Exception as e:
        logging.error(f"Erro durante o processo de inovação: {str(e)}")
        raise


def visualizar_ultimo_resultado():
    ultimo_arquivo = obter_ultimo_resultado()
    if not ultimo_arquivo:
        logging.info("Nenhum resultado anterior encontrado.")
        return

    resultado = carregar_resultado(ultimo_arquivo)

    # Formatar e exibir ideias geradas
    ideias_geradas = resultado.get('ideias_geradas', [])
    ideias_formatadas = formatar_ideias(ideias_geradas)
    logging.info(f"Ideias geradas:\n{ideias_formatadas}")

    # Calcular e exibir métricas
    metricas = calcular_metricas_inovacao(resultado)
    logging.info("Métricas de Inovação:")
    logging.info(f"Total de ideias geradas: {metricas['total_ideias']}")
    logging.info(f"Ideias aprovadas para prototipagem: {metricas['ideias_aprovadas']}")
    logging.info(f"Taxa de aprovação: {metricas['taxa_aprovacao']:.2f}%")

    nome_arquivo_grafico = gerar_grafico_avaliacoes(resultado.get('ideias_avaliadas', []))
    markdown = gerar_markdown(resultado, nome_arquivo_grafico)
    nome_arquivo_md = salvar_markdown(markdown)

    logging.info(f"Relatório do último processo de inovação gerado: {nome_arquivo_md}")


def exibir_menu():
    print("\n=== Ecossistema de Inovação Corporativa ===")
    print("1. Executar novo processo de inovação")
    print("2. Visualizar resultados do último processo")
    print("3. Sair")
    return input("Escolha uma opção: ")


def main():
    while True:
        escolha = exibir_menu()
        if escolha == '1':
            executar_processo_inovacao()
        elif escolha == '2':
            visualizar_ultimo_resultado()
        elif escolha == '3':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
