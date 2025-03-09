import tkinter as tk
from tkinter import messagebox
from googletrans import Translator

# Create the Translator instance
translator = Translator()

# Supported languages for simplicity
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi"
}

# Function to perform translation
def translate_text():
    try:
        input_text = input_text_box.get("1.0", tk.END).strip()
        selected_language = selected_lang.get()

        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        # Translate text
        translated = translator.translate(input_text, dest=LANGUAGES[selected_language])

        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translated.text)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")

# Function to reset fields
def reset_fields():
    input_text_box.delete("1.0", tk.END)
    output_text_box.delete("1.0", tk.END)
    selected_lang.set("English")

# Initialize Tkinter Window
root = tk.Tk()
root.title("Translator App")
root.geometry("600x400")

# Title Label
title_label = tk.Label(root, text="Language Translator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input Text
input_label = tk.Label(root, text="Enter Text:", font=("Arial", 12))
input_label.pack(anchor="w", padx=20)
input_text_box = tk.Text(root, height=5, width=70, wrap=tk.WORD)
input_text_box.pack(pady=5)

# Language Selection with Radio Buttons
lang_frame = tk.Frame(root)
lang_frame.pack(pady=10)

selected_lang = tk.StringVar(value="English")  # Default selected language
lang_label = tk.Label(lang_frame, text="Translate To:", font=("Arial", 12))
lang_label.grid(row=0, column=0, padx=10)

row = 1
for lang in LANGUAGES.keys():
    lang_radio = tk.Radiobutton(lang_frame, text=lang, variable=selected_lang, value=lang, font=("Arial", 10))
    lang_radio.grid(row=row // 3, column=row % 3, padx=10, pady=5, sticky="w")
    row += 1

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text, bg="blue", fg="white", font=("Arial", 12))
translate_button.pack(pady=10)

# Output Text
output_label = tk.Label(root, text="Translated Text:", font=("Arial", 12))
output_label.pack(anchor="w", padx=20)
output_text_box = tk.Text(root, height=5, width=70, wrap=tk.WORD, state="normal")
output_text_box.pack(pady=5)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset_fields, bg="red", fg="white", font=("Arial", 12))
reset_button.pack(pady=10)

# Run the Application
root.mainloop()