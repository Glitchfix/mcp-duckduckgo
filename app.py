from fastmcp import FastMCP
from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

mcp = FastMCP("DuckDuckGo MCP Server")

@mcp.tool()
def duckduckgo_search(query: str, max_results: int = 5) -> list:
    """
    Perform a DuckDuckGo search and return a list of results.
    Each result includes the title, snippet, and URL.
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title"),
                "snippet": r.get("body"),
                "url": r.get("href")
            })
    return results

@mcp.tool()
def fetch_page_content(url: str) -> str:
    """
    Fetch and return the textual content of the specified URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract text from paragraphs
        paragraphs = soup.find_all("p")
        text_content = "\n".join(p.get_text() for p in paragraphs if p.get_text())
        return text_content.strip()
    except Exception as e:
        return f"Error fetching content from {url}: {e}"

if __name__ == "__main__":
    mcp.run()
