from app import assistant_chain
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

def test_science_quiz():
  assistant = assistant_chain()
  question  = "Generate a quiz about science."
  answer = assistant.invoke({"question": question})
  expected_subjects = ["davinci", "telescope", "physics", "curie"]
  print(answer)
  assert any(subject in answer.lower() for subject in expected_subjects), f"Expected the assistant questions to include '{expected_subjects}', but it did not"

def test_geography_quiz():
  assistant = assistant_chain()
  question  = "Generate a quiz about geography."
  answer = assistant.invoke({"question": question})
  expected_subjects = ["paris"]
  print(answer)
  assert any(subject in answer.lower() for subject in expected_subjects), f"Expected the assistant questions to include '{expected_subjects}', but it did not"
