from langchain.prompts                import ChatPromptTemplate
from langchain.chat_models            import ChatOpenAI
from langchain.schema.output_parser   import StrOutputParser

# Other libs
from datetime import datetime
from dotenv   import load_dotenv
from operator import itemgetter

def assistant_chain(name):
  template        = "You are a helpful assistant who's name is %s." % name
  human_template  = "{question}"

  chat_prompt = ChatPromptTemplate.from_messages([
      ("system", template),
      ("human", human_template),
  ])
  return chat_prompt | ChatOpenAI(model="gpt-3.5-turbo-16k", temperature=0) | StrOutputParser()

def main():
  question = "What is the meaning of life"
  assistant = assistant_chain("HAL")
  response = assistant.invoke({"question": question})
  print(response)

if __name__ == "__main__":
  main()
