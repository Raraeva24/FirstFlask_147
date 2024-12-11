from flask import Flask, render_template, request  # Import Flask dan modul yang dibutuhkan

app = Flask(__name__)  # Inisialisasi aplikasi Flask

@app.route('/')  # Route untuk halaman utama (/) -> tampilan awal
def index(): ##fungi index
    return render_template('index.html')  # Render file HTML "index.html" untuk halaman utama

@app.route('/submit', methods=['POST'])  # Route untuk menangani form yang dikirim dari halaman utama
def submit(): #fungsi supmit
    # Ambil data dari input form (dengan nama field 'name')
    name = request.form.get('name')
    # Render file "submit.html" sambil kirimkan data nama yang diambil
    return render_template('submit.html', name=name)

if __name__ == '__main__':  # Blok buat memastikan kode hanya berjalan kalau file ini dijalanin langsung
    app.run(debug=True)  # jalanin aplikasi Flask dalam mode debug (biar gampang cek error)
