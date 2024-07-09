import warnings
warnings.filterwarnings("ignore")

import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
# from .key import OPENAI_API_KEY
 
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks
from crewai_tools import  FileReadTool
from tools.f_write import FileWriteTool
from tools.dir_write import DirWriteTool
from tools.excel import ReadExcelTool
from tools.read_dirs import DirReadTool
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()
file_read_tool = FileReadTool()
file_write_tool = FileWriteTool.file_write_tool
dir_write_tool = DirWriteTool.dir_write_tool
extractor_tool = ReadExcelTool.excel_read_tool
listdir_tool = DirReadTool.dir_read_tool

# Tools
architect_tools = [search_tool, file_read_tool, extractor_tool]
extractor_tools = [file_read_tool, file_write_tool, dir_write_tool, extractor_tool, listdir_tool]
programmer_tools = [file_read_tool, file_write_tool, dir_write_tool, listdir_tool]
reviewer_tools = [file_read_tool, file_write_tool, dir_write_tool, listdir_tool]

# os.environ["OPENAI_API_KEY"] = ""


class CustomCrew:
    def __init__(self, user_input):
        self.user_input = user_input
    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        # Agents
        architect_agent = agents.architect_agent(architect_tools)
        extractor_agent = agents.extractor_agent(extractor_tools)
        programmer_agent = agents.programmer_agent(programmer_tools)
        reviewer_agent = agents.reviewer_agent(reviewer_tools)

        # Tasks
        architecture_task = tasks.architecture_task(architect_agent, architect_tools, self.user_input)
        extracting_task = tasks.excel_task(extractor_agent, extractor_tools, [architecture_task])
        implementation_task = tasks.implementation_task(programmer_agent, programmer_tools, [extracting_task])
        reviewing_task = tasks.reviewing_task(reviewer_agent, reviewer_tools, [architecture_task, implementation_task, extracting_task])

        crew = Crew(
            agents=[architect_agent, extractor_agent, programmer_agent, reviewer_agent],
            tasks=[architecture_task, extracting_task,implementation_task,  reviewing_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result



if __name__ == "__main__":

    user_input = input("Provide task and the input excel\n")
    crew = CustomCrew(user_input)
    result = crew.run()
    
    print("\n\n########################")
    print("## Here is you crew run result:")
    print("########################\n")
    print(result)
