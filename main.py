from flask import Flask, render_template, request
from blockchain import write_block, validate

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pemilik = request.form.get('pemilik')
        penyewa = request.form.get('penyewa')
        lokasi = request.form.get('lokasi')
        harga = request.form.get('harga')

        write_block(pemilik=pemilik, penyewa=penyewa, lokasi=lokasi, harga=harga)

    return render_template('index.html')


@app.route('/checking')
def check():
    results = validate()
    return render_template('index.html', checking_results=results)

if __name__ == '__main__':
    app.run(debug=True)

