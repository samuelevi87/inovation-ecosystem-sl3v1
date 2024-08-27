import json
import spacy
from typing import Dict, List
from textblob import TextBlob


class AnalisadorImpactoEtico:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.criterios = {
            "Privacidade e Proteção de Dados": {
                "palavras_chave": ["privacidade", "dados pessoais", "confidencialidade", "criptografia",
                                   "consentimento", "GDPR"],
                "palavras_negativas": ["violação", "exposição", "venda de dados", "rastreamento não autorizado"]
            },
            "Transparência e Explicabilidade": {
                "palavras_chave": ["transparência", "explicável", "auditável", "compreensível", "código aberto"],
                "palavras_negativas": ["caixa preta", "opaco", "inexplicável", "secreto"]
            },
            "Justiça e Não-Discriminação": {
                "palavras_chave": ["equidade", "imparcialidade", "inclusão", "diversidade",
                                   "igualdade de oportunidades"],
                "palavras_negativas": ["viés", "discriminação", "preconceito", "exclusão", "desigualdade"]
            },
            "Segurança e Confiabilidade": {
                "palavras_chave": ["segurança", "confiável", "robusto", "resiliente", "testado", "validado"],
                "palavras_negativas": ["vulnerável", "instável", "falha", "risco", "ameaça"]
            },
            "Sustentabilidade Ambiental": {
                "palavras_chave": ["sustentável", "eco-friendly", "eficiência energética", "reciclável",
                                   "carbono neutro"],
                "palavras_negativas": ["poluente", "desperdício", "alto consumo de energia", "não reciclável"]
            },
            "Impacto Social": {
                "palavras_chave": ["benefício social", "comunidade", "bem-estar", "qualidade de vida", "empoderamento"],
                "palavras_negativas": ["dano social", "desemprego", "desigualdade", "divisão social"]
            },
            "Autonomia e Liberdade de Escolha": {
                "palavras_chave": ["autonomia", "liberdade de escolha", "controle do usuário", "personalização"],
                "palavras_negativas": ["manipulação", "coerção", "limitação de escolhas", "dependência"]
            },
            "Responsabilidade e Prestação de Contas": {
                "palavras_chave": ["responsabilidade", "prestação de contas", "governança", "auditoria",
                                   "monitoramento"],
                "palavras_negativas": ["irresponsável", "falta de supervisão", "não rastreável",
                                       "sem responsabilização"]
            }
        }

    def analisar(self, ideia: str) -> Dict:
        resultado = {
            "ideia": ideia,
            "pontuacao_geral": 0,
            "avaliacoes": {},
            "recomendacoes": []
        }

        for criterio, palavras in self.criterios.items():
            pontuacao = self._avaliar_criterio(ideia, criterio, palavras)
            resultado["avaliacoes"][criterio] = pontuacao
            resultado["pontuacao_geral"] += pontuacao

        resultado["pontuacao_geral"] /= len(self.criterios)
        resultado["recomendacoes"] = self._gerar_recomendacoes(resultado["avaliacoes"])

        return resultado

    def _avaliar_criterio(self, ideia: str, criterio: str, palavras: Dict[str, List[str]]) -> float:
        doc = self.nlp(ideia.lower())
        palavras_chave = palavras["palavras_chave"]
        palavras_negativas = palavras["palavras_negativas"]

        # Contagem de palavras-chave e negativas
        contagem_positiva = sum(1 for palavra in palavras_chave if any(token.text == palavra.lower() for token in doc))
        contagem_negativa = sum(
            1 for palavra in palavras_negativas if any(token.text == palavra.lower() for token in doc))

        # Análise de contexto
        contexto_positivo = self._analisar_contexto(doc, palavras_chave)
        contexto_negativo = self._analisar_contexto(doc, palavras_negativas)

        # Análise de sentimento
        sentimento = TextBlob(ideia).sentiment.polarity

        # Cálculo da pontuação
        pontuacao_base = (contagem_positiva - contagem_negativa) / max(len(palavras_chave), len(palavras_negativas))
        pontuacao_contexto = (contexto_positivo - contexto_negativo) / 2
        pontuacao_final = (pontuacao_base + pontuacao_contexto + sentimento) / 3

        # Normalizar para escala de 1 a 5
        pontuacao_normalizada = max(1, min(5, (pontuacao_final + 1) * 2.5))

        return round(pontuacao_normalizada, 2)

    def _analisar_contexto(self, doc, palavras_alvo: List[str]) -> float:
        pontuacao_contexto = 0
        for palavra in palavras_alvo:
            for token in doc:
                if token.text == palavra.lower():
                    # Verifica o contexto (palavras ao redor)
                    contexto = [t for t in token.subtree if t.dep_ in ['amod', 'advmod', 'compound']]
                    pontuacao_contexto += sum(1 for _ in contexto) / len(contexto) if contexto else 0
        return pontuacao_contexto / len(palavras_alvo) if palavras_alvo else 0

    def _gerar_recomendacoes(self, avaliacoes: Dict[str, float]) -> List[str]:
        recomendacoes = []
        for criterio, pontuacao in avaliacoes.items():
            if pontuacao < 3:
                recomendacoes.append(
                    f"Melhoria crítica necessária em {criterio}. Considere redesenhar aspectos da ideia relacionados a este critério.")
            elif pontuacao < 4:
                recomendacoes.append(
                    f"Atenção requerida em {criterio}. Explore maneiras de fortalecer este aspecto na sua inovação.")
            elif pontuacao > 4.5:
                recomendacoes.append(
                    f"Excelente desempenho em {criterio}. Considere compartilhar esta abordagem como melhor prática.")
        return recomendacoes


def analisar_impacto_etico(ideia: str) -> str:
    analisador = AnalisadorImpactoEtico()
    resultado = analisador.analisar(ideia)
    return json.dumps(resultado, indent=2)