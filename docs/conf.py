project = 'Ancestry'
author = 'Your Name'
release = '1.0'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'

html_static_path = ['_static']

# Add extra files (like robots.txt) that should be copied to the root of the output
html_extra_path = ['_static/robots.txt']

# Optional: If you want to keep the chatbot (but note: .js files in html_static_path are fine)
html_js_files = [
    'chatbot.js',
]

# Optional but recommended: favicon should be a relative path inside _static/
# html_favicon = '_static/favicon.png'   # ← fix: add _static/ prefix if the file is there

# Optional: Help control Sphinx version compatibility if needed
# needs_sphinx = '8.2'
