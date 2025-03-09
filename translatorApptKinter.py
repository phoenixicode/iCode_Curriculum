import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, messagebox
import google.generativeai as genai
import datetime  # Import the datetime module

class UserInfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Labels and Entry fields
        tk.Label(self, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        tk.Label(self, text="Date of Birth (YYYY-MM-DD):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.dob_entry = tk.Entry(self)
        self.dob_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        tk.Label(self, text="Profession:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.profession_choices = ["Student", "Working Professional", "Other"]
        self.profession_var = tk.StringVar(value=self.profession_choices[0])
        self.profession_dropdown = ttk.Combobox(self, textvariable=self.profession_var, values=self.profession_choices, state="readonly")
        self.profession_dropdown.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        # Submit Button
        submit_button = tk.Button(self, text="Submit", command=self.submit_info)
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def submit_info(self):
        name = self.name_entry.get()
        dob_str = self.dob_entry.get()
        profession = self.profession_var.get()

        # Simple Validation
        try:
            dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d").date()
            today = datetime.date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 0 or age > 120:
                raise ValueError("Invalid age.")  # Added age validation
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid Date of Birth.  Use YYYY-MM-DD format and ensure it's a valid date.")
            return

        # Store User Info
        self.controller.user_info = {
            "name": name,
            "dob": dob,
            "profession": profession,
            "age": age
        }

        # Switch to Main Chat Page
        self.controller.show_frame("ChatPage")
        self.controller.frames["ChatPage"].greet_user()  # Greet the user after switching pages


class ChatPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.api_key = "API Key"  # Replace with your actual API key

        # UI Elements
        self.chat_log = scrolledtext.ScrolledText(self, width=80, height=20, state="disabled")
        self.chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.prompt_entry = tk.Entry(self, width=70)
        self.prompt_entry.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(self, text="Send", command=self.send_prompt)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

    def greet_user(self):
        user_info = self.controller.user_info
        name = user_info["name"]
        profession = user_info["profession"]
        age = user_info["age"] # Access the age

        greeting = f"Hello {name}! Welcome to the chatbot.\n"

        if profession == "Student":
            greeting += "I hope you're having a productive day of learning!"
        elif profession == "Working Professional":
            greeting += "Ready to tackle some challenges?"
        else:
            greeting += "How can I assist you today?"

        greeting += f"\nIt's nice to have someone of {age} years old chatting with us." # Added age information

        self.update_chat_log(greeting, "System")

    def send_prompt(self):
        prompt = self.prompt_entry.get()
        self.prompt_entry.delete(0, tk.END)  # Clear the input
        self.update_chat_log(prompt, "User")  # Display user prompt

        # Get user info for tailored response
        user_info = self.controller.user_info
        name = user_info["name"]
        profession = user_info["profession"]
        age = user_info["age"]

        # Tailor the prompt based on user info
        tailored_prompt = f"The user's name is {name}, they are {age} years old, and their profession is {profession}.\n"
        tailored_prompt += f"Respond to the following prompt in a way that takes this information into account:\n{prompt}"

        self.get_gemini_response(tailored_prompt)  # Send tailored prompt

    def get_gemini_response(self, prompt):
        try:
            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel('gemini-2.0-flash')  # Or 'gemini-pro-vision' for image input
            response = model.generate_content(prompt)  # Pass the tailored prompt
            self.update_chat_log(response.text, "Gemini")
        except Exception as e:
            self.update_chat_log(f"Error: {e}", "System")
            messagebox.showerror("Error", f"Error generating response: {e}")  # More user-friendly error message


    def update_chat_log(self, message, sender):
        self.chat_log.config(state="normal")  # Enable editing
        self.chat_log.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_log.config(state="disabled") # Disable editing
        self.chat_log.yview(tk.END)  # Scroll to the bottom

class ChatbotApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Chatbot Application")
        self.geometry("800x600")  # Set initial window size

        self.user_info = {} # Store user info

        # Container to hold all frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (UserInfoPage, ChatPage):  # Add pages here
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew") # Make frames fill container

        self.show_frame("UserInfoPage") # Start on the user info page

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise() # Bring frame to the top

if __name__ == "__main__":
    app = ChatbotApp()
    app.mainloop()
