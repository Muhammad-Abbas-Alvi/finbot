from app.schemas import ChatRequest, ChatResponse
from app.prompts import build_prompt
from langchain.llms import HuggingFacePipeline
from langchain.chains import LLMChain

llm = HuggingFacePipeline.from_model_id(model_id="google/flan-t5-base")
chat_chain = LLMChain(llm=llm, prompt=build_prompt())

def process_chat(request: ChatRequest) -> ChatResponse:
    result = chat_chain.run(question=request.message)
    return ChatResponse(reply=result)
