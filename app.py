# from flask import Flask, request, render_template
# import joblib
# from catboost import CatBoostRegressor

# app = Flask(__name__)

# # Load model
# model = joblib.load('model_denda1.pkl')

# # Fungsi untuk prediksi denda
# def prediksi_denda(jenis_kendaraan, pasal, usia, hakim_code):
#     try:
#         input_data = [[jenis_kendaraan, pasal, usia, hakim_code]]
#         prediksi = model.predict(input_data)
#         return round(prediksi[0], 2)
#     except Exception as e:
#         return f"Error: {str(e)}"

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     hasil = None 
#     error_message = None 
#     jenis_kendaraan_label = None
#     hakim_label = None
#     pasal = None
#     usia = None

#     # Mapping kode ke label
#     jenis_kendaraan_map = {
#         0: "Bus",
#         1: "Mobil Barang/Pick Up",
#         2: "Mobil Penumpang Pribadi",
#         3: "Mobil Penumpang Umum",
#         4: "Sepeda Motor",
#         5: "Tronton",
#         6: "Truk",
#         7: "Truk Gandeng"
#     }

#     hakim_map = {
#         0: "Achmad Ukayat, S.H.,M.H.",
#         1: "Adil Hakim, S.H.,M.H.",
#         2: "Adrianus Agung Putrantono, S.H.",
#         3: "Agam Syarief Baharudin, S.H.,M.H.",
#         4: "Ambo Masse, S.H.,M.H.",
#         5: "Andi Eddy Viyata, S.H.,M.H.",
#         6: "Asep Sumirat Danaatmaja, S.H.,M.H.",
#         7: "Asmudi, S.H.,M.H.",
#         8: "Astea Bidarsari, S.H.,M.H.",
#         9: "Bambang Ariyanto, S.H.,M.H.",
#         10: "Catur Prasetyo, S.H.,M.H.",
#         11: "Dame Parulian Pandiangan, S.H.",
#         12: "Daru Swastika Rini, S.H.",
#         13: "Dinahayati Syofyan, S.H., M.H.",
#         14: "Dr. Abdul Aziz, S.H., M.Hum.",
#         15: "Dwi Sugianto, S.H., M.H.",
#         16: "Eka Ratnawidiastuti, S.H., M.Hum.",
#         17: "Erven Langgeng Kaseh, S.H., M.H.",
#         18: "Eryusman, S.H.",
#         19: "Fauziah Hanum Harahap, S.H., Mh.",
#         20: "Fauziah Hanum, S.H.,M.H.",
#         21: "Firlana Trisnila, S.H.",
#         22: "Firza Andriansyah, S.H. M.H.",
#         23: "Heny Faridha, S.H., M.H.",
#         24: "Heru Dinarto, S.H., M.H.",
#         25: "Idi Il Amin, S.H.,M.H.",
#         26: "Ika Lusiana Riyanti, S.H.",
#         27: "Ikhwan Hendrato, S.H., M.H.",
#         28: "Itong Isnaeni Hidayat, S.H., M.H.",
#         29: "Jasael, S.H., M.H.",
#         30: "Joko Dwi Atmoko, S.H.,M.H.",
#         31: "Kukuh Kalinggo Yuwono, S.H., M.H.",
#         32: "Kusman, S.H., M.H.",
#         33: "Maju Purba, S.H.",
#         34: "Muhamad Martin Helmy, S.H., M.H.",
#         35: "Nendi Rusnendi, S.H.",
#         36: "Nenny Ekawaty Barus, S.H.,M.H.",
#         37: "Novie Ermawati, S.H.",
#         38: "Nurhayati Nasution, S.H., M.H.",
#         39: "Ojo Sumarna, S.H., M.H.",
#         40: "Oktafiatri Kusumaningsih, S.H., M.Hum.",
#         41: "Panji Surono, S.H., M.H.",
#         42: "Raden Zaenal Arief, S.H., M.H.",
#         43: "Renaldo Meiji Hasoloan Tobing, S.H., M.H.",
#         44: "Ristati, S.H., M.H.",
#         45: "Riyanti Desiwati, S.H., M.H.",
#         46: "Rudita Setya Hermawan, S.H., M.H.",
#         47: "Saputro Handoyo, S.H., M.H.",
#         48: "Saut Erwin Hartono A. Munthe, S.H., M.H.",
#         49: "Sigit Pradewa, S.H., M.H.",
#         50: "Siswatmono Radiantoro, S.H.",
#         51: "Siti Hamidah, S.H., M.H.",
#         52: "Sri Asmarani, S.H., C.N.",
#         53: "Susilo Utomo, S.H.",
#         54: "Suwandi, S.H., M.H.",
#         55: "Syihabuddin, S.H., M.H.",
#         56: "Tarima Saragih, S.H., M.Hum.",
#         57: "Teguh Arifiano, S.H., M.H.",
#         58: "Titi Maria Romlah, S.H.",
#         59: "Tohari Tapsirin, Bc.Ip. S.H., M.H.",
#         60: "Ujang Irfan Hadiana, S.H.",
#         61: "Unggul Ahmadi, S.H., M.H.",
#         62: "Vici Daniel Valentino, S.H., M.H.",
#         63: "Wiyono, S.H.",
#         64: "Yose Ana Roslinda, S.H., M.H.",
#         65: "Yusuf Syamsuddin, S.H., M.H."
#     }

#     if request.method == 'POST':
#         # Ambil data input dari form
#         jenis_kendaraan = request.form.get('Jenis Kendaraan Code')
#         pasal = request.form.get('Pasal')
#         usia = request.form.get('Usia')
#         hakim_code = request.form.get('Hakim Code')

#         # Validasi input: pastikan semua kolom tidak kosong
#         if not jenis_kendaraan or not pasal or not usia or not hakim_code:
#             error_message = "Semua kolom input harus diisi!"
#         else:
#             try:
#                 # Konversi input menjadi angka
#                 jenis_kendaraan = int(jenis_kendaraan)
#                 pasal = int(pasal)
#                 usia = int(usia)
#                 hakim_code = int(hakim_code)

#                 # Ambil label dari mapping
#                 jenis_kendaraan_label = jenis_kendaraan_map.get(jenis_kendaraan, "Tidak Diketahui")
#                 hakim_label = hakim_map.get(hakim_code, "Tidak Diketahui")

#                 # Prediksi hanya dijalankan jika semua input valid
#                 hasil = prediksi_denda(jenis_kendaraan, pasal, usia, hakim_code)
#             except ValueError:
#                 error_message = "Semua input harus berupa angka valid!"

#     # Kirim hasil dan error_message ke template
#     return render_template(
#         'index.html',
#         hasil=hasil,
#         error_message=error_message,
#         jenis_kendaraan_label=jenis_kendaraan_label,
#         pasal=pasal,
#         usia=usia,
#         hakim_label=hakim_label
#     )


# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template
import joblib
from catboost import CatBoostRegressor

app = Flask(__name__)

# Load model
model = joblib.load('model_denda1.pkl')

# Fungsi untuk prediksi denda
def prediksi_denda(jenis_kendaraan, pasal, usia, hakim_code):
    try:
        input_data = [[jenis_kendaraan, pasal, usia, hakim_code]]
        prediksi = model.predict(input_data)
        return round(prediksi[0], 2)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None 
    error_message = None 
    jenis_kendaraan_label = None
    hakim_label = None
    pasal = None
    usia = None

    # Mapping kode ke label
    jenis_kendaraan_map = {
        0: "Bus",
        1: "Mobil Barang/Pick Up",
        2: "Mobil Penumpang Pribadi",
        3: "Mobil Penumpang Umum",
        4: "Sepeda Motor",
        5: "Tronton",
        6: "Truk",
        7: "Truk Gandeng"
    }

    hakim_map = {
        0: "Achmad Ukayat, S.H.,M.H.",
        1: "Adil Hakim, S.H.,M.H.",
        2: "Adrianus Agung Putrantono, S.H.",
        3: "Agam Syarief Baharudin, S.H.,M.H.",
        4: "Ambo Masse, S.H.,M.H.",
        5: "Andi Eddy Viyata, S.H.,M.H.",
        6: "Asep Sumirat Danaatmaja, S.H.,M.H.",
        7: "Asmudi, S.H.,M.H.",
        8: "Astea Bidarsari, S.H.,M.H.",
        9: "Bambang Ariyanto, S.H.,M.H.",
        10: "Catur Prasetyo, S.H.,M.H.",
        11: "Dame Parulian Pandiangan, S.H.",
        12: "Daru Swastika Rini, S.H.",
        13: "Dinahayati Syofyan, S.H., M.H.",
        14: "Dr. Abdul Aziz, S.H., M.Hum.",
        15: "Dwi Sugianto, S.H., M.H.",
        16: "Eka Ratnawidiastuti, S.H., M.Hum.",
        17: "Erven Langgeng Kaseh, S.H., M.H.",
        18: "Eryusman, S.H.",
        19: "Fauziah Hanum Harahap, S.H., Mh.",
        20: "Fauziah Hanum, S.H.,M.H.",
        21: "Firlana Trisnila, S.H.",
        22: "Firza Andriansyah, S.H. M.H.",
        23: "Heny Faridha, S.H., M.H.",
        24: "Heru Dinarto, S.H., M.H.",
        25: "Idi Il Amin, S.H.,M.H.",
        26: "Ika Lusiana Riyanti, S.H.",
        27: "Ikhwan Hendrato, S.H., M.H.",
        28: "Itong Isnaeni Hidayat, S.H., M.H.",
        29: "Jasael, S.H., M.H.",
        30: "Joko Dwi Atmoko, S.H.,M.H.",
        31: "Kukuh Kalinggo Yuwono, S.H., M.H.",
        32: "Kusman, S.H., M.H.",
        33: "Maju Purba, S.H.",
        34: "Muhamad Martin Helmy, S.H., M.H.",
        35: "Nendi Rusnendi, S.H.",
        36: "Nenny Ekawaty Barus, S.H.,M.H.",
        37: "Novie Ermawati, S.H.",
        38: "Nurhayati Nasution, S.H., M.H.",
        39: "Ojo Sumarna, S.H., M.H.",
        40: "Oktafiatri Kusumaningsih, S.H., M.Hum.",
        41: "Panji Surono, S.H., M.H.",
        42: "Raden Zaenal Arief, S.H., M.H.",
        43: "Renaldo Meiji Hasoloan Tobing, S.H., M.H.",
        44: "Ristati, S.H., M.H.",
        45: "Riyanti Desiwati, S.H., M.H.",
        46: "Rudita Setya Hermawan, S.H., M.H.",
        47: "Saputro Handoyo, S.H., M.H.",
        48: "Saut Erwin Hartono A. Munthe, S.H., M.H.",
        49: "Sigit Pradewa, S.H., M.H.",
        50: "Siswatmono Radiantoro, S.H.",
        51: "Siti Hamidah, S.H., M.H.",
        52: "Sri Asmarani, S.H., C.N.",
        53: "Susilo Utomo, S.H.",
        54: "Suwandi, S.H., M.H.",
        55: "Syihabuddin, S.H., M.H.",
        56: "Tarima Saragih, S.H., M.Hum.",
        57: "Teguh Arifiano, S.H., M.H.",
        58: "Titi Maria Romlah, S.H.",
        59: "Tohari Tapsirin, Bc.Ip. S.H., M.H.",
        60: "Ujang Irfan Hadiana, S.H.",
        61: "Unggul Ahmadi, S.H., M.H.",
        62: "Vici Daniel Valentino, S.H., M.H.",
        63: "Wiyono, S.H.",
        64: "Yose Ana Roslinda, S.H., M.H.",
        65: "Yusuf Syamsuddin, S.H., M.H."
    }


    if request.method == 'POST':
        # Ambil data input dari form
        jenis_kendaraan = request.form.get('Jenis Kendaraan Code')
        pasal = request.form.get('Pasal')
        usia = request.form.get('Usia')
        hakim_code = request.form.get('Hakim Code')

        # Validasi input: pastikan semua kolom tidak kosong
        if not jenis_kendaraan or not pasal or not usia or not hakim_code:
            error_message = "Semua kolom input harus diisi!"
        else:
            try:
                # Konversi input menjadi angka
                jenis_kendaraan = int(jenis_kendaraan)
                pasal = int(pasal)
                usia = int(usia)
                hakim_code = int(hakim_code)

                # Ambil label dari mapping
                jenis_kendaraan_label = jenis_kendaraan_map.get(jenis_kendaraan, "Tidak Diketahui")
                hakim_label = hakim_map.get(hakim_code, "Tidak Diketahui")

                # Prediksi hanya dijalankan jika semua input valid
                hasil = prediksi_denda(jenis_kendaraan, pasal, usia, hakim_code)
            except ValueError:
                error_message = "Semua input harus berupa angka valid!"

    # Kirim hasil dan error_message ke template
    return render_template(
        'index.html',
        hasil=hasil,
        error_message=error_message,
        jenis_kendaraan_label=jenis_kendaraan_label,
        pasal=pasal,
        usia=usia,
        hakim_label=hakim_label
    )

# Ini diperlukan oleh Vercel untuk mengenali WSGI
# app = app
if __name__ == '__main__':
    app.run()
