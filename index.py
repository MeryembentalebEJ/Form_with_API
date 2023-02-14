from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # handle form submission
        return 'Form submitted'
    else:
        # display the form
        return '''
            <form method="post">
                <label>Name:</label><br>
                <input type="text" name="name"><br>
                <label>Email:</label><br>
                <input type="email" name="email"><br>
                <button type="submit">Submit</button>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)

