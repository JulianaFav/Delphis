import customtkinter as ctk
from ui.subject_view import SubjectView


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Delphis")
        self.geometry("1000x600")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.sidebar = ctk.CTkFrame(self.container, width=200)
        self.sidebar.pack(side="left", fill="y")

        self.content = ctk.CTkFrame(self.container)
        self.content.pack(side="right", fill="both", expand=True)

        self.subject_button = ctk.CTkButton(
            self.sidebar,
            text="Matérias",
            command=self.show_subjects
        )
        self.subject_button.pack(pady=10, padx=10, fill="x")

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_subjects(self):
        self.clear_content()
        SubjectView(self.content)
