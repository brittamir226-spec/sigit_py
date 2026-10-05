import os
import tkinter as tk


def show_answer():
    image_label.config(image=answer_image)
    image_label.pack(pady=10)
    button.config(state="disabled")


root = tk.Tk()
root.title("Question")
root.minsize(360, 140)

question = tk.Label(root, text="What is the coolest animal in the world?",
                    font=("Arial", 14, "bold"), pady=15)
question.pack()

button = tk.Button(root, text="Click for the answer", font=("Arial", 12),
                   command=show_answer)
button.pack()

image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "answer.png")
answer_image = tk.PhotoImage(file=image_path)
image_label = tk.Label(root)

root.mainloop()



