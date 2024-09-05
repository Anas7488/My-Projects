import tkinter as tk
from tkinter import filedialog, messagebox
import requests

def upload_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("All Files", "*.*"), ("PDF Files", "*.pdf"), ("Word Files", "*.docx")]
    )

    if file_path:
        try:
            with open(file_path, 'rb') as file:
                response = requests.post('http://127.0.0.1:5000/upload', files={'file': file})
                
                if response.status_code == 200:
                    try:
                        data = response.json()
                        summary = data.get('summary', 'No summary found.')
                        text_box.delete(1.0, tk.END)
                        text_box.insert(tk.END, summary)
                    except ValueError:
                        messagebox.showerror("Error", "Received an invalid response from the server.")
                else:
                    messagebox.showerror("Error", response.json().get('error', 'Unknown error occurred'))
        except requests.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
root = tk.Tk()
root.title("Document Summarizer Client")

# Create and pack widgets
open_button = tk.Button(root, text="Open File", command=upload_file)
open_button.pack(pady=20)

text_box = tk.Text(root, wrap=tk.WORD, height=20, width=80)
text_box.pack(padx=20, pady=20)

# Run the application
root.mainloop()
