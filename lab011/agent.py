from google.adk.agents.llm_agent import Agent
from datetime import datetime
from zoneinfo import ZoneInfo

def get_hora_cidade(cidade: str) -> dict:
    """retorna a hora atual de uma cidade suportada
    Args
     cidade: nome da cidade
    """
    fusos = {
        'são paulo': "America/Sao_Paulo",
        'tóquio': "Asia/Tokyo",
    }

    fuso = fusos.get(cidade.lower())
    if not fuso:
        return {'status': 'error', 'mensagem': 'cidade nao suportada'} 
    agora = datetime.now(ZoneInfo(fuso)).strftime('%H:%M')
    return {'status': 'ok', 'cidade': cidade, 'hora': agora} 

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='El horario de una ciudad',
    instruction='voce é um agente de consolidadcao de horarios e deve usar uma ferramenta get_hora_cidade. Se a cidade nao for suportada, explique ao usuario',
    tools=[get_hora_cidade],
)
