import re
import string

# ─── Scoring Engine ──────────────────────────────────────────────────────────

def check_length(password):
    length = len(password)
    if length >= 16:
        return 3, "✅ Great length (16+ characters)"
    elif length >= 12:
        return 2, "✅ Good length (12+ characters)"
    elif length >= 8:
        return 1, "⚠️  Minimum length met (8+ characters)"
    else:
        return 0, "❌ Too short (minimum 8 characters)"


def check_uppercase(password):
    if any(c.isupper() for c in password):
        return 1, "✅ Contains uppercase letters"
    return 0, "❌ Missing uppercase letters (A-Z)"


def check_lowercase(password):
    if any(c.islower() for c in password):
        return 1, "✅ Contains lowercase letters"
    return 0, "❌ Missing lowercase letters (a-z)"


def check_digits(password):
    digit_count = sum(c.isdigit() for c in password)
    if digit_count >= 2:
        return 2, "✅ Contains multiple digits"
    elif digit_count == 1:
        return 1, "⚠️  Contains only one digit (add more)"
    return 0, "❌ Missing numbers (0-9)"


def check_special_chars(password):
    special = set(string.punctuation)
    special_count = sum(c in special for c in password)
    if special_count >= 2:
        return 2, "✅ Contains multiple special characters"
    elif special_count == 1:
        return 1, "⚠️  Contains only one special character (add more)"
    return 0, "❌ Missing special characters (!@#$%^&*...)"


def check_common_passwords(password):
    common = [
        "password", "123456", "password123", "admin", "letmein",
        "qwerty", "abc123", "monkey", "111111", "iloveyou",
        "welcome", "login", "passw0rd", "master", "hello"
    ]
    if password.lower() in common:
        return -3, "🚨 This is a very common password — change it!"
    return 0, ""


def check_repeated_chars(password):
    if re.search(r'(.)\1{2,}', password):
        return -1, "⚠️  Avoid repeating characters (e.g. 'aaa', '111')"
    return 0, ""


def check_sequential(password):
    sequences = ["abcdef", "qwerty", "123456", "654321", "fedcba"]
    lower = password.lower()
    for seq in sequences:
        if seq in lower:
            return -1, "⚠️  Avoid sequential patterns (e.g. 'abc', '123')"
    return 0, ""


# ─── Strength Evaluator ──────────────────────────────────────────────────────

def evaluate_password(password):
    total_score = 0
    feedback = []

    checks = [
        check_length(password),
        check_uppercase(password),
        check_lowercase(password),
        check_digits(password),
        check_special_chars(password),
        check_common_passwords(password),
        check_repeated_chars(password),
        check_sequential(password),
    ]

    for score, message in checks:
        total_score += score
        if message:
            feedback.append(message)

    # Determine strength label
    if total_score <= 2:
        strength = "VERY WEAK"
        color = "🔴"
        bar = "█░░░░"
    elif total_score <= 4:
        strength = "WEAK"
        color = "🟠"
        bar = "██░░░"
    elif total_score <= 6:
        strength = "MODERATE"
        color = "🟡"
        bar = "███░░"
    elif total_score <= 8:
        strength = "STRONG"
        color = "🟢"
        bar = "████░"
    else:
        strength = "VERY STRONG"
        color = "💪"
        bar = "█████"

    return {
        "score": total_score,
        "strength": strength,
        "color": color,
        "bar": bar,
        "feedback": feedback,
    }


# ─── Suggestions ─────────────────────────────────────────────────────────────

def get_suggestions(result):
    suggestions = []
    feedback_text = " ".join(result["feedback"])

    if "Too short" in feedback_text or "Minimum length" in feedback_text:
        suggestions.append("→ Make your password at least 12 characters long")
    if "uppercase" in feedback_text and "Missing" in feedback_text:
        suggestions.append("→ Add uppercase letters like A, B, C...")
    if "lowercase" in feedback_text and "Missing" in feedback_text:
        suggestions.append("→ Add lowercase letters like a, b, c...")
    if "numbers" in feedback_text or "digit" in feedback_text:
        suggestions.append("→ Include numbers like 3, 7, 9...")
    if "special" in feedback_text and "Missing" in feedback_text:
        suggestions.append("→ Add special characters like @, #, $, !")
    if "common password" in feedback_text:
        suggestions.append("→ Choose a completely unique password")

    if not suggestions and result["strength"] in ["VERY STRONG", "STRONG"]:
        suggestions.append("→ Great job! Your password is secure 🎉")

    return suggestions


# ─── Display ─────────────────────────────────────────────────────────────────

def display_result(password, result):
    print("\n" + "=" * 50)
    print(f"  Password : {'*' * len(password)}")
    print(f"  Strength : {result['color']} {result['strength']}")
    print(f"  Score    : {result['score']} points")
    print(f"  Meter    : [{result['bar']}]")
    print("=" * 50)

    print("\n📋 Analysis:")
    for item in result["feedback"]:
        print(f"   {item}")

    suggestions = get_suggestions(result)
    if suggestions:
        print("\n💡 Suggestions:")
        for s in suggestions:
            print(f"   {s}")

    print()


# ─── Main Program ─────────────────────────────────────────────────────────────

def run_checker():
    print("=" * 50)
    print("   🔐 Password Strength Checker")
    print("   Check how secure your password is!")
    print("   Type 'quit' to exit")
    print("=" * 50)

    while True:
        try:
            password = input("\nEnter password: ").strip()

            if password.lower() == "quit":
                print("👋 Stay secure out there!")
                break

            if not password:
                print("⚠️  Please enter a password.")
                continue

            result = evaluate_password(password)
            display_result(password, result)

            another = input("Check another password? (yes/no): ").strip().lower()
            if another not in ["yes", "y"]:
                print("👋 Stay secure out there!")
                break

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break


# ─── Entry Point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_checker()
