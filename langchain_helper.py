from langchain.llm import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load.dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType


load_dotenv()

def generate_pet_name(animal_type, pet_color):
  llm = OpenAI(temperature=0.7)
  
  prompt_template_name = PromptTemplate(
    imput_variable=['animal_type','pet_color'],
    template = llm("I have a {animal_type} pet and I want a cool name for 
it, it is {pet_color} in color, Suggest 5 names")
  )
  name_chain = LLMChain(llm=llm,prompt=prompt_template_name, 
output_key="pet_name")
  response = name_chain({'animal_type': animal_type,'pet_color': pet_color})
  return response

def langchain_agent()
  llm= OpenAI(temparature=0.5)
  tools = load_tools(["wikipedia","llm-math"],llm=llm)
  agent = initialize_agent(
  tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True
)
  result = agent.run("
	What is the average age of dog, multiply by 3
")
  
if __name__ == "__main__"
  # print(generate_pat_name('cat'))
  # langchain_agnet()

  
  
