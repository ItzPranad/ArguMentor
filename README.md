ArguMentor
ArguMentor is an AI-powered debate simulation platform developed by Team Tech Intelligence. It enables users to experience complete debate rounds with AI opponents, voice-based interactions, and judge-style feedback. With support for multiple debate formats, ArguMentor delivers an immersive and on-demand debate training experience — anytime, anywhere.

🔧 System Overview
This repository contains all the working models and modules for ArguMentor AI, including:

🧠 Core Functionalities:
Speech Generation (LLMs via Groq & LLaMA)

Text-to-Speech (TTS) using Edge TTS for realistic voice output

Speech-to-Text (STT) via JavaScript for listening to user inputs

POI (Point of Information) Engine for dynamic interruption simulation

🗂️ Key Folders and Features
🔹 Asian_Par/
Contains member speech generation models for the Asian Parliamentary format

Integrated via the AsianThread file, which runs all six member roles and stores each speech as a .txt file inside the Data/ folder.

🔹 AsianThreadSummary/
Processes the speeches and provides bullet-point summaries for note-taking and overview.

🔹 MockDebate/
Implements the Mock Debate format:

3-minute Opening Statement

2-minute Rebuttal

Q&A Round (1v1 AI vs User)

Contains the main speech generation pipelines for this format.

🔹 AI_Judge/
AI_Judge.py – Delivers final verdicts and scoring.

AsianFeedback.py – Provides structured feedback for Asian Parliamentary speakers.

MockFeedback.py – Gives feedback for users in the Mock Debate format.

💡 What's Working So Far
Front-end website is in development

AI speakers, judge modules, and multiple debate formats are implemented

TTS/STT pipelines are integrated

POI engine is developed

