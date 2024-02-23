import tkinter as tk
from tkinter import ttk
import googletrans

def translate(text, target_language):
    try:
        translator = googletrans.Translator() 
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        return f"Translation Error: {e}"

def get_language_name(language_code):
    try:
        return googletrans.LANGUAGES[language_code]
    except KeyError:
        return "Unknown"

class TranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simpler Translator Program")
        self.geometry("800x600")

        font = ('Arial', 24, 'bold')
        label = tk.Label(self, text="Welcome to my Simple Translator!", font=font)
        label.pack()

        font = ('Arial', 14)
        label = tk.Label(self, text="Currently we offer the ability to translate from English to one of 5 languages: French, Spanish, German, Japanese and Simplified Chinese. The top text bar will be where you input your desired statement. To maintain the most accurate translation, opt to translate sentences at a time rather than great big paragraphs. The translator is not perfect, so please do not take it as fact.", font=font, wraplength=800)
        label.pack()

        self.title_label1 = tk.Label(self, text="Enter a message in English:", font=font)
        self.title_label1.pack()

        # Text box for input with a specific width of 70
        self.text_input = tk.Text(self, width=70, height=5, font=font)
        self.text_input.insert("1.0", "Enter your message here...")
        self.text_input.pack(side="top", fill="both", expand=True)
        self.text_input.bind("<FocusIn>", self.clear_placeholder)
        self.text_input.bind("<FocusOut>", self.set_placeholder)

        # Subtitle for the language selection
        subtitle_label = tk.Label(self, text="Select Target Language:", font=font)
        subtitle_label.pack()

        # Scrollable and searchable language selection menu with the same font and size as the translation box
        self.language_combobox = ttk.Combobox(self, width=20, font=font)  # Reduced width to 20
        self.language_combobox.pack(pady=5, fill="x", expand=False)  # Add some padding between subtitle and combobox
        self.language_combobox.set("")

        self.language_names = {code: get_language_name(code) for code in googletrans.LANGUAGES}
        self.language_combobox['values'] = list(self.language_names.values())

        # Align the Combobox below the subtitle and above the "Translate" button
        self.language_combobox.pack(pady=(0, 5))

        self.translate_button = tk.Button(self, text="Translate", bg="black", fg="white", command=self.on_translate_button_click, font=font)
        self.translate_button.pack(side="top")

        self.title_label2 = tk.Label(self, text="Here is your message in your desired language:", font=font)
        self.title_label2.pack()

        # Text box for output with a specific width of 70
        self.text_output = tk.Text(self, width=70, height=10, font=font)
        self.text_output.pack(side="top", fill="both", expand=True)

    def center_widget(self, widget, relative_to_widget):
        widget.update_idletasks()
        x = relative_to_widget.winfo_x() + (relative_to_widget.winfo_width() - widget.winfo_reqwidth()) // 2
        y = relative_to_widget.winfo_y() + relative_to_widget.winfo_height() + 5
        widget.place(x=x, y=y)

    def clear_placeholder(self, event):
        if self.text_input.get("1.0", "end-1c") == "Enter your message here...":
            self.text_input.delete("1.0", "end-1c")
            self.text_input.config(fg="black")

    def set_placeholder(self, event):
        if not self.text_input.get("1.0", "end-1c"):
            self.text_input.insert("1.0", "Enter your message here...")
            self.text_input.config(fg="grey")

    def on_translate_button_click(self):
        text = self.text_input.get("1.0", "end").lower()  # Convert user-inputted text to lowercase
        target_language_name = self.language_combobox.get()
        target_language_code = [code for code, name in self.language_names.items() if name == target_language_name]
        if target_language_code:
            target_language_code = target_language_code[0]
            target_language_name = get_language_name(target_language_code)
            translated_text = translate(text, target_language_code)
            self.text_output.delete("1.0", "end")
            self.text_output.insert("1.0", f"Translation to {target_language_name} ({target_language_code}):\n{translated_text}")

app = TranslatorApp()
app.mainloop()
