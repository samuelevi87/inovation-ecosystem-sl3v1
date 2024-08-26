import json
from datetime import datetime
import matplotlib.pyplot as plt


def salvar_resultado(resultado, nome_arquivo=None):
    if nome_arquivo is None:
        nome_arquivo = f"resultado_inovacao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=4)

    print(f"Resultado salvo em: {nome_arquivo}")


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


def calcular_metricas_inovacao(resultado):
    total_ideias = len(resultado.get('ideias_geradas', []))
    ideias_aprovadas = len([ideia for ideia in resultado.get('ideias_avaliadas', []) if ideia['pontuacao'] > 7])
    taxa_aprovacao = (ideias_aprovadas / total_ideias) * 100 if total_ideias > 0 else 0

    return {
        "total_ideias": total_ideias,
        "ideias_aprovadas": ideias_aprovadas,
        "taxa_aprovacao": taxa_aprovacao
    }
