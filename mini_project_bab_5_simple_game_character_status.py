# Pembuatan struktur data nama karakter

# ### = artinya --> kode eksperimen yang sudah di gunakan, tapi harus dinonaktifkan karena kira harus fokus dengan arena utama 
# final version yang dipakai orang-orang. 

# karakter = ["ZeldaVivos", "PangeranPrice", "Mekaliniop"] ### 1

# Pembuatan struktur data umur karakter

# usia_karakter = []

"""
Gpt ini kita lagi bikin game RP ya ? Jadi kayak gabungan antara data informasi pribadi di dunia nyata dan data informasi
karakter di game kita, terus informasi tersebut dijadikan dasar seberapa banyak akses kamu terhadap apa yang ada di game tersebut.
Begitu ya ? Soalnya ada usia gitu wkwkwkkw. Gimana kalau misal-nya saya rubah konsep usia jadi level ? Biar judgment di game
berdasarkan informasi yang tersedia yang ada di dalam game / apa yang kamu lakukan dan perbuat di game, 
bukan-nya menarik informasi pribadi tersebut ke dalam game untuk judgment player di game. Sangat mind blowing sekali sih. 
Kamu juga sih gak memberikan yang spesifik ini game apa dan game ini mau bagaimana, saya jadi harus melakukan pengembangan
game sendiri berdasarkan requiement dari kamu, bukan dari saya.

Oke saya sudah memutuskan saya akan merubah usia menjadi level ya. Dan lihat selanjutnya saya akan bikin game-nya ini
seperti apa ya.

"""

# level_karakter = [11, 3, 27] ### 1

# Akses khusus

# karakter_khusus = ["ZeldaVivos"] ### 1

# Daftar item

# item = ["Luciana", "HunterSword", "AxeGigantorus"] ### 1

# Pintu masuk Arena XhampionWarf

# for karak in karakter: ### 1
#     if karak in karakter_khusus: ### 1
#        print(f"Silahkan Masuk {karak}. Persiapkan mental kamu 😈") ### 1

# Gpt karena saya bingung bagaimana mekanisme game yang kamu maksud seperti apa dan arah-nya kemana. Saya jadi butuh konsep
# nested dictionary untuk menyatukan nama karakter dan level serta item yang dia punya untuk masuk server yang lebih elit gitu.
# Saya gak kepikiran bagaimana memanfaatkan bab 5 untuk konsep game saya sendiri. Maka dari itu saya membutuhkan konsep 
# di luar bab 5 untuk memaksimalkan game saya.

 #player_information = { ### 1
#                     "player_1" : {"name" : "ZeldaVivos" ,"Level" : 11, "Item" : ["Huntersowrd", "Luciana", "Bomber"]},
#                     "player_2" : {"name" : "PangeranPrice", "Level" : 7, "Item" : ["Voidbringer", "Vanguard's, Bulwark", "Celestial Aegis"]},
#                     "player_3" : {"name" : "Mekaliniop", "Level" : 37, "Item" : ["Chronos Heart", "Rune of Undying", "Elixir of the Phoenix"]}
#                     }

# strong_items = ["Huntersowrd", "Voidbringer", "Elixir of the Phoenix", "Stardust Nectar", "Dreadnought Plate"] ### 1

# The Eliter Apex Coliseum # The Greatest Arena

# for player, information in player_information.items(): ### 1
#    match = set(strong_items) & set(information["Item"]) ### 1
#    if match: ### 1
#        print(f"Berhasil: {information['name']} memiliki skill {match}!") ### 1
#        print(f"-------{information['name']} dipersilahkan masuk ke dunia The Eliter Apex Coliseum.") ### 1
#    else: ### 1
#        print("I'm Sorry Buddy. You To Young.") ### 1

# Gpt sebelum saya lanjut saya mau curhat dulu. Berjam-jam saya ingin membuat sistem yang bisa menampilkan bahwa player cocok 
# dan diperbolehkan masuk ke server elite dengan bantuan AI Model Google. Dan saya dibantu atas materi-materi pendukung yang 
# dapat membantu saya menyelsaikan dengan baik dan pengembangan sendiri. Saya ingin membuat game saya untuk project bab 5, tapi  
# saya tidak melihat urgensi atas PCC bab 5 ketika saya membuat game dengan pikiran saya. Jadi kalau misal-nya saya membuat project 
# berdasarkan bab 5, saya harus lihat dulu bab 5 belajar apa aja, karena saya merasa tidak butuh tapi harus di taro pada project 
# untuk melatih, karena ini project bab 5 kan ? Maka dari itu ini cukup membingungkan. Yang membingungkan itu pikiran aku sih 
# wkwkkwkwk. Saya akan melanjutkan game. Saya memilih tidak biner. Jadi saya akan membuat program sesuai imajinasi saya dan 
# akan tetap menggunakan PCC Bab 5 untuk pemenuhan project bab 5. Kita lihat apa yang bisa saya lakukan. Kalau untuk materi yang
# belum dipelajari tapi diperlukan dalam project ini, saya akan mempelajari-nya secara cepat yang langsung mengeksekusi program 
# yang saya inginkan.
  
# Gpt saya sudah memutuskan saya mau bikin program apa di dalam game. Jadi saya akan membuat program yang menyeleksi player 
# menggunakan if statement untuk masuk arena-arena hebat disini. Jadi setiap player harus melewati seleksi diri sebelum benar-benar 
# di tempatkan dalam arena sesuai dengan level-nya. Dan saya akan coba menerapkan seluruh materi bab 5 yang sebelum-nya saya pelajari.
# Let's Gooooo

# Gpt saya akan membuat salah satu bagian game yang isi-nya status sebuah character menentukan dia dapat memasuki arena/land 
# kompetitif tinggi atau tidak.
# Dan saya akan coba menerapkan konsep bab 5 seperlu-nya. Semoga banyak yang perlu.


print("\n")

# player_information = { ### 2
#                      "player_1" : {"name" : "ZeldaVivos" ,"Level" : 11, "Item" : ["Huntersowrd", "Luciana", "Bomber"]},
#                     "player_2" : {"name" : "PangeranPrice", "Level" : 7, "Item" : ["Voidbringer", "Vanguard's, Bulwark", "Celestial Aegis"]},
#                     "player_3" : {"name" : "Mekaliniop", "Level" : 37, "Item" : ["Chronos Heart", "Rune of Undying", "Elixir of the Phoenix"]},
#                     "player_4" : {"name" : "ZenithBlitz" ,"Level" : 47, "Item" : ["Nebula Slasher", "Bhasma Wyrm", "Vajra Shard"]},
#                     "player_5" : {"name" : "WildTitan", "Level" : 33, "Item" : ["Titan's Carapace", "Akasha Crown", "Nirvana Aegis"]},
#                     "player_6" : {"name" : "KriegLord", "Level" : 10, "Item" : ["Vortex Greaves", "Kala Ring", "Volt-Igniter"]},
#                     "player_7" : {"name" : "NovaStellar" ,"Level" : 19, "Item" : ["Void Key", "Nanite Overcoat", "Overclock Core"]},
#                     "player_8" : {"name" : "AstralEcho", "Level" : 7, "Item" : ["Tears of the Goddess", "Rustburn Blade", "Astral Tether"]}
#                     }

# player_played_for_3_yearz = ["AstralEcho"] ### 2

# The Arena

# rare_item = ["Huntersowrd", "Voidbringer", "Chronos Heart", "Nebula Slasher", "Titan's Carapace", "Vortex Greaves", "Void Key", "Tears of the Goddess", "Phantom Edge",
#              "Whisperwind Bow", "Ruinbringer", "Nightstalker Vestment", "Ashen Cuirass"] ### 2

# for player, information in player_information.items(): ### 2
#    match = set(rare_item) & set(information["Item"]) ### 2
#    match_legend_player = set(player_played_for_3_yearz) & set([information["name"]]) ### 2
#    if information["Level"] >= 35 and information["Level"] <= 50 and match: # Gpt disini saya tambahkan kondisi spesifik ### 2 
                                                                           # agar program mengeksekusi dengan benar, dimana
                                    # saya menambahkan batasan level yang spesifik. inti-nya programm jadi tau batasan program apa
                                    # yang harus dieksekusi berdasarkan batasan level-nya. Sistem ini saya buat karena saya bingung
                                    # kenapa kondisi elif or di paling bawah tidak dieeksekusi untuk player AstralEcho. Padahal
                                    # saya sudah merekayasa sistem agar AstralEcho mengeksekusi program itu. Dan ternyata itu 
                                    # bisa terjadi karena information["Level"] < 20 and match: (Sebelum saya rekayasa) itu 
                                    # diatas-nya ada sistem yang menerima 2 kondisi true, dan yang harus diperhatikan disini adalah
                                    # < 20 diterima dibandingkan < 10 pada elif or dibawah-nya. Ternyata < 20 sampai 1,dst itu
                                    # merupakan bagian dari < 20. Dan karena kondisi-nya "True" juga maka-nya dieksekusi. Tapi point
                                    # nya adalah level 7 merupakan bagian dari < 20. bukan bagian < 10. Maka dari itu saya menambah
                                    # kan kondisi batasan level agar pengambilan keputusan sesuai dengan apa yang saya inginkan.
        # print(f"Berhasil: {information['name']} memiliki skill {match} dengan Level : {information['Level']}!") ### 2
        # print(f"-------{information['name']} dipersilahkan masuk ke dunia The Complex Iron Amphitheater.") ### 2
    # elif information["Level"] >= 20 and information["Level"] < 35 and match: # Ini sudah kita rubah menjadi and, agar player tidak match dan stuck ### 2 
                                               # di The Abyssal Ring. Dan saya berterimakasih kepada kamu gpt serta mengakui 
                                               # bahwa setiap player yang memiliki kondisi salah satu benar, akan dieksekusi or ini. Sedangkan
                                               # kondisi di bawah-bawah ini membutuhkan kondisi yang sempurna / 2 kondisi True (Karena and),
                                               # dan jika kita mengeksekusi dengan kondisi seperti ini, maka kondisi yang dibawah 
                                               # or tidak akan dieksekusi. Karena kondisi or sendiri aja sudah menerima keputusan
                                               # yang salah satu benar, sedangkan kondisi and membutuhkan 2 kondisi benar. Struktur
                                               # kode yang seperti ini akan terus mengeksekusi or dan tidak akan memutuskan kondisi
                                               # dibawah-nya. Dalam kode-nya, jika information["Level"] >= 20 and match masih or
                                               # maka semua kondisi yang baik salah satu benar atau kedua-nya benar, akan
                                               # di eksekusi oleh or. Karena or akan menerima semua input match walaupun
                                               # level tidak sesuai. Sedangkan and membutuhkan 2 kondisi benar. Maka and dibawah
                                               # nya tidak akan dieksekusi. Sehingga keputusan yang akan dieksekusi oleh program
                                               # hanya keputusan dengan kondisi diatas information["Level"] >= 20 and match.
                                               # Sedangkan dibawah-nya tidak akan, karena struktur multiple condition yang kurang
                                               # tepat. Tapi darisitu saya belajar gpt bahwa or itu harus di posisikan dalam 
                                               # struktur if-elif-else pada urutan akhir atau kondisi khusus. Agar tidak 
                                               # cacat program-nya karena or ditengah atau or di awal, yang merusak struktur
                                               # pengambilan keputusan if karena menerima salah satu kondisi dan menghalangi 
                                               # pengambilan keputusan dengan 2 kondisi true, saya belajar bahwa if harus
                                               # ditaro di akhir atau kondisi khusus agar tidak menghalangi program mengeksekusi
                                               # kondisi yang sesuai dengan requirement / dieksekusi secara terstruktur. 
        # print(f"Berhasil: {information['name']} memiliki skill {match} dengan Level : {information['Level']}!")
        # print(f"-------{information['name']} dipersilahkan masuk ke dunia The Abyssal Ring.")
    # elif information["Level"] == 10: 
    #        print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!") ### 2
    #        print(f"-------{information['name']} dipersilahkan masuk ke dunia The Omega Zone.") ### 2
    # elif information["Level"] < 20 and information["Level"] > 10 and match: ### 2 
    #        print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!") ### 2
    #        print(f"-------{information['name']} dipersilahkan masuk ke dunia The Vortex Dome.") ### 2
    # elif information["Level"] < 10 or match_legend_player and match: # In sudah. or sudah. Dia jadi satu ### 2
    #        print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!") ### 2
    #        print(f"-------{information['name']} dipersilahkan masuk ke dunia The Valhalla’s Crucible.") ### 2
    # elif "ItachiSay" not in information["name"]: # Kita sudah selsai menggunakan not in pada kode kita. ### 2
    #        print("Player bisa bermain game dengan tenang. ItachiSay tidak ada.") # "ItachiSay" adalah seorang player yang jago
                                                                                  #  banget dalam game itu. Kamu harus berhati
                                                                                  # -hati sama dia.
            #print(f"Berhasil: {information['name']} dengan level : {information['Level']}!")
            #print(f"-------{information['name']} dipersilahkan masuk ke dunia The Valhalla’s Crucible.")
    # else:
    #    print("No")

        # Gpt saya ingin nanya, ketika kode-nya di running kok "ItachiSay" malah muncul di paling atas terminal sih ?
        # Bukan-nya dia harus-nya muncul di paling bawah ya ? Karena struktur elif-nya saya taro paling bawah. Tapi kenapa ya
        # dia malah muncul paling atas ? Nah sebenarnya saya sudah mengetahui alasan-nya , itu bisa terjadi karena for kan ? 
        # Jadi karena for harus eksekusi database yang terstruktur itu, ketika saya running kode-nya, kan python baca dulu kode
        # saya kan ? Nah pas baca dan melihat bahwa "ItachiSay" bukan merupakan bagian dari for, maka-nya dia diesekusi duluan.
        # Tapi apakah benar seperti itu ? Peryanyaan selanjut-nya adalah, apakah yang non-iterasi itu sendiri pada for loop ? 
        # Karena menurut saya proses-nya itu adalah if statement harus-nya 
        #  memproses if dan elif pertama terlebih dahulu karena mereka di taro diatas, dan elif bagian "ItachiSay" diiterasi terakhir
        # karena dia ada di paling bawah. Kalau misal-nya itu karena for loop merupakan proses yang panjang dan lebih sederhana
        # elif bagian "ItachiSay" karena bukan merupakan bagian dari looping, apakah cara kerjanya begitu ? Tolong jawab dengan baik ya gpt



# Abaikan aja sekarang kata dibawah ini ya.

## Dan btw saya menulis semua cooment ini dengan sengaja, agar kamu mengetahui bagaimana alur proses saya berpikir dan punya 
## ide/kritis terhadap apa yang saya kerjakan. Btw saya suka kritis dengan apa yang saya kerjakan, saya suka mengejarkan sesuatu 
## dengan benar dan sebagaimana mesti-nya.  

print("\n")

# Ini adalah kode yang sudah di revisi.

player_information = {
                     "player_1" : {"name" : "ZeldaVivos" ,"Level" : 11, "Item" : ["Huntersword", "Luciana", "Bomber"]},
                     "player_2" : {"name" : "PangeranPrice", "Level" : 7, "Item" : ["Voidbringer", "Vanguard's, Bulwark", "Celestial Aegis"]},
                     "player_3" : {"name" : "Mekaliniop", "Level" : 37, "Item" : ["Chronos Heart", "Rune of Undying", "Elixir of the Phoenix"]},
                     "player_4" : {"name" : "ZenithBlitz" ,"Level" : 47, "Item" : ["Nebula Slasher", "Bhasma Wyrm", "Vajra Shard"]},
                     "player_5" : {"name" : "WildTitan", "Level" : 33, "Item" : ["Titan's Carapace", "Akasha Crown", "Nirvana Aegis"]},
                     "player_6" : {"name" : "KriegLord", "Level" : 10, "Item" : ["Vortex Greaves", "Kala Ring", "Volt-Igniter"]},
                     "player_7" : {"name" : "NovaStellar" ,"Level" : 19, "Item" : ["Void Key", "Nanite Overcoat", "Overclock Core"]},
                     "player_8" : {"name" : "AstralEcho", "Level" : 3, "Item" : ["Tears of the Goddess", "Rustburn Blade", "Astral Tether"]},
                     "player_9" : {"name" : "Shadpw", "Level" : 999, "Item" : ["Kuantum"]},
                     "player_10" : {"name" : "ZenithRagnar", "Level" : 40, "Item" : ["Calamity Edge", "Immortal Bulwark", "Aegis of the Vanguard"]},
                     "player_11" : {"name" : "Asgardian", "Level" : 25, "Item" : ["Galebound Treads", "Titan's Hearth", "Bastion Girdle"]},
                     "player_12" : {"name" : "HeliosRise", "Level" : 10, "Item" : ["Solstice Band", "Duskweave Cloak", "Astral Lexicon"]},
                     "player_13" : {"name" : "Sunder", "Level" : 3, "Item" : ["Voidfury Spire", "Abyssal Codex", "Seraphim Wand"]},
                     }

player_played_for_3_yearz = ["AstralEcho"]

# The Arena

rare_item = ["Huntersword", "Voidbringer", "Chronos Heart", "Nebula Slasher", "Titan's Carapace", "Vortex Greaves", "Void Key", 
             "Tears of the Goddess", "Phantom Edge", "Whisperwind Bow", "Ruinbringer", "Nightstalker Vestment", "Ashen Cuirass", 
             "Calamity Edge", "Nightfall Pierce", "Souldrinker", "Voidfury Spire"]

for player, information in player_information.items():
    match = set(rare_item) & set(information["Item"])
    match_legend_player = set(player_played_for_3_yearz) & set([information["name"]])
    if information["Level"] >= 35 and match: 
        print(f"Berhasil: {information['name']} memiliki skill {match} dengan Level : {information['Level']}!")
        print(f"-------{information['name']} dipersilahkan masuk ke dunia The Complex Iron Amphitheater.")
    elif information["Level"] >= 20 and information["Level"] < 35 and match:  
        print(f"Berhasil: {information['name']} memiliki skill {match} dengan Level : {information['Level']}!")
        print(f"-------{information['name']} dipersilahkan masuk ke dunia The Abyssal Ring.")
    elif information["Level"] == 10: 
        print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!")
        print(f"-------{information['name']} dipersilahkan masuk ke dunia The Omega Zone.")
    elif information["Level"] < 20 and information["Level"] > 10 and match: 
        print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!")
        print(f"-------{information['name']} dipersilahkan masuk ke dunia The Vortex Dome.")
    elif information["Level"] < 10 and information["Level"] > 5 and match: 
        print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!")
        print(f"-------{information['name']} dipersilahkan masuk ke dunia The Valhalla’s Crucible.")
    elif (information["Level"] <= 5 and information["Level"] > 0) and match and match_legend_player: # Kesempatan untuk level 1-5
        print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!")    # Bisa join Valhalla.
        print(f"-------{information['name']} dipersilahkan masuk ke dunia The Valhalla’s Crucible.")        
# Di mulai-nya arena untuk user tanpa rare item atau privillage apapun :
    elif (information["Level"] <= 5 and information["Level"] > 0): 
            print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!")
            print(f"-------{information['name']} Kamu masih di dunia training ya untuk berlatih.")    
    elif information["Level"] >= 35:
            print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!")
            print(f"-------{information['name']} dipersilahkan masuk ke dunia The Blood Sands.")
    elif information["Level"] >= 20 and information["Level"] < 35: 
        print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!")
        print(f"-------{information['name']} dipersilahkan masuk ke dunia Valor Dome.")
    elif information["Level"] < 20 and information["Level"] > 10: 
            print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!")  
            print(f"-------{information['name']} dipersilahkan masuk ke dunia The Iron Gridiron.") # Setelah pengujian dari kode ini
                                                                                        # saya menyadari bahwa kode saya
                                                                                        # tidak memberikan kesempatan pada user
                                                                                        # yang tidak memiliki rare item. Maka dari
                                                                                        # itu saya membuat program "Polosan" untuk
                                                                                        # user yang tidak memiliki kedua-nya walaupun
                                                                                        # level-nya sudah tinggi.
                                                                                        # Saya tidak memikirkan konsep game sepanjang itu,
                                                                                        # tapi ini jadi proteksi bagi orang level-nya
                                                                                        # tinggi tapi tidak memiliki rare item
                                                                                        # atau seorang legenda.
    elif information["Level"] < 10 and information["Level"] > 5 : 
            print(f"Berhasil: {information['name']} dengan Level : {information['Level']}!")  
            print(f"-------{information['name']} dipersilahkan masuk ke dunia Ashen Crater.")
    else:
         print("No")