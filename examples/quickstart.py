import asyncio
from agents import Agent, Runner
from openai_agent_capsolver import get_capsolver_tools


async def main() -> None:
    agent = Agent(name="Browser recovery agent", instructions="Use tools only for authorized work.", tools=get_capsolver_tools())
    print((await Runner.run(agent, "Check my CapSolver balance.")).final_output)


asyncio.run(main())
