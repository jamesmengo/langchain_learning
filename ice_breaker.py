from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

from third_parties.twitter_with_stubs import scrape_user_tweets


# if __name__ == "__main__":
#     print("Hello LangChain!")

#     linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco Udemy")

#     summary_template = """
#          given the Linkedin information {information} about a person from I want you to create:
#          1. a short summary
#          2. two interesting facts about them
#      """

#     summary_prompt_template = PromptTemplate(
#         input_variables=["information"], template=summary_template
#     )

#     llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

#     chain = LLMChain(llm=llm, prompt=summary_prompt_template)

#     linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

#     print(chain.run(information=linkedin_data))

if __name__ == "__main__":
    print("Hello LangChain!")
    user_tweets = scrape_user_tweets(username="elonmusk", num_tweets=10)
    print(user_tweets)
