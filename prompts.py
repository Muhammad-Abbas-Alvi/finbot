from langchain.prompts import PromptTemplate

def build_prompt():
    template = """You are FinBot, a financial assistant. Answer the following question clearly:\n\nQuestion: {question}\nAnswer:"""
    return PromptTemplate(input_variables=["question"], template=template)
