from flask import Flask
import random

random_number= random.randint(0,9)

app= Flask(__name__)

@app.route("/")
def display():

    return '<h1>Guess a number between 0 and 9 \n</h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"widht=200>'


@app.route("/<int:usernumber>")
def show_webpage(usernumber):
    if usernumber== random_number:
        return '<h1>Yes, Its correct number</h1>' \
        '<img src="https://media0.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dWx2cGpneDM5bnYzZHZyMTF6dGJ4YXpndHZuazB3MGlldzFvN3E5bSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/RrVzUOXldFe8M/200.webp">'

    elif usernumber> random_number:
        return '<h1>The number is too high</h1>' \
        '<img src="https://media2.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MWZzMDNmNXdwY3BlYmRmOGMyeGd0dGpiMXJqbDduN3kxbms2d3kxMSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/PtZzHZzuSmPCWxS5MJ/giphy.webp">'

    else:
        return '<h1>The number is too low</h1>' \
        '<img src="https://media3.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3emc4ancxNXFmbHNyZDN3YTNpM3N4endyamtpNHV1cHI5a2JrbXU5ciZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/9HQRIttS5C4Za/200.webp">'







if __name__== "__main__":
    app.run(debug=True)
