from typing import Generator, Any
import httpx
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ProductHuntTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        try:
            url = "https://api.rss2json.com/v1/api.json?rss_url=https://www.producthunt.com/feed"
            response = httpx.get(url, timeout=10)
            data = response.json()
            
            products = []
            for item in data.get("items", [])[:3]:
                products.append({
                    "title": item.get("title"),
                    "description": item.get("description"),
                    "url": item.get("link")
                })

            yield self.create_text_message("Here are the top trending Product Hunt launches today:")
            for product in products:
                yield self.create_text_message(f"\n{product['title']}\n{product['description']}\n{product['url']}")
        except Exception as e:
            yield self.create_text_message(f"Failed to fetch Product Hunt data: {str(e)}")
