from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# template = ChatPromptTemplate(
template="""
    
    Answer the question below.
    
    Here is the conversation history{context}
    
    Question: {question}
    
    Answer:
    
    """
    
    
    # )
# model = OllamaLLM(model="llama3", device="cuda")
# result = model.invoke(input="Hello")
# print(result)
model = OllamaLLM(model="llama3", device="cuda")
prompt= ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("welcome to the AI chatbot, ask me anything, Type 'exit' to end the conversation")
    while True:
        question = input("You: ")
        if question.lower == "exit":
            break
        result = chain.invoke({"context": context, "question": question})
        print("AI: ", result)
        context += f"\nYou: {question}\nAI: {result}"
        
        
# result = chain.invoke({"context": "context", "question": "question"})   
# print(result)

if __name__ == "__main__":
    handle_conversation()