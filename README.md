# Simple Game Character Status — The Arena

## Deskripsi

Mini-project Python Chapter 5 berdasarkan pembelajaran *Python Crash Course (3rd Edition)*.

Program ini menentukan arena yang dapat dimasuki pemain berdasarkan level, kepemilikan rare item, dan status legend. Program menggunakan data 13 pemain dan menampilkan hasil penentuan arena melalui terminal.

## Aturan Arena

|                      Kondisi                  |             Arena             |
|                        ---                    |              ---              |
| Level ≥ 35 dan memiliki rare item             | The Complex Iron Amphitheater |
| Level ≥ 35 tanpa rare item                    | The Blood Sands               |
| Level 20–34 dan memiliki rare item            | The Abyssal Ring              |
| Level 20–34 tanpa rare item                   | Valor Dome                    |
| Level = 10                                    | The Omega Zone                |
| Level 11–19 dan memiliki rare item            | The Vortex Dome               |
| Level 11–19 tanpa rare item                   | The Iron Gridiron             |
| Level 6–9 dan memiliki rare item              | The Valhalla’s Crucible       |
| Level 6–9 tanpa rare item                     | Ashen Crater                  |
| Level 1–5 dengan rare item dan status legend  | The Valhalla’s Crucible       |
| Level 1–5 tanpa memenuhi kedua syarat khusus  | Training                      |

## Konsep Python

- **Dictionary:** menyimpan informasi pemain.
- **List:** menyimpan data pemain, item, dan rare item.
- **For loop:** memproses informasi setiap pemain.
- **If, elif, dan else:** menentukan arena berdasarkan kondisi.
- **Comparison operators:** membandingkan level pemain.
- **Logical operator `and`:** memastikan beberapa kondisi terpenuhi sekaligus.
- **Set intersection (`&`):** mencari kesamaan item pemain dengan daftar rare item dan memeriksa status legend.
- **F-string:** menampilkan informasi pemain dan hasil akses arena.

## Teknologi

- Python 3.12.13
- Visual Studio Code

## Cara Menjalankan

1. Pastikan Python sudah terpasang.
2. Buka file program Python di Visual Studio Code.
3. Jalankan melalui terminal menggunakan perintah:

   ```bash
   python nama_file.py
   ```

   Ganti `nama_file.py` dengan nama file program yang sebenarnya.

4. Periksa hasil penentuan arena di terminal.

## Tujuan Pembelajaran

Melatih pemahaman tentang conditional tests, comparison operators, logical operators, perulangan, dan struktur data dasar Python melalui simulasi penentuan akses arena.

Project ini merupakan latihan pembelajaran berbasis terminal, bukan game dengan antarmuka interaktif.