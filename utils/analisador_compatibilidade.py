import json
from typing import Dict, List, Tuple
import re


class AnalisadorCompatibilidadeAvancado:
    def __init__(self):
        self.tecnologias_existentes = {
            "Sistemas Operacionais": ["Windows Server 2016", "Linux CentOS 7", "Ubuntu 18.04 LTS"],
            "Bancos de Dados": ["Oracle 12c", "MySQL 5.7", "Microsoft SQL Server 2017"],
            "Linguagens de Programação": ["Java 8", "Python 3.6", "C# .NET Framework 4.7"],
            "Frameworks Web": ["Spring Boot 2.1", "Django 2.2", "ASP.NET MVC 5"],
            "Servidores de Aplicação": ["Tomcat 8.5", "Nginx 1.14", "IIS 10"],
            "Protocolos de Comunicação": ["REST", "SOAP", "gRPC"],
            "Sistemas de Mensageria": ["RabbitMQ 3.7", "Apache Kafka 2.1"],
            "Contêineres e Orquestração": ["Docker 18.09", "Kubernetes 1.13"],
            "Monitoramento": ["Nagios", "Prometheus", "ELK Stack"]
        }
        self.regras_compatibilidade = self._definir_regras_compatibilidade()

    def _definir_regras_compatibilidade(self) -> Dict:
        return {
            "Sistemas Operacionais": self._compatibilidade_so,
            "Bancos de Dados": self._compatibilidade_bd,
            "Linguagens de Programação": self._compatibilidade_linguagem,
            "Frameworks Web": self._compatibilidade_framework,
            "Servidores de Aplicação": self._compatibilidade_servidor,
            "Protocolos de Comunicação": self._compatibilidade_protocolo,
            "Sistemas de Mensageria": self._compatibilidade_mensageria,
            "Contêineres e Orquestração": self._compatibilidade_container,
            "Monitoramento": self._compatibilidade_monitoramento
        }

    def analisar_compatibilidade(self, nova_tecnologia: Dict[str, str]) -> Dict:
        resultado = {
            "tecnologia": nova_tecnologia['nome'],
            "compatibilidade_geral": 0,
            "analises": {},
            "recomendacoes": []
        }

        for categoria, tecnologias in self.tecnologias_existentes.items():
            compatibilidade, detalhes = self.regras_compatibilidade[categoria](nova_tecnologia, tecnologias)
            resultado["analises"][categoria] = {
                "compatibilidade": compatibilidade,
                "detalhes": detalhes
            }
            resultado["compatibilidade_geral"] += compatibilidade

        resultado["compatibilidade_geral"] /= len(self.tecnologias_existentes)
        resultado["recomendacoes"] = self._gerar_recomendacoes(resultado["analises"], nova_tecnologia)

        return resultado

    def _compatibilidade_so(self, nova_tecnologia: Dict[str, str], sistemas_existentes: List[str]) -> Tuple[float, str]:
        compatibilidade = 0
        detalhes = ""

        if "Linux" in nova_tecnologia['requisitos']:
            compatibilidade = sum('Linux' in so or 'Ubuntu' in so for so in sistemas_existentes) / len(
                sistemas_existentes)
            detalhes = "Compatível com sistemas Linux existentes. "
        elif "Windows" in nova_tecnologia['requisitos']:
            compatibilidade = sum('Windows' in so for so in sistemas_existentes) / len(sistemas_existentes)
            detalhes = "Compatível com sistemas Windows existentes. "
        else:
            compatibilidade = 0.5
            detalhes = "Compatibilidade parcial ou não especificada com os sistemas operacionais existentes. "

        return compatibilidade, detalhes

    def _compatibilidade_bd(self, nova_tecnologia: Dict[str, str], bds_existentes: List[str]) -> Tuple[float, str]:
        compatibilidade = 0
        detalhes = ""

        for bd in bds_existentes:
            if bd.lower() in nova_tecnologia['requisitos'].lower():
                compatibilidade = 1
                detalhes = f"Altamente compatível com {bd}. "
                break

        if compatibilidade == 0:
            compatibilidade = 0.3
            detalhes = "Pode requerer adaptação ou camada de abstração para integração com os bancos de dados existentes. "

        return compatibilidade, detalhes

    def _compatibilidade_linguagem(self, nova_tecnologia: Dict[str, str], linguagens_existentes: List[str]) -> Tuple[
        float, str]:
        compatibilidade = 0
        detalhes = ""

        for linguagem in linguagens_existentes:
            if linguagem.split()[0].lower() in nova_tecnologia['requisitos'].lower():
                versao_existente = re.search(r'\d+(\.\d+)*', linguagem)
                versao_requerida = re.search(r'\d+(\.\d+)*', nova_tecnologia['requisitos'])

                if versao_existente and versao_requerida:
                    if float(versao_existente.group()) >= float(versao_requerida.group()):
                        compatibilidade = 1
                        detalhes = f"Compatível com a versão existente de {linguagem}. "
                    else:
                        compatibilidade = 0.7
                        detalhes = f"Requer atualização da versão de {linguagem}. "
                break

        if compatibilidade == 0:
            compatibilidade = 0.2
            detalhes = "Incompatível com as linguagens de programação existentes. Pode requerer adição de nova linguagem ao ambiente. "

        return compatibilidade, detalhes

    def _compatibilidade_framework(self, nova_tecnologia: Dict[str, str], frameworks_existentes: List[str]) -> Tuple[
        float, str]:
        compatibilidade = 0
        detalhes = ""

        for framework in frameworks_existentes:
            if framework.lower().split()[0] in nova_tecnologia['nome'].lower():
                compatibilidade = 0.8
                detalhes = f"Baseado em framework similar ao existente ({framework}). Provável boa integração. "
                break

        if compatibilidade == 0:
            compatibilidade = 0.4
            detalhes = "Framework diferente dos existentes. Pode requerer treinamento da equipe e ajustes na arquitetura. "

        return compatibilidade, detalhes

    def _compatibilidade_servidor(self, nova_tecnologia: Dict[str, str], servidores_existentes: List[str]) -> Tuple[
        float, str]:
        compatibilidade = 0
        detalhes = ""

        for servidor in servidores_existentes:
            if servidor.lower().split()[0] in nova_tecnologia['requisitos'].lower():
                compatibilidade = 0.9
                detalhes = f"Compatível com o servidor de aplicação existente ({servidor}). "
                break

        if compatibilidade == 0:
            compatibilidade = 0.5
            detalhes = "Pode requerer configuração de novo servidor de aplicação ou adaptação dos existentes. "

        return compatibilidade, detalhes

    def _compatibilidade_protocolo(self, nova_tecnologia: Dict[str, str], protocolos_existentes: List[str]) -> Tuple[
        float, str]:
        compatibilidade = 0
        detalhes = ""

        for protocolo in protocolos_existentes:
            if protocolo.lower() in nova_tecnologia['requisitos'].lower():
                compatibilidade = 1
                detalhes = f"Utiliza protocolo de comunicação existente ({protocolo}). "
                break

        if compatibilidade == 0:
            compatibilidade = 0.6
            detalhes = "Pode requerer implementação de novo protocolo de comunicação. Verificar impacto na arquitetura existente. "

        return compatibilidade, detalhes

    def _compatibilidade_mensageria(self, nova_tecnologia: Dict[str, str], sistemas_mensageria: List[str]) -> Tuple[
        float, str]:
        compatibilidade = 0
        detalhes = ""

        for sistema in sistemas_mensageria:
            if sistema.lower().split()[0] in nova_tecnologia['requisitos'].lower():
                compatibilidade = 0.9
                detalhes = f"Compatível com o sistema de mensageria existente ({sistema}). "
                break

        if compatibilidade == 0:
            compatibilidade = 0.4
            detalhes = "Pode requerer implementação de novo sistema de mensageria ou adaptador para os sistemas existentes. "

        return compatibilidade, detalhes

    def _compatibilidade_container(self, nova_tecnologia: Dict[str, str], containers_existentes: List[str]) -> Tuple[
        float, str]:
        compatibilidade = 0
        detalhes = ""

        if "Docker" in nova_tecnologia['requisitos']:
            compatibilidade = 0.8
            detalhes = "Compatível com a infraestrutura de contêineres existente. "
        elif "Kubernetes" in nova_tecnologia['requisitos']:
            compatibilidade = 0.9
            detalhes = "Altamente compatível com o ambiente de orquestração existente. "
        else:
            compatibilidade = 0.5
            detalhes = "Pode requerer ajustes na infraestrutura de contêineres ou criação de novos ambientes isolados. "

        return compatibilidade, detalhes

    def _compatibilidade_monitoramento(self, nova_tecnologia: Dict[str, str], ferramentas_monitoramento: List[str]) -> \
            Tuple[float, str]:
        compatibilidade = 0
        detalhes = ""

        for ferramenta in ferramentas_monitoramento:
            if ferramenta.lower() in nova_tecnologia['requisitos'].lower():
                compatibilidade = 1
                detalhes = f"Compatível com a ferramenta de monitoramento existente ({ferramenta}). "
                break

        if compatibilidade == 0:
            compatibilidade = 0.7
            detalhes = "Pode requerer configuração adicional nas ferramentas de monitoramento existentes ou implementação de novos agentes de monitoramento. "

        return compatibilidade, detalhes

    def _gerar_recomendacoes(self, analises: Dict[str, Dict], nova_tecnologia: Dict[str, str]) -> List[str]:
        recomendacoes = []
        for categoria, analise in analises.items():
            if analise['compatibilidade'] < 0.5:
                recomendacoes.append(f"Atenção crítica necessária para {categoria}. {analise['detalhes']}")
            elif analise['compatibilidade'] < 0.8:
                recomendacoes.append(f"Considere ajustes em {categoria}. {analise['detalhes']}")

        if not recomendacoes:
            recomendacoes.append(
                f"A {nova_tecnologia['nome']} parece ser altamente compatível com os sistemas existentes. Prossiga com a integração, monitorando de perto durante as fases iniciais.")

        return recomendacoes


def analisar_compatibilidade_sistemas(nova_tecnologia_json: str) -> str:
    try:
        nova_tecnologia = json.loads(nova_tecnologia_json)
        analisador = AnalisadorCompatibilidadeAvancado()
        resultado = analisador.analisar_compatibilidade(nova_tecnologia)
        return json.dumps(resultado, indent=2)
    except json.JSONDecodeError:
        return json.dumps({"erro": "Formato JSON inválido para a nova tecnologia."})
    except KeyError as e:
        return json.dumps({"erro": f"Chave obrigatória ausente na descrição da nova tecnologia: {str(e)}"})
    except Exception as e:
        return json.dumps({"erro": f"Erro ao analisar compatibilidade: {str(e)}"})
