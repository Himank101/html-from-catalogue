from crewai import Task
from textwrap import dedent


class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def architecture_task(self, agent, tools, user_input):
        return Task(
            description=dedent(
                f"""
            Provide a high-level solution architecture for the given problem: {user_input}. 
            Your final answer must include a clear overview and major components involved.
            {self.__tip_section()}
            You have access to tools which can search the internet, read files, write files and create directories
            save your output in a file.
            """
            ),
            expected_output='A document outlining the high-level architecture including any specifics provided in the input propmt such as filepaths',
            tools=tools,
            agent=agent,
        )
    
    
    def excel_task(self, agent, tools, context):
        return Task(
            description=dedent(
                f"""
            
            {self.__tip_section()}
            You have access to tools which can search the internet, read files,
            write files and create directories. you need to store all the images in a folder and provide those along the text and tabular data present in the excel as the output
            save your output in a file 
            """
            ),
            expected_output='provide all the information from the excel including image filepath and tabular data',
            tools=tools,
            agent=agent,
            context=context
        )
    

    def implementation_task(self, agent, tools, context):
        return Task(
            description=dedent(
                f"""
            Implement the solution as per the architect's overview.
            Your final answer must include the code implementing the solution.                          
            {self.__tip_section()}
            You have access to tools which can read files, write files and create directories,
            save your output in a file 
            """
            ),
            expected_output='code implementing the solution.',
            tools=tools,
            agent=agent,
            context=context
        )


    def reviewing_task(self, agent, tools, context):
        return Task(
            description=dedent(
                f"""
            Review the work done by each agent at each step.
            Your final answer must include feedback and necessary revisions.
            You should also know how to run the application which can be useful to the users.
            ensure that the requirements put up by the user are met
            {self.__tip_section()}
            You have access to tools which can read files, write files and create directories.
            save your output in a file 
            """
            ),
            expected_output='Feedback and revisions for each step of the process. Also a final document which has steps to run the code given which can serve as a documentation for users',
            tools=tools,
            agent=agent,
            context=context
        )

