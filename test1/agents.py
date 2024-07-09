from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI


class CustomAgents:
    def __init__(self):
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4o", temperature=0.7)
        # self.Ollama = 
    def extractor_agent(self, tools):
        return Agent(
            role = "Excel extractor",
            backstory =dedent(f"""\
            You are really good at extracting tabular and image data from an excel sheet
            and are able to effectively map the text and images present to each other.
            You are able to provide this data efectively to the rest of the crew.
            """),
            goal= dedent(f"""\
            Extract images and text from the excel and provide the same as output
            """),
            tools = tools,
            alow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
            
        )
    def architect_agent(self, tools):
        return Agent(
            role="Software Architect",
            backstory=dedent(f"""\
            With years of experience in system design, 
            you excel at breaking down complex problems into manageable solutions,
            providing a solid foundation for implementation."""),
            goal=dedent(f"""\
            Provide a high-level solution overview for a given problem"""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def programmer_agent(self, tools):
        return Agent(
            role="Software Programmer",
            backstory=dedent(f"""\
            You havea keen eye for detail and a knack for translating high-level design solutions into robust,
            efficient code."""),
            goal=dedent(f"""Implement the solution provided by the architect"""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )


    def reviewer_agent(self, tools):
        return Agent(
            role="Software Reviewer",
            backstory=dedent("""\
            With a critical eye, you review each step of the development process, ensuring quality and consistency."""),
            goal=dedent("""\
            Review the work of each agent at each step and ensure that the final pages made are similar to the initially provided excel pages."""),
            tools=tools,            
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )
