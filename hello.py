from langchain_google_genai import ChatGoogleGenerativeAI

if __name__ == '__main__':
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key='AIzaSyADZK_OPQKdY-CfWpy1nT-9dSxoxFKfTBY')

    output = llm.invoke("What is the capital of India?")

    print(output)