from fastmcp import FastMCP


mcp = FastMCP("mcp-think-as")


def think_as_architect(thought: str) -> str:
    """Use the tool to think about something. It will not obtain new information or make any changes to the repository, but just log the thought.

    You are an analytical thinking assistant designed to help users explore complex topics. When a user shares their thoughts, your role is to:
    1. Break down the problem into clear, manageable components
    2. Provide valuable context that enriches their understanding
    3. Identify connections or implications they may have missed
    4. Ask thoughtful questions that deepen their analysis
    5. Suggest alternative perspectives when appropriate

    Your goal is not to solve problems for users, but to enhance their thinking process by offering structured analysis and relevant insights. Respond in a clear, thoughtful manner that respects the user's level of expertise while adding substantive value to their exploration.

    Args:
        thought (str): "A thought to think about."
    """

    return thought


def think_as_coder(thought: str) -> str:
    """Use the tool to think about something. It will not obtain new information or make any changes to the repository, but just log the thought. Use it when complex reasoning or brainstorming is needed. For example, if you explore the repo and discover the source of a bug, call this tool to brainstorm several unique ways of fixing the bug, and assess which change(s) are likely to be simplest and most effective. Alternatively, if you receive some test results, call this tool to brainstorm ways to fix the failing tests.

    Before taking any action or responding to the user after receiving tool results, use the think tool as a scratchpad to:
    - List the specific rules that apply to the current request
    - Check if all required information is collected
    - Verify that the planned action complies with all policies
    - Iterate over tool results for correctness

    Args:
        thought (str): "A thought to think about."
    """
    return thought


def main():
    mcp.tool()(think_as_architect)
    mcp.tool()(think_as_coder)
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
