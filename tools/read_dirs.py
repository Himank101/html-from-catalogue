from langchain.tools import tool
import os

class DirReadTool():
    @tool("Create directory")
    def dir_read_tool(directory_path):
        """Useful to list files and directories with the given path."""
        return os.listdir()
