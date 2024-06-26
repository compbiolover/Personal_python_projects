import random
import os

def get_affirmation():
    affirmations = [
        "I am worthy of love, respect, and kindness.",
        "Every day, I become stronger and more resilient.",
        "I believe in myself and my abilities.",
        "I am constantly growing and evolving.",
        "I am deserving of happiness and success.",
        "I am in control of my thoughts, feelings, and actions.",
        "Challenges are opportunities for growth.",
        "I am surrounded by love and support.",
        "My past does not define me; it strengthens me.",
        "I embrace change and trust the journey.",
        "I am capable of achieving my dreams and goals.",
        "I am deserving of all the good things life has to offer.",
        "I am a beacon of positivity and light.",
        "My potential is limitless.",
        "I am enough, just as I am.",
        "I attract positive energy and opportunities into my life.",
        "Every experience in my life helps me grow.",
        "I am deserving of abundance in all areas of my life.",
        "I release all doubts and fears and embrace confidence.",
        "My journey is unique and valuable."
    ]
    
    return random.choice(affirmations)

def display_notification(message):
    os.system(f'/usr/bin/osascript -e \'display notification "{message}" with title "Positive Affirmation"\'')

if __name__ == "__main__":
    affirmation = get_affirmation()
    display_notification(affirmation)
