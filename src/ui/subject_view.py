import customtkinter as ctk


class SubjectView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="Matérias",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        title.pack(pady=20)
