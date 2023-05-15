import mysql.connector
import tkinter as tk
import tkinter.ttk as ttk

global USER, PASSWORD
USER = 'root'
PASSWORD = ''

class App(tk.Tk):
    def get_data_from_db(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user=USER,
            password=PASSWORD,
            database="test_db"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT people.name, projects.title FROM people LEFT JOIN projects ON people.projects_id = projects.id;")
        myresult = mycursor.fetchall()
        return myresult

    def __init__(self):
        super().__init__()
        self.title("Test")

        columns = ("#1", "#2")
        self.tree = ttk.Treeview(self, show="headings", columns=columns)
        self.tree.heading("#1", text="Имя участника")
        self.tree.heading("#2", text="Название проекта")
        ysb = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)

        for item in self.get_data_from_db():
            self.tree.insert("", tk.END, values=item)

        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    
if __name__ == "__main__":
    app = App()
    app.mainloop()