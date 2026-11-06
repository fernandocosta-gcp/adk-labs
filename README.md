# ADK Labs Monorepo
## by @fernandocosta

## Pre-Req

### (For Linux)
Install venv first if you haven't:
sudo apt install python3.11-venv

Create a new venv:
VENV_PATH=~/venvs/adk-quickstart
command -v deactivate >/dev/null 2>&1 && deactivate
rm -rf $VENV_PATH \
    && python3.11 -m venv $VENV_PATH \
    && source $VENV_PATH/bin/activate
pip install google-adk


### (For Mac)
VENV_PATH=~/venvs/adk-quickstart
command -v deactivate >/dev/null 2>&1 && deactivate
rm -rf $VENV_PATH \
    && python3.11 -m venv $VENV_PATH \
    && source $VENV_PATH/bin/activate
pip install google-adk

## Monorepo detail
This repository contains multiple ADK lab projects:
- `lab011/`: Quickstart project and basic agent.
- `lab022/`: Multiagent, parent agents, pair agent and subagent concepts.
- `lab033/`: Sequential Agent pattern
- `lab044/`: Loop Agent pattern
- `lab055/`: Parallel Agent pattern
- `lab066/`: Hybrid approach (from previous pattern)
- `lab077/`: HITL (Human in the Loop)
- `lab088/`: WebRAG
- `lab099/`: Multi-agent offer intelligence pipeline
- `lab100/`: SequentialAgent + WebRAG
- `lab101/`: Bypass Tools Limit + WebRAG + Context State

## Performance alert
### Performance Alert: System instructions were modified between consecutive turns in this session. This change breaks context cache alignment, resulting in a cache miss that increases generation latency for subsequent requests.

Modern LLM infrastructures (such as Gemini's context caching) optimize generation latency and cost through prefix caching (KV caching).

When an API request is evaluated, the token sequence follows a structured prefix:

...
[System Instructions] -> [Tool Declarations] -> [Turn 1 History] -> [Turn 2 History] -> ... -> [Current User Prompt]
...

Cache Hit: If the initial prefix (system instructions, tool declarations, and prior turns) remains bit-for-bit identical to earlier calls, the model reuses pre-computed Key-Value (KV) attention states. This drastically lowers Time to First Token (TTFT) and generation latency.

Cache Miss: If anything in that prefix is altered—especially the system_instruction at the very start—the entire downstream cache is invalidated. The engine must re-tokenize and re-evaluate every token from the beginning.


### Root Causes in ADK Development
- Unintentional Dynamic Modifications (Single Agent)
- Multi-Agent Workflows (Known Dev UI False Positive)

### Best Practices
- Keep system_instruction static and constant throughout the agent lifecycle.
- Put dynamic runtime data (user variables, session context, retrieval data) into the user message, tool responses, or session state / memory rather than changing the system prompt.
- Register all supported tools statically in a fixed order, and rely on tool choice settings or instructions to guide usage.
- Filter, sanitize, and summarize tool return payloads before passing them back as FunctionResponse.
- Implement sliding-window history retention or configure memory summarization checkpoints for long-running sessions.
- Set explicit iteration limits, validate routing preconditions, and define deterministic termination conditions.
