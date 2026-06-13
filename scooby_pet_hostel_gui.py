
import tkinter as tk
from tkinter import scrolledtext


def get_response(user):
    user = user.lower().strip()

    if any(word in user for word in [
        "hi", "hello", "hey", "hii",
        "good morning", "good evening", "namaste"
    ]):
        return "Welcome to Scooby Pet Hostel. How may I assist you today?"

    elif any(word in user for word in [
        "price", "cost", "charges", "charge",
        "fee", "fees", "rate", "amount",
        "kitna", "boarding cost", "boarding charges"
    ]):
        return (
            "Our dog boarding charge is ₹600 per day. "
            "This includes accommodation, play time, AC environment and basic care."
        )

    elif any(word in user for word in [
        "location", "address", "where",
        "place", "located", "ajmer",
        "kaha", "kahan"
    ]):
        return "Scooby Pet Hostel is located in Ajmer, Rajasthan."

    elif any(word in user for word in [
        "service", "services", "facility",
        "facilities", "care", "provide"
    ]):
        return (
            "We provide dog boarding in a comfortable and safe environment. "
            "Dogs receive regular play time, social interaction, AC accommodation, "
            "fresh drinking water, feeding care and personal attention. "
            "We do not tie dogs and we do not keep them in cages."
        )

    elif any(word in user for word in [
        "boarding", "stay", "hostel",
        "accommodation"
    ]):
        return (
            "We provide comfortable dog boarding with supervised care, "
            "play time and a stress-free environment."
        )

    elif any(word in user for word in [
        "cage", "cages", "tie", "tied",
        "chain", "chained"
    ]):
        return (
            "No. We do not keep dogs in cages and we do not tie them. "
            "Our goal is to provide a comfortable and stress-free stay."
        )

    elif any(word in user for word in [
        "aggressive", "violent", "dangerous",
        "attack", "attacking", "bite",
        "biting", "hostile"
    ]):
        return (
            "For the safety of all pets and staff, we are currently unable "
            "to accommodate aggressive or dangerous dogs."
        )

    elif any(word in user for word in [
        "dog", "dogs", "puppy", "puppies"
    ]):
        return "Yes, we accept dogs for boarding."

    elif any(word in user for word in [
        "cat", "cats", "kitten", "kittens"
    ]):
        return (
            "Sorry, we currently provide boarding services only for dogs."
        )

    elif any(word in user for word in [
        "book", "booking", "reservation",
        "reserve", "availability"
    ]):
        return (
            "For booking and availability details, "
            "please contact Scooby Pet Hostel directly."
        )

    elif any(word in user for word in [
        "contact", "phone", "number",
        "call", "mobile"
    ]):
        return (
            "Please contact Scooby Pet Hostel for booking and service information."
        )

    elif any(word in user for word in [
        "thanks", "thank you", "thx"
    ]):
        return (
            "You're welcome. If you have any other questions, feel free to ask."
        )

    elif user in ["bye", "exit", "quit"]:
        return (
            "Thank you for contacting Scooby Pet Hostel. Have a great day."
        )

    else:
        return (
            "I may not have understood your question. "
            "You can ask about boarding charges, services, location, booking process or pet policies."
        )


def send_message():
    user_message = entry_box.get().strip()

    if user_message == "":
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, f"You: {user_message}\n\n")

    response = get_response(user_message)

    chat_area.insert(tk.END, f"{response}\n\n")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    entry_box.delete(0, tk.END)


root = tk.Tk()
root.title("Scooby Pet Hostel Assistant")

try:
    root.state("zoomed")
except:
    root.geometry("1000x700")

title = tk.Label(
    root,
    text="Scooby Pet Hostel Assistant",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 12),
    state=tk.DISABLED
)
chat_area.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

chat_area.config(state=tk.NORMAL)
chat_area.insert(
    tk.END,
    "Scooby Pet Hostel Assistant\n\n"
    "Welcome.\n\n"
    "You can ask about:\n"
    "- Boarding Charges\n"
    "- Services\n"
    "- Location\n"
    "- Booking\n"
    "- Pet Policies\n\n"
    "How may I help you today?\n\n"
)
chat_area.config(state=tk.DISABLED)

bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X, padx=15, pady=10)

entry_box = tk.Entry(
    bottom_frame,
    font=("Arial", 13)
)
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

send_button = tk.Button(
    bottom_frame,
    text="Send",
    font=("Arial", 11, "bold"),
    width=12,
    command=send_message
)
send_button.pack(side=tk.RIGHT)

entry_box.bind("<Return>", lambda event: send_message())

root.mainloop()
