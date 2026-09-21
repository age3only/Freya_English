import json

with open("bilingual_spoken_english.json", "r", encoding="utf-8") as f:
    chapters_data = json.load(f)

# Update chapter badges with cute magical, unicorn, kitty, candy theme badges
magical_badges = [
    "🦄", # Ch 1: Good Manners
    "🎡", # Ch 2: Public Places
    "🎀", # Ch 3: Social Interaction
    "🛍️", # Ch 4: Shopping
    "✈️", # Ch 5: Air Travel
    "🏰", # Ch 6: Rental / Castle
    "🏨", # Ch 7: Hotel
    "🩺", # Ch 8: Doctor
    "🧁", # Ch 9: Eating Out / Treats
    "🚨", # Ch 10: Emergencies
    "📱", # Ch 11: Telephoning
]

for i, ch in enumerate(chapters_data):
    if i < len(magical_badges):
        ch["badge"] = magical_badges[i]

html_code = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Freya English">
<title>Freya's Magical English Adventure 🦄🎀</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@600;700;800&family=Baloo+2:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>
  :root{
    --pink-light:#FFF0F5;
    --pink-soft:#FFE4EC;
    --pink-mid:#FFB6C1;
    --pink-bright:#FF69B4;
    --pink-deep:#E75480;
    --pink-dark:#C2185B;
    --lavender:#E8D7FF;
    --lavender-deep:#9C27B0;
    --mint:#D4F8E8;
    --mint-dark:#20BF6B;
    --sky:#E0F4FF;
    --sky-dark:#2D98DA;
    --butter:#FFF9D2;
    --gold:#FFB800;
    --cream:#FFFFFF;
    --plum:#4A154B;
    --text-dark:#3A2A45;
  }
  *{ box-sizing:border-box; -webkit-tap-highlight-color: transparent; }
  
  html,body{
    margin:0; padding:0; height:100%;
    font-family:'Quicksand', 'Nunito', sans-serif;
    background:
      radial-gradient(circle at 12% 10%, #FFE4F0 0%, transparent 35%),
      radial-gradient(circle at 88% 12%, #E8D7FF 0%, transparent 35%),
      radial-gradient(circle at 50% 85%, #D7F3FE 0%, transparent 45%),
      linear-gradient(180deg, #FFF0F6 0%, #FAEDF8 40%, #F0F4FF 100%);
    color:var(--text-dark);
    overflow-x:hidden;
    -webkit-user-select:none;
    user-select:none;
  }

  /* Floating decorative sparkles */
  .bg-sparkles{
    position:fixed; inset:0; pointer-events:none; z-index:0; overflow:hidden;
  }
  .bg-sparkle{
    position:absolute; font-size:16px; opacity:0.6;
    animation:twinkle 3.5s ease-in-out infinite alternate;
  }
  @keyframes twinkle{ 0%{ transform:scale(0.8) rotate(0deg); opacity:0.3; } 100%{ transform:scale(1.2) rotate(20deg); opacity:0.85; } }

  h1,h2,h3,.display{ font-family:'Baloo 2', 'Fredoka One', cursive, sans-serif; }
  button{ font-family:'Quicksand', sans-serif; cursor:pointer; border:none; }
  .screen{ min-height:100vh; padding:18px 16px 60px; position:relative; max-width:620px; margin:0 auto; z-index:1; }
  .hidden{ display:none !important; }

  /* ---------- TOP BAR ---------- */
  .topbar{
    display:flex; align-items:center; justify-content:space-between;
    margin-bottom:14px;
  }
  .topbar .stars{
    background:#FFFFFF; border-radius:999px; padding:7px 18px;
    font-weight:800; font-size:15px;
    border:2.5px solid var(--pink-soft);
    box-shadow:0 4px 12px rgba(231, 84, 128, 0.15);
    display:flex; align-items:center; gap:6px; color:var(--pink-dark);
  }
  .name-badge{
    background:linear-gradient(135deg, #FFB6C1, #FF69B4);
    color:#fff; padding:6px 16px; border-radius:999px; font-weight:800;
    font-size:13px; letter-spacing:0.5px; box-shadow:0 3px 8px rgba(255, 105, 180, 0.35);
    display:flex; align-items:center; gap:5px;
  }
  .backbtn{
    background:#FFFFFF; width:44px; height:44px; border-radius:50%;
    font-size:22px; border:2.5px solid var(--pink-soft);
    box-shadow:0 4px 10px rgba(231, 84, 128, 0.15);
    display:flex; align-items:center; justify-content:center;
    transition:transform .12s ease; color:var(--pink-dark); font-weight:900;
  }
  .backbtn:active{ transform:translateY(2px); box-shadow:0 2px 4px rgba(231, 84, 128, 0.15); }

  /* ---------- HERO SECTION ---------- */
  .hero{ text-align:center; margin-bottom:16px; }
  .mascot-row{
    display:flex; align-items:center; justify-content:center; gap:8px;
    margin-bottom:6px;
  }
  .mascot-icon{
    font-size:52px; display:inline-block;
    filter:drop-shadow(0 6px 12px rgba(255, 105, 180, 0.25));
  }
  .mascot-icon.unicorn{ animation:bounce 2.6s ease-in-out infinite; }
  .mascot-icon.kitty{ animation:bounce 2.6s ease-in-out infinite 0.4s; }
  .mascot-icon.bow{ font-size:36px; animation:wiggle 2s ease-in-out infinite; }
  @keyframes bounce{ 0%,100%{transform:translateY(0) rotate(-4deg);} 50%{transform:translateY(-10px) rotate(4deg);} }
  @keyframes wiggle{ 0%,100%{transform:rotate(-8deg);} 50%{transform:rotate(8deg);} }

  .hero h1{
    font-size:27px; margin:4px 0 3px; color:var(--plum); line-height:1.2;
    text-shadow:0 2px 0 rgba(255, 255, 255, 0.8);
  }
  .hero-tag{
    display:inline-block; background:#FFEBF2; color:var(--pink-dark);
    font-weight:800; font-size:12.5px; padding:4px 14px; border-radius:999px;
    border:1.5px solid #FFCCD9; margin-bottom:4px;
  }
  .hero p{ margin:0; font-weight:800; color:#85586F; font-size:14px; }

  /* ---------- SOUND TIP BANNER FOR IPAD ---------- */
  .sound-tip{
    background:#FFF5EB; border:1.5px dashed #FFA94D; border-radius:16px;
    padding:8px 14px; margin:10px auto 14px; font-size:12px; font-weight:800;
    color:#D9480F; display:flex; align-items:center; gap:8px; text-align:left;
  }

  /* ---------- CHAPTER CARDS ---------- */
  .chapter-list{ display:flex; flex-direction:column; gap:13px; margin-top:16px; }
  .chapter-card{
    background:#FFFFFF; border-radius:26px; padding:16px 18px;
    display:flex; align-items:center; gap:16px;
    border:2.5px solid #FFDFE9;
    box-shadow:0 6px 18px rgba(255, 140, 180, 0.14), 0 3px 0 #FFCCD9;
    transition:transform .14s ease, box-shadow .14s ease;
    cursor:pointer; text-align:left; position:relative; overflow:hidden;
  }
  .chapter-card::after{
    content:''; position:absolute; top:-20px; right:-20px; width:60px; height:60px;
    background:radial-gradient(circle, rgba(255,182,193,0.35) 0%, transparent 70%);
    border-radius:50%;
  }
  .chapter-card:active{ transform:translateY(3px); box-shadow:0 2px 8px rgba(255, 140, 180, 0.15), 0 1px 0 #FFCCD9; }
  
  .ch-badge{
    width:66px; height:66px; border-radius:50%; flex:0 0 auto;
    display:flex; align-items:center; justify-content:center;
    font-size:32px; border:3px solid #FFF;
    box-shadow:0 4px 12px rgba(255, 105, 180, 0.25);
    background:linear-gradient(135deg, #FFE3EC, #FFCCD9);
  }
  .ch-info{ flex:1; min-width:0; }
  .ch-tag{ font-weight:900; font-size:11px; text-transform:uppercase; letter-spacing:1px; color:var(--pink-bright); }
  .ch-title{ font-family:'Baloo 2',sans-serif; font-weight:800; font-size:20px; color:var(--plum); line-height:1.2; margin:2px 0 1px; }
  .ch-sub-id{ font-size:13px; font-weight:800; color:var(--pink-dark); }
  .ch-sub-en{ font-size:11.5px; font-weight:700; color:#8A7A90; }
  .ch-stars{ font-size:15px; color:var(--gold); font-weight:800; margin-top:3px; }
  .ch-arrow{
    width:34px; height:34px; border-radius:50%; background:#FFF0F5;
    display:flex; align-items:center; justify-content:center;
    font-size:18px; color:var(--pink-bright); font-weight:900; flex:0 0 auto;
  }

  /* ---------- STATION SCREEN ---------- */
  .station-header{ text-align:center; margin-bottom:14px; }
  .station-header .badge-halo{
    width:90px; height:90px; border-radius:50%; margin:0 auto 6px;
    display:flex; align-items:center; justify-content:center; font-size:48px;
    background:linear-gradient(135deg, #FFE4EC, #FFCCD9);
    border:3px solid #FFF; box-shadow:0 6px 20px rgba(255, 105, 180, 0.28);
  }
  .station-header .id-title{ font-size:19px; font-weight:900; color:var(--pink-dark); }
  .station-header h2{ margin:2px 0; font-size:24px; color:var(--plum); }
  .station-header .sub{ font-weight:800; color:#85586F; font-size:13.5px; }

  .topic-box{
    background:#FFFFFF; border-radius:24px; padding:16px 18px;
    border:2.5px solid #FFDFE9; box-shadow:0 4px 14px rgba(255, 105, 180, 0.12);
    margin-bottom:18px; text-align:left;
  }
  .topic-label{ font-weight:900; font-size:13.5px; color:var(--plum); margin-bottom:8px; display:flex; align-items:center; gap:6px; }
  .topic-select{
    width:100%; padding:13px 14px; border-radius:16px; border:2px solid #FFCCD9;
    font-family:'Quicksand',sans-serif; font-size:14.5px; font-weight:800;
    color:var(--plum); background:#FFF8FA; outline:none;
    box-shadow:inset 0 2px 4px rgba(255, 182, 193, 0.15);
  }

  .mode-buttons{ display:flex; flex-direction:column; gap:14px; }
  .mode-btn{
    padding:18px 22px; border-radius:24px; font-weight:900; font-size:17px;
    display:flex; align-items:center; gap:15px; color:#fff; text-align:left;
    position:relative; overflow:hidden;
  }
  .mode-btn:active{ transform:translateY(3px); }
  .mode-btn .icon{ font-size:32px; filter:drop-shadow(0 2px 4px rgba(0,0,0,0.15)); }
  .mode-btn.learn{
    background:linear-gradient(135deg, #FF7597, #FF4D79);
    box-shadow:0 6px 0 #D81B60, 0 10px 20px rgba(216, 27, 96, 0.25);
  }
  .mode-btn.learn:active{ box-shadow:0 2px 0 #D81B60; }
  .mode-btn.play{
    background:linear-gradient(135deg, #B388EB, #8F00FF);
    box-shadow:0 6px 0 #6A0DAD, 0 10px 20px rgba(106, 13, 173, 0.25);
  }
  .mode-btn.play:active{ box-shadow:0 2px 0 #6A0DAD; }
  .mode-btn small{ display:block; font-weight:700; font-size:12.5px; opacity:0.95; margin-top:2px; }

  /* ---------- FLASHCARD SCREEN ---------- */
  .card-wrap{ margin-top:4px; }
  .progress-info{ text-align:center; font-weight:900; font-size:14px; color:var(--pink-dark); margin-bottom:8px; }
  .progress-bar-bg{
    width:100%; height:10px; background:#FFE6F0; border-radius:999px;
    margin-bottom:16px; overflow:hidden; border:1.5px solid #FFCCD9;
  }
  .progress-bar-fill{
    height:100%; background:linear-gradient(90deg, #FF85A2, #FF4D79);
    width:0%; transition:width .25s ease; border-radius:999px;
  }

  .flashcard{
    background:#FFFFFF; border-radius:30px; padding:24px 20px 20px;
    border:3px solid #FFCCD9;
    box-shadow:0 10px 30px rgba(255, 105, 180, 0.18), 0 5px 0 #FFB6C1;
    text-align:left; display:flex; flex-direction:column; gap:14px;
    min-height:320px; justify-content:center; position:relative;
  }
  .card-topic-tag{
    align-self:flex-start; background:linear-gradient(135deg, #FFE4EC, #FFD1E0);
    color:var(--pink-dark); font-weight:900; font-size:12px; padding:5px 14px;
    border-radius:14px; border:1.5px solid #FFAFCC;
  }
  .bubble{
    border-radius:22px; padding:15px 18px; font-size:16px; line-height:1.4;
    position:relative; cursor:pointer; transition:transform .12s ease;
  }
  .bubble:active{ transform:scale(0.98); }
  .bubble-speaker{
    font-size:12px; font-weight:900; text-transform:uppercase; letter-spacing:0.5px;
    margin-bottom:5px; display:flex; align-items:center; justify-content:space-between;
  }
  .speaker-sound-icon{ font-size:14px; background:rgba(255,255,255,0.7); padding:2px 8px; border-radius:999px; }
  .bubble.speaker-a{
    background:#F5EEFD; color:#5B2C6F; border-bottom-left-radius:6px;
    border:2px solid #E4D0FC;
  }
  .bubble.speaker-a .bubble-speaker{ color:#8E44AD; }
  .bubble.speaker-b{
    background:#FFF0F5; color:#78284A; border-bottom-right-radius:6px;
    border:2px solid #FFCCD9; align-self:flex-end; width:95%;
  }
  .bubble.speaker-b .bubble-speaker{ color:#C2185B; }

  .en-text{
    font-family:'Baloo 2', cursive, sans-serif; font-weight:800; font-size:20px;
    line-height:1.25; margin-bottom:5px;
  }
  .id-text{
    font-weight:800; font-size:13.5px; color:#4A3B4F;
    background:rgba(255,255,255,0.85); padding:5px 12px; border-radius:12px;
    display:inline-block; border:1px dashed #FFB6C1;
  }

  .card-note{
    background:#FFF9D2; border-left:5px solid #FFB800; padding:12px 14px;
    border-radius:14px; font-size:13px; font-weight:800; color:#875A00;
    margin-top:4px; line-height:1.45;
  }
  .card-audio-row{ display:flex; justify-content:center; gap:10px; margin-top:8px; }
  .listen-btn{
    background:linear-gradient(135deg, #FFE66D, #FFB800); color:#5A3E00;
    border-radius:999px; padding:12px 26px; font-weight:900; font-size:15.5px;
    box-shadow:0 4px 0 #D48800, 0 8px 16px rgba(255, 184, 0, 0.25);
    display:inline-flex; align-items:center; gap:9px; transition:transform .12s ease;
  }
  .listen-btn:active{ transform:translateY(2px); box-shadow:0 2px 0 #D48800; }

  .card-nav{ display:flex; justify-content:space-between; align-items:center; margin-top:20px; gap:12px; }
  .nav-btn{
    background:#FFFFFF; width:54px; height:54px; border-radius:50%; font-size:22px;
    border:2.5px solid #FFCCD9; box-shadow:0 4px 0 #FFCCD9;
    display:flex; align-items:center; justify-content:center;
    color:var(--pink-dark); font-weight:900;
  }
  .nav-btn:disabled{ opacity:0.35; pointer-events:none; }
  .finish-btn{
    flex:1; background:linear-gradient(135deg, #48DBBB, #20BF6B); color:#fff;
    font-weight:900; font-size:16.5px; padding:16px; border-radius:22px;
    box-shadow:0 5px 0 #0FA655, 0 8px 16px rgba(32, 191, 107, 0.25);
    text-align:center;
  }
  .finish-btn:active{ transform:translateY(2px); box-shadow:0 2px 0 #0FA655; }

  /* ---------- QUIZ SCREEN ---------- */
  .quiz-wrap{ margin-top:6px; }
  .quiz-top{ display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; }
  .quiz-hearts{ font-size:22px; letter-spacing:4px; filter:drop-shadow(0 2px 4px rgba(255, 105, 180, 0.25)); }
  .quiz-progress{ font-weight:900; font-size:14.5px; color:var(--pink-dark); }
  
  .quiz-question{
    background:#FFFFFF; border-radius:28px; padding:24px 20px; text-align:center;
    border:3px solid #FFCCD9; box-shadow:0 8px 24px rgba(255, 105, 180, 0.15), 0 4px 0 #FFCCD9;
    margin-bottom:16px;
  }
  .quiz-question .kicker{
    font-weight:900; font-size:13.5px; color:var(--pink-dark); margin-bottom:6px;
    background:#FFEAF2; display:inline-block; padding:3px 12px; border-radius:999px;
  }
  .quiz-question .qtext{
    font-family:'Baloo 2',sans-serif; font-weight:800; font-size:21px; color:var(--plum); line-height:1.3;
  }
  .quiz-question .subhint{ font-weight:800; font-size:13px; color:#7E6B88; margin-top:6px; }
  .quiz-listen-icon{
    margin-top:10px; display:inline-block; font-size:22px; cursor:pointer;
    background:#FFF0F5; border-radius:50%; width:42px; height:42px; line-height:42px; text-align:center;
    border:2px solid #FFCCD9; box-shadow:0 2px 6px rgba(255, 105, 180, 0.15);
  }

  .options{ display:flex; flex-direction:column; gap:12px; }
  .option{
    background:#FFFFFF; border-radius:20px; padding:16px 20px; font-weight:800; font-size:15px;
    text-align:left; border:2.5px solid #FFDFE9;
    box-shadow:0 4px 0 #FFCCD9, 0 6px 14px rgba(255, 105, 180, 0.08);
    color:var(--plum); line-height:1.4; transition:all .12s ease;
  }
  .option:active{ transform:translateY(2px); box-shadow:0 2px 0 #FFCCD9; }
  .option.correct{
    background:#D9F5E3 !important; border-color:#7FCE9C !important;
    box-shadow:0 4px 0 #5CB881 !important; color:#155724 !important;
  }
  .option.wrong{
    background:#FFE1DD !important; border-color:#FFA296 !important;
    box-shadow:0 4px 0 #E8503F !important; color:#842029 !important;
  }
  .option.disabled{ pointer-events:none; }
  .feedback{ text-align:center; font-weight:900; font-size:16.5px; min-height:26px; margin-top:14px; }
  .feedback.good{ color:var(--mint-dark); text-shadow:0 1px 2px rgba(32, 191, 107, 0.2); }
  .feedback.bad{ color:var(--coral-dark); }

  /* ---------- RESULT SCREEN ---------- */
  .result-wrap{ margin:36px auto 0; text-align:center; }
  .result-wrap .big-emoji{ font-size:78px; animation:pop .5s ease; filter:drop-shadow(0 6px 16px rgba(255, 105, 180, 0.3)); }
  @keyframes pop{ 0%{transform:scale(0);} 70%{transform:scale(1.2);} 100%{transform:scale(1);} }
  .result-wrap h2{ font-size:28px; margin:10px 0 4px; color:var(--plum); }
  .result-wrap p{ font-weight:800; color:var(--pink-dark); font-size:16.5px; }
  .result-stars{ font-size:46px; margin:14px 0; letter-spacing:8px; filter:drop-shadow(0 4px 8px rgba(255, 184, 0, 0.4)); }
  .result-score-tag{
    font-size:18px; font-weight:900; color:#fff; background:linear-gradient(135deg, #FF69B4, #C2185B);
    display:inline-block; padding:8px 24px; border-radius:999px; margin-bottom:18px;
    box-shadow:0 4px 12px rgba(194, 24, 91, 0.25);
  }
  .result-buttons{ display:flex; flex-direction:column; gap:13px; margin-top:22px; }

  /* ---------- CONFETTI ---------- */
  .confetti{ position:fixed; inset:0; pointer-events:none; z-index:50; overflow:hidden; }
  .confetti span{ position:absolute; top:-20px; font-size:26px; animation:fall linear forwards; }
  @keyframes fall{ to{ transform:translateY(110vh) rotate(360deg); opacity:0.25; } }

  .footer-note{ text-align:center; font-size:13px; color:#A4879F; font-weight:800; margin-top:30px; }
</style>
</head>
<body>

<!-- Floating background sparkles -->
<div class="bg-sparkles">
  <span class="bg-sparkle" style="top:5%; left:6%;">✨</span>
  <span class="bg-sparkle" style="top:12%; right:8%;">🌸</span>
  <span class="bg-sparkle" style="top:25%; left:85%;">💖</span>
  <span class="bg-sparkle" style="top:45%; left:3%;">⭐</span>
  <span class="bg-sparkle" style="top:60%; right:4%;">🎀</span>
  <span class="bg-sparkle" style="top:75%; left:8%;">🦄</span>
  <span class="bg-sparkle" style="top:90%; right:12%;">🍭</span>
</div>

<div class="confetti" id="confetti"></div>

<!-- ===================== HOME SCREEN ===================== -->
<section class="screen" id="screen-home">
  <div class="topbar">
    <div class="name-badge">👑 Freya Shyam</div>
    <div class="stars">⭐ <span id="totalStars">0</span> / <span id="maxStars">0</span> Bintang</div>
  </div>

  <div class="hero">
    <div class="mascot-row">
      <span class="mascot-icon unicorn">🦄</span>
      <span class="mascot-icon bow">🎀</span>
      <span class="mascot-icon kitty">🐱</span>
      <span class="mascot-icon sparkle">✨</span>
    </div>
    <div class="hero-tag">🌸 Hello Kitty &amp; Unicorn Edition 🦄</div>
    <h1>Petualangan Bahasa Inggris Freya!</h1>
    <p>Ayo belajar percakapan seru bersama Unicorn &amp; Kitty! 🎀</p>
  </div>

  <!-- iPad sound tip -->
  <div class="sound-tip">
    <span>🔊</span>
    <span><strong>Tips iPad:</strong> Jika suara tidak bunyi, pastikan iPad tidak dalam <em>Mode Hening (Silent Mode)</em> dan naikkan volume ya! ✨</span>
  </div>

  <div class="chapter-list" id="chaptersList"></div>

  <div class="footer-note">Sentuh 🔊 untuk mendengarkan suara putri cantik! ✨</div>
</section>

<!-- ===================== STATION MENU SCREEN ===================== -->
<section class="screen hidden" id="screen-station">
  <div class="topbar">
    <button class="backbtn" onclick="goHome()">←</button>
    <div class="name-badge">🦄 Freya's Island</div>
    <div class="stars">⭐ <span id="stationStars">0</span> / 3</div>
  </div>

  <div class="station-header">
    <div class="badge-halo" id="stHeaderBadge">🦄</div>
    <div class="id-title" id="stHeaderTitleId">Sopan Santun</div>
    <h2 id="stHeaderTitleEn">Good Manners</h2>
    <div class="sub" id="stHeaderSub">Greetings, Politeness &amp; Social Etiquette</div>
  </div>

  <div class="topic-box">
    <label class="topic-label" for="topicDropdown">🎀 Pilih Topik Percakapan:</label>
    <select class="topic-select" id="topicDropdown" onchange="onTopicChange()"></select>
  </div>

  <div class="mode-buttons">
    <button class="mode-btn learn" onclick="startLearn()">
      <span class="icon">📖</span>
      <span>Kartu Percakapan Ajaib<small>Baca, dengarkan suara &amp; lihat arti Indonesianya 🌸</small></span>
    </button>
    <button class="mode-btn play" onclick="startQuiz()">
      <span class="icon">🎯</span>
      <span>Main Kuis Bintang ⭐<small>Kumpulkan 3 bintang emas untuk Freya!</small></span>
    </button>
  </div>
</section>

<!-- ===================== FLASHCARD SCREEN ===================== -->
<section class="screen hidden" id="screen-learn">
  <div class="topbar">
    <button class="backbtn" onclick="showStation()">←</button>
    <div class="progress-info" id="learnProgressText">Kartu 1 dari 10 🌸</div>
    <button class="backbtn" onclick="speakCurrentDialogue()" title="Dengarkan Suara">🔊</button>
  </div>

  <div class="card-wrap">
    <div class="progress-bar-bg">
      <div class="progress-bar-fill" id="learnProgressBar"></div>
    </div>
    
    <div class="flashcard">
      <div class="card-topic-tag" id="cardTopicTag">🎀 Topik Percakapan</div>

      <!-- Speaker A (Unicorn Friend) - Tap to listen -->
      <div class="bubble speaker-a" onclick="speakSpeakerA()">
        <div class="bubble-speaker">
          <span>🦄 Teman Unicorn (Speaker A)</span>
          <span class="speaker-sound-icon">🔊 Ketuk</span>
        </div>
        <div class="en-text" id="cardTextAEn">Hello!</div>
        <div class="id-text" id="cardTextAId">🇮🇩 Halo!</div>
      </div>

      <!-- Speaker B (Kitty / Freya) - Tap to listen -->
      <div class="bubble speaker-b" onclick="speakSpeakerB()">
        <div class="bubble-speaker">
          <span>🐱 Putri Freya (Speaker B)</span>
          <span class="speaker-sound-icon">🔊 Ketuk</span>
        </div>
        <div class="en-text" id="cardTextBEn">Hi there!</div>
        <div class="id-text" id="cardTextBId">🇮🇩 Halo juga!</div>
      </div>

      <!-- Vocabulary / Note -->
      <div class="card-note hidden" id="cardNote"></div>

      <div class="card-audio-row">
        <button class="listen-btn" onclick="speakCurrentDialogue()">🔊 Dengarkan Semuanya ✨</button>
      </div>
    </div>

    <div class="card-nav">
      <button class="nav-btn" id="prevBtn" onclick="prevCard()">←</button>
      <button class="finish-btn" id="cardMainBtn" onclick="nextCard()">Lanjut 🌸 →</button>
      <button class="nav-btn" id="listenSmallBtn" onclick="speakCurrentDialogue()">🔊</button>
    </div>
  </div>
</section>

<!-- ===================== QUIZ SCREEN ===================== -->
<section class="screen hidden" id="screen-quiz">
  <div class="topbar">
    <button class="backbtn" onclick="showStation()">←</button>
    <div class="quiz-hearts" id="quizHearts">💖💖💖</div>
  </div>

  <div class="quiz-wrap">
    <div class="quiz-top">
      <div class="quiz-progress" id="quizProgressText">Soal 1 / 5 🦄</div>
    </div>
    <div class="quiz-question">
      <div class="kicker" id="quizKicker">Apa arti kalimat ini?</div>
      <div class="qtext" id="quizQ">Good morning! How are you?</div>
      <div class="subhint" id="quizSubhint"></div>
      <div class="quiz-listen-icon" onclick="speakQuizQuestion()">🔊</div>
    </div>
    <div class="options" id="quizOptions"></div>
    <div class="feedback" id="quizFeedback"></div>
  </div>
</section>

<!-- ===================== RESULT SCREEN ===================== -->
<section class="screen hidden" id="screen-result">
  <div class="result-wrap">
    <div class="big-emoji" id="resultEmoji">🦄</div>
    <h2 id="resultTitle">Luar Biasa, Princess Freya! 👑</h2>
    <p id="resultSub">Kamu berhasil menyelesaikan bab ini!</p>
    <div class="result-stars" id="resultStars">⭐⭐⭐</div>
    <div class="result-score-tag" id="resultScore">Nilai: 5 / 5 ⭐</div>
    <div class="result-buttons">
      <button class="finish-btn" onclick="retryQuiz()" id="retryBtn">🔁 Main Kuis Lagi 🎀</button>
      <button class="mode-btn learn" onclick="goHome()">🏝️ Kembali ke Pulau Impian 🦄</button>
    </div>
  </div>
</section>

<script>
/* =========================================================
   IOS / IPADOS AUDIO & SPEECH FIXES
   - Global memory retention (prevents iOS garbage collection bug)
   - AudioContext unlocking on touch
   - Speech synthesis queue unfreezing
   ========================================================= */
window._activeUtterances = [];
let audioCtx = null;
let audioUnlocked = false;

function getAudioContext(){
  if(!audioCtx){
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if(AudioContext) audioCtx = new AudioContext();
  }
  if(audioCtx && audioCtx.state === 'suspended'){
    audioCtx.resume().catch(()=>{});
  }
  return audioCtx;
}

function unlockAudioOnIOS(){
  if(audioUnlocked) return;
  audioUnlocked = true;

  // 1. Unlock Web Audio
  try{
    const ctx = getAudioContext();
    if(ctx && ctx.state === 'suspended') ctx.resume();
  }catch(e){}

  // 2. Unlock Speech Synthesis on iOS Safari
  try{
    if('speechSynthesis' in window){
      window.speechSynthesis.resume();
      const dummy = new SpeechSynthesisUtterance('');
      dummy.volume = 0;
      window.speechSynthesis.speak(dummy);
    }
  }catch(e){}
}

// Attach to all user touch/click events so iOS unlocks immediately
['touchstart', 'touchend', 'click'].forEach(evt => {
  window.addEventListener(evt, unlockAudioOnIOS, { passive: true });
});

/* =========================================================
   WEB AUDIO SOUND EFFECTS (100% Offline & Instant)
   ========================================================= */
function playMagicalSound(type){
  try{
    const ctx = getAudioContext();
    if(!ctx) return;
    const now = ctx.currentTime;

    if(type === 'sparkle' || type === 'correct'){
      // Ascending magical pentatonic chime (C6, E6, G6, B6, C7)
      const freqs = [1046.5, 1318.5, 1567.9, 1975.5, 2093.0];
      freqs.forEach((f, i) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(f, now + i * 0.08);
        gain.gain.setValueAtTime(0.18, now + i * 0.08);
        gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.08 + 0.4);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now + i * 0.08);
        osc.stop(now + i * 0.08 + 0.45);
      });
    } else if(type === 'wrong'){
      // Gentle soft tone
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(320, now);
      osc.frequency.linearRampToValueAtTime(260, now + 0.25);
      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now);
      osc.stop(now + 0.26);
    } else if(type === 'pop'){
      // Cute bubble pop
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(600, now);
      osc.frequency.exponentialRampToValueAtTime(1100, now + 0.09);
      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.09);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now);
      osc.stop(now + 0.1);
    }
  }catch(e){}
}

/* =========================================================
   ROBUST TEXT TO SPEECH (Tested for iOS & Safari)
   ========================================================= */
function findEnglishVoice(){
  if(!('speechSynthesis' in window)) return null;
  const voices = window.speechSynthesis.getVoices() || [];
  return voices.find(v => v.lang === 'en-US' || v.lang === 'en_US') ||
         voices.find(v => v.lang && v.lang.startsWith('en')) || null;
}

// Warm up voices when available
if('speechSynthesis' in window){
  window.speechSynthesis.onvoiceschanged = () => { findEnglishVoice(); };
}

function speakSingle(text, pitch = 1.1, rate = 0.88, onEnd = null){
  try{
    if(!('speechSynthesis' in window)) return;
    unlockAudioOnIOS();

    window.speechSynthesis.resume();
    window.speechSynthesis.cancel();

    setTimeout(() => {
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-US';
      u.rate = rate;
      u.pitch = pitch;

      const voice = findEnglishVoice();
      if(voice) u.voice = voice;

      // Keep reference to prevent iOS garbage collection
      window._activeUtterances = [u];

      u.onend = () => {
        window._activeUtterances = [];
        if(onEnd) onEnd();
      };
      u.onerror = () => {
        window._activeUtterances = [];
      };

      window.speechSynthesis.speak(u);
    }, 40);
  }catch(e){}
}

function speakDialoguePair(textA, textB){
  try{
    if(!('speechSynthesis' in window)) return;
    unlockAudioOnIOS();

    window.speechSynthesis.resume();
    window.speechSynthesis.cancel();

    setTimeout(() => {
      const uA = new SpeechSynthesisUtterance(textA);
      uA.lang = 'en-US';
      uA.rate = 0.86;
      uA.pitch = 1.25; // Unicorn pitch

      const uB = new SpeechSynthesisUtterance(textB);
      uB.lang = 'en-US';
      uB.rate = 0.86;
      uB.pitch = 1.05; // Freya reply pitch

      const voice = findEnglishVoice();
      if(voice){
        uA.voice = voice;
        uB.voice = voice;
      }

      // Retain both utterances in memory
      window._activeUtterances = [uA, uB];

      uB.onend = () => { window._activeUtterances = []; };
      uB.onerror = () => { window._activeUtterances = []; };

      // Queue both synchronously inside user tap
      window.speechSynthesis.speak(uA);
      window.speechSynthesis.speak(uB);
    }, 40);
  }catch(e){}
}

function speakCurrentDialogue(){
  const card = activeCards[learnIndex];
  if(!card) return;
  playMagicalSound('pop');
  speakDialoguePair(card.q, card.a);
}

function speakSpeakerA(){
  const card = activeCards[learnIndex];
  if(!card) return;
  playMagicalSound('pop');
  speakSingle(card.q, 1.25, 0.86);
}

function speakSpeakerB(){
  const card = activeCards[learnIndex];
  if(!card) return;
  playMagicalSound('pop');
  speakSingle(card.a, 1.05, 0.86);
}

function speakQuizQuestion(){
  if(!quizState) return;
  const q = quizState.questions[quizState.index];
  if(q && q.speakText){
    playMagicalSound('pop');
    speakSingle(q.speakText, 1.15, 0.88);
  }
}

/* =========================================================
   DATA - All 11 Chapters with Indonesian Translations
   ========================================================= */
const CHAPTERS = """ + json.dumps(chapters_data, ensure_ascii=False) + """;

/* =========================================================
   STATE & PERSISTENCE
   ========================================================= */
let progress = {};
CHAPTERS.forEach(c => progress[c.id] = 0);

function saveProgress(){
  try{ localStorage.setItem('freya_english_progress', JSON.stringify(progress)); }catch(e){}
}
function loadProgress(){
  try{
    const raw = localStorage.getItem('freya_english_progress');
    if(raw){ const parsed = JSON.parse(raw); Object.assign(progress, parsed); }
  }catch(e){}
}
loadProgress();

let currentChapterIdx = 0;
let currentTopicFilter = "all";
let activeCards = [];
let learnIndex = 0;
let quizState = null;

/* =========================================================
   NAVIGATION
   ========================================================= */
function show(id){
  document.querySelectorAll('.screen').forEach(s => s.classList.add('hidden'));
  document.getElementById(id).classList.remove('hidden');
  window.scrollTo(0,0);
}

function goHome(){
  if('speechSynthesis' in window) window.speechSynthesis.cancel();
  playMagicalSound('pop');
  renderHome();
  show('screen-home');
}

function openChapter(idx){
  playMagicalSound('pop');
  currentChapterIdx = idx;
  currentTopicFilter = "all";
  showStation();
}

function showStation(){
  const ch = CHAPTERS[currentChapterIdx];
  document.getElementById('stHeaderBadge').textContent = ch.badge;
  document.getElementById('stHeaderTitleId').textContent = ch.title_id || ch.title;
  document.getElementById('stHeaderTitleEn').textContent = `Bab ${ch.number}: ${ch.title}`;
  document.getElementById('stHeaderSub').textContent = ch.sub_id || ch.sub;
  document.getElementById('stationStars').textContent = progress[ch.id];

  // Populate dropdown
  const select = document.getElementById('topicDropdown');
  select.innerHTML = `<option value="all">⭐ Semua Topik di Bab Ini (${getChapterTotalCount(ch)} Percakapan)</option>`;
  ch.topics.forEach((t, i) => {
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = `🌸 ${t.title} (${t.items.length})`;
    select.appendChild(opt);
  });
  select.value = currentTopicFilter;

  updateActiveCards();
  show('screen-station');
}

function getChapterTotalCount(ch){
  return ch.topics.reduce((sum, t) => sum + t.items.length, 0);
}

function onTopicChange(){
  const select = document.getElementById('topicDropdown');
  currentTopicFilter = select.value;
  playMagicalSound('pop');
  updateActiveCards();
}

function updateActiveCards(){
  const ch = CHAPTERS[currentChapterIdx];
  activeCards = [];
  if(currentTopicFilter === "all"){
    ch.topics.forEach(t => {
      t.items.forEach(item => {
        activeCards.push({ ...item, topicTitle: t.title });
      });
    });
  } else {
    const t = ch.topics[parseInt(currentTopicFilter, 10)];
    if(t){
      t.items.forEach(item => {
        activeCards.push({ ...item, topicTitle: t.title });
      });
    }
  }
}

/* =========================================================
   HOME SCREEN
   ========================================================= */
function renderHome(){
  const totalEarned = Object.values(progress).reduce((a, b) => a + b, 0);
  document.getElementById('totalStars').textContent = totalEarned;
  document.getElementById('maxStars').textContent = CHAPTERS.length * 3;

  const list = document.getElementById('chaptersList');
  list.innerHTML = '';

  CHAPTERS.forEach((ch, i) => {
    const count = getChapterTotalCount(ch);
    const card = document.createElement('div');
    card.className = 'chapter-card';
    card.onclick = () => openChapter(i);

    const stars = '⭐'.repeat(progress[ch.id]) + '☆'.repeat(3 - progress[ch.id]);

    card.innerHTML = `
      <div class="ch-badge">${ch.badge}</div>
      <div class="ch-info">
        <div class="ch-tag">Pulau Impian ${ch.number} 🦄</div>
        <div class="ch-title">${ch.title}</div>
        <div class="ch-sub-id">${ch.title_id || ''}</div>
        <div class="ch-sub-en">${ch.topics.length} Topik • ${count} Percakapan</div>
        <div class="ch-stars">${stars}</div>
      </div>
      <div class="ch-arrow">›</div>
    `;
    list.appendChild(card);
  });
}

/* =========================================================
   FLASHCARD MODE
   ========================================================= */
function startLearn(){
  playMagicalSound('pop');
  updateActiveCards();
  if(!activeCards.length) return;
  learnIndex = 0;
  renderLearnCard(true);
  show('screen-learn');
}

function renderLearnCard(autoPlay = true){
  const card = activeCards[learnIndex];
  const total = activeCards.length;

  document.getElementById('cardTopicTag').textContent = '🌸 ' + (card.topicTitle || 'Percakapan Cantik');
  document.getElementById('cardTextAEn').textContent = card.q;
  document.getElementById('cardTextAId').textContent = '🇮🇩 ' + (card.q_id || 'Arti kalimat');

  document.getElementById('cardTextBEn').textContent = card.a;
  document.getElementById('cardTextBId').textContent = '🇮🇩 ' + (card.a_id || 'Arti jawaban');

  const noteEl = document.getElementById('cardNote');
  const noteText = card.note_id || card.note;
  if(noteText){
    noteEl.textContent = '💡 Catatan Manis: ' + noteText;
    noteEl.classList.remove('hidden');
  } else {
    noteEl.classList.add('hidden');
  }

  document.getElementById('learnProgressText').textContent = `Kartu ${learnIndex + 1} dari ${total} 🌸`;
  const pct = Math.round(((learnIndex + 1) / total) * 100);
  document.getElementById('learnProgressBar').style.width = pct + '%';

  document.getElementById('prevBtn').disabled = (learnIndex === 0);
  const mainBtn = document.getElementById('cardMainBtn');
  mainBtn.textContent = (learnIndex === total - 1) ? 'Selesai! Main Kuis Seru 🎯' : 'Lanjut 🌸 →';

  if(autoPlay){
    speakCurrentDialogue();
  }
}

function nextCard(){
  playMagicalSound('pop');
  if(learnIndex < activeCards.length - 1){
    learnIndex++;
    renderLearnCard(true);
  } else {
    startQuiz();
  }
}

function prevCard(){
  playMagicalSound('pop');
  if(learnIndex > 0){
    learnIndex--;
    renderLearnCard(true);
  }
}

/* =========================================================
   QUIZ MODE FOR FREYA (8 YEARS OLD)
   ========================================================= */
function shuffle(arr){
  const a = arr.slice();
  for(let i = a.length - 1; i > 0; i--){
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function buildQuizQuestions(){
  updateActiveCards();
  const pool = activeCards.length >= 4 ? activeCards : getAllChapterCards();
  const sampleCount = Math.min(6, pool.length);
  const selected = shuffle(pool).slice(0, sampleCount);

  return selected.map((item, idx) => {
    const distractors = shuffle(pool.filter(c => c.q !== item.q)).slice(0, 2);
    const qType = idx % 3;

    if(qType === 0){
      // EN -> ID meaning
      const options = shuffle([item.q_id, distractors[0].q_id, distractors[1].q_id]);
      return {
        kicker: "🌸 Apa arti kalimat bahasa Inggris ini?",
        qText: item.q,
        subhint: "Pilihlah arti yang tepat untuk Freya:",
        speakText: item.q,
        correct: item.q_id,
        options: options
      };
    } else if(qType === 1){
      // How to reply in English
      const options = shuffle([item.a, distractors[0].a, distractors[1].a]);
      return {
        kicker: "🦄 Teman Unicorn bertanya:",
        qText: item.q,
        subhint: "Bagaimana cara Freya membalasnya dalam bahasa Inggris?",
        speakText: item.q,
        correct: item.a,
        options: options
      };
    } else {
      // ID -> EN
      const options = shuffle([item.q, distractors[0].q, distractors[1].q]);
      return {
        kicker: "🎀 Bagaimana bilang ini dalam bahasa Inggris?",
        qText: item.q_id,
        subhint: "Pilihlah jawaban yang benar:",
        speakText: item.q,
        correct: item.q,
        options: options
      };
    }
  });
}

function getAllChapterCards(){
  const ch = CHAPTERS[currentChapterIdx];
  const list = [];
  ch.topics.forEach(t => t.items.forEach(i => list.push(i)));
  return list;
}

function startQuiz(){
  playMagicalSound('sparkle');
  const questions = buildQuizQuestions();
  quizState = {
    questions: questions,
    index: 0,
    lives: 3,
    correctCount: 0
  };
  renderQuizQuestion();
  show('screen-quiz');
}

function renderQuizQuestion(){
  const q = quizState.questions[quizState.index];
  document.getElementById('quizHearts').textContent = '💖'.repeat(quizState.lives) + '🤍'.repeat(3 - quizState.lives);
  document.getElementById('quizProgressText').textContent = `Soal ${quizState.index + 1} dari ${quizState.questions.length} 🦄`;

  document.getElementById('quizKicker').textContent = q.kicker;
  document.getElementById('quizQ').textContent = q.qText;
  document.getElementById('quizSubhint').textContent = q.subhint;

  const optContainer = document.getElementById('quizOptions');
  optContainer.innerHTML = '';
  document.getElementById('quizFeedback').textContent = '';
  document.getElementById('quizFeedback').className = 'feedback';

  q.options.forEach(optText => {
    const btn = document.createElement('button');
    btn.className = 'option';
    btn.textContent = optText;
    btn.onclick = () => answerQuiz(btn, optText, q);
    optContainer.appendChild(btn);
  });

  if(q.speakText) speakSingle(q.speakText, 1.15, 0.88);
}

function answerQuiz(btn, selectedText, q){
  const isCorrect = (selectedText === q.correct);
  document.querySelectorAll('.option').forEach(o => o.classList.add('disabled'));

  const fb = document.getElementById('quizFeedback');
  if(isCorrect){
    playMagicalSound('correct');
    btn.classList.add('correct');
    fb.textContent = 'Hebat Sekali Freya! Betul 100%! 🎉✨';
    fb.className = 'feedback good';
    quizState.correctCount++;
    speakSingle(q.speakText || q.correct, 1.15, 0.88);
  } else {
    playMagicalSound('wrong');
    btn.classList.add('wrong');
    document.querySelectorAll('.option').forEach(o => {
      if(o.textContent === q.correct) o.classList.add('correct');
    });
    fb.textContent = 'Hampir tepat! Jawaban yang benar ditandai ya, Freya! 💪🌸';
    fb.className = 'feedback bad';
    quizState.lives--;
    speakSingle(q.speakText || q.correct, 1.05, 0.88);
  }

  setTimeout(() => {
    if(quizState.lives <= 0){
      finishQuiz(false);
      return;
    }
    quizState.index++;
    if(quizState.index >= quizState.questions.length){
      finishQuiz(true);
    } else {
      renderQuizQuestion();
    }
  }, 1450);
}

function finishQuiz(completed){
  const ch = CHAPTERS[currentChapterIdx];
  const total = quizState.questions.length;
  const ratio = quizState.correctCount / total;
  let stars = 0;

  if(completed){
    if(ratio >= 0.85) stars = 3;
    else if(ratio >= 0.6) stars = 2;
    else stars = 1;
  } else {
    stars = 0;
  }

  const passed = stars >= 1;
  if(passed && stars > progress[ch.id]){
    progress[ch.id] = stars;
    saveProgress();
  }

  document.getElementById('resultEmoji').textContent = passed ? '🦄' : '💖';
  document.getElementById('resultTitle').textContent = passed 
    ? 'Luar Biasa, Princess Freya! 👑✨' 
    : 'Semangat Terus, Freya Cantik! 🌸';
  document.getElementById('resultSub').textContent = passed 
    ? `Freya berhasil menguasai pulau ${ch.title_id || ch.title}!`
    : `Bagus sekali usahanya! Ayo lihat kartu lagi dan kumpulkan bintangnya!`;
  document.getElementById('resultStars').textContent = passed ? ('⭐'.repeat(stars) + '☆'.repeat(3 - stars)) : '☆☆☆';
  document.getElementById('resultScore').textContent = `Jawaban Benar: ${quizState.correctCount} / ${total} ⭐`;
  document.getElementById('retryBtn').textContent = passed ? '🔁 Main Kuis Lagi 🎀' : '🔁 Coba Lagi 🌸';

  show('screen-result');
  if(passed){
    playMagicalSound('sparkle');
    launchConfetti();
  }
}

function retryQuiz(){
  playMagicalSound('pop');
  startQuiz();
}

/* =========================================================
   CONFETTI (Magical Unicorn, Hello Kitty Bows & Stars)
   ========================================================= */
function launchConfetti(){
  const holder = document.getElementById('confetti');
  const emojis = ['🦄', '🎀', '🐱', '💖', '✨', '🌈', '🍭', '⭐', '🌸', '🧁', '👑'];
  for(let i = 0; i < 32; i++){
    const span = document.createElement('span');
    span.textContent = emojis[Math.floor(Math.random() * emojis.length)];
    span.style.left = (Math.random() * 96) + 'vw';
    span.style.animationDuration = (2.2 + Math.random() * 1.8) + 's';
    span.style.fontSize = (18 + Math.random() * 22) + 'px';
    holder.appendChild(span);
    setTimeout(() => span.remove(), 4200);
  }
}

/* =========================================================
   INIT
   ========================================================= */
renderHome();
show('screen-home');
</script>
</body>
</html>
"""

with open("Freya_Shyam_English.html", "w", encoding="utf-8") as f:
    f.write(html_code)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Updated with complete iOS/iPad sound & speech synthesis fixes!")
