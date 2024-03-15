import sys
import threading

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
from backend import Chatbot


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Instantiate the instance of chatbot class
        self.chatbot = Chatbot()

        self.setMinimumSize(800, 600)
        # Chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 640, 480)
        self.chat_area.setReadOnly(True)

        # Input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 500, 640, 40)
        # Send input by Enter
        self.input_field.returnPressed.connect(self.send_message)

        # Button widget
        self.button = QPushButton("Send", self)
        self.button.setGeometry(660, 500, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        # Get the input from user
        user_input = self.input_field.text().strip()

        # Display it in chat area
        self.chat_area.append(f"Me: {user_input}")
        self.chat_area.append("\n")
        self.input_field.clear()

        # Send message to the chat GPT in separate thread, not to slow down the process
        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        # Display response in chat area
        self.chat_area.append(f"<p style='color:#333333; background-color:#E9E9E9'> ChatGPT 3.5: {response}</p>")
        self.chat_area.append("\n")


app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())
