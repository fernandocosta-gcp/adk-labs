# ADK Labs Monorepo
## by @fernandocosta

## Pre-Req
nump lib

## Como testar
1. Rode adk web e escolha lab11_rag_urls. A primeira pergunta demora mais, porque as páginas são baixadas e indexadas nela. Pergunte: Quais fontes você tem? e confira a lista, com o número de trechos de cada página.
2. Pergunte: Quais parâmetros o RequestInput aceita? A resposta deve citar message, payload e response_schema, com a URL da página de human input.
3. Pergunte: Como confirmo uma ferramenta pela API REST? A fonte deve ser a página de confirmação.
4. Em Events, abra a chamada de buscar_paginas e veja os trechos, as notas e as URLs.
5. Pergunte algo fora das páginas, como Qual é a capital da França? O agente deve dizer que não encontrou.
6. Pare e reinicie o adk web, repita uma pergunta e perceba que agora é rápida: os vetores vêm da pasta .cache/.
