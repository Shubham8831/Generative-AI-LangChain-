from langchain_openai import OpenAI # this is integration package of langchain and openai
from dotenv import load_dotenv # loads all the secreat keys form the enviornment files

load_dotenv() # this invokes all the enviornment variables 

llm = OpenAI(model='gpt-3.5-turbo-instruct') # here we write which model to communicate with

result = llm.invoke("What is the capital of India") #  invoke - it helps with communication with llm model

print(result)