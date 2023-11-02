from app import assistant_chain
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

def test_name():
  assistant = assistant_chain("Bob")
  question  = "What is your name?"
  answer = assistant.invoke({"question": question})
  expected_name = "bob"
  assert expected_name in answer.lower(), f"Expected the assistant to say its name was '{expected_name}', but it answered '{answer}'"

def test_geography_facts():
  assistant = assistant_chain("Carmen SanDiego")
  question  = "What the capital of France?"
  answer = assistant.invoke({"question": question})
  expected_capital = "Paris"
  assert expected_capital.lower() in answer.lower(), f"Expected the capital of France to contain '{expected_capital}' got {answer}"
