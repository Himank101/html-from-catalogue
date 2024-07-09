from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain.tools import tool

class ReadExcelTool():
    @tool("load excel")
    def excel_read_tool(filepath):
        """Useful to write content to a file with the given filename."""
        
        loader = UnstructuredExcelLoader(filepath, mode="elements")
        docs = loader.load()
        return docs + f"\n file has been read at {filepath}"


