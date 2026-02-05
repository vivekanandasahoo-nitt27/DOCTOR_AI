import gradio as gr
from voice_of_the_patient import transcribe_with_groq
from brain_of_the_doctor import analyze_image_with_query
from voice_of_the_doctor import text_to_speech_with_elevenlabs
from doctor_report import create_medical_report
from disease_chat import disease_followup_chat

SYSTEM_PROMPT = """
You have to act as a professional doctor i know you are not but this is for learning purpose
Whats in this image Do you find anything wrong with it medically
If you make a differential suggest some remedies for them
please give a brief descripting of the problem 
Important include the medication and medicine in oder for the patient
Donot add any numbers or special characters in your response
Your response should be in one long paragraph
Always answer as if you are answering a real person
Donot say In the image I see but say With what I see I think you have
Dont respond as an AI model or in markdown
Mimic an actual doctor not an AI bot
in last please ask the person for the consult a doctor and give wishesto get well soon
No preamble start your answer right away
"""


# --------------------------
# INITIAL PROCESS
# --------------------------
def process_initial(audio_filepath, image_filepath, state):
    state = state or []

    if not audio_filepath and not image_filepath:
        return "", state, None, state

    patient_text = transcribe_with_groq(audio_filepath)
    if not patient_text.strip():
        patient_text = "Analyze this medical image."

    final_query = f"{SYSTEM_PROMPT}\nPatient says: {patient_text}"

    if image_filepath:
        doctor_response = analyze_image_with_query(final_query, image_filepath)
    else:
        doctor_response = "Please upload an image."

    audio_path = text_to_speech_with_elevenlabs(doctor_response)

    state = [
        {"question": patient_text, "answer": doctor_response}
    ]

    chatbot_history = [(patient_text, doctor_response)]

    return "", chatbot_history, audio_path, state


# --------------------------
# FOLLOW-UP CHAT
# --------------------------
def continue_chat(user_message, state):
    if not state:
        return "", [], state

    initial_response = state[0]["answer"]
    history_only = state[1:]

    answer, updated_history = disease_followup_chat(
        doctor_response=initial_response,
        user_question=user_message,
        history=history_only
    )

    state = (
        [state[0]] +
        updated_history +
        [{"question": user_message, "answer": answer}]
    )

    chatbot_history = [(e["question"], e["answer"]) for e in state]

    return "", chatbot_history, state


# --------------------------
# FINAL REPORT
# --------------------------
def generate_final_report(state):
    if not state:
        return None

    full_text = "\n".join(
        f"Patient: {e['question']}\nDoctor: {e['answer']}"
        for e in state
    )

    return create_medical_report(full_text)


# ===============================
# GRADIO UI
# ===============================
with gr.Blocks(title="AI Doctor with Vision, Voice, and Chat") as demo:
    gr.Markdown("# 🩺 AI Doctor with Vision, Voice, and Chat")

    session_state = gr.State([])

    with gr.Row():
        audio_input = gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="Patient Voice"
        )
        image_input = gr.Image(type="filepath", label="Upload Image")
        submit_btn = gr.Button("Submit Initial")

    chatbot = gr.Chatbot(label="Doctor Chat")
    user_message = gr.Textbox(label="Type your message here")
    send_btn = gr.Button("Send Message")

    final_report_btn = gr.Button("Generate Final Report")
    report_file = gr.File(label="Download Final Medical Report (PDF)")

    audio_output = gr.Audio(label="Doctor Voice", autoplay=True)

    submit_btn.click(
        fn=process_initial,
        inputs=[audio_input, image_input, session_state],
        outputs=[user_message, chatbot, audio_output, session_state],
        api_name=False
    )

    send_btn.click(
        fn=continue_chat,
        inputs=[user_message, session_state],
        outputs=[user_message, chatbot, session_state],
        api_name=False
    )

    final_report_btn.click(
        fn=generate_final_report,
        inputs=[session_state],
        outputs=[report_file],
        api_name=False
    )

demo.launch(
    server_name="0.0.0.0",
    server_port=7860,
    share=True
)
