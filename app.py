from flask import Flask, render_template

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('Biodata.html')

if __name__ == '__main__':
    app.run(debug=True)
