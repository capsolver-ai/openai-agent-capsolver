from __future__ import annotations

import json

from agents import FunctionTool, function_tool
from capsolver_agent.schema import create_executor


def get_capsolver_tools(api_key: str | None = None) -> list[FunctionTool]:
    executor = create_executor(api_key=api_key)

    @function_tool
    async def solve_captcha(captcha_type: str, website_url: str, website_key: str) -> str:
        """Solve a CAPTCHA for a user-authorized workflow and return the structured result."""
        return json.dumps(await executor.execute("solve_captcha", {
            "captcha_type": captcha_type, "website_url": website_url, "website_key": website_key,
        }))

    @function_tool
    async def get_capsolver_balance() -> str:
        """Return the current CapSolver balance."""
        return json.dumps(await executor.execute("get_balance", {}))

    return [solve_captcha, get_capsolver_balance]

__version__ = "0.1.0"
