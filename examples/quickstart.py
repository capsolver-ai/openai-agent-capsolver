"""Expose CapSolver Agent execution as OpenAI Agents SDK function tools."""

import asyncio
import json
import os

from agents import Agent, Runner, function_tool
from capsolver_agent import create_executor


capsolver = create_executor()


@function_tool
async def get_capsolver_balance() -> str:
    """Return the current CapSolver account balance."""
    return json.dumps(await capsolver.execute("get_balance", {}), ensure_ascii=False)


@function_tool
async def solve_captcha(captcha_type: str, website_url: str, website_key: str) -> str:
    """Solve a supported CAPTCHA for a lawful, user-authorized workflow."""
    result = await capsolver.execute(
        "solve_captcha",
        {
            "captcha_type": captcha_type,
            "website_url": website_url,
            "website_key": website_key,
        },
    )
    return json.dumps(result, ensure_ascii=False)


async def main() -> None:
    agent = Agent(
        name="CapSolver demo",
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        instructions=(
            "Use CapSolver only for lawful, user-authorized workflows. "
            "Never invent target details."
        ),
        tools=[get_capsolver_balance, solve_captcha],
    )
    result = await Runner.run(
        agent,
        os.getenv("DEMO_PROMPT", "Check my CapSolver balance and summarize the result."),
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
