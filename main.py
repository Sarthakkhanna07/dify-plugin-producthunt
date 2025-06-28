# Entry point for the Dify plugin. Main logic for trending Product Hunt products is implemented in tools/product_hunt.py.

from dify_plugin import Plugin, DifyPluginEnv

plugin = Plugin(DifyPluginEnv(MAX_REQUEST_TIMEOUT=120))

if __name__ == '__main__':
    plugin.run()
