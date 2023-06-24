import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import openai
from apikey import api_data
import pyttsx3
import webbrowser

openai.api_key = api_data

engine = pyttsx3.init()

context = ""

def get_openai_response(question, context):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=context + "\nUser: " + question + "\nChatbot:",
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def send_message():
    global context
    user_input = user_entry.get()
    chat_log.insert(tk.END, user_input + "\n", "user")

    if user_input.lower() == "bye":
        response = "Chatbot: Goodbye!"
        speak("Goodbye!")
    elif user_input.lower() == "open youtube":
        webbrowser.open("www.youtube.com")
    elif user_input.lower() == "open google":
        webbrowser.open("www.google.com")
    else:
        response = get_openai_response(user_input, context)
        chat_log.insert(tk.END, response + "\n", "bot")
        speak(response[9:])
        context += "\n" + user_input + "\n" + response[9:]

    user_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Chatbot")
root.geometry("900x550")
root.configure(bg="#000c66")

# Create a frame to hold the image and chat log
frame = tk.Frame(root)
frame.configure(bg="#000c66")
frame.pack(pady=10)

image = Image.open("chatbot.png")
img = image.resize((350,400))
photo = ImageTk.PhotoImage(img)
image_label = tk.Label(frame, image=photo, bd=0)
image_label.grid(row=0, column=0, padx=10, pady=10)


chat_log = tk.Text(frame, width=65, height=25, border=0, font=("Helvetica", 10))
chat_log.configure(bg="#000c66")

chat_log.grid(row=0, column=1, padx=10, pady=10)




search_image = tk.PhotoImage(file="Images/rect.png")
# Create the label and display the image
myimage = Label(image=search_image, bg="#000c66")
myimage.place(x=260, y=430)

user_entry = tk.Entry(root, font=("Helvetica", 14), background="#f3f3f3",width=30,border=0,fg="black")
user_entry.pack(pady=10)
user_entry.focus_set()

# Create a custom style for the button
search_icon = PhotoImage(file="Images/Layer 6.png")
myimage_icon = tk.Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#f3f3f3", command=send_message)
myimage_icon.place(x=637, y=435)

# Add tag configurations for colors
chat_log.tag_configure("user", foreground="white", font=("Helvetica", 13,'bold'))
chat_log.tag_configure("bot", foreground="white")

root.mainloop()
