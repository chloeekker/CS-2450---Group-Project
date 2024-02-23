import tkinter as tk

root = tk.Tk()
root.title("UVUAdvisorbot")
root.geometry("400x300")
root.configure(bg="#333333")


label = tk.Label(root, text="UVUAdvisor", font=("Helvetica", 64, "bold"), fg="green", bg="lightgray", padx=10, pady=10, bd=3)





whatif_button = tk.Button(root, text="What-if", font=("Helvetica", 12),fg="green", bg="lightgrey")
search_button = tk.Button(root, text="Search", font=("Helvetica", 12),fg="green", bg="lightgrey")
profile_button = tk.Button(root, text="My Profile", font=("Helvetica", 12), fg="green", bg="lightgrey")
ai_reply = tk.Text(root, height=10, width=40, font=("Helvetica", 12),bg="#333333")
ai_reply.insert("1.0", "Hi, how can I help you?")

input_bar = tk.Entry(root,justify="center",fg="lightgrey")
input_bar.insert(0,"type here")



label.grid(row = 0, column=0, columnspan=3)
whatif_button.grid(row=1,column=0)
search_button.grid(row=1,column=1)
profile_button.grid(row=1,column=2)
ai_reply.grid(row=3, column=0, rowspan=2, columnspan=3)
input_bar.grid(row=5, column=0, columnspan=3)









root.mainloop()
