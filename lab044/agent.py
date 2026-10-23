from google.adk.agents import Agent, LoopAgent
from google.adk.tools.tool_context import ToolContext


MODEL='gemini-3.5-flash'


def aprovar_texto(tool_context: ToolContext) -> dict:
    """Chame esta função somente quando o texto estiver aprovado e não precisar de mais ajustes."""
    tool_context.actions.escalate = True  # encerra o loop
    return {'status': 'aprovado'}

escritor = Agent(
    name = "escritor",
    model = MODEL,
    instruction = (
        'Escreva um paragrafo sobre o tema informado pelo usuario'
        'Se houver texto anterior ({texto?) e critica ({critica?}),'
        'reescreva incoporando as melhorias solicitadas e sugeridas'  
    ),
    output_key='texto',
)

critico = Agent(
    name = 'critico',
    model = MODEL,
    instruction = (
        "Avalie o texto gerado: {texto} com base nos critérios de clareza, objetividade e gramática.\n"
        "Seu comportamento de aprovação depende estritamente do número de tentativas restantes:\n"
        "\n"
        "1. Se estivermos na primeira ou segunda iteração: Seja EXTREMAMENTE exigente. "
        "Não chame a ferramenta 'aprovar_texto' a menos que o texto esteja impecável e perfeito. "
        "Se houver qualquer detalhe a melhorar, forneça 3 sugestões de melhoria.\n"
        "\n"
        "2. Se estivermos na terceira iteração (iteração final): Sua prioridade máxima é encerrar o ciclo. "
        "Seja extremamente tolerante, traduza ao espanhol argentino e chame OBRIGATORIAMENTE a ferramenta 'aprovar_texto' "
        "para consolidar a versão atual, mesmo que ainda restem pequenas melhorias pendentes."
    ),
    output_key='critica',
    tools=[aprovar_texto],
)


root_agent = LoopAgent(
    name='refinamento',
    sub_agents=[escritor, critico],
    max_iterations=3,
)
