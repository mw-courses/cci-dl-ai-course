# note, you will need to run the cell to write the app file for these imports to work.
from app import system_message, quiz_information_bank, assistant_chain
from langchain.prompts                import ChatPromptTemplate
from langchain.chat_models            import ChatOpenAI
from langchain.schema.output_parser   import StrOutputParser

def create_eval_chain(user_request, context, agent_response):
  eval_system_prompt = """You are an assistant that evaluates how well the quiz assistant
    creates quizzes for a user by looking at the context that the assistant is using to generate quizzes"""
  
  eval_user_message = f"""You are evaluating a generated quiz based on the context that the assistant uses to create the quiz.
  Here is the data:
    [BEGIN DATA]
    ************
    [Question]: {user_request}
    ************
    [Context]: {context}
    ************
    [Submission]: {agent_response}
    ************
    [END DATA]

Compare the content of the quiz with the fact context
Ignore any differences in style, grammar, or punctuation.
Is the quiz based on the context provided.

Output Y or N
"""
  eval_prompt = ChatPromptTemplate.from_messages([
      ("system", eval_system_prompt),
      ("human", eval_user_message),
  ])

  return eval_prompt | ChatOpenAI(model="gpt-3.5-turbo-16k", temperature=0) | StrOutputParser()

def test_model_graded_eval():
  assistant = assistant_chain()
  quiz_request = "Write me a quiz about geography."
  result = assistant.invoke({"question": "Write me a quiz about science."})
  print(result)
  eval_agent = create_eval_chain(quiz_request, quiz_information_bank, result)
  eval_response = eval_agent.invoke({})
  assert eval_response == "Y"
