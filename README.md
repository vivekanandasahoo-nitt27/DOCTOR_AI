# 🩺 Doctor AI – Multimodal Medical Assistant

## 📌 Overview
Doctor AI is a **multimodal medical assistant** designed to simulate a real-world doctor–patient interaction.  
The system accepts **voice, image, and text inputs**, performs medical reasoning using **Groq LLMs**, supports **follow-up chatbot conversations**, generates a **final medical report (PDF with signature)**, and provides **spoken responses** using text-to-speech.

The application is **containerized, deployed on AWS EC2**, and uses a **CI/CD pipeline with GitHub Actions and Amazon ECR**.

⚠️ This project is built for **learning and demonstration purposes only** and does **not replace a licensed medical professional**.

---

## 🚀 Key Features

- 🎙️ **Voice Input** (Speech-to-Text using Groq Whisper)
- 🖼️ **Medical Image Analysis** (Vision-capable Groq LLM)
- 💬 **Follow-up Medical Chatbot**
- 🧠 **LLM-based Medical Reasoning (Doctor Brain)**
- 🧾 **Final Medical Report Generation (PDF)**
  - Medical observations
  - Medication suggestions
  - Handwritten-style formatting
  - Doctor signature
- 🔊 **Natural Voice Output** (ElevenLabs Text-to-Speech)
- 🖥️ **Interactive Frontend** using Gradio
- 🐳 **Dockerized Application**
- ☁️ **AWS Deployment (EC2 + ECR)**
- 🔁 **CI/CD Pipeline using GitHub Actions**

---

## 🧠 System Architecture

Patient (Voice / Image / Text)
↓
Speech → Groq Whisper
Image → Vision LLM (Groq)
↓
Dynamic Prompt Construction
↓
Doctor Brain (Groq LLM)
↓
Initial Medical Response
↓
Follow-up Chatbot
↓
Structured Medical Report (PDF)
↓
Voice Output (ElevenLabs)
↓
Gradio Frontend (AWS EC2)


---

## 🛠️ Tech Stack

- **LLMs:** Groq (LLaMA-based models)
- **Speech-to-Text:** Groq Whisper
- **Text-to-Speech:** ElevenLabs
- **LLM Orchestration:** LangChain
- **Frontend:** Gradio
- **Backend:** Python
- **PDF Generation:** ReportLab
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Cloud:** AWS EC2, Amazon ECR, IAM

---

## ☁️ AWS Deployment & CI/CD Pipeline

### 🔹 Deployment Strategy
- The application is **containerized using Docker**
- Docker images are stored in **Amazon Elastic Container Registry (ECR)**
- The container runs on an **AWS EC2 instance**

### 🔹 CI/CD with GitHub Actions
A CI/CD pipeline is configured to automate deployment:

1. Code is pushed to GitHub
2. GitHub Actions workflow is triggered
3. Docker image is built
4. Image is pushed to **Amazon ECR**
5. EC2 instance pulls the latest image from ECR
6. Container is restarted with the updated version

### 🔹 Security
- **IAM roles and policies** are used for secure access
- No AWS credentials are hardcoded
- Secrets are managed using **GitHub Secrets** and **EC2 environment variables**

📌 **Why this approach?**
> This ensures reproducible builds, faster deployments, and production-ready ML system practices.

---

## 📂 Project Structure

├── app.py # Main Gradio application
├── brain_of_the_doctor.py # Image analysis & medical reasoning
├── voice_of_the_patient.py # Speech-to-text using Groq Whisper
├── voice_of_the_doctor.py # Text-to-speech using ElevenLabs
├── disease_chat.py # Follow-up medical chatbot
├── doctor_report.py # Medical report (PDF) generation
├── Dockerfile
├── .github/workflows/ # GitHub Actions CI/CD pipeline
├── assets/
│ └── signature.jpeg
├── fonts/
│ └── DoctorHandwriting.ttf
└── requirements.txt


---

## 🔄 Application Flow

1. Patient provides **voice, image, or text**
2. Voice is transcribed using **Groq Whisper**
3. Image is analyzed using a **vision-enabled LLM**
4. Inputs are merged into a **dynamic medical prompt**
5. Doctor Brain LLM generates a medical response
6. User interacts via **chatbot for follow-ups**
7. A **final signed medical report (PDF)** is generated
8. Doctor response is converted to **speech**
9. Output is served via **Gradio on AWS EC2**

---

## 📊 Why Multimodal AI?

Medical consultations are inherently multimodal:
- Patients **speak** symptoms
- **Show visual signs**
- Ask **follow-up questions**

Doctor AI mirrors real clinical interaction using AI.

---

## ⚠️ Limitations & Disclaimer

- ❗ Not a real diagnostic system
- ❗ Depends on input quality
- ❗ No real-time vitals or lab integration
- ❗ Always advises consulting a licensed doctor

> This project is for **educational and research purposes only**.

---

## 🌱 Future Improvements

- Retrieval-Augmented Generation (RAG) with verified medical sources
- Multilingual speech support
- Wearable device integration
- Doctor-in-the-loop validation
- Scalable production frontend

---

## 👨‍💻 Creator

**Vivekananda Sahoo**  
Machine Learning | Generative AI | MLOps Enthusiast  

---

## ⭐ Acknowledgements

- Groq for low-latency LLM inference
- ElevenLabs for natural voice synthesis
- Gradio for rapid AI UI development
- AWS for cloud infrastructure

---

## 📜 License

This project is released for **learning and demonstration purposes only**.