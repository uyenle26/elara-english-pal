def generate_feedback(result):
    expected_words = ["book", "cook", "would", "pool", "school", "women"]
    transcript = result["transcript"]
    matched = [word for word in expected_words if word in transcript]
    missed = list(set(expected_words) - set(matched))

    if len(missed) == 0:
        rating = "Excellent"
    elif len(missed) <= 2:
        rating = "Very Good"
    else:
        rating = "Good"

    feedback = f"""
    🌟 Elara says: You're doing great! I heard: {', '.join(matched)}.
    Let's work on: {', '.join(missed)}.
    Overall rating: {rating} 💬
    Try again and keep practicing! 🎉
    """
    return feedback
