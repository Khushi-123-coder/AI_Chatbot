# AI_Chatbot

A lightweight, stateful, terminal-themed desktop chatbot built in Python using **Tkinter**. Featuring a **Deep Minimalist Cyber Theme**, this application implements a state-driven engine for interactive mini-games, dynamic utilities, system checks, and educational commands.

---

## 📌 Features & Capabilities

The bot operates on a multi-mode architecture (**State Machine** pattern). It can switch between standard command processing and specialized interactive modes.

### 1. 🎮 Interactive State Modes
- **Rock-Paper-Scissors (`play game` / `rps`)**: Enters an interactive game loop against the bot with win/loss/tie logic.
- **Temperature Converter (`convert`)**: Interactive prompt that converts input temperature from Celsius (°C) to Fahrenheit (°F).
- **Secure Password Generator (`pass` / `password`)**: Generates cryptographically randomized passwords based on user-specified lengths (4 to 32 characters).
- **Global Cancel (`cancel` / `stop` / `menu`)**: Immediately exits any active mode and returns to normal operation.

### 2. ⚡ Utilities & Infrastructure
- **Server Health Check (`check server`)**: Simulates live DevOps infrastructure monitoring (Production, Staging, Database).
- **Real-time Clock (`time` / `date`)**: Displays current timestamp formatted as `YYYY-MM-DD HH:MM:SS`.

### 3. 📚 Student & Tech Learning Panel
- **Developer Roadmap (`roadmap`)**: Step-by-step guidance for software engineering progression.
- **DSA Reference (`explain dsa`)**: Quick summaries of fundamental Data Structures & Algorithms (Arrays, Stacks, Queues).
- **Technical Dictionary (`define api`, `define cicd`)**: Explains core software engineering concepts inline.

### 4. 🎯 Fun & Motivation
- **Jokes & Riddles (`joke`, `riddle`, `another one`)**: Context-aware joke/riddle system that remembers your last request to serve follow-ups.
- **Motivational Quotes (`motivate me` / `quote`)**: Randomly selects inspiring tech and life quotes.

---

## 🎨 UI & Design Theme

- **Cyber Minimalist Aesthetic**: Deep dark palette (`#121214` background, `#06b6d4` cyan accents, `#a855f7` purple bot headers).
- **Developer Focus**: Monospaced `Consolas` font styled like a terminal environment.
- **Auto-scrolling Chat Log**: Smooth message append with auto-scroll down to latest response.

---

