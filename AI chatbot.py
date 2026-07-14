import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random
import string

class TrulyInteractiveBot:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Chatbot Pro")
        self.root.geometry("380x540")
        self.root.resizable(False, False)
        
        # Deep Minimalist Cyber Theme
        self.BG_MAIN = "#121214"         
        self.BG_CHAT = "#1a1a1e"         
        self.TEXT_MAIN = "#e2e8f0"       
        self.ACCENT_CYAN = "#06b6d4"     
        self.ACCENT_PURPLE = "#a855f7"   
        self.BUBBLE_BOX = "#26262b"      

        self.root.configure(bg=self.BG_MAIN)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.main_frame = tk.Frame(self.root, bg=self.BG_MAIN, padx=12, pady=12)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        # Mode States for Dynamic User Prompts
        self.current_mode = "NORMAL" # Options: NORMAL, GAME, CONVERT, PASSWORD
        self.last_topic = None

        self.create_layout()
        self.display_bot_message("Hi, I am your AI Chatbot")

    def create_layout(self):
        self.chat_log = scrolledtext.ScrolledText(
            self.main_frame, wrap=tk.WORD, state='disabled', font=("Consolas", 10),
            bg=self.BG_CHAT, fg=self.TEXT_MAIN, insertbackground=self.TEXT_MAIN,
            borderwidth=0, highlightbackground="#2d3139", highlightthickness=1
        )
        self.chat_log.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=(0, 12))
        
        self.chat_log.tag_configure("user_header", foreground=self.ACCENT_CYAN, font=("Consolas", 10, "bold"))
        self.chat_log.tag_configure("bot_header", foreground=self.ACCENT_PURPLE, font=("Consolas", 10, "bold"))
        self.chat_log.tag_configure("message_payload", foreground=self.TEXT_MAIN, font=("Consolas", 10))

        bottom_bar = tk.Frame(self.main_frame, bg=self.BG_MAIN)
        bottom_bar.grid(row=1, column=0, columnspan=2, sticky="ew")
        bottom_bar.columnconfigure(0, weight=1)

        entry_wrapper = tk.Frame(bottom_bar, bg=self.BUBBLE_BOX, bd=0, padx=10, pady=8)
        entry_wrapper.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        entry_wrapper.columnconfigure(0, weight=1)

        self.user_entry = tk.Entry(
            entry_wrapper, font=("Consolas", 11), bg=self.BUBBLE_BOX, fg=self.TEXT_MAIN, 
            bd=0, highlightthickness=0, insertbackground=self.TEXT_MAIN
        )
        self.user_entry.grid(row=0, column=0, sticky="ew")
        self.user_entry.bind("<Return>", lambda event: self.process_input())
        self.user_entry.focus()

        self.send_button = tk.Button(
            bottom_bar, text="EXECUTE", font=("Consolas", 9, "bold"),
            bg=self.ACCENT_CYAN, fg="#000000", activebackground="#0891b2",
            activeforeground="#ffffff", bd=0, padx=14, pady=8, cursor="hand2",
            command=self.process_input
        )
        self.send_button.grid(row=0, column=1, sticky="ns")

    def display_user_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, f"$ user_input ({self.current_mode}):\n", "user_header")
        self.chat_log.insert(tk.END, f"{message}\n\n", "message_payload")
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)

    def display_bot_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, "> chatbot_response:\n", "bot_header")
        self.chat_log.insert(tk.END, f"{message}\n\n", "message_payload")
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)

    def process_input(self):
        raw_text = self.user_entry.get()
        user_input = raw_text.strip().lower()
        if not user_input: return

        self.display_user_message(raw_text)
        self.user_entry.delete(0, tk.END)

        # Global cancellation command
        if user_input in ['cancel', 'stop', 'menu']:
            self.current_mode = "NORMAL"
            self.display_bot_message("Operation canceled. Returned to normal mode. Type 'help' for commands.")
            return

        # -----------------------------------------------
        # 1. INTERACTIVE GAME MODE
        # -----------------------------------------------
        if self.current_mode == "GAME":
            if user_input in ['rock', 'paper', 'scissors']:
                bot_choice = random.choice(['rock', 'paper', 'scissors'])
                if user_input == bot_choice:
                    res = f"It's a tie! We both picked {bot_choice}."
                elif (user_input == 'rock' and bot_choice == 'scissors') or \
                     (user_input == 'paper' and bot_choice == 'rock') or \
                     (user_input == 'scissors' and bot_choice == 'paper'):
                    res = f"You win! Bot selected {bot_choice}."
                else:
                    res = f"Bot wins! Bot selected {bot_choice}."
                self.display_bot_message(f"{res}\n\nGo again? Enter 'rock', 'paper', 'scissors', or type 'cancel' to stop.")
            else:
                self.display_bot_message("Invalid move. Choose 'rock', 'paper', or 'scissors' (or type 'cancel').")
            return

        # -----------------------------------------------
        # 2. INTERACTIVE CONVERTER MODE
        # -----------------------------------------------
        elif self.current_mode == "CONVERT":
            try:
                celsius = float(user_input)
                fahrenheit = (celsius * 9/5) + 32
                self.display_bot_message(f"🌡️ Result: {celsius}°C is equal to {fahrenheit}°F.\n\nMode cleared. Back to normal operational standard.")
                self.current_mode = "NORMAL"
            except ValueError:
                self.display_bot_message("Error: Please input a valid numerical digit or type 'cancel' to back out.")
            return

        # -----------------------------------------------
        # 3. INTERACTIVE PASSWORD GENERATOR MODE
        # -----------------------------------------------
        elif self.current_mode == "PASSWORD":
            try:
                length = int(user_input)
                if length < 4 or length > 32:
                    self.display_bot_message("Security Risk: Please input a size integer between 4 and 32 characters.")
                    return
                chars = string.ascii_letters + string.digits + "!@#$%^&*"
                secure_pass = "".join(random.choice(chars) for _ in range(length))
                self.display_bot_message(f"[SECURITY MATCH] Your requested {length}-char key generated:\n🔒 {secure_pass}\n\nMode cleared.")
                self.current_mode = "NORMAL"
            except ValueError:
                self.display_bot_message("Error: Please input an integer number for the length (e.g., 12) or type 'cancel'.")
            return

        # -----------------------------------------------
        # 4. STANDARD NORMAL MODE RULE ENGINE
        # -----------------------------------------------
        if user_input in ['exit', 'quit', 'shutdown']:
            self.display_bot_message("Session terminated. Goodbye.")
            self.root.after(1000, self.root.destroy)
            return

        elif user_input in ['help', 'commands']:
            self.display_bot_message(
                "=== INTERACTIVE SYSTEM PANEL ===\n"
                "• 'play game' - Play Rock-Paper-Scissors\n"
                "• 'convert' - Request a temp conversion sequence\n"
                "• 'generate pass' - Request a custom password generation\n"
                "• 'check server' - Infrastructure system checker\n"
                "• 'study roadmap' / 'explain dsa' - Student learning\n"
                "• 'joke' / 'riddle' / 'another one' - Fun panel\n"
                "• 'motivate me' - System quotes\n"
                "• 'define api' / 'define cicd' - Vocabulary lookup"
            )

        elif user_input in ['hi', 'hello', 'ping']:
            self.display_bot_message("System online. Awaiting interactive runtime prompts.")

        elif user_input in ['time', 'date']:
            self.display_bot_message(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Triggering Interactive Converters
        elif user_input == 'convert':
            self.current_mode = "CONVERT"
            self.display_bot_message("Enter the temperature value in Celsius (°C) you want to convert:")

        # Triggering Custom Password Generation Length
        elif 'pass' in user_input or 'password' in user_input:
            self.current_mode = "PASSWORD"
            self.display_bot_message("Enter the character length desired for your safe password (e.g., 8 to 16):")

        # Triggering Game State
        elif user_input in ['play game', 'game', 'rps']:
            self.current_mode = "GAME"
            self.display_bot_message("Rock-Paper-Scissors initialized! 🪨📄✂️\nEnter your move: 'rock', 'paper', or 'scissors'.")

        # DevOps Management Module
        elif 'server' in user_input or 'check server' in user_input:
            statuses = ["ONLINE (Optimal)", "ONLINE (High Load Environment - 84%)", "BACKUP INSTANCE ACTIVE"]
            self.display_bot_message(
                f"[Infrastructure Report]\n"
                f"• Production Server Status: {random.choice(statuses)}\n"
                f"• Staging Environment Cluster: ONLINE\n"
                f"• System Database Architecture: STABLE"
            )

        # Fun / Jokes
        elif 'joke' in user_input:
            self.display_bot_message("Why do programmers wear glasses? ... Because they can't C#!")
            self.last_topic = 'joke'

        elif 'riddle' in user_input:
            self.display_bot_message("What has to be broken before you can use it? ... An egg!")
            self.last_topic = 'riddle'

        elif user_input in ['another one', 'more']:
            if self.last_topic == 'joke':
                self.display_bot_message("There are 10 types of people in the world: those who understand binary, and those who don't.")
            elif self.last_topic == 'riddle':
                self.display_bot_message("I’m tall when I’m young, and I’m short when I’m old. What am I? ... A candle!")
            else:
                self.display_bot_message("Please trigger a standard 'joke' or 'riddle' sequence first.")

        # Student Tools
        elif 'roadmap' in user_input:
            self.display_bot_message(
                "[DEVELOPMENT ROADMAP]\n"
                "Step 1: Core Fundamentals (Syntax proficiency via Python or C++).\n"
                "Step 2: DSA (Data Structures & Algorithm structural analysis).\n"
                "Step 3: Build Portfolio (Launch 2 minor repositories on GitHub).\n"
                "Step 4: Specialization (Web Architecture or Machine Learning)."
            )

        elif 'dsa' in user_input or 'explain dsa' in user_input:
            self.display_bot_message(
                "[DSA REFERENCE]\n"
                "• Array: Linear structural blocks storing data elements sequentially.\n"
                "• Stack: LIFO (Last In First Out) system architecture logic parameters.\n"
                "• Queue: FIFO (First In First Out) sequential pipeline processing structures."
            )

        elif 'define' in user_input:
            if 'api' in user_input:
                self.display_bot_message("API: A code configuration that allows two distinct applications to communicate with each other.")
            elif 'cicd' in user_input:
                self.display_bot_message("CI/CD: Automated application building, testing, and deployment structural pipelines.")
            else:
                self.display_bot_message("Keyword absent. Try 'define api' or 'define cicd'.")

        elif 'motivate' in user_input or 'quote' in user_input:
            quotes = [
                "Talk is cheap. Show me the code. - Linus Torvalds",
                "The only way to do great work is to love what you do. - Steve Jobs",
                "Believe you can and you're halfway there. - Theodore Roosevelt"
            ]
            self.display_bot_message(f"Inspirational payload:\n\"{random.choice(quotes)}\"")

        else:
            self.display_bot_message("Unrecognized runtime instruction. Type 'help' to review structural commands.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TrulyInteractiveBot(root)
    root.mainloop()
