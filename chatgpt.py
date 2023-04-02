import openai
from tkinter import *
from tkinter.ttk import *
import customtkinter
import os
import time

openai.api_key = os.getenv("OPENAI_API_KEY")


chat_history = " "

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


app = customtkinter.CTk()
app.geometry("1000x1000")
app.title("Ask ChatGPT App")
app.grid_rowconfigure((0,1,2), weight=1)
app.grid_columnconfigure((0,1,2,3), weight=1)



def onSubmit():
    global chat_history
    inputuser = userinput.get("0.0", "end")
    input_role = rolSel.get().split("|")
    name = input_role[0].strip()
    role = input_role[1].strip()

    try:
        output = openai.ChatCompletion.create(
            model="gpt-4",
            temperature=1,
            presence_penalty=0,
            frequency_penalty=0,
            messages=[
            {
                    "role":"user", "content":f'{inputuser}',
            }
            ]

        )
        for item in output["choices"]:
            chatgpt_out = item["message"]["content"]
        chat_history = f"{chat_history}:{chatgpt_out}\n\n"
        print(chat_history)
        getchatgptout.insert("0.0", chat_history)
        userinput.delete("0.0", "end")


    except:
        time.sleep(10)
        output = openai.ChatCompletion.create(
            model="gpt-4",
            temperature=1,
            presence_penalty=0,
            frequency_penalty=0,
            messages=[{
                    "role":"user", "content":f'{inputuser}',
            }]

        )
        for item in output["choices"]:
            chatgpt_out = item["message"]["content"]
        chat_history = f"{chat_history}:{chatgpt_out}\n\n"
        getchatgptout.insert("0.0", chat_history)
        userinput.delete("0.0", "end")

    return chat_history


def onReset():
    userinput.delete("0.0", "end")
    getchatgptout.delete("0.0","end")


def onExit():
    app.destroy()

def onSave():
    global chat_history
    chat_history = onSubmit()
    with open("chatgptreply.txt", "w") as f:
        f.write(chat_history)




frame_1 = customtkinter.CTkFrame(master=app)
frame_1.grid(row=0, column=0, pady=20, padx=20)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Ask chatGPT anyting", font=("Helvetica",20))
label_1.grid(row=0, column=0, pady=20, padx=20)

userinput = customtkinter.CTkTextbox(master=frame_1, width=980, height=300, font=("Helvetica", 20))
userinput.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
userinput.insert("0.0", "Write your request to gpt4")


rolSel = customtkinter.CTkOptionMenu(frame_1, font=("Helvetica", 20), values=["Assistance | ChatGPT Assistance", "Paul Dirac | Famous Mathematical physicist","Rob | comics explained"])
rolSel.grid(row=2, column=0, pady=10, padx=10)

explisitSel = customtkinter.CTkSwitch(frame_1, text="Explicit", onvalue="on", offvalue="off", font=("Helvetica",20))
explisitSel.grid(row=3, column=0, pady=10, padx=10)

subButton = customtkinter.CTkButton(master=frame_1, command=onSubmit, text="Submit", font=("Helvetica", 20))
subButton.grid(row=4, column=0, pady=10, padx=10)

resetButton = customtkinter.CTkButton(master=frame_1, command=onReset, text="Reset", font=("Helvetica", 20))
resetButton.grid(row=4, column=1, pady=10, padx=10)

saveTofilebtn = customtkinter.CTkButton(master=frame_1, command=onSave, text="Save", font=("Helvetica", 20))
saveTofilebtn.grid(row=4, column=2, pady=10, padx=10)

exitButton = customtkinter.CTkButton(master=frame_1, command=onExit, text="Exit", font=("Helvetica",20))
exitButton.grid(row=4, column=3, pady=10, padx=10)

getchatgptout = customtkinter.CTkTextbox(master=frame_1, font=("Helvetica", 20), width=980, height=500)
getchatgptout.grid(row=5, column=0, columnspan=4, pady=20, padx=20)
getchatgptout.insert("0.0", "gpt4 answer")






def main():
    app.mainloop()


main()
