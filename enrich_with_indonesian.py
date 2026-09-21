# Python script to enrich all 11 chapters with accurate, child-friendly Indonesian translations and notes
import json

with open("spoken_english_data.json", "r", encoding="utf-8") as f:
    chapters = json.load(f)

# Translation dictionary mapping english dialogue / topic to Indonesian
translations = {
    # Chapter titles & sub
    "Good Manners": {"title_id": "Sopan Santun", "sub_id": "Sapaan, Ucapan Terima Kasih, Minta Maaf & Izin"},
    "Going to Public Places": {"title_id": "Tempat Umum", "sub_id": "Bioskop, Tempat Senam, Antre, Taksi, Bus & Kereta"},
    "Social Interaction": {"title_id": "Berkenalan & Bertamu", "sub_id": "Perkenalan, Menyambut Teman, Menjamu Tamu & Pesta"},
    "Shopping": {"title_id": "Belanja", "sub_id": "Supermarket, Beli Baju, Diskon & Menawar Harga"},
    "Air Travel": {"title_id": "Naik Pesawat", "sub_id": "Tiket Pesawat, Bandara, Bagasi & Pemeriksaan Paspor"},
    "Car & Flat Rental": {"title_id": "Sewa Mobil & Tempat Tinggal", "sub_id": "Sewa Mobil, Sewa Rumah, Uang Sewa & Kontrak"},
    "Staying in a Hotel": {"title_id": "Menginap di Hotel", "sub_id": "Pesan Kamar, Sarapan, Layanan Kamar & Kolam Renang"},
    "Seeing a Doctor": {"title_id": "Periksa ke Dokter", "sub_id": "Janji Dokter, Gejala Sakit, Obat & Istirahat"},
    "Eating Out": {"title_id": "Makan di Restoran", "sub_id": "Pesan Meja, Memilih Makanan & Minuman, Minta Bon"},
    "Solving Problems & Emergencies": {"title_id": "Mengatasi Masalah & Darurat", "sub_id": "Barang Rusak, Mobil Mogok, Sakit Tiba-Tiba & Panggil Polisi"},
    "Telephoning": {"title_id": "Menelepon", "sub_id": "Menghubungi Teman, Tinggalkan Pesan & Sinyal HP"},
}

# Detailed translations for all items across all chapters
item_translations = {
    # Chapter 1
    "Good morning! How are you?": {
        "q_id": "Selamat pagi! Apa kabar?",
        "a_id": "Aku baik-baik saja, terima kasih. Bagaimana kabarmu?",
        "note_id": "formal = percakapan sopan/resmi"
    },
    "Hello! How are you doing?": {
        "q_id": "Halo! Bagaimana kabarmu?",
        "a_id": "Baik, sangat baik. Bagaimana denganmu?",
        "note_id": "informal = santai bersama teman"
    },
    "Hi, how is it going?": {
        "q_id": "Hai, bagaimana kabarmu hari ini?",
        "a_id": "Cukup baik. Kalau kamu bagaimana?",
        "note_id": "informal = sapaan santai"
    },
    "Hi, what’s up?": {
        "q_id": "Hai, ada apa / lagi apa?",
        "a_id": "Tidak banyak. Kalau kamu?",
        "note_id": "what's up = sapaan sangat akrab"
    },
    "What have you been up to?": {
        "q_id": "Lagi sibuk apa saja belakangan ini?",
        "a_id": "Biasa saja seperti biasanya.",
        "note_id": "the same as usual = seperti biasa"
    },
    "Thank you for looking after my son.": {
        "q_id": "Terima kasih sudah menjaga anak laki-lakiku.",
        "a_id": "Sama-sama, dengan senang hati.",
        "note_id": "looking after = merawat / menjaga"
    },
    "Thanks for your help.": {
        "q_id": "Terima kasih atas bantuanmu.",
        "a_id": "Sama-sama / tidak masalah.",
        "note_id": "no problem = tidak masalah"
    },
    "Thank you for carrying my bag.": {
        "q_id": "Terima kasih sudah membawakan tasku.",
        "a_id": "Sama-sama saja / santai saja.",
        "note_id": "don’t mention it = tidak usah sungkan"
    },
    "That’s very kind of you but you really shouldn’t have gone to all this trouble.": {
        "q_id": "Kamu baik sekali, tapi kamu tidak perlu sampai repot-repot begini.",
        "a_id": "Aku sangat senang bisa membantu.",
        "note_id": "gone to all this trouble = repot-repot membantu"
    },
    "Sorry to have kept you waiting.": {
        "q_id": "Maaf sudah membuatmu menunggu.",
        "a_id": "Tidak apa-apa.",
        "note_id": "kept you waiting = membuat menunggu"
    },
    "Sorry I’m late.": {
        "q_id": "Maaf aku terlambat.",
        "a_id": "Tidak masalah. Aku juga baru saja sampai di sini.",
        "note_id": "just got here = baru sampai"
    },
    "I’m sorry about reading your messages.": {
        "q_id": "Aku minta maaf karena membaca pesan-pesanmu.",
        "a_id": "Jangan ulangi lagi ya.",
        "note_id": "don't let it happen again = jangan diulangi lagi"
    },
    "Could you open the window, please?": {
        "q_id": "Bisakah kamu membukakan jendela, tolong?",
        "a_id": "Tentu saja.",
        "note_id": "could you... please = cara sopan meminta tolong"
    },
    "Could you make me a cup of tea, please?": {
        "q_id": "Bisakah kamu membuatkan aku secangkir teh, tolong?",
        "a_id": "Ya, tentu saja.",
        "note_id": "of course = tentu saja"
    },
    "Could you give me his phone number, please?": {
        "q_id": "Bisakah kamu memberikan nomor teleponnya, tolong?",
        "a_id": "Maafkan aku, tapi aku tidak tahu nomornya.",
        "note_id": "I'm sorry but... = cara sopan menolak permintaan"
    },
    "Could you look after my son tonight?": {
        "q_id": "Bisakah kamu menjaga anakku malam ini?",
        "a_id": "Maaf sepertinya tidak bisa. Aku kerja giliran malam hari ini.",
        "note_id": "evening shift = giliran kerja malam"
    },
    "Do you mind moving your seat so that I and my friend could sit together?": {
        "q_id": "Apakah kamu keberatan pindah kursi agar aku dan temanku bisa duduk bersama?",
        "a_id": "Tentu tidak keberatan sama sekali.",
        "note_id": "No, of course not = Tentu tidak keberatan (jawaban setuju)"
    },
    "Do you mind lending me some money?": {
        "q_id": "Apakah kamu keberatan meminjamkan aku uang?",
        "a_id": "Maaf, aku lagi tidak punya uang sama sekali.",
        "note_id": "to be broke = lagi tidak punya uang"
    },
    "My flight arrives at 7 am.": {
        "q_id": "Penerbanganku tiba jam 7 pagi.",
        "a_id": "Apakah kamu mau aku jemput di bandara?",
        "note_id": "would you like me to... = maukah aku bantu..."
    },
    "My car is broken, so I came to work by underground today.": {
        "q_id": "Mobilku rusak, jadi aku berangkat kerja naik kereta bawah tanah hari ini.",
        "a_id": "Mau aku beri tumpangan mobil pulang ke rumah?",
        "note_id": "give a lift = memberi tumpangan mobil"
    },
    "The suitcase is so heavy.": {
        "q_id": "Koper ini berat sekali.",
        "a_id": "Biar aku bawakan untukmu!",
        "note_id": "let me... = biar aku bantu..."
    },
    "What do these statistics mean?": {
        "q_id": "Apa arti angka-angka statistik ini?",
        "a_id": "Biar kujelaskan kepadamu.",
        "note_id": "explain = menjelaskan"
    },
    "Can I switch the TV on?": {
        "q_id": "Boleh aku menyalakan TV-nya?",
        "a_id": "Tentu, silakan.",
        "note_id": "go ahead = silakan lakukan"
    },
    "Can I read this e-mail?": {
        "q_id": "Boleh aku membaca email ini?",
        "a_id": "Maaf, sebaiknya jangan.",
        "note_id": "I'm afraid not = maaf tidak boleh"
    },
    "Do you mind if I sit here?": {
        "q_id": "Apakah boleh aku duduk di sini?",
        "a_id": "Tentu tidak apa-apa, silakan.",
        "note_id": "No, of course not = silakan"
    },
    "Do you mind if I borrow your car tomorrow?": {
        "q_id": "Bolehkah aku meminjam mobilmu besok?",
        "a_id": "Maaf, aku tidak bisa meminjamkannya karena kupakai.",
        "note_id": "to borrow = meminjam barang"
    },
    "It’s hot in here.": {
        "q_id": "Di sini panas sekali.",
        "a_id": "Ayo kita buka jendelanya. — Baiklah.",
        "note_id": "Let's... = Ayo kita..."
    },
    "Let’s ask your mum to look after Johnny while we are away.": {
        "q_id": "Ayo minta tolong ibumu menjaga Johnny selagi kita pergi.",
        "a_id": "Sebaiknya jangan.",
        "note_id": "I'd rather not = sebaiknya tidak usah"
    },
    "How about going there by train?": {
        "q_id": "Bagaimana kalau kita pergi ke sana naik kereta?",
        "a_id": "Kedengarannya bagus!",
        "note_id": "sounds good = ide yang bagus"
    },
    "How about painting the walls blue?": {
        "q_id": "Bagaimana kalau kita cat dindingnya warna biru?",
        "a_id": "Kedengarannya kurang bagus deh.",
        "note_id": "doesn't sound good = kurang cocok"
    },
    "Why don’t we go to the beach?": {
        "q_id": "Kenapa kita tidak pergi ke pantai saja?",
        "a_id": "Ide yang hebat!",
        "note_id": "Why don't we... = ajakan untuk melakukan sesuatu"
    },
    "Why don’t you get a new hairstyle?": {
        "q_id": "Kenapa kamu tidak coba gaya rambut baru?",
        "a_id": "Aku lagi tidak ingin potong rambut.",
        "note_id": "don't feel like it = lagi tidak berminat"
    },
    "Kevin is musically gifted.": {
        "q_id": "Kevin sangat berbakat dalam bermusik.",
        "a_id": "Itu benar sekali!",
        "note_id": "gifted = sangat berbakat"
    },
    "I think Martin Freeman is a brilliant actor!": {
        "q_id": "Menurutku Martin Freeman adalah aktor yang hebat!",
        "a_id": "Tentu saja, sangat setuju!",
        "note_id": "absolutely = sangat setuju"
    },
    "The facts he gave us are convincing.": {
        "q_id": "Fakta-fakta yang dia berikan sangat meyakinkan.",
        "a_id": "Aku rasa tidak begitu!",
        "note_id": "convincing = meyakinkan"
    },
    "He is an honest man.": {
        "q_id": "Dia adalah pria yang jujur.",
        "a_id": "Aku rasa tidak begitu!",
        "note_id": "honest = jujur"
    },
    "Your cake is really delicious!": {
        "q_id": "Kue buatanmu sangat lezat!",
        "a_id": "Aku senang sekali kamu menyukainya!",
        "note_id": "delicious = enak / lezat"
    },
    "You look gorgeous in this outfit. You have a great fashion sense!": {
        "q_id": "Kamu terlihat sangat cantik memakai pakaian ini. Selera gayamu keren!",
        "a_id": "Kamu baik sekali sudah memujiku.",
        "note_id": "gorgeous = sangat cantik/menawan; outfit = setelan pakaian"
    },
    "Your presentation was great!": {
        "q_id": "Presentasimu tadi sangat hebat!",
        "a_id": "Terima kasih banyak, aku sangat butuh mendengar pujian itu.",
        "note_id": "great = hebat luar biasa"
    },
    "Jill has had a heart attack! She’s just been taken to hospital!": {
        "q_id": "Jill terkena serangan jantung! Dia baru saja dibawa ke rumah sakit!",
        "a_id": "Astaga, mengerikan sekali!",
        "note_id": "how awful / terrible = ungkapan rasa iba/prihatin"
    },
    "My back kills me!": {
        "q_id": "Punggungku sakit sekali!",
        "a_id": "Aku turut sedih mendengarnya!",
        "note_id": "kills me = ungkapan untuk rasa sakit yang hebat"
    },
    "I’ve lost one of my gloves.": {
        "q_id": "Salah satu sarung tanganku hilang.",
        "a_id": "Sayang sekali ya!",
        "note_id": "what a shame = sayang sekali"
    },
    "I spent half an hour looking for my car key! When I got to my car, I saw I had a flat tyre.": {
        "q_id": "Aku habiskan setengah jam mencari kunci mobil! Pas sampai di mobil, bannya kempes.",
        "a_id": "Bisa kubayangkan betapa kesalnya! Oh tidak!",
        "note_id": "flat tyre = ban kempes"
    },
    "Are you following me?": {
        "q_id": "Apakah kamu mengerti penjelasanku sejauh ini?",
        "a_id": "Tidak, aku ketinggalan. Bisakah kamu jelaskan sekali lagi?",
        "note_id": "are you following me = apakah kamu paham"
    },
    "Are you with me?": {
        "q_id": "Kamu masih mendengarkan dan paham kan?",
        "a_id": "Maaf, tadi kamu bilang apa ya?",
        "note_id": "are you with me = apakah kamu menyimak"
    },
    "Am I making sense?": {
        "q_id": "Apakah penjelasanku masuk akal dan mudah dipahami?",
        "a_id": "Bisakah kamu jelaskan dengan cara lain sekali lagi, tolong?",
        "note_id": "making sense = masuk akal / jelas"
    },
    "It was nice to talk to you but I’ve got to go now.": {
        "q_id": "Senang mengobrol denganmu, tapi aku harus pergi sekarang.",
        "a_id": "Aku juga senang mengobrol. Sampai jumpa nanti.",
        "note_id": "see you around = sampai jumpa"
    },
    "It was great to see you, but I must dash now.": {
        "q_id": "Senang sekali bertemu denganmu, tapi aku harus buru-buru sekarang.",
        "a_id": "Senang bertemu denganmu juga. Jaga diri baik-baik.",
        "note_id": "must dash = harus bergegas buru-buru"
    },
    "I should get going.": {
        "q_id": "Aku harus berangkat sekarang.",
        "a_id": "Baiklah. Sampai jumpa nanti ya.",
        "note_id": "get going = mulai jalan/pergi"
    },
    "I’m running terribly late!": {
        "q_id": "Aku terlambat parah sekali!",
        "a_id": "Baiklah. Sampai jumpa nanti.",
        "note_id": "running terribly late = sangat terlambat"
    },
    "I hope we meet again soon.": {
        "q_id": "Semoga kita bisa segera bertemu lagi.",
        "a_id": "Ya, mari tetap saling memberi kabar ya.",
        "note_id": "keep in touch = saling berkomunikasi"
    },

    # Chapter 2
    "Let’s go to the cinema. What’s on?": {
        "q_id": "Ayo pergi ke bioskop. Film apa yang sedang tayang?",
        "a_id": "Film The Martian. Aktornya Matt Damon.",
        "note_id": "what's on = film apa yang sedang diputar di bioskop"
    },
    "Can we have two tickets for The Martian, please?": {
        "q_id": "Bisa beli dua tiket untuk film The Martian, tolong?",
        "a_id": "Totalnya 30 euro. Ini tiketnya. — Terima kasih.",
        "note_id": "here you are = ini barangnya / silakan"
    },
    "Excuse me, you’re in my seat.": {
        "q_id": "Permisi, Anda duduk di kursi saya.",
        "a_id": "Maaf? Ini kursi saya nomor 8 baris 15. — Oh iya betul, maaf ya.",
        "note_id": "row = barisan kursi bioskop"
    },
    "What are your hours?": {
        "q_id": "Jam berapa saja tempat ini buka?",
        "a_id": "Kami buka dari jam 9 pagi sampai 10 malam, tujuh hari seminggu.",
        "note_id": "hours = jam operasional buka"
    },
    "I’d like to sign up for a membership. How much is the charge?": {
        "q_id": "Saya ingin mendaftar menjadi anggota. Berapa biayanya?",
        "a_id": "Biayanya 80 euro.",
        "note_id": "sign up = mendaftar; membership = keanggotaan"
    },
    "I’d like to sign up for pilates classes. What days and what time are they?": {
        "q_id": "Saya ingin ikut kelas pilates. Hari apa dan jam berapa saja?",
        "a_id": "Ada hari Selasa dan Jumat jam 7 malam. — Baguslah.",
        "note_id": "classes = kelas latihan"
    },
    "Is this the end of the line?": {
        "q_id": "Apakah ini ujung antrean paling belakang?",
        "a_id": "Bukan, ujung antreannya ada di sebelah sana.",
        "note_id": "end of the line = ujung paling belakang antrean"
    },
    "Are you in the line?": {
        "q_id": "Apakah kamu sedang mengantre di sini?",
        "a_id": "Iya, betul.",
        "note_id": "in the line = sedang mengantre"
    },
    "Could you hold my place in the queue? I should be back right now.": {
        "q_id": "Bisakah kamu tolong jagakan tempat antreanku? Aku akan segera kembali sebentar.",
        "a_id": "Tentu saja.",
        "note_id": "hold my place = jagakan tempat antrean"
    },
    "Can I sneak ahead of you? I only have one item.": {
        "q_id": "Bolehkah aku mendahului antreanmu? Barangkuku cuma satu.",
        "a_id": "Ya, silakan duluan.",
        "note_id": "sneak ahead = mendahului antrean; item = barang"
    },
    "Excuse me, I was here before you. I should be ahead of you in the queue.": {
        "q_id": "Permisi, saya sudah di sini lebih dulu dari Anda. Seharusnya saya di depan.",
        "a_id": "Maafkan saya.",
        "note_id": "queue = antrean orang"
    },
    "I’d like to exchange dollars into euros. What’s the exchange rate, please?": {
        "q_id": "Saya mau menukar uang dolar ke euro. Berapa kurs tukarnya sekarang?",
        "a_id": "Satu euro adalah 1,2 dolar.",
        "note_id": "exchange rate = kurs nilai tukar mata uang"
    },
    "Do you charge a commission?": {
        "q_id": "Apakah ada biaya komisi penukaran uang?",
        "a_id": "Iya, Pak. Komisinya 2%. — Baiklah, saya ingin tukar 500 euro ke dolar.",
        "note_id": "commission = biaya jasa penukaran"
    },
    "How would you like your money?": {
        "q_id": "Anda ingin pecahan uang berapa?",
        "a_id": "Dalam lembaran uang kertas seratus dolar, tolong. — Totalnya 588 dolar.",
        "note_id": "banknote = uang kertas"
    },
    "I’d like to book a tour of Niagara Falls.": {
        "q_id": "Saya ingin memesan tur wisata ke Air Terjun Niagara.",
        "a_id": "Tentu saja. Kami ada tur setiap hari. Mau pesan untuk dua orang dewasa dan satu anak.",
        "note_id": "tour = perjalanan wisata"
    },
    "When does the tour start and when does it finish?": {
        "q_id": "Jam berapa turnya dimulai dan jam berapa selesai?",
        "a_id": "Mulai jam 8 pagi. Selesai jam 4 sore.",
        "note_id": "start = mulai; finish = selesai"
    },
    "Where does the tour leave from?": {
        "q_id": "Dari mana bus turnya berangkat?",
        "a_id": "Bus wisata akan menjemput Anda tepat di depan hotel.",
        "note_id": "pick up = menjemput"
    },
    "I need a taxi to the Louvre. Where from?": {
        "q_id": "Saya butuh taksi ke museum Louvre. Dari mana jemputnya?",
        "a_id": "Dari jalan Rue Michel-Ange.",
        "note_id": "taxi = taksi"
    },
    "What time is it for?": {
        "q_id": "Untuk jam berapa taksinya?",
        "a_id": "Secepat mungkin, tolong.",
        "note_id": "as soon as possible = secepat mungkin"
    },
    "How long will it be till it comes?": {
        "q_id": "Berapa lama sampai taksinya tiba?",
        "a_id": "Kira-kira 15 menit.",
        "note_id": "how long = berapa lama"
    },
    "How do I get to the Museum of Modern Art?": {
        "q_id": "Bagaimana cara saya menuju Museum Seni Modern?",
        "a_id": "Jalan lurus terus lalu belok kanan di belokan kedua. Nanti terlihat papan namanya.",
        "note_id": "go straight ahead = jalan lurus terus"
    },
    "How do I get to the nearest metro station, please?": {
        "q_id": "Bagaimana cara menuju stasiun metro/kereta terdekat?",
        "a_id": "Ikuti jalan ini sampai supermarket, lewati supermarket lalu belok kiri. Ada di kananmu.",
        "note_id": "nearest = paling dekat"
    },
    "Is there a bank near here, please?": {
        "q_id": "Apakah ada bank di dekat sini?",
        "a_id": "Belok kanan di lampu merah berikutnya. — Jadi saya belok kiri? — Bukan, belok kanan.",
        "note_id": "traffic light = lampu lalu lintas"
    },
    "Is there a chemist’s near here?": {
        "q_id": "Apakah ada apotek di dekat sini?",
        "a_id": "Ikuti aku. Biar kuantar ke sana. — Terima kasih, kamu baik sekali.",
        "note_id": "chemist's = apotek / toko obat"
    },
    "Does this bus go to the city centre?": {
        "q_id": "Apakah bus ini menuju ke pusat kota?",
        "a_id": "Tidak. Kamu harus naik bus nomor 23.",
        "note_id": "city centre = pusat kota"
    },
    "Does it stop outside the Opera House?": {
        "q_id": "Apakah busnya berhenti di depan Gedung Opera?",
        "a_id": "Ya, busnya berhenti di sana.",
        "note_id": "stop outside = berhenti di depan"
    },
    "Can I buy a ticket on the bus?": {
        "q_id": "Bolehkah saya membeli tiket langsung di dalam bus?",
        "a_id": "Tidak bisa, tapi Anda bisa beli dari mesin tiket otomatis di sebelah sana.",
        "note_id": "ticket machine = mesin tiket"
    },
    "Is anybody sitting here? / Is this seat taken?": {
        "q_id": "Apakah ada yang duduk di sini? / Kursi ini sudah ada orangnya?",
        "a_id": "Tidak ada, silakan duduk. / Maaf, istri saya duduk di sini.",
        "note_id": "seat taken = kursi sudah terisi"
    },
    "How many stops is it to Central Park?": {
        "q_id": "Berapa pemberhentian lagi sampai ke Central Park?",
        "a_id": "Tinggal 4 pemberhentian lagi.",
        "note_id": "stops = halte / pemberhentian"
    },
    "Where do I get off for the hospital?": {
        "q_id": "Di mana saya harus turun kalau mau ke rumah sakit?",
        "a_id": "Di pemberhentian berikutnya.",
        "note_id": "get off = turun dari bus/kereta"
    },
    "How do I get to Bilbao?": {
        "q_id": "Bagaimana rute ke Bilbao?",
        "a_id": "Naik jalur ungu di Ventilla lalu transit ganti jalur biru muda di Plaza de Castilla.",
        "note_id": "change line = pindah/ganti jalur kereta"
    },
    "I'd like a ticket to Rome, please.": {
        "q_id": "Saya ingin beli tiket ke Roma, tolong.",
        "a_id": "Tiket sekali jalan atau tiket pulang-pergi? — Sekali jalan saja.",
        "note_id": "single = sekali jalan; return = pulang-pergi"
    },
    "Are there any trains leaving tomorrow?": {
        "q_id": "Apakah ada kereta yang berangkat besok?",
        "a_id": "Ada dua kereta ke Roma: jam 10.20 pagi dan jam 5 sore. — Pesan yang jam 10.20 ya.",
        "note_id": "leaving = berangkat"
    },

    # Chapter 3
    "Great party, isn’t it? I’m Ruth.": {
        "q_id": "Pesta yang seru ya? Aku Ruth.",
        "a_id": "Iya keren sekali. Aku Julia. Senang berkenalan denganmu. — Aku juga.",
        "note_id": "nice to meet you = senang berkenalan denganmu"
    },
    "Hi, I’m Kevin. So, how do you know the host?": {
        "q_id": "Hai, aku Kevin. Dari mana kamu kenal tuan rumah pestanya?",
        "a_id": "Hai Kevin! Aku David. Aku dan Daniel teman kerja. Kalau kamu? — Aku tetangga sebelahnya.",
        "note_id": "host = tuan rumah; next door = tetangga sebelah"
    },
    "Laura, meet Seon! Seon, this is Laura!": {
        "q_id": "Laura, kenalkan ini Seon! Seon, ini Laura!",
        "a_id": "Senang berkenalan denganmu, Seon. — Kamu juga, Laura!",
        "note_id": "meet... = kenalkan dengan..."
    },
    "James, this is Chris. Chris, this is James.": {
        "q_id": "James, ini Chris. Chris, ini James.",
        "a_id": "Senang berkenalan denganmu, James! — Aku sudah banyak mendengar cerita tentangmu! — Semoga cerita yang baik ya.",
        "note_id": "heard a lot about you = sudah sering mendengar ceritamu"
    },
    "Hi, I’m Claire. Are you new here?": {
        "q_id": "Hai, aku Claire. Apakah kamu karyawan baru di sini?",
        "a_id": "Senang berkenalan denganmu. Aku Robert. Iya, ini hari pertamaku bekerja.",
        "note_id": "first day = hari pertama"
    },
    "You must be Susan. I’m Jill. Let me show you around.": {
        "q_id": "Kamu pasti Susan ya. Aku Jill. Mari kuajak berkeliling melihat kantor.",
        "a_id": "Iya betul. Senang berkenalan denganmu juga Jill. Terima kasih.",
        "note_id": "show you around = mengajak berkeliling melihat tempat"
    },
    "Hello, Jake. Welcome to the Nesco Company. Let me introduce you to some people.": {
        "q_id": "Halo Jake. Selamat datang di Perusahaan Nesco. Mari kuperkenalkan dengan rekan kerja.",
        "a_id": "Terima kasih, itu akan sangat menyenangkan.",
        "note_id": "introduce = memperkenalkan"
    },
    "Hi, I’m Jeff. Where will you be working?": {
        "q_id": "Hai, aku Jeff. Di lantai berapa kamu akan bekerja?",
        "a_id": "Aku Alex, asisten hukum baru. Di lantai tujuh. — Berarti kita bakal sering bertemu ya.",
        "note_id": "seeing a lot of each other = bakal sering bertemu"
    },
    "Would you like to come to my birthday party at 5 pm?": {
        "q_id": "Maukah kamu datang ke pesta ulang tahunku jam 5 sore?",
        "a_id": "Aku mau sekali! Aku pasti datang ke sana. Terima kasih ya!",
        "note_id": "birthday party = pesta ulang tahun"
    },
    "Would you like to come over for dinner tonight?": {
        "q_id": "Maukah kamu mampir makan malam di rumahku malam ini?",
        "a_id": "Pasti menyenangkan sekali, tapi aku sudah punya janji lain sebelumnya. Lain kali ya!",
        "note_id": "previous arrangement = sudah ada janji terlebih dahulu"
    },
    "I’d love it if you could come to stay but do you mind dogs?": {
        "q_id": "Aku senang kalau kamu mau menginap, tapi apakah kamu takut/keberatan dengan anjing?",
        "a_id": "Tentu tidak keberatan sama sekali. Terima kasih sudah mengundangku.",
        "note_id": "do you mind = apakah kamu keberatan"
    },
    "Hi, come in! I’m glad you could make it.": {
        "q_id": "Hai, silakan masuk! Aku senang sekali kamu bisa datang.",
        "a_id": "Senang bertemu denganmu! Terima kasih sudah mengajakku. — Senang sekali menyambutmu di sini.",
        "note_id": "make it = berhasil datang"
    },
    "Nice to have you here. How was your journey?": {
        "q_id": "Senang kamu ada di sini. Bagaimana perjalananmu ke sini tadi?",
        "a_id": "Tadi sempat kena macet, tapi setelah itu lancar-lancar saja.",
        "note_id": "traffic jam = macet; smooth = lancar"
    },
    "You’ve got a lovely house.": {
        "q_id": "Rumahmu indah dan nyaman sekali.",
        "a_id": "Terima kasih. Mari kuajak melihat-lihat ke dalam.",
        "note_id": "lovely house = rumah yang manis dan indah"
    },
    "Come into the living room and have a seat. Make yourself comfortable.": {
        "q_id": "Ayo masuk ke ruang tamu dan duduklah. Anggap seperti rumah sendiri.",
        "a_id": "Ruang tamumu cantik sekali! Terima kasih banyak!",
        "note_id": "make yourself comfortable = anggap rumah sendiri / santai saja"
    },
    "Would you like a drink? / Can I get you something to drink?": {
        "q_id": "Apakah kamu mau minum? / Mau kubuatkan minuman apa?",
        "a_id": "Boleh, tolong secangkir teh. / Ada minuman apa saja?",
        "note_id": "cup of tea = secangkir teh"
    },
    "How do you take your coffee?": {
        "q_id": "Kopinya mau diracik bagaimana?",
        "a_id": "Dua sendok gula, jangan pakai susu ya.",
        "note_id": "how do you take... = bagaimana selera racikannya"
    },
    "Help yourself to the cookies.": {
        "q_id": "Silakan cicipi kuenya ya, ambil sendiri.",
        "a_id": "Terima kasih! Kuenya enak sekali.",
        "note_id": "help yourself = silakan ambil sendiri"
    },
    "Please, go ahead with the salad, I’ll bring the lamb in red wine in a minute.": {
        "q_id": "Silakan nikmati saladnya dulu, nanti hidangan utamanya segera kubawakan.",
        "a_id": "Kedengarannya lezat sekali!",
        "note_id": "go ahead = silakan mulai santap"
    },
    "Can I get anyone anything? / Are you done?": {
        "q_id": "Ada yang mau tambah makanan/minuman lagi? / Apakah makannya sudah selesai?",
        "a_id": "Tidak usah, terima kasih. Kami sudah kenyang sekali. Masakannya enak sekali!",
        "note_id": "we are full = kami sudah kenyang"
    },
    "Thank you for having us. / Thank you for inviting us.": {
        "q_id": "Terima kasih sudah menerima kami di rumahmu. / Terima kasih sudah mengundang kami.",
        "a_id": "Kami senang kalian bisa datang. Hati-hati di jalan pulang ya. Datang lagi nanti!",
        "note_id": "thank you for having us = terima kasih sudah menjamu kami"
    },
    "What are you up to today? Would you like to go to the cinema tonight?": {
        "q_id": "Kamu ada rencana apa hari ini? Mau nonton bioskop nanti malam?",
        "a_id": "Lagi santai tidak ada acara. Boleh juga, film apa yang lagi tayang?",
        "note_id": "nothing really = tidak ada acara penting"
    },
    "I was thinking... Do you want to meet up for a drink some time?": {
        "q_id": "Aku terpikir... Mau tidak kapan-kapan kita ngobrol sambil minum?",
        "a_id": "Boleh juga! Bagaimana kalau besok malam?",
        "note_id": "meet up = ketemuan"
    },
    "I was wondering if you would have dinner with me?": {
        "q_id": "Kira-kira maukah kamu makan malam denganku?",
        "a_id": "Makan malam? Boleh, kapan? — Bagaimana kalau malam ini? — Maaf malam ini tidak bisa, kalau besok bisa.",
        "note_id": "can't make it = tidak bisa datang"
    },
    "Would you like to go out some time?": {
        "q_id": "Maukah kamu jalan bareng kapan-kapan?",
        "a_id": "Kamu baik sekali, tapi aku sudah punya pasangan.",
        "note_id": "seeing someone = sudah punya pasangan"
    },
    "I just thought we could grab a coffee sometime.": {
        "q_id": "Aku cuma berpikir kita bisa ngopi bareng kapan-kapan.",
        "a_id": "Maaf ya, kamu orang baik, tapi aku tidak punya perasaan lebih kepadamu.",
        "note_id": "not into you = tidak tertarik secara romantis"
    },
    "Nice day, isn’t it?": {
        "q_id": "Hari yang cerah dan indah ya?",
        "a_id": "Iya, di luar cuacanya sangat menyenangkan.",
        "note_id": "small talk = obrolan ramah basa-basi"
    },
    "Can you believe all this rain we’ve been having?": {
        "q_id": "Hujan terus belakangan ini, tidak berhenti-henti ya?",
        "a_id": "Iya betul sekali, deras terus!",
        "note_id": "weather small talk = ngobrol tentang cuaca"
    },
    "How much do you earn?": {
        "q_id": "Berapa gaji/penghasilanmu?",
        "a_id": "Sebaiknya aku tidak menjawab itu.",
        "note_id": "I'd rather not say = cara sopan menolak pertanyaan pribadi"
    },
    "Can we meet on the 16th of July?": {
        "q_id": "Bisakah kita bertemu tanggal 16 Juli?",
        "a_id": "Iya, waktu itu sangat pas buatku.",
        "note_id": "suits me perfectly = sangat cocok buatku"
    },
    "We were going to meet on Friday but something has come up. Can we fix another time?": {
        "q_id": "Rencananya kita ketemu hari Jumat, tapi ada urusan mendadak. Bisa atur waktu lain?",
        "a_id": "Tentu. Bagaimana kalau hari Senin?",
        "note_id": "something has come up = ada urusan mendadak"
    },

    # Chapter 4
    "Hello! Have you got souvenir mugs?": {
        "q_id": "Halo! Apakah ada cangkir suvenir kenang-kenangan di sini?",
        "a_id": "Ya, kami menyediakannya di sini.",
        "note_id": "souvenir mugs = cangkir suvenir"
    },
    "Have you got umbrellas?": {
        "q_id": "Apakah ada payung?",
        "a_id": "Ada. Kamu cari payung untuk pria atau wanita? — Yang untuk wanita.",
        "note_id": "umbrellas = payung"
    },
    "Can I have this calendar, please? How much is it?": {
        "q_id": "Bolehkah saya beli kalender ini? Berapa harganya?",
        "a_id": "Ini dia kalendernya. Harganya 10 poundsterling.",
        "note_id": "how much is it = berapa harganya"
    },
    "Can I have a carton of milk and a loaf of bread, please?": {
        "q_id": "Bisa beli sekotak susu dan sebongkah roti tawar, tolong?",
        "a_id": "Ini dia. Totalnya 4 euro.",
        "note_id": "carton of milk = susu kotak; loaf of bread = sebongkah roti"
    },
    "Can I have a box of tissues, please?": {
        "q_id": "Bisa beli sekotak tisu, tolong?",
        "a_id": "Maaf sekali, tisu kami sedang habis stoknya.",
        "note_id": "out of tissues = stok tisu habis"
    },
    "I’m looking for a dishwasher.": {
        "q_id": "Saya mencari mesin cuci piring.",
        "a_id": "Mau model yang berdiri sendiri atau yang menyatu di kabinet dapur?",
        "note_id": "freestanding = berdiri sendiri; built-in = tertanam di dapur"
    },
    "Can I help you?": {
        "q_id": "Ada yang bisa saya bantu?",
        "a_id": "Tidak, terima kasih, saya hanya sedang melihat-lihat dulu. — Beri tahu saya jika butuh bantuan ya.",
        "note_id": "just looking around = cuma lihat-lihat dulu"
    },
    "Excuse me, where can I find flour?": {
        "q_id": "Permisi, di mana saya bisa menemukan tepung terigu?",
        "a_id": "Ada di lorong rak nomor 4, tepat di samping gula.",
        "note_id": "aisle = lorong antar-rak supermarket"
    },
    "Where can I weigh my fruit?": {
        "q_id": "Di mana saya bisa menimbang buah-buahan ini?",
        "a_id": "Timbangan ada di ujung lorong itu.",
        "note_id": "scales = timbangan buah"
    },
    "Are the bags free of charge?": {
        "q_id": "Apakah kantong belanjanya gratis?",
        "a_id": "Iya, kami tidak memungut biaya untuk kantong belanja.",
        "note_id": "free of charge = gratis tanpa biaya"
    },
    "I’m looking for a pair of trousers. I’m a 40 for trousers.": {
        "q_id": "Saya mencari celana panjang. Ukuran celana saya 40.",
        "a_id": "Warna apa yang kamu cari?",
        "note_id": "trousers = celana panjang"
    },
    "I’m looking for a pair of shoes. I’m a 9 for shoes.": {
        "q_id": "Saya mencari sepasang sepatu. Ukuran sepatu saya nomor 9.",
        "a_id": "Mau jenis sepatu apa? Sepatu pesta, sepatu santai tanpa tali, atau pantofel?",
        "note_id": "shoe size = ukuran sepatu"
    },
    "What’s this dress made of? Can it be machine washed?": {
        "q_id": "Gaun ini terbuat dari bahan apa? Apakah boleh dicuci pakai mesin cuci?",
        "a_id": "Bahan wol murni. Petunjuk perawatannya harus dicuci dengan tangan.",
        "note_id": "pure wool = wol murni; care instructions = petunjuk pencucian"
    },
    "Where are the changing/fitting rooms? Can I try these jeans on?": {
        "q_id": "Di mana kamar pas untuk coba pakaian? Boleh saya coba celana jeans ini?",
        "a_id": "Di sebelah sana. Tentu, kamar pas ada di sana.",
        "note_id": "fitting room = kamar pas"
    },
    "Does the dress fit?": {
        "q_id": "Apakah gaunnya pas di badan?",
        "a_id": "Terlalu sempit. Apakah ada ukuran yang lebih besar? — Ini dia. — Yang ini pas, saya beli yang ini.",
        "note_id": "too tight = terlalu sempit"
    },
    "Are the trousers ok?": {
        "q_id": "Apakah celananya pas?",
        "a_id": "Terlalu kebesaran. Apakah ada ukuran lebih kecil? — Maaf tidak ada. — Kalau begitu tidak jadi beli.",
        "note_id": "leave them = tidak jadi beli"
    },
    "Is this shirt in the sale? How long does the sale last?": {
        "q_id": "Apakah kemeja ini sedang diskon? Sampai kapan diskonnya berlangsung?",
        "a_id": "Iya, diskon 30%. Diskonnya berakhir hari Minggu depan.",
        "note_id": "30% off = potongan harga 30%"
    },
    "Are you in the tax-free shopping scheme? How much to qualify for a VAT refund?": {
        "q_id": "Apakah toko ini melayani belanja bebas pajak turis? Berapa belanja minimal untuk dapat pengembalian pajak?",
        "a_id": "Iya, Pak. Boleh lihat paspornya? Jumlah belanja minimal adalah 175 euro.",
        "note_id": "VAT refund = pengembalian uang pajak belanja"
    },
    "Can I pay by credit card? / Do you take credit cards?": {
        "q_id": "Bisa bayar pakai kartu kredit? / Apakah menerima kartu kredit?",
        "a_id": "Bisa, silakan masukkan nomor PIN Anda. / Maaf, kami hanya menerima uang tunai.",
        "note_id": "credit card = kartu kredit; cash = uang tunai"
    },
    "Do you have a refund policy?": {
        "q_id": "Apakah ada aturan pengembalian barang dan uang?",
        "a_id": "Ada, Anda harus menyimpan struk belanja dan mengembalikan barang dalam waktu 2 minggu.",
        "note_id": "receipt = struk belanja; refund = uang kembali"
    },
    "I’d like to return this skirt. The stitching is coming undone.": {
        "q_id": "Saya ingin mengembalikan rok ini. Jahitannya lepas/terurai.",
        "a_id": "Tentu. Boleh saya lihat struk pembeliannya?",
        "note_id": "stitching coming undone = jahitan pakaian terlepas"
    },
    "I’d like to return these trousers. They shrank a lot after I washed them.": {
        "q_id": "Saya mau kembalikan celana ini. Celananya menciut banyak setelah dicuci.",
        "a_id": "Apa kendalanya? Apakah Anda mencuci sesuai petunjuk perawatannya?",
        "note_id": "shrink (shrank) = kain menciut jadi kecil"
    },
    "How much is it? 30 euros. That’s pretty steep. Can you knock a few dollars off?": {
        "q_id": "Berapa harganya? 30 euro. Agak kemahalan ya. Bisa kurangi sedikit harganya?",
        "a_id": "Baiklah, kamu boleh bayar 28 euro saja.",
        "note_id": "steep = mahal; knock off = potong harga"
    },
    "How much is this vase? 100 euros. How about 70 euros?": {
        "q_id": "Berapa harga vas bunga ini? 100 euro. Kalau 70 euro bagaimana?",
        "a_id": "Boleh 85 euro. — Maaf, itu masih terlalu mahal buat saya.",
        "note_id": "bargain = tawar-menawar harga"
    },
    "How much are these gloves? 30 dollars. Will you take 20 for them?": {
        "q_id": "Berapa harga sarung tangan ini? 30 dolar. Boleh 20 dolar saja?",
        "a_id": "25 dolar adalah harga paling pas.",
        "note_id": "best price = harga pas terbaik"
    },

    # Chapter 5
    "What flights are there to Oslo?": {
        "q_id": "Penerbangan apa saja yang ada ke Oslo?",
        "a_id": "Ada dua penerbangan besok: jam 7.30 pagi dan jam 4 sore.",
        "note_id": "flight = penerbangan pesawat"
    },
    "Are there any direct flights to Dallas?": {
        "q_id": "Apakah ada penerbangan langsung (tanpa transit) ke Dallas?",
        "a_id": "Tidak ada, Anda harus transit ganti pesawat di Chicago atau Kansas City.",
        "note_id": "direct flight = penerbangan langsung; transfer = transit ganti pesawat"
    },
    "I’d like to book a flight to Beijing, please. The 19th of March.": {
        "q_id": "Saya mau pesan tiket penerbangan ke Beijing untuk tanggal 19 Maret.",
        "a_id": "Ada penerbangan jam 5.20 pagi. Mau dipesankan di jadwal itu? — Iya, tolong.",
        "note_id": "book a flight = memesan tiket pesawat"
    },
    "I’d like to change my flight reservation. I'm booked on flight XPL on April 12.": {
        "q_id": "Saya mau mengubah jadwal reservasi penerbangan saya di tiket pesawat nomor XPL tanggal 12 April.",
        "a_id": "Mau berangkat tanggal berapa? Kena biaya ubah jadwal karena tiket dipesan lebih dari 24 jam lalu.",
        "note_id": "change fee = biaya perubahan jadwal"
    },
    "Can I see your passport and tickets, please?": {
        "q_id": "Boleh saya lihat paspor dan tiket pesawat Anda?",
        "a_id": "Ini dia. Maaf penerbangan Anda tertunda (delay). Sekarang dijadwalkan terbang jam 4.30 sore.",
        "note_id": "delayed = tertunda (delay); passport = paspor"
    },
    "Would you like an aisle or a window seat?": {
        "q_id": "Anda ingin kursi di dekat lorong jalan atau dekat jendela pesawat?",
        "a_id": "Kursi dekat jendela, tolong.",
        "note_id": "aisle seat = kursi dekat lorong; window seat = kursi dekat jendela"
    },
    "Are you checking in any bags?": {
        "q_id": "Apakah Anda membawa bagasi untuk dimasukkan ke bagasi pesawat?",
        "a_id": "Ada satu koper bagasi dan satu tas jinjing kabin. — Ukurannya melebihi batas, letakkan di alat ukur tas dulu.",
        "note_id": "carry-on = tas jinjing yang boleh dibawa ke kabin pesawat"
    },
    "Did you pack your bags yourself? Are there any sharp or prohibited items?": {
        "q_id": "Apakah Anda mengemas tas Anda sendiri? Apakah ada benda tajam atau barang terlarang?",
        "a_id": "Iya, saya kemas sendiri. Tidak ada barang terlarang.",
        "note_id": "prohibited items = barang-barang terlarang"
    },
    "I have a stopover in Miami. Will I have to collect my luggage there?": {
        "q_id": "Saya transit di Miami. Apakah saya harus mengambil koper bagasi di sana?",
        "a_id": "Tidak perlu, bagasi Anda langsung diteruskan sampai tujuan akhir Montevideo. Ini boarding pass Anda.",
        "note_id": "boarding pass = tiket masuk ke pesawat"
    },
    "Do I need to take my mobile out of the bag?": {
        "q_id": "Apakah saya perlu mengeluarkan ponsel HP dari dalam tas?",
        "a_id": "Iya perlu. Tolong taruh ponselnya di keranjang plastik baki pemeriksaan.",
        "note_id": "bin = wadah baki plastik pemeriksaan bandara"
    },
    "Do you have any coins or keys in your pockets?": {
        "q_id": "Apakah ada uang koin logam atau kunci di kantong celana Anda?",
        "a_id": "Tidak ada, sudah saya keluarkan semua. — Kalau begitu silakan jalan lewat pemindai tubuh.",
        "note_id": "body scan = alat pemindai tubuh bandara"
    },
    "Can I take this bottle of water on board?": {
        "q_id": "Bolehkah saya membawa sebotol air minum ini ke dalam pesawat?",
        "a_id": "Maaf Pak, tidak boleh membawa cairan melewati pemeriksaan keamanan.",
        "note_id": "on board = di dalam pesawat"
    },
    "Is this the gate for flight 234 to Madrid?": {
        "q_id": "Apakah ini pintu gerbang ruang tunggu untuk penerbangan nomor 234 ke Madrid?",
        "a_id": "Iya betul, di sini gerbangnya.",
        "note_id": "gate = pintu gerbang keberangkatan pesawat"
    },
    "Welcome to the USA. Where are you travelling from and what is the purpose of your trip?": {
        "q_id": "Selamat datang di Amerika. Dari mana asal penerbangan Anda dan apa tujuan kunjungan Anda?",
        "a_id": "Dari Prancis. Saya ke sini untuk liburan selama 10 hari.",
        "note_id": "purpose of trip = tujuan kunjungan / liburan"
    },
    "Who are you travelling with and where will you be staying?": {
        "q_id": "Bersama siapa Anda bepergian dan di mana Anda akan menginap?",
        "a_id": "Bersama suami saya. Di Hotel Hilton.",
        "note_id": "immigration = pemeriksaan imigrasi"
    },
    "My luggage hasn’t arrived. I think it’s lost. What does your bag look like?": {
        "q_id": "Koper bagasi saya belum keluar di korsel bagasi. Sepertinya hilang. Seperti apa ciri-ciri koper Anda?",
        "a_id": "Koper warna cokelat dan ada label namaku. — Koper Anda sedang ditahan di bea cukai di lorong itu.",
        "note_id": "lost luggage = bagasi yang hilang"
    },
    "I picked up my suitcase and found that it’s been damaged.": {
        "q_id": "Saya mengambil koper saya dan mendapati kopernya rusak.",
        "a_id": "Apa bagian yang rusak? — Rodanya patah dan bagian sampingnya penyok.",
        "note_id": "dented = penyok"
    },
    "Hello! Are you Ms. Jones? Welcome to Brazil.": {
        "q_id": "Halo! Apakah Anda Nona Jones? Selamat datang di Brasil.",
        "a_id": "Iya betul, saya sendiri. Saya Sanches dari Netco. Saya di sini untuk mengantar Anda ke kantor kami.",
        "note_id": "meeting visitor = menjemput tamu di bandara"
    },
    "Did you have a good flight? You must be very tired.": {
        "q_id": "Apakah penerbanganmu nyaman? Kamu pasti lelah sekali setelah perjalanan panjang.",
        "a_id": "Penerbangannya lancar tapi sangat lama. Iya aku lumayan lelah. Mobilku di sebelah sini.",
        "note_id": "tired = lelah"
    },

    # Chapter 6
    "I’d like to rent a car for 3 days. What type of car would you like?": {
        "q_id": "Saya ingin menyewa mobil selama 3 hari. Mau jenis mobil yang mana?",
        "a_id": "Saya mau mobil ukuran sedang (sedan). Berapa biaya sewanya? — 30 dolar per hari.",
        "note_id": "rent a car = sewa mobil"
    },
    "Would you like insurance on your car? How many people are going to drive?": {
        "q_id": "Apakah Anda mau menambahkan asuransi mobil? Berapa orang yang akan menyetir?",
        "a_id": "Iya tolong pakai asuransi. Hanya saya sendiri yang menyetir.",
        "note_id": "insurance = asuransi pelindung jika ada kecelakaan"
    },
    "Can I see your driver’s licence?": {
        "q_id": "Bolehkah saya melihat Surat Izin Mengemudi (SIM) Anda?",
        "a_id": "Apakah SIM internasional saya bisa digunakan?",
        "note_id": "driver's licence = SIM (Surat Izin Mengemudi)"
    },
    "Do I have to return the car to this location?": {
        "q_id": "Apakah saya harus mengembalikan mobil sewa ke cabang ini juga?",
        "a_id": "Tidak perlu, Anda bisa kembalikan di cabang kami mana saja sebelum jam 2 pagi hari Rabu.",
        "note_id": "return location = lokasi pengembalian mobil"
    },
    "How much would you charge me if I’m an hour late?": {
        "q_id": "Berapa denda biaya yang dikenakan jika saya terlambat mengembalikan 1 jam?",
        "a_id": "Ada biaya denda keterlambatan per jam.",
        "note_id": "late fee = denda keterlambatan"
    },
    "I’m calling about the flat for rent. Is it still available? Can I see it today?": {
        "q_id": "Saya menelepon mengenai apartemen/rumah sewa. Apakah masih tersedia? Boleh saya survei hari ini?",
        "a_id": "Iya masih ada.",
        "note_id": "flat for rent = apartemen yang disewakan"
    },
    "How much is the rent? Are utilities included?": {
        "q_id": "Berapa biaya sewa bulanannya? Apakah sudah termasuk biaya air dan listrik?",
        "a_id": "Uang sewanya 1200 dolar per bulan. Biaya listrik dan air bayar sendiri.",
        "note_id": "utilities = tagihan air, listrik, dan gas"
    },
    "When is the rent due?": {
        "q_id": "Kapan tanggal jatuh tempo pembayaran sewa rumah?",
        "a_id": "Setiap tanggal satu awal bulan. Dibayar di muka.",
        "note_id": "in advance = dibayar di muka"
    },
    "Will the rent go up?": {
        "q_id": "Apakah uang sewanya akan naik?",
        "a_id": "Tidak akan naik sampai masa kontrak sewa selesai.",
        "note_id": "lease = surat perjanjian sewa"
    },
    "How much is the security deposit?": {
        "q_id": "Berapa uang jaminan depositnya?",
        "a_id": "Uang depositnya setara dengan uang sewa satu bulan.",
        "note_id": "security deposit = uang jaminan (dikembalikan saat masa sewa selesai)"
    },
    "Can I sublet? How much notice do I need to give if I want to leave early?": {
        "q_id": "Bolehkah saya menyewakan ulang ke orang lain? Berapa lama pemberitahuan jika mau pindah lebih awal?",
        "a_id": "Boleh kalau ada izin tertulis. Harus memberi tahu satu bulan sebelumnya.",
        "note_id": "sublet = menyewakan ulang ke pihak lain"
    },
    "Who do I contact if there is a problem? When will the flat be available?": {
        "q_id": "Siapa yang harus saya hubungi jika ada kerusakan? Kapan rumahnya siap ditempati?",
        "a_id": "Hubungi saya di nomor ini. Siap ditempati bulan depan.",
        "note_id": "available = tersedia untuk ditempati"
    },

    # Chapter 7
    "How much is a room? Are your basic rooms en suite?": {
        "q_id": "Berapa harga kamar per malam? Apakah kamar standarnya ada kamar mandi di dalam?",
        "a_id": "Mulai dari $50 sampai $250 untuk suite. Kamar standar kamar mandi luar, kamar lain kamar mandi dalam.",
        "note_id": "en-suite = kamar dengan kamar mandi di dalam"
    },
    "I need a room for 3 people (one double bed and one single bed).": {
        "q_id": "Saya butuh kamar untuk 3 orang (satu kasur besar dan satu kasur kecil).",
        "a_id": "Ada, kami punya kamar tipe suite untuk tiga orang.",
        "note_id": "double bed = kasur besar; single bed = kasur untuk satu orang"
    },
    "Is breakfast included? Do you have free wi-fi?": {
        "q_id": "Apakah sudah termasuk sarapan pagi? Apakah ada wi-fi gratis?",
        "a_id": "Kafe dekat hotel ada diskon untuk tamu. Wi-fi gratis tersedia di seluruh area hotel.",
        "note_id": "breakfast included = sudah termasuk sarapan"
    },
    "What are your check-in and check-out times? What is your cancellation policy?": {
        "q_id": "Jam berapa waktu check-in dan check-out? Bagaimana aturan pembatalan kamar?",
        "a_id": "Check-in jam 2 siang, check-out jam 12 siang. Batalkan minimal 24 jam sebelumnya agar tidak kena denda.",
        "note_id": "check-in = masuk hotel; check-out = keluar hotel"
    },
    "I’d like to book a double room for three nights starting Monday the 9th.": {
        "q_id": "Saya mau pesan kamar kasur ganda untuk tiga malam mulai hari Senin tanggal 9.",
        "a_id": "Atas nama siapa pemesanannya? — Victoria Garcia. Apakah kartu kredit saya akan ditahan saldonya?",
        "note_id": "put a hold on credit card = menahan saldo jaminan sementara di kartu"
    },
    "Hello, I’m checking in. My name is Julia Lawrence.": {
        "q_id": "Halo, saya mau check-in. Nama saya Julia Lawrence.",
        "a_id": "Baik Bu Lawrence... Pesanan kamar single untuk 5 malam ya? — Iya, betul sekali.",
        "note_id": "checking in = proses mendaftar masuk kamar hotel"
    },
    "Are you still open for breakfast?": {
        "q_id": "Apakah restoran masih buka untuk sarapan?",
        "a_id": "Masih, tapi sebentar lagi restorannya tutup, jadi sebaiknya Anda bergegas.",
        "note_id": "closes soon = sebentar lagi tutup"
    },
    "What time is dinner served? When does breakfast start?": {
        "q_id": "Jam berapa makan malam disajikan? Kapan sarapan dimulai?",
        "a_id": "Makan malam jam 6 sampai 9 malam. Sarapan mulai jam 7.30 pagi.",
        "note_id": "served = disajikan"
    },
    "What time does the pool open? Do I have to bring my own towel?": {
        "q_id": "Jam berapa kolam renang buka? Apakah saya harus membawa handuk sendiri dari kamar?",
        "a_id": "Buka jam 6.30 pagi. Anda bisa mengambil handuk langsung di kolam renang.",
        "note_id": "pool = kolam renang; towel = handuk"
    },
    "Can you send laundry service up to room 236, please?": {
        "q_id": "Bisakah Anda mengirim petugas penatu (laundry) ke kamar nomor 236?",
        "a_id": "Baik, saya akan segera kirimkan petugas ke kamar Anda.",
        "note_id": "laundry service = layanan cuci baju hotel"
    },
    "Can I have my suit pressed?": {
        "q_id": "Bisakah setelan jas saya disetrika?",
        "a_id": "Kami ada ruang setrika lengkap dengan setrikaan dan mejanya di lantai 2.",
        "note_id": "pressed = disetrika rapi"
    },
    "My room is noisy. Could I move to a quieter one?": {
        "q_id": "Kamar saya bising sekali. Bisakah saya pindah ke kamar yang lebih tenang?",
        "a_id": "Sebentar saya cek apakah masih ada kamar lain yang kosong sekarang.",
        "note_id": "noisy = berisik / bising; quiet = tenang"
    },
    "I just checked into my room and there’s hair in the bathtub.": {
        "q_id": "Saya baru masuk kamar dan ada rambut di bak mandi (bathtub).",
        "a_id": "Mohon maaf sekali. Saya akan segera panggil petugas kebersihan ke kamar Anda.",
        "note_id": "housekeeping = bagian kebersihan hotel"
    },
    "The air conditioner isn’t working / The bulb isn't working.": {
        "q_id": "AC kamarnya tidak menyala / Lampunya mati.",
        "a_id": "Saya akan panggil petugas teknisi untuk menggantinya sekarang juga.",
        "note_id": "maintenance = teknisi perawatan dan perbaikan"
    },
    "The toilet is not flushing properly.": {
        "q_id": "Air toiletnya tidak bisa disiram/flushing dengan lancar.",
        "a_id": "Saya akan segera kirimkan tukang leding (plumber) untuk memperbaikinya.",
        "note_id": "plumber = tukang pipa dan leding air"
    },
    "The mini bar is empty. Could you get someone to restock it?": {
        "q_id": "Kulkas mini bar di kamar kosong. Tolong diisi ulang camilan dan minumannya ya?",
        "a_id": "Tentu saja, akan segera kami isi.",
        "note_id": "restock = mengisi kembali persediaan"
    },
    "I am checking out of room 451. Could I have my bill, please?": {
        "q_id": "Saya mau check-out dari kamar 451. Boleh minta tagihan pembayarannya?",
        "a_id": "Ini dia tagihannya. Mau bayar bagaimana? Langsung potong kartu kredit yang terdaftar?",
        "note_id": "bill = tagihan biaya hotel"
    },
    "Can I leave my suitcase with the hotel for 2 days?": {
        "q_id": "Bolehkah saya menitipkan koper saya di hotel selama 2 hari?",
        "a_id": "Tentu saja, kami akan menjaga koper Anda tanpa dipungut biaya sepeser pun.",
        "note_id": "leave my suitcase = menitipkan koper"
    },

    # Chapter 8
    "I’d like to make an appointment with a GP, please.": {
        "q_id": "Saya ingin membuat janji temu dengan dokter umum, tolong.",
        "a_id": "Kapan Anda ingin datang berkonsultasi?",
        "note_id": "GP (General Practitioner) = dokter umum"
    },
    "I’d like to make an appointment with Dr. Taylor, please?": {
        "q_id": "Saya mau buat janji periksa dengan Dr. Taylor, tolong?",
        "a_id": "Jadwal Dr. Taylor penuh hari ini, tapi besok jam 3 sore masih ada waktu. — Boleh, saya ambil jadwal itu.",
        "note_id": "booked up = jadwal periksa sudah penuh"
    },
    "Can I make an appointment with the dentist, please?": {
        "q_id": "Bolehkah saya membuat janji periksa ke dokter gigi, tolong?",
        "a_id": "Bisa besok jam 10 pagi atau jam 3.30 sore. Jam berapa yang paling pas buat Anda? — Jam 10 pagi boleh.",
        "note_id": "dentist = dokter gigi"
    },
    "Would 5.30 pm be ok with you? Do you have anything earlier?": {
        "q_id": "Apakah jam 5.30 sore cocok buat Anda? Apakah ada jadwal yang lebih awal?",
        "a_id": "Maaf tidak ada lagi. Kalau ada pasien lain yang batal lebih awal, tolong kabari saya ya.",
        "note_id": "earlier = lebih awal / lebih cepat"
    },
    "What seems to be the trouble?": {
        "q_id": "Apa keluhan sakit yang Anda rasakan?",
        "a_id": "Ada bintik-bintik merah di seluruh tubuhku. — Apakah kamu memakan makanan yang membuat alergi?",
        "note_id": "blotches = bercak bintik merah pada kulit; allergic = alergi"
    },
    "I’ll prescribe you a cream. You should apply it twice a day.": {
        "q_id": "Saya akan resepkan krim obat. Oleskan dua kali sehari ya.",
        "a_id": "Berapa lama bengkaknya akan mengempis dan sembuh? — Kira-kira satu minggu.",
        "note_id": "prescribe = meresepkan obat; swelling = bengkak"
    },
    "You should go to the hospital for some blood tests / X-ray.": {
        "q_id": "Anda sebaiknya ke rumah sakit untuk tes darah atau rontgen foto sinar-X.",
        "a_id": "Apakah menurut dokter ada persendian yang robek? — Kalau dalam dua hari belum membaik, kembali periksa ke sini ya.",
        "note_id": "blood test = tes darah; X-ray = foto rontgen sinar-X"
    },

    # Chapter 9
    "I’d like to book a table for tonight, please. For 4 people at 7 pm.": {
        "q_id": "Saya mau pesan meja makan untuk nanti malam. Untuk 4 orang jam 7 malam.",
        "a_id": "Baik, sudah saya catat meja untuk 4 orang jam 7 malam.",
        "note_id": "book a table = memesan meja makan di restoran"
    },
    "Good evening. Do you have a reservation?": {
        "q_id": "Selamat malam. Apakah Anda sudah membuat reservasi meja sebelumnya?",
        "a_id": "Sudah, meja untuk dua orang atas nama Johnson. / Saya gabung dengan rombongan Tom Jenkin.",
        "note_id": "reservation = pesanan meja terlebih dahulu"
    },
    "Do you have a booking? / Have you got any free tables?": {
        "q_id": "Apakah Anda sudah memesan meja? / Apakah ada meja kosong malam ini?",
        "a_id": "Belum ada pesanan meja. Apakah ada yang kosong? — Anda harus menunggu sekitar 10 menit.",
        "note_id": "free table = meja kosong yang siap dipakai"
    },
    "Can we have a table by the window / on the terrace?": {
        "q_id": "Bolehkah kami duduk di meja dekat jendela / di balkon teras luar?",
        "a_id": "Tentu saja boleh. / Sebentar saya lihat apakah ada yang kosong.",
        "note_id": "by the window = di samping jendela"
    },
    "Do you have a high chair for little children?": {
        "q_id": "Apakah ada kursi tinggi khusus anak-anak kecil?",
        "a_id": "Ada, tentu saja. Biar kuambilkan sekarang.",
        "note_id": "high chair = kursi makan tinggi khusus anak kecil"
    },
    "What should I order? What’s best here?": {
        "q_id": "Menu apa yang paling enak dipesan di sini?",
        "a_id": "Masakan ikan di sini sangat lezat. Menu andalan kami adalah makanan laut (seafood).",
        "note_id": "speciality = menu andalan istimewa"
    },
    "Are you ready to order? Can I take your order?": {
        "q_id": "Apakah Anda sudah siap memesan makanan? Mau pesan apa saja?",
        "a_id": "Ya, saya mau salad tuna dan sebotol air mineral tanpa soda.",
        "note_id": "take your order = mencatat pesanan makanan Anda"
    },
    "Could you serve the salad on the side, please? What dressings do you have?": {
        "q_id": "Bisa tolong pisahkan saus salad di piring kecil terpisah? Ada saus apa saja?",
        "a_id": "Tentu. Kami punya saus Italia, saus Prancis, dan saus keju biru.",
        "note_id": "on the side = saus ditaruh di mangkuk terpisah"
    },
    "How would you like your steak done? Rare, medium, well-done?": {
        "q_id": "Steak dagingnya mau tingkat kematangan apa? Setengah matang, matang sedang, atau matang sempurna?",
        "a_id": "Matang sedang (medium) ya. Kami agak buru-buru, berapa lama masaknya? — Sekitar 10 menit.",
        "note_id": "well-done = daging matang sempurna"
    },
    "Would you like a dessert? Is there anything you would recommend?": {
        "q_id": "Mau pesan hidangan penutup pencuci mulut? Ada menu penutup yang direkomendasikan?",
        "a_id": "Kue Tiramisu. Rasanya sangat lezat.",
        "note_id": "dessert = hidangan penutup manis"
    },
    "Excuse me, I dropped my fork. Can I get another, please?": {
        "q_id": "Permisi, garpuku jatuh ke lantai. Boleh minta garpu yang baru?",
        "a_id": "Tentu saja. Segera kuambilkan yang baru.",
        "note_id": "fork = garpu makan"
    },
    "Excuse me, this cup is dirty. / There’s a hair in the soup.": {
        "q_id": "Permisi, cangkir ini kotor. / Ada rambut di dalam sup ini.",
        "a_id": "Saya mohon maaf sebesar-besarnya. Saya ganti yang baru dan supnya gratis tidak kami tagih.",
        "note_id": "apologize = meminta maaf"
    },
    "My baked potato is raw inside. / This meat is undercooked.": {
        "q_id": "Kentang panggangku masih mentah di dalam. / Daging ini masih belum cukup matang.",
        "a_id": "Maafkan kami, Bu. Saya akan segera ganti dengan yang dipanggang matang sempurna.",
        "note_id": "raw = mentah; undercooked = belum cukup matang"
    },
    "Let’s split it.": {
        "q_id": "Ayo kita bayar patungan bagi dua tagihannya.",
        "a_id": "Jangan, biar aku saja yang bayar semuanya, ini traktiran dariku. — Terima kasih banyak ya.",
        "note_id": "split = patungan; my treat = traktiran saya"
    },
    "Can I have the bill, please? We’d like separate bills.": {
        "q_id": "Boleh minta bon tagihan pembayarannya? Tolong bon tagihannya dipisah masing-masing ya.",
        "a_id": "Segera kami bawakan bonnya. Tentu bisa.",
        "note_id": "separate bills = bon pembayaran dipisah sendiri-sendiri"
    },
    "I’m afraid there is a mistake in the bill. You charged me twice for dessert.": {
        "q_id": "Sepertinya ada kesalahan di bon ini. Anda menagih kue penutup dua kali lipat.",
        "a_id": "Maafkan saya, Bu. Saya akan segera bawakan bon yang sudah diperbaiki.",
        "note_id": "mistake in the bill = ada kesalahan hitung di bon"
    },

    # Chapter 10
    "The washing machine isn’t working. Do you know what’s wrong with it?": {
        "q_id": "Mesin cucinya tidak mau menyala. Kamu tahu apa kerusakannya?",
        "a_id": "Remote control TV-nya juga tidak menyala. Sepertinya baterainya sudah habis.",
        "note_id": "not working = tidak menyala / rusak"
    },
    "My lock is broken. The key doesn’t turn.": {
        "q_id": "Kunci pintuku rusak macet. Kuncinya tidak bisa diputar.",
        "a_id": "Kamu sebaiknya memanggil tukang kunci (locksmith).",
        "note_id": "locksmith = ahli kunci pintu"
    },
    "The tap in the kitchen is dripping.": {
        "q_id": "Keran air di dapur bocor menetes terus.",
        "a_id": "Saya akan panggil tukang leding sekarang juga.",
        "note_id": "tap is dripping = keran air menetes bocor"
    },
    "One of my burners won’t light. / The bulb is blown.": {
        "q_id": "Salah satu tungku kompor tidak mau menyala. / Bohlam lampunya putus mati.",
        "a_id": "Bisa jadi tersumbat kotoran, cukup dibersihkan. / Segera kuganti bohlamnya sekarang.",
        "note_id": "burner = tungku kompor; bulb is blown = bohlam lampu putus"
    },
    "I’ve locked myself out of my car.": {
        "q_id": "Kunci mobilku tertinggal terkunci di dalam mobil.",
        "a_id": "Apakah kamu memegang kunci cadangannya?",
        "note_id": "locked out = terkunci dari luar"
    },
    "My car won’t start. The battery must be dead.": {
        "q_id": "Mobilku tidak bisa distarter. Pasti akinya habis mati.",
        "a_id": "Apakah kamu butuh bantuan jumper aki mobil? / Sebaiknya cepat panggil montir bengkel.",
        "note_id": "battery dead = aki mobil mati; need a boost = butuh kabel jumper aki"
    },
    "Your right brake light is out. / My car tyre is flat.": {
        "q_id": "Lampu rem kanan mobilmu mati. / Ban mobilku kempes bocor.",
        "a_id": "Terima kasih banyak sudah memberi tahu. / Apakah bannya tertusuk paku bocor?",
        "note_id": "brake light = lampu rem; puncture = bocor tertusuk paku"
    },
    "The man has fallen over and badly hurt himself.": {
        "q_id": "Pria itu jatuh tersandung dan terluka parah.",
        "a_id": "Dia harus segera dibawa ke klinik khusus tulang dan patah kaki.",
        "note_id": "fracture clinic = klinik khusus cedera dan patah tulang"
    },
    "The woman has fainted in the heat. She is unconscious.": {
        "q_id": "Wanita itu pingsan karena kepanasan terik. Dia tidak sadarkan diri.",
        "a_id": "Cepat telepon ambulans! Dia butuh pertolongan napas buatan (CPR).",
        "note_id": "unconscious = tidak sadarkan diri; CPR = pertolongan pertama henti napas"
    },
    "I’ve burned myself. It’s my hand.": {
        "q_id": "Tanganku terkena luka bakar air panas.",
        "a_id": "Cepat basuh dan rendam tanganmu di bawah kucuran air dingin.",
        "note_id": "burn = luka bakar"
    },
    "There is a robbery in progress / fight outside the bar.": {
        "q_id": "Sedang terjadi perampokan / ada perkelahian di luar.",
        "a_id": "Berapa alamat tempat kejadiannya? Tunggu sebentar, saya segera kirimkan mobil polisi ke sana.",
        "note_id": "police dispatched = polisi segera dikirimkan ke lokasi"
    },
    "There’s a car accident. Is anyone trapped inside?": {
        "q_id": "Ada kecelakaan tabrakan mobil. Apakah ada korban terjebak di dalam mobil?",
        "a_id": "Satu orang pria terjebak. Ambulans sedang dalam perjalanan ke sini. Apa yang harus kita lakukan sambil menunggu?",
        "note_id": "trapped = terjebak di dalam kendaraan"
    },
    "My house is on fire! / My house is flooding!": {
        "q_id": "Rumahku kebakaran! / Rumahku kebanjiran air!",
        "a_id": "Petugas pemadam kebakaran sedang meluncur ke sana. / Apakah ada pipa air utama yang pecah?",
        "note_id": "on fire = kebakaran; burst pipe = pipa air pecah"
    },
    "I’d like to report a crime / break-in. My bag has been stolen.": {
        "q_id": "Saya mau melaporkan tindak kejahatan pencurian / pembobolan rumah. Tasku dicuri orang.",
        "a_id": "Bisa ceritakan apa yang terjadi? Kapan dan di mana kejadiannya?",
        "note_id": "stolen = dicuri"
    },

    # Chapter 11
    "Can I speak to Mary Taylor, please?": {
        "q_id": "Bolehkah saya berbicara dengan Mary Taylor?",
        "a_id": "Iya saya sendiri yang bicara. — Hai Mary, ini Rita Cooper.",
        "note_id": "speaking = saya sendiri (jawaban saat ditelepon)"
    },
    "Could I speak to Peter Wright, please? Who is calling?": {
        "q_id": "Bisakah saya bicara dengan Peter Wright? Boleh tahu dengan siapa yang menelepon?",
        "a_id": "Dengan Brian Evans. — Tunggu sebentar ya, saya panggilkan dia.",
        "note_id": "hold on = tunggu sebentar di telepon"
    },
    "Hi, Brian. How are you doing? What can I do for you?": {
        "q_id": "Hai Brian, apa kabar? Ada yang bisa kubantu?",
        "a_id": "Aku menelepon untuk mengingatkan rencana makan malam kita.",
        "note_id": "remind = mengingatkan janji"
    },
    "Can I speak to someone from the HR department? Can I ask what it is in connection with?": {
        "q_id": "Bolehkah saya bicara dengan bagian personalia HRD? Terkait urusan apa ya?",
        "a_id": "Saya menelepon terkait lamaran pekerjaan staf penjualan. — Baik saya sambungkan ke bagian terkait.",
        "note_id": "connect you = menyambungkan panggilan telepon"
    },
    "She is at lunch. Would you like to leave a message or call her back later?": {
        "q_id": "Beliau sedang makan siang di luar. Apakah Anda ingin meninggalkan pesan atau menelepon lagi nanti?",
        "a_id": "Saya akan telepon lagi nanti, terima kasih. / Boleh titip pesan? — Boleh, sebentar saya ambil pulpen.",
        "note_id": "leave a message = meninggalkan pesan telepon"
    },
    "He isn’t at his desk now. Is it urgent?": {
        "q_id": "Beliau sedang tidak ada di meja kerjanya. Apakah ini sangat mendesak/penting?",
        "a_id": "Tidak terlalu mendesak. Boleh saya tinggalkan pesan saja untuknya? — Boleh, silakan sebutkan pesannya.",
        "note_id": "urgent = mendesak dan penting"
    },
    "Is this a good time to call?": {
        "q_id": "Apakah ini waktu yang tepat untuk meneleponmu?",
        "a_id": "Tentu, sekarang waktu yang pas. Ada apa? / Maaf aku lagi sibuk mengurus sesuatu, bisa telepon lagi 2 jam lagi?",
        "note_id": "good time to call = waktu yang santai untuk ditelepon"
    },
    "He is in a meeting. Do you know when it’ll be over?": {
        "q_id": "Beliau sedang rapat. Apakah kamu tahu jam berapa rapatnya selesai?",
        "a_id": "Kira-kira berapa lama lagi beliau akan selesai rapat?",
        "note_id": "meeting = rapat; be over = selesai"
    },
    "The line is bad. Can you speak up?": {
        "q_id": "Suara teleponnya putus-putus dan kresek-kresek. Bisakah kamu bicara lebih keras?",
        "a_id": "Aku akan coba telepon lagi saat aku sudah sampai di kantor.",
        "note_id": "speak up = bicara lebih keras; line is bad = suara telepon tidak jelas"
    },
    "My phone is dying. I’m afraid we’ll get cut off now.": {
        "q_id": "Baterai ponselku mau habis mati. Takutnya telepon kita bakal terputus tiba-tiba.",
        "a_id": "Biar kutelepon kamu lewat telepon yang satu lagi ya.",
        "note_id": "phone is dying = baterai HP hampir habis; cut off = telepon terputus"
    }
}

# Attach translations to each item in each chapter
for c in chapters:
    t_info = translations.get(c["title"], {})
    c["title_id"] = t_info.get("title_id", c["title"])
    c["sub_id"] = t_info.get("sub_id", c["sub"])

    for topic in c["topics"]:
        for item in topic["items"]:
            en_q = item["q"]
            # Look for exact match or substring match in item_translations
            match = item_translations.get(en_q)
            if not match:
                for k, v in item_translations.items():
                    if k in en_q or en_q in k:
                        match = v
                        break
            
            if match:
                item["q_id"] = match["q_id"]
                item["a_id"] = match["a_id"]
                if "note_id" in match:
                    item["note_id"] = match["note_id"]
            else:
                # Default fallback
                item["q_id"] = ""
                item["a_id"] = ""

with open("bilingual_spoken_english.json", "w", encoding="utf-8") as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)

print("Saved bilingual_spoken_english.json successfully!")
