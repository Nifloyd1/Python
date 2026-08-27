import time

def decide_strength(length, caps, numbers, special):
    score = 0
    suggestions = []

   
    if length >= 12:
        score += 4
        print("\n\nBimothy says... Length is Strong!")
    elif length >= 8:
        score += 3
        print("\n\nBimothy says... Length is Mid!")
        suggestions.append("Increase length to 12+ characters")
    elif length >= 6:
        score += 2
        print("\n\nBimothy says... Length is Weak!")
        suggestions.append("Increase length to at least 8–12 characters")
    else:
        score += 1
        print("\n\nBimothy says... Did you even try?")
        suggestions.append("Make your password longer (minimum 8 characters)")

    time.sleep(1)

    if caps > 0:
        score += 2
        print("\n\nBimothy says... Capital letter is present!")
    else:
        print("\n\nBimothy says... No capital letters found!")
        suggestions.append("Add at least one capital letter")

    time.sleep(1)

    if numbers:
        score += 2
        print("\n\nBimothy says... Number detected!")
    else:
        print("\n\nBimothy says... No numbers found!")
        suggestions.append("Include at least one number")

    time.sleep(1)

    # SPECIAL (always runs)
    if special:
        score += 2
        print("\n\nBimothy says... Special character detected!")
    else:
        print("\n\nBimothy says... No special characters found!")
        suggestions.append("Add a special character (e.g. !, @, #)")

    return score, suggestions
    
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~Bimothy's Password Checker~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    try:
        pwd = input("\n Type Your Password Here and Bimothy's Personal Assitant will check it ASAP\n> ")
        
        #Length Check
        length = len(pwd)
        #Caps Check
        caps = sum(1 for char in pwd if char.isupper())
        #Numbers?
        numbers = any(char.isdigit() for char in pwd) 
        #Special Characters?
        special = any(not char.isalnum() and not char.isspace() for char in pwd)
        #This will give us out final rating 1/10.
        strength, suggestions = decide_strength(length, caps, numbers, special)
        
        print(f"\nPassword Strength: {strength}/10")
        
        if suggestions:
            print(f"\nTips:")
            for s in suggestions:
                print(f"- {s}")
        else:
            print("\nBimothy says your password is good to use!")
    except:
        break
    