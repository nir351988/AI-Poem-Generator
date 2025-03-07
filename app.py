from flask import Flask, render_template, request, flash, redirect, url_for
import logging
import random

app = Flask(__name__)
# Secret key for session management (for flashing messages)
app.secret_key = "supersecretkey"

# Configure basic logging
logging.basicConfig(level=logging.INFO)

def dummy_ai_response(user_input):
    """
    Generate a short poem based on the input.
    """
    # Clean input text
    clean_input = user_input.strip()
    
    # List of poem templates
    poem_templates = [
        f"{clean_input} in the morning light,\nShining bright, a beautiful sight.\nWhispers of the wind, so free,\n{clean_input} brings joy to me.",
        f"Under the sky so blue,\n{clean_input} comes into view.\nWith a heart so true,\n{clean_input} makes dreams come true.",
        f"In the garden of delight,\n{clean_input} blooms in the night.\nWith petals soft and bright,\n{clean_input} is a lovely sight.",
        f"On a journey far and wide,\n{clean_input} by my side.\nThrough the valleys we glide,\n{clean_input} is my guide.",
        f"By the river's gentle flow,\n{clean_input} begins to grow.\nWith a gentle glow,\n{clean_input} sets my heart aglow.",
        f"{clean_input} dances in the breeze,\nAmong the autumn leaves.\nA symphony of colors,\n{clean_input} never deceives.",
        f"High above the mountains,\n{clean_input} takes its flight.\nWith wings of inspiration,\n{clean_input} ignites the night.",
        f"In the depths of the forest,\n{clean_input} whispers softly.\nA tale of ancient times,\n{clean_input} speaks to me.",
        f"Across the endless ocean,\n{clean_input} sails so free.\nWith dreams of distant lands,\n{clean_input} calls to me.",
        f"Underneath the starlit sky,\n{clean_input} shines so bright.\nA beacon in the darkness,\n{clean_input} is my light."
    ]
    
    # Select a random poem template
    poem = random.choice(poem_templates)
    
    return poem

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Render the home page with a form for text input.
    On POST, validates the input and redirects appropriately.
    """
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        
        if not user_input.strip():
            flash("Please enter some valid text!", "danger")
            return redirect(url_for("index"))
        
        return redirect(url_for("process", user_input=user_input))
    
    return render_template("index.html")

@app.route("/process")
def process():
    """
    Process input text to generate a poem and render the result.
    """
    user_input = request.args.get("user_input", "")
    ai_poem = dummy_ai_response(user_input)
    logging.info("Processing input: %s", user_input)
    return render_template("result.html", user_input=user_input, ai_poem=ai_poem)

if __name__ == "__main__":
    # Run the Flask development server.
    app.run(debug=True)