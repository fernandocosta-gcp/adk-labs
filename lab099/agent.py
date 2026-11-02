from typing import List, Optional
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search
from pydantic import BaseModel, Field

MODEL_FAST = "gemini-3.5-flash"


class OfertaProduto(BaseModel):
  titulo: str = Field(description="Nome completo do anúncio do produto.")
  preco_a_vista: float = Field(
      description="Preço final à vista encontrado em Reais (BRL)."
  )
  preco_parcelado: Optional[float] = Field(
      None, description="Valor total parcelado, se houver."
  )
  parcelas: Optional[int] = Field(
      None, description="Número máximo de parcelas sem juros."
  )
  vendedor: str = Field(
      description="Nome da loja oficial ou vendedor no Mercado Livre."
  )
  reputacao_confiavel: bool = Field(
      description="True se for Loja Oficial, MercadoLíder Platinum/Gold."
  )
  envio_full: bool = Field(
      description="True se o envio for Mercado Livre Full (entrega rápida)."
  )
  link_anuncio: str = Field(description="URL direta do anúncio encontrado.")


class CatalogoOfertas(BaseModel):
  termo_buscado: str = Field(description="Termo ou produto pesquisado.")
  ofertas: List[OfertaProduto] = Field(
      description="Lista contendo de 3 a 5 ofertas estruturadas."
  )

coletor_mercado_livre = Agent(
    name="coletor_marketplace_agent",
    model=MODEL_FAST,
    instruction=(
        "Você é um pesquisador focado no domínio mercadolivre.com.br.\n"
        "1. Utilize o google_search para encontrar de 3 a 5 ofertas reais do"
        " produto solicitado.\n"
        "2. Colete todos os detalhes: título, preço à vista, preço parcelado,"
        " reputação do vendedor, frete Full e link.\n"
        "3. Ignore acessórios irrelevantes e liste os dados detalhados em texto."
    ),
    tools=[google_search],
    output_key="dados_brutos_pesquisa",
)

estruturador_catalogo = Agent(
    name="extrator_catalogo_agent",
    model=MODEL_FAST,
    instruction=(
        "Você é um formatador de dados.\n"
        "Converta as informações de ofertas encontradas em"
        " {dados_brutos_pesquisa} para a estrutura exata do catálogo."
    ),
    output_schema=CatalogoOfertas,
    output_key="catalogo_estruturado",
)

analista_pricing = Agent(
    name="pricing_analyst_agent",
    model=MODEL_FAST,
    instruction=(
        "Você é um analista sênior de pricing e inteligência competitiva de"
        " varejo.\n"
        "Analise o catálogo recebido em: {catalogo_estruturado}.\n"
        "Tarefas obrigatórias:\n"
        "- Identifique a oferta com o menor preço absoluto.\n"
        "- Identifique a oferta de Melhor Custo-Benefício (ponderando reputação"
        " confiável + Envio Full).\n"
        "- Aponte potenciais riscos (ex: preços suspeitosamente abaixo da média"
        " ou vendedores sem histórico).\n"
        "- Calcule a dispersão de preços entre o menor e o maior valor"
        " encontrado."
    ),
    output_key="relatorio_analitico",
)

consultor_ecommerce = Agent(
    name="advisor_agent",
    model=MODEL_FAST,
    instruction=(
        "Você é um consultor executivo de compras digitais.\n"
        "Com base na análise técnica em {relatorio_analitico} e nos dados de"
        " {catalogo_estruturado}, gere uma recomendação de compra executiva"
        " contendo:\n"
        "1. Tabela comparativa dos produtos elegíveis.\n"
        "2. O 'Veredito de Compra' claro (Qual comprar à vista e qual comprar"
        " parcelado).\n"
        "3. Alertas de segurança ou dicas de envio (ex: priorizar Full para"
        " garantia de prazo)."
    ),
)

root_agent = SequentialAgent(
    name="ecommerce_intelligence_pipeline",
    sub_agents=[
        coletor_mercado_livre,
        estruturador_catalogo,
        analista_pricing,
        consultor_ecommerce,
    ],
)
