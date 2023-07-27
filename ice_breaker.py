from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup_linkedin

from linkedin import scrape_linkedin_profile

information = """
  name: John Doe
  age: 35
  occupation: Software Engineer
  hobbies: playing guitar, reading books, playing video games
  personality: introverted, shy, kind, friendly
"""

if __name__ == "__main__":
    print("Hello, Langchain!")

    summary_template = """
      given the information {information} about a person I want you to create:
      1. a short summary of the person with their name
      2. two interesting facts about the person
      3. a short description of the person's personality
      """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_profile_url = lookup_linkedin(name="James Meng UBC")

    print(linkedin_profile_url)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)

    print(chain.run(information=linkedin_data))
