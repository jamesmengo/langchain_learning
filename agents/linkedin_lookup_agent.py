from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import google_linkedin_url


def lookup_linkedin(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name of {person_name}, find the URL of their LinkedIn profile and return it."""
    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile",
            description="uses Google to find URL's of LinkedIn profiles",
            func=google_linkedin_url,
        )
    ]
    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    prompt_template = PromptTemplate(template=template, input_variables=["person_name"])

    linked_in_profile_url = agent.run(prompt_template.format_prompt(person_name=name))
    return linked_in_profile_url
