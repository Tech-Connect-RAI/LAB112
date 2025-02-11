import gradio as gr
import ollama

class MedicalChatbot:

    def __init__(self, model="phi3"):
        self.history = ""
        self.model = model
        with open("./utils/system_prompt.md", "r") as file:
            self.system_prompt = file.read()

        
    def format_history(self, msg: str, history: list[list[str, str]]):
        
        self.history = [{"role": "system", "content": self.system_prompt}]

        for query, response in history:
            self.history.append({"role": "user", "content": query})
            self.history.append({"role": "assistant", "content": response})  
        self.history.append({"role": "user", "content": msg})
        
        return self.history
    

    def get_response(self, user_input: str, history: list[list[str, str]]):
        chat_history = self.format_history(user_input, history)
        response = ollama.chat(model=self.model, stream=True, messages=chat_history)
        
        message = ""
        for partial_resp in response:
            token = partial_resp["message"]["content"]
            message += token
            yield message
    

    def launch(self):
        chatbot = gr.ChatInterface(
            self.get_response,
            chatbot=gr.Chatbot(label="MD Web: Medical Terminology AI Assistant", value=[[None, "Hello! How can I help you today?"]]),
            title="MD Web: Medical Terminology AI Assistant",
            description="This is an AI Assistant that can help you to understand medical terms and concepts.",
        )

        chatbot.launch()