from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool


@CrewBase
class LatestAiDevelopment():
    """Applications assistant crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def question_gatherer(self) -> Agent:
        return Agent(
            config=self.agents_config['question_gatherer'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def simplifier(self) -> Agent:
        return Agent(
            config=self.agents_config['simplifier'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def answer_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['answer_generator'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @task
    def extract_questions_task(self) -> Task:
        return Task(
            config=self.tasks_config['extract_questions_task'],
        )

    @task
    def simplify_questions_task(self) -> Task:
        return Task(
            config=self.tasks_config['simplify_questions_task'],
        )

    @task
    def gather_user_responses_task(self) -> Task:
        return Task(
            config=self.tasks_config['gather_user_responses_task'],
            human_input=True
        )

    @task
    def generate_responses_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_responses_task'],
            output_file="report.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
