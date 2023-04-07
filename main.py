from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9)
text = "Opisz mi jak można opisać piękny dzień wiosenny:D"
print(llm(text))