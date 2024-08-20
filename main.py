from tkinter import *
from tkinter import messagebox, simpledialog
from tkinter.font import Font


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x600')
        self.root.title('To-Do List App')
        self.root.config(bg='#2C3E50')

        self.task_list = []
        self._setup_ui()

    def _setup_ui(self):
        # Custom Font
        self.custom_font = Font(family="Helvetica", size=18, weight="bold")

        # Frame setup
        frame = Frame(self.root, bg='#2C3E50')
        frame.pack(pady=10, fill=BOTH, expand=True)

        # Listbox and Scrollbar
        self.lb = Listbox(frame, width=35, height=10, font=self.custom_font, bd=0, fg='#ECF0F1', selectbackground='#a6a6a6', activestyle="none", bg='#34495E')
        self.lb.pack(side=LEFT, fill=BOTH, expand=True)

        # Scrollbar
        sb = Scrollbar(frame)
        sb.pack(side=RIGHT, fill=Y)

        # Configure the listbox and scrollbar
        self.lb.config(yscrollcommand=sb.set)
        sb.config(command=self.lb.yview)

        # Entry widget with placeholder
        self.my_entry = Entry(self.root, font=('Helvetica', 16), bg='#34495E', fg='#ECF0F1', insertbackground='white')
        self.my_entry.pack(pady=20, padx=20, fill=X)
        self.my_entry.insert(0, "Enter your task here...")
        self.my_entry.bind("<FocusIn>", self.clear_placeholder)
        self.my_entry.bind("<FocusOut>", self.set_placeholder)

        # Button frame
        button_frame = Frame(self.root, bg='#2C3E50')
        button_frame.pack(pady=20)

        # Add Task Button
        addTask_btn = Button(button_frame, text='Add Task', font='Helvetica 14', bg='#27AE60', fg='#ECF0F1', padx=20, pady=10, command=self.add_task)
        addTask_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=5)

        # Delete Task Button
        delTask_btn = Button(button_frame, text='Delete Task', font='Helvetica 14', bg='#C0392B', fg='#ECF0F1', padx=20, pady=10, command=self.delete_task)
        delTask_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=5)

        # Edit Task Button
        editTask_btn = Button(button_frame, text='Edit Task', font='Helvetica 14', bg='#2980B9', fg='#ECF0F1', padx=20, pady=10, command=self.edit_task)
        editTask_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=5)

        # Status Bar
        self.status_bar = Label(self.root, text="0 Tasks", bd=1, relief=SUNKEN, anchor=W, bg='#2C3E50', fg='#ECF0F1', width=10, font=('Helvetica', 16))
        self.status_bar.pack(fill=X, side=BOTTOM)

    # function to clear the placeholder text
    def clear_placeholder(self, event):
        if self.my_entry.get() == "Enter your task here...":
            self.my_entry.delete(0, END)

    # function to set the placeholder text
    def set_placeholder(self, event):
        if self.my_entry.get() == "":
            self.my_entry.insert(0, "Enter your task here...")

    # function to add a task
    def add_task(self):
        task = self.my_entry.get()
        if task and task != "Enter your task here...":
            self.lb.insert(END, task)
            self.task_list.append(task)
            self.my_entry.delete(0, 'end')
            self.update_status()
        else:
            messagebox.showwarning("Warning", "Please enter some task.")

    # function to delete a task
    def delete_task(self):
        selected_task = self.lb.curselection()
        if selected_task:
            task = self.lb.get(selected_task)
            self.lb.delete(selected_task)
            self.task_list.remove(task)
            self.update_status()

    # function to edit a task
    def edit_task(self):
        selected_task = self.lb.curselection()
        if selected_task:
            task = self.lb.get(selected_task)
            new_task = simpledialog.askstring("Edit Task", "Modify the selected task:", initialvalue=task)
            if new_task:
                self.lb.delete(selected_task)
                self.lb.insert(selected_task, new_task)
                index = self.task_list.index(task)
                self.task_list[index] = new_task

    # function to update the status bar
    def update_status(self):
        task_count = len(self.task_list)
        self.status_bar.config(text=f"{task_count} Tasks")

    # function to run the app
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = ToDoApp(root)
    app.run()
