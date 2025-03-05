'''
OPEN SOURCE LANGUAGE MODELS 
- free
- can modify, fine tune and deploy anywhere
- runs locally
- can fine tune on specific dataset
- can be deployed on any on-premise server or cloud

WHERE TO FIND THEM?
HugginFace - The largest repository of open-source LLMs

Ways to use opensource?
- use HF Inference API (free and paid)
- running locally

DISADVANTAGE
- high hardware requirements
- setup complexity
- lack of complexity
- limited multimodal abilities
'''
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)