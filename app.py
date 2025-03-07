from flask import Flask, render_template, request, redirect, url_for, flash, session
import random
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default-secret-key-for-development')

# Flag to track if we should try to use the AI model
use_ai_model = True

# Try to import and initialize the text generation pipeline
try:
    from transformers import pipeline
    # Using a smaller model with ONNX runtime
    generator = pipeline('text-generation', model='distilgpt2')
    text_generation_available = True
    logger.info("Hugging Face text generation model loaded successfully")
except Exception as e:
    text_generation_available = False
    logger.error(f"Failed to load text generation model: {e}")

# Fallback templates if AI generation fails
templates = [
    "The {} whispers secrets\nIn the depths of my heart\nLike {} waves crashing\nWe shall never part",
    "Beneath the {} sky\nI wander through fields of {}\nTime stands still",
    "In the realm of {}\nWhere {} dreams come alive\nI find my peace",
    "The {} dances\nAmong the shadows of {}\nEternal bliss",
    "When {} falls\nAnd {} rises\nThe world transforms",
    "Whispers of {} echo\nThrough corridors of {}\nMemories linger",
    "The {} of yesterday\nMeets the {} of tomorrow\nTime intertwines",
    "Silent {} waits\nAs {} unfolds its secrets\nWisdom revealed",
    "Mountains of {} rise\nValleys of {} below\nNature's balance",
    "Through the mist of {}\nI search for the essence of {}\nEndless journey"
]

def generate_ai_poem(prompt, style=None):
    """
    Generate a poem using Hugging Face's text generation model.
    
    Args:
        prompt (str): The user's input to incorporate into the poem
        style (str, optional): The style of poem to generate (e.g., "haiku", "sonnet")
        
    Returns:
        str: The generated poem or None if generation failed
    """
    try:
        if not text_generation_available or not use_ai_model:
            logger.warning("Text generation model not available, falling back to templates")
            return None
            
        style_text = f" in the style of a {style}" if style else ""
        
        # Create a poetry-specific prompt
        full_prompt = f"Write a short poem about {prompt}{style_text}:\n\n"
        
        # Generate text
        outputs = generator(
            full_prompt, 
            max_length=100, 
            num_return_sequences=1, 
            temperature=0.8,
            top_k=50,
            do_sample=True
        )
        
        # Extract the generated text and remove the prompt
        generated_text = outputs[0]['generated_text']
        poem = generated_text.replace(full_prompt, "").strip()
        
        # Clean up the poem (remove incomplete sentences at the end)
        lines = poem.split('\n')
        
        # If we have a very short result, fall back to templates
        if len(lines) < 2:
            logger.warning("Generated poem too short, falling back to templates")
            return None
            
        return poem
            
    except Exception as e:
        logger.error(f"Error generating AI poem: {e}")
        return None

def generate_template_poem(user_input):
    """
    Generate a poem using predefined templates.
    
    Args:
        user_input (str): The user's input to incorporate into the template
        
    Returns:
        str: The generated poem
    """
    # Select a random template
    template = random.choice(templates)
    
    # Replace all placeholders with the user input
    poem = template.format(user_input, user_input)
    
    return poem

@app.route('/')
def index():
    """Render the home page with the input form."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Process the form submission and generate a poem."""
    user_input = request.form.get('user_input', '').strip()
    poem_style = request.form.get('poem_style', None)
    
    # Validate input
    if not user_input:
        flash('Please enter a word or phrase to generate a poem.')
        return redirect(url_for('index'))
    
    # Try to generate an AI poem first
    poem = generate_ai_poem(user_input, poem_style)
    
    # If AI generation failed, fall back to template-based generation
    if poem is None:
        poem = generate_template_poem(user_input)
        session['ai_generated'] = False
        logger.info(f"Generated template-based poem for input: '{user_input}'")
    else:
        session['ai_generated'] = True
        logger.info(f"Generated AI poem for input: '{user_input}' with style: '{poem_style}'")
    
    # Store the poem in the session
    session['poem'] = poem
    session['user_input'] = user_input
    session['poem_style'] = poem_style
    
    return redirect(url_for('result'))

@app.route('/result')
def result():
    """Display the generated poem."""
    # Retrieve the poem from the session
    poem = session.get('poem', None)
    user_input = session.get('user_input', None)
    ai_generated = session.get('ai_generated', False)
    poem_style = session.get('poem_style', None)
    
    if not poem or not user_input:
        flash('Something went wrong. Please try again.')
        return redirect(url_for('index'))
    
    return render_template('result.html', 
                          poem=poem, 
                          user_input=user_input, 
                          ai_generated=ai_generated,
                          poem_style=poem_style)

if __name__ == '__main__':
    # Check for required environment variables
    if not os.getenv('SECRET_KEY'):
        logger.warning("SECRET_KEY not set. Using default development key.")
        
    app.run(debug=True)