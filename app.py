from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world()
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

    # Introduce a NameError
    # return undefined_variable

    # Introduce a TypeError
    # return 5 + "hello"

    # Introduce a ZeroDivisionError
    return 1 / 0

    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)