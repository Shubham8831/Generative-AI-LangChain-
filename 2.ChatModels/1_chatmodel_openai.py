from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)

'''temperature=1.5  -> this is the parameter that controls the randomness of model (how creative or deterministic response are)
[low -> more deterministic and predictable
high -> more random, creative and diverse]
[factual answer (0-0.3)
balanced_response, QA, explanation (0.5-0.7)
creative writing, story telling (0.9-1.2)
brain stroming (1.5+)
]

 max_completion_tokens=10 -> how much token we get in output '''