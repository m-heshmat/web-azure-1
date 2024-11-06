from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For session handling and flash messages

# In-memory storage for messages (will reset when the server restarts)
messages = []

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save to in-memory list instead of database
        messages.append({
            'name': name,
            'email': email,
            'message': message
        })

        flash('Message sent successfully!')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/messages')
def view_messages():
    # Display stored messages (for demo purposes only)
    return render_template('messages.html', messages=messages)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
