good_deeds = {
    "today": [
        "Make a compliment to a friend",
        "Call your grandparents",
        "Embrace parents",
    ],
    "tomorrow": [
        "Feed the birds in the park",
        "Give unnecessary things to those who need them",
        "Smile",
    ],
}

for day, deeds in good_deeds.items():
    print(f"{day}:")
    for deed in deeds:
        print(deed)