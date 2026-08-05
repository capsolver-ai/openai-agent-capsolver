# OpenAI Agents SDK + CapSolver Agent examples

[![Demo repository](https://img.shields.io/badge/type-runnable%20demo-0A7BBB)](#repository-scope)
[![CI](https://github.com/capsolver-ai/openai-agent-capsolver/actions/workflows/ci.yml/badge.svg)](https://github.com/capsolver-ai/openai-agent-capsolver/actions/workflows/ci.yml)
[![License: ISC](https://img.shields.io/badge/license-ISC-green.svg)](LICENSE)

Runnable OpenAI Agents SDK examples using the official [`capsolver-agent`](https://github.com/capsolver-ai/capsolver-agent) executor.

> Examples only: this repository does not publish an additional Python library.

## Repository scope

The demo uses OpenAI Agents SDK function tools as a thin framework boundary. Tool execution, schemas, supported CAPTCHA types, retries, and errors remain centralized in CapSolver Agent and Core.

## Quick start

```bash
git clone https://github.com/capsolver-ai/openai-agent-capsolver.git
cd openai-agent-capsolver
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Export [`.env.example`](.env.example) values, then run `python examples/quickstart.py`.

## Key integration code

```python
from agents import Agent, function_tool
from capsolver_agent import create_executor

capsolver = create_executor()

@function_tool
async def get_capsolver_balance() -> str:
    return str(await capsolver.execute("get_balance", {}))

agent = Agent(name="CapSolver demo", tools=[get_capsolver_balance])
```

See [`examples/quickstart.py`](examples/quickstart.py) for the complete runner flow and a solve tool.

## Project layout

```text
examples/quickstart.py   OpenAI agent, runner, and function tools
requirements.txt         Shared SDK repositories plus openai-agents
tests/test_demo.py        Offline validation
.github/workflows/ci.yml  Demo checks
```

## Documentation

- [CapSolver Agent tools](https://docs.capsolver.com/en/guide/ai/agent-tools/)
- [CapSolver for AI agents](https://docs.capsolver.com/en/guide/ai/capsolver-for-ai-agents/)
- [OpenAI Agents SDK tools](https://openai.github.io/openai-agents-python/tools/)
- [Running OpenAI agents](https://openai.github.io/openai-agents-python/running_agents/)

## Responsible use

Use the example only for lawful, user-authorized workflows that respect target-site terms. Never commit API keys or private target data.

## Contributing, support, and license

See [CONTRIBUTING.md](CONTRIBUTING.md), [SUPPORT.md](SUPPORT.md), and [SECURITY.md](SECURITY.md). Licensed under the [ISC License](LICENSE).

OpenAI and the OpenAI Agents SDK are third-party to this repository. This project is maintained by CapSolver and is not affiliated with or endorsed by OpenAI.
