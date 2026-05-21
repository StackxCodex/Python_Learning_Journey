import random
# affirmation quotes list
affirmation_quotes = [
    " ✨ I don’t chase opportunities — my skills create them.",
    "💻 Pretty girls debug too.",
    "👩🏽‍💻 Every line of code I write changes my future.",
    "💎 I bring luxury energy into every project I touch.",
    "🚀 I am becoming the woman I once dreamed about.",
    "🧠 Beauty and intelligence exist perfectly within me.",
    "✨ My creativity and tech skills make room for abundance.",
    "💻 I code with confidence, clarity, and purpose.",
    "👑 I belong in every tech space I enter.",
    "🌸 Soft life, sharp mind, powerful skills.",
    "⚡ I turn ideas into income and vision into reality.",
    "💖 I am the blueprint for the next generation of tech girlies.",
    "👩🏽‍💻 My future is built one commit at a time.",
    "✨ I can learn anything I dedicate myself to.",
    "💻 Smart is sexy.",
    "🚀 I attract success, opportunities, and aligned collaborations.",
    "💎 My presence is powerful both online and offline.",
    "🧠 I am disciplined, focused, and unstoppable.",
    "🌷 Coding is my superpower.",
    "👑 I deserve luxury, success, and freedom.",
    "💻 I’m not “trying” tech — I’m mastering it.",
    "✨ My goals are valid, achievable, and already unfolding.",
    "⚡ I glow differently because I build differently.",
    "💖 Tech isn’t just my career — it’s my elevation story.",
    "👩🏽‍💻 I am building a legacy through technology.",
    "💎 The more I learn, the more powerful I become.",
    "🚀 Millionaire coder mindset activated.",
    "🌸 I romanticize growth, discipline, and self-investment.",
    "💻 My intelligence opens doors no one can close.",
    "👑 StackxCodex is more than a brand — it’s a movement.",
]


def generate_affirmation():
    #pick a random affirmation quote from the list
    return random.choice(affirmation_quotes)


print("---Affirmation Quote Generator---")
print(generate_affirmation())
