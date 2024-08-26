import json
from datetime import datetime
import matplotlib.pyplot as plt
import os


def salvar_resultado(resultado, nome_arquivo=None):
    if nome_arquivo is None:
        nome_arquivo = f"resultado_inovacao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=4)

    print(f"Resultado salvo em: {nome_arquivo}")
    return nome_arquivo


def carregar_resultado(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def formatar_ideias(lista_ideias):
    return "\n".join([f"- {ideia}" for ideia in lista_ideias])


def gerar_grafico_avaliacoes(ideias_avaliadas):
    nomes = [ideia['nome'] for ideia in ideias_avaliadas[:5]]
    pontuacoes = [ideia['pontuacao'] for ideia in ideias_avaliadas[:5]]

    plt.figure(figsize=(10, 6))
    plt.bar(nomes, pontuacoes)
    plt.title("Top 5 Ideias Avaliadas")
    plt.xlabel("Ideias")
    plt.ylabel("Pontuação")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    nome_arquivo = f"grafico_avaliacoes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(nome_arquivo)
    print(f"Gráfico salvo em: {nome_arquivo}")
    return nome_arquivo


def calcular_metricas_inovacao(resultado):
    total_ideias = len(resultado.get('ideias_geradas', []))
    ideias_aprovadas = len([ideia for ideia in resultado.get('ideias_avaliadas', []) if ideia['pontuacao'] > 7])
    taxa_aprovacao = (ideias_aprovadas / total_ideias) * 100 if total_ideias > 0 else 0

    return {
        "total_ideias": total_ideias,
        "ideias_aprovadas": ideias_aprovadas,
        "taxa_aprovacao": taxa_aprovacao
    }


def gerar_markdown(resultado, nome_arquivo_grafico):
    markdown = f"""
# Relatório de Inovação Corporativa

Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Resumo

- Total de ideias geradas: {len(resultado.get('ideias_geradas', []))}
- Ideias aprovadas para prototipagem: {len([ideia for ideia in resultado.get('ideias_avaliadas', []) if ideia['pontuacao'] > 7])}

## Ideias Geradas

{formatar_ideias(resultado.get('ideias_geradas', []))}

## Top 5 Ideias Avaliadas

"""
    for i, ideia in enumerate(resultado.get('ideias_avaliadas', [])[:5], 1):
        markdown += f"{i}. **{ideia['nome']}** - Pontuação: {ideia['pontuacao']}\n   {ideia.get('descricao', 'Sem descrição disponível.')}\n\n"

    markdown += f"""
## Gráfico de Avaliações

![Gráfico de Avaliações das Top 5 Ideias]({nome_arquivo_grafico})

## Métricas de Inovação

- Taxa de aprovação: {calcular_metricas_inovacao(resultado)['taxa_aprovacao']:.2f}%

## Próximos Passos

1. Revisar as ideias top-ranking em detalhes
2. Iniciar o processo de prototipagem para as ideias selecionadas
3. Preparar apresentações para stakeholders
4. Definir cronograma de implementação

"""
    return markdown


def salvar_markdown(conteudo, nome_arquivo=None):
    if nome_arquivo is None:
        nome_arquivo = f"relatorio_inovacao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

    print(f"Relatório Markdown salvo em: {nome_arquivo}")
    return nome_arquivo


def obter_ultimo_resultado():
    arquivos = [f for f in os.listdir('.') if f.startswith('resultado_inovacao_') and f.endswith('.json')]
    if not arquivos:
        return None
    return max(arquivos)