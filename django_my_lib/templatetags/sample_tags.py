
import time

from django import template

# Create an instance of the template library
register = template.Library()


# Use the simple_tag decorator to register the function as a template tag
@register.simple_tag
def show_today_timestamp():
    """
    Returns the current Unix timestamp (seconds since epoch).
    """
    # time.time() returns the timestamp as a float
    timestamp = int(time.time())

    # mark_safe is optional here, but it's good practice if the output were raw HTML
    return str(timestamp)


# --- Example of how you would do it if the tag needed arguments ---
@register.simple_tag
def greeting(name):
    """Returns a personalized greeting."""
    return f"Hello, {name}!"
