# 635
"6-3-5 Brainwriting (or 635 Method, Method 635) is a group-structured brainstorming technique[1] aimed at aiding innovation processes by stimulating creativity developed by Bernd Rohrbach who originally published it in a German sales magazine, the Absatzwirtschaft, in 1968.[2]

In brief, it consists of 6 participants supervised by a moderator who are required to write down 3 ideas on a specific worksheet within 5 minutes; this is also the etymology of the methodology's name. The outcome after 6 rounds, during which participants swap their worksheets passing them on to the team member sitting at their right, is 108 ideas generated in 30 minutes. The technique is applied in various sectors but mainly in business, marketing, design, and writing, as well as everyday real life situations.[1] "
https://en.wikipedia.org/wiki/6-3-5_Brainwriting

---

# 🧠 6-3-5 Ideation Method – AI-Powered Digital Twin

This project presents a **digital twin of the 6-3-5 ideation method**, adapted for use with **LLM-powered personas**. The goal is to **simulate structured group creativity** with diverse perspectives by automating idea generation and evolution using LangChain and Ollama.

### 🎯 Aim

We developed this tool to replicate and enhance the **6-3-5 brainwriting technique** through artificial intelligence. By assigning six unique **personas** (entrepreneur, thinker, futurist, engineer, environmentalist, and artist), each acting as an initiator and contributor, we simulate the method's collaborative rounds and produce idea chains.

Each session works as follows:

* A **user-defined problem** is posed in Turkish.
* One persona initiates by generating **three unique ideas**.
* Other personas iterate over these ideas for **four improvement rounds**, mimicking the "3 ideas x 6 participants" format.
* The initiator then **finalizes** the evolved ideas.
* All results are saved in **Markdown tables**, ready for documentation or further review.

### 🧰 Tech Stack

* Python
* [LangChain](https://www.langchain.com/)
* [Ollama](https://ollama.ai/) for local LLM inference

### 📄 Sample Problem (in Turkish)

```
Evlerde enerji verimliliğini arttırmak için neler yapılmalı?
```

### 🧑‍🤝‍🧑 Personas Used

* **Girişimci** (Entrepreneur)
* **Düşünür** (Thinker)
* **Fütürist** (Futurist)
* **Mühendis** (Engineer)
* **Çevreci** (Environmentalist)
* **Sanatçı** (Artist)

Each persona has a distinct voice and priority, influencing how ideas evolve.

### 📂 Output

* A markdown file (e.g., `ideation_output_2025-06-03_20-15.md`) with 6 tables—one for each initiator—showing all idea iterations and final outcomes.

---

Developed by

**Kenan Acar**

**Serhat Yağcı**

*Yıldız Teknik Üniversitesi, 2025*

---
