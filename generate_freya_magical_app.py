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
    margin-bottom:14px; gap:8px;
  }
  .topbar .stars{
    background:#FFFFFF; border-radius:999px; padding:7px 16px;
    font-weight:800; font-size:14.5px;
    border:2.5px solid var(--pink-soft);
    box-shadow:0 4px 12px rgba(231, 84, 128, 0.15);
    display:flex; align-items:center; gap:6px; color:var(--pink-dark);
  }
  .name-badge{
    background:linear-gradient(135deg, #FFB6C1, #FF69B4);
    color:#fff; padding:6px 14px; border-radius:999px; font-weight:800;
    font-size:13px; letter-spacing:0.5px; box-shadow:0 3px 8px rgba(255, 105, 180, 0.35);
    display:flex; align-items:center; gap:5px;
    cursor:pointer; user-select:none; -webkit-user-select:none;
    transition:transform .12s ease;
  }
  .name-badge:active{ transform:scale(0.94); }
  .voice-btn{
    background:#FFFFFF; border-radius:999px; padding:6px 14px;
    font-weight:800; font-size:13px; border:2.5px solid var(--pink-soft);
    box-shadow:0 3px 8px rgba(231, 84, 128, 0.15);
    display:flex; align-items:center; gap:5px; color:var(--pink-dark);
    transition:transform .12s ease;
  }
  .voice-btn:active{ transform:scale(0.96); }

  .backbtn{
    background:#FFFFFF; width:44px; height:44px; border-radius:50%;
    font-size:22px; border:2.5px solid var(--pink-soft);
    box-shadow:0 4px 10px rgba(231, 84, 128, 0.15);
    display:flex; align-items:center; justify-content:center;
    transition:transform .12s ease; color:var(--pink-dark); font-weight:900;
  }
  .backbtn:active{ transform:translateY(2px); box-shadow:0 2px 4px rgba(231, 84, 128, 0.15); }

  /* ---------- HERO SECTION ---------- */
  .hero{ text-align:center; margin-bottom:14px; }
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

  /* ---------- OVERALL PROGRESS CARD ---------- */
  .overall-progress-card{
    background:#FFFFFF; border-radius:24px; padding:16px 18px;
    border:2.5px solid #FFCCD9;
    box-shadow:0 8px 22px rgba(255, 105, 180, 0.16);
    margin:14px 0 16px; text-align:left; position:relative; overflow:hidden;
  }
  .overall-progress-card::after{
    content:'🦄'; position:absolute; right:10px; bottom:-10px;
    font-size:60px; opacity:0.12; pointer-events:none;
  }
  .op-title-row{
    display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;
  }
  .op-title{
    font-weight:900; font-size:14.5px; color:var(--plum); display:flex; align-items:center; gap:6px;
  }
  .op-percent{
    font-family:'Baloo 2', cursive, sans-serif; font-weight:900; font-size:22px; color:var(--pink-dark);
  }
  .op-bar-bg{
    width:100%; height:14px; background:#FFE8F1; border-radius:999px;
    overflow:hidden; border:2px solid #FFCCD9; margin-bottom:8px;
  }
  .op-bar-fill{
    height:100%; width:0%;
    background:linear-gradient(90deg, #FF85A2 0%, #FF4D79 45%, #B388EB 80%, #48DBBB 100%);
    border-radius:999px; transition:width .45s ease;
  }
  .op-stats{
    display:flex; justify-content:space-between; font-size:12px; font-weight:800; color:#85586F;
  }
  .op-stats strong{ color:var(--pink-dark); }

  /* ---------- SOUND TIP BANNER FOR IPAD ---------- */
  .sound-tip{
    background:#FFF5EB; border:1.5px dashed #FFA94D; border-radius:16px;
    padding:8px 14px; margin:0 auto 16px; font-size:12px; font-weight:800;
    color:#D9480F; display:flex; align-items:center; gap:8px; text-align:left;
  }

  /* ---------- CHAPTER CARDS WITH 10 STARS ---------- */
  .chapter-list{ display:flex; flex-direction:column; gap:14px; margin-top:8px; }
  .chapter-card{
    background:#FFFFFF; border-radius:26px; padding:16px 18px;
    display:flex; flex-direction:column; gap:12px;
    border:2.5px solid #FFDFE9;
    box-shadow:0 6px 18px rgba(255, 140, 180, 0.14), 0 3px 0 #FFCCD9;
    transition:transform .14s ease, box-shadow .14s ease;
    cursor:pointer; text-align:left; position:relative; overflow:hidden;
  }
  .chapter-card.completed{
    border-color:#7FCE9C; box-shadow:0 6px 18px rgba(32, 191, 107, 0.16), 0 3px 0 #5CB881;
  }
  .chapter-card:active{ transform:translateY(3px); box-shadow:0 2px 8px rgba(255, 140, 180, 0.15), 0 1px 0 #FFCCD9; }
  
  .ch-top-row{
    display:flex; align-items:center; gap:15px;
  }
  .ch-badge{
    width:64px; height:64px; border-radius:50%; flex:0 0 auto;
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
  .ch-arrow{
    width:34px; height:34px; border-radius:50%; background:#FFF0F5;
    display:flex; align-items:center; justify-content:center;
    font-size:18px; color:var(--pink-bright); font-weight:900; flex:0 0 auto;
  }

  /* 10-Star Progress Bar inside each chapter card */
  .ch-prog-wrap{
    background:#FFF5F8; border-radius:18px; padding:10px 14px;
    border:1.5px solid #FFE0EB;
  }
  .ch-prog-header{
    display:flex; justify-content:space-between; align-items:center;
    margin-bottom:6px; font-size:12px; font-weight:800;
  }
  .ch-stars-row, .station-stars-level, .quiz-stars-live, .result-stars-10{
    display:inline-flex; align-items:center; gap:2px; font-size:16px;
    user-select:none; -webkit-user-select:none;
  }
  .star-item{
    display:inline-block; font-size:16px; line-height:1;
    transition:transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275), filter 0.25s ease;
    user-select:none; -webkit-user-select:none;
  }
  .star-item.gold{
    filter:drop-shadow(0 2px 4px rgba(255, 184, 0, 0.75));
    transform:scale(1.08);
  }
  .star-item.empty{
    filter:grayscale(100%) opacity(0.24);
    transform:scale(0.92);
  }
  .quiz-stars-wrap{
    background:#FFF0F5; border:1.5px solid #FFCCD9; border-radius:999px;
    padding:4px 10px; display:inline-flex; align-items:center; gap:6px;
  }
  .quiz-score-badge{
    background:linear-gradient(135deg, #FFB6C1, #FF69B4);
    color:#fff; padding:4px 12px; border-radius:999px;
    font-weight:900; font-size:13px; box-shadow:0 2px 6px rgba(255, 105, 180, 0.3);
  }
  .ch-pct-badge{
    background:#FFE0EB; color:var(--pink-dark); padding:3px 10px;
    border-radius:999px; font-weight:900; font-size:12px;
  }
  .ch-pct-badge.done{
    background:#D4F8E8; color:var(--mint-dark);
  }
  .ch-bar-bg{
    width:100%; height:9px; background:#FFFFFF; border-radius:999px;
    overflow:hidden; border:1.5px solid #FFCCD9;
  }
  .ch-bar-fill{
    height:100%; width:0%;
    background:linear-gradient(90deg, #FF85A2, #FF4D79);
    border-radius:999px; transition:width .35s ease;
  }
  .ch-bar-fill.done{
    background:linear-gradient(90deg, #48DBBB, #20BF6B);
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
  .station-stars-level{
    margin-top:6px; font-size:15px; font-weight:900; color:var(--gold);
    background:#FFFDF0; display:inline-block; padding:4px 16px; border-radius:999px;
    border:1.5px solid #FFE680;
  }

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
  .speaker-sound-icon{ font-size:13px; background:rgba(255,255,255,0.75); padding:2px 8px; border-radius:999px; font-weight:800; }
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

  /* ---------- RESULT SCREEN (10 STARS) ---------- */
  .result-wrap{ margin:32px auto 0; text-align:center; }
  .result-wrap .big-emoji{ font-size:76px; animation:pop .5s ease; filter:drop-shadow(0 6px 16px rgba(255, 105, 180, 0.3)); }
  @keyframes pop{ 0%{transform:scale(0);} 70%{transform:scale(1.2);} 100%{transform:scale(1);} }
  .result-wrap h2{ font-size:26px; margin:10px 0 4px; color:var(--plum); }
  .result-wrap p{ font-weight:800; color:var(--pink-dark); font-size:16px; }
  .result-stars-10{
    font-size:28px; margin:14px 0; letter-spacing:4px;
    display:flex; justify-content:center; flex-wrap:wrap; gap:4px;
  }
  .result-score-tag{
    font-size:18px; font-weight:900; color:#fff; background:linear-gradient(135deg, #FF69B4, #C2185B);
    display:inline-block; padding:8px 24px; border-radius:999px; margin-bottom:18px;
    box-shadow:0 4px 12px rgba(194, 24, 91, 0.25);
  }
  .result-buttons{ display:flex; flex-direction:column; gap:13px; margin-top:18px; }

  /* ---------- VOICE & SETTINGS MODAL ---------- */
  .modal-overlay{
    position:fixed; inset:0; background:rgba(43, 34, 80, 0.55);
    backdrop-filter:blur(5px); -webkit-backdrop-filter:blur(5px);
    z-index:100; display:flex; align-items:center; justify-content:center;
    padding:20px 16px; animation:fadeIn .2s ease;
  }
  @keyframes fadeIn{ from{opacity:0;} to{opacity:1;} }
  .modal-card{
    background:#FFFFFF; border-radius:30px; padding:24px 22px; max-width:440px; width:100%;
    border:3px solid #FFCCD9; box-shadow:0 15px 35px rgba(255, 105, 180, 0.3);
    text-align:left; animation:scaleUp .25s ease;
  }
  @keyframes scaleUp{ from{transform:scale(0.92); opacity:0;} to{transform:scale(1); opacity:1;} }
  .modal-header{
    display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;
  }
  .modal-title{ font-family:'Baloo 2',sans-serif; font-size:22px; font-weight:800; color:var(--plum); margin:0; }
  .modal-close{
    background:#FFF0F5; border-radius:50%; width:38px; height:38px; font-size:20px;
    display:flex; align-items:center; justify-content:center; color:var(--pink-dark); font-weight:900;
  }
  .setting-group{ margin-bottom:16px; }
  .setting-label{ display:block; font-weight:900; font-size:13.5px; color:var(--plum); margin-bottom:6px; }
  .setting-select{
    width:100%; padding:12px 14px; border-radius:14px; border:2px solid #FFCCD9;
    font-family:'Quicksand',sans-serif; font-size:14px; font-weight:800;
    color:var(--plum); background:#FFF8FA; outline:none;
  }
  .setting-slider-row{ display:flex; align-items:center; gap:12px; }
  .setting-slider{ flex:1; accent-color:var(--pink-bright); }
  .setting-val{ font-weight:800; font-size:13px; color:var(--pink-dark); min-width:48px; text-align:right; }
  .modal-actions{ display:flex; gap:10px; margin-top:20px; }
  .btn-test{
    flex:1; background:linear-gradient(135deg, #FFE66D, #FFB800); color:#5A3E00;
    padding:13px; border-radius:16px; font-weight:900; font-size:14.5px;
    box-shadow:0 4px 0 #D48800; text-align:center;
  }
  .btn-save{
    flex:1; background:linear-gradient(135deg, #FF7597, #FF4D79); color:#fff;
    padding:13px; border-radius:16px; font-weight:900; font-size:14.5px;
    box-shadow:0 4px 0 #D81B60; text-align:center;
  }
  .reset-btn-row{
    text-align:center; margin-top:16px; padding-top:14px; border-top:1px dashed #FFCCD9;
  }
  .reset-btn{
    background:none; color:#A0AEC0; font-size:12px; font-weight:800; text-decoration:underline;
  }

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
    <div class="name-badge" id="freyaNameBadge" onclick="handleFreyaNameClick(event)" title="👑 Freya Shyam (Klik 5x untuk reset skor)">👑 Freya Shyam</div>
    <div style="display:flex; gap:8px;">
      <button class="voice-btn" onclick="openVoiceModal()" title="Pilih Suara (Voice Settings)">🎙️ Suara</button>
      <div class="stars">⭐ <span id="totalStars">0</span> / <span id="maxStars">110</span></div>
    </div>
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

  <!-- Overall Progress Card for Freya (110 Total Stars) -->
  <div class="overall-progress-card">
    <div class="op-title-row">
      <div class="op-title">👑 Total Progres Belajar Freya</div>
      <div class="op-percent" id="overallPercent">0%</div>
    </div>
    <div class="op-bar-bg">
      <div class="op-bar-fill" id="overallBarFill"></div>
    </div>
    <div class="op-stats">
      <span>⭐ Bintang: <strong id="overallStarsLabel">0 / 110</strong></span>
      <span>🏝️ Pulau Selesai: <strong id="overallIslandsLabel">0 / 11</strong></span>
      <span>📖 Kartu: <strong id="overallCardsLabel">0 / 239</strong></span>
    </div>
  </div>

  <!-- iPad sound tip -->
  <div class="sound-tip">
    <span>🔊</span>
    <span><strong>Tips Suara:</strong> Pastikan iPad tidak dalam <em>Mode Hening (Silent Mode)</em> dan naikkan volume ya! Sentuh tombol <strong>🎙️ Suara</strong> di atas untuk ganti suara. ✨</span>
  </div>

  <div class="chapter-list" id="chaptersList"></div>

  <div class="footer-note">Setiap bab memiliki 10 ⭐ untuk menguji level kemampuan Freya! 🌸✨</div>
</section>

<!-- ===================== STATION MENU SCREEN ===================== -->
<section class="screen hidden" id="screen-station">
  <div class="topbar">
    <button class="backbtn" onclick="goHome()">←</button>
    <div class="name-badge" onclick="handleFreyaNameClick(event)" title="👑 Freya Shyam (Klik 5x untuk reset skor)">👑 Freya Shyam</div>
    <div style="display:flex; gap:8px;">
      <button class="voice-btn" onclick="openVoiceModal()">🎙️ Suara</button>
      <div class="stars">⭐ <span id="stationStars">0</span> / 10</div>
    </div>
  </div>

  <div class="station-header">
    <div class="badge-halo" id="stHeaderBadge">🦄</div>
    <div class="id-title" id="stHeaderTitleId">Sopan Santun</div>
    <h2 id="stHeaderTitleEn">Good Manners</h2>
    <div class="sub" id="stHeaderSub">Greetings, Politeness &amp; Social Etiquette</div>
    <div class="station-stars-level" id="stHeaderStarsRow">⭐⭐⭐⭐⭐☆☆☆☆☆ (0/10)</div>
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
      <span>Main Kuis 10 Bintang ⭐<small>Dapatkan hingga 10 bintang emas untuk Freya!</small></span>
    </button>
  </div>
</section>

<!-- ===================== FLASHCARD SCREEN ===================== -->
<section class="screen hidden" id="screen-learn">
  <div class="topbar">
    <button class="backbtn" onclick="showStation()">←</button>
    <div class="progress-info" id="learnProgressText">Kartu 1 dari 10 🌸</div>
    <div style="display:flex; gap:6px;">
      <button class="voice-btn" onclick="openVoiceModal()">🎙️</button>
      <button class="backbtn" onclick="speakCurrentDialogue()" title="Dengarkan Suara">🔊</button>
    </div>
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
          <span class="speaker-sound-icon">🔊 Ketuk Suara</span>
        </div>
        <div class="en-text" id="cardTextAEn">Hello!</div>
        <div class="id-text" id="cardTextAId">🇮🇩 Halo!</div>
      </div>

      <!-- Speaker B (Kitty / Freya) - Tap to listen -->
      <div class="bubble speaker-b" onclick="speakSpeakerB()">
        <div class="bubble-speaker">
          <span>🐱 Putri Freya (Speaker B)</span>
          <span class="speaker-sound-icon">🔊 Ketuk Suara</span>
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
    <div class="name-badge" onclick="handleFreyaNameClick(event)" title="👑 Freya Shyam (Klik 5x untuk reset skor)">👑 Freya Shyam</div>
    <div class="quiz-score-badge" id="quizLiveScore">0 / 10 ⭐</div>
  </div>

  <div class="quiz-wrap">
    <div class="quiz-top">
      <div class="quiz-progress" id="quizProgressText">Soal 1 dari 10 🦄</div>
      <div class="quiz-stars-wrap">
        <div class="quiz-stars-live" id="quizLiveStars"></div>
      </div>
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

<!-- ===================== RESULT SCREEN (10 STARS) ===================== -->
<section class="screen hidden" id="screen-result">
  <div class="result-wrap">
    <div class="big-emoji" id="resultEmoji">🦄</div>
    <h2 id="resultTitle">Luar Biasa, Princess Freya! 👑</h2>
    <p id="resultSub">Kamu berhasil menyelesaikan bab ini!</p>
    <div class="result-stars-10" id="resultStars10"></div>
    <div class="result-score-tag" id="resultScore">Nilai: 10 / 10 ⭐</div>
    <div class="result-buttons">
      <button class="finish-btn" onclick="retryQuiz()" id="retryBtn">🔁 Main Kuis Lagi 🎀</button>
      <button class="mode-btn learn" onclick="goHome()">🏝️ Kembali ke Pulau Impian 🦄</button>
    </div>
  </div>
</section>

<!-- ===================== VOICE & SETTINGS MODAL ===================== -->
<div class="modal-overlay hidden" id="voiceModal" onclick="closeVoiceModalOnOutside(event)">
  <div class="modal-card">
    <div class="modal-header">
      <h3 class="modal-title">🎙️ Pilihan Suara (Voice) ✨</h3>
      <button class="modal-close" onclick="closeVoiceModal()">✕</button>
    </div>

    <!-- Voice Picker -->
    <div class="setting-group">
      <label class="setting-label" for="voiceSelect">Pilih Suara Bahasa Inggris:</label>
      <select class="setting-select" id="voiceSelect" onchange="onVoiceSelected()"></select>
    </div>

    <!-- Speed / Rate Slider -->
    <div class="setting-group">
      <label class="setting-label">Kecepatan Bicara (Speed):</label>
      <div class="setting-slider-row">
        <span>🐢 Pelan</span>
        <input type="range" class="setting-slider" id="speedSlider" min="0.6" max="1.2" step="0.05" value="0.88" oninput="onSpeedChange()">
        <span>🐰 Cepat</span>
        <span class="setting-val" id="speedVal">0.88x</span>
      </div>
    </div>

    <!-- Pitch Slider -->
    <div class="setting-group">
      <label class="setting-label">Tinggi Nada (Pitch):</label>
      <div class="setting-slider-row">
        <span>Deep</span>
        <input type="range" class="setting-slider" id="pitchSlider" min="0.8" max="1.4" step="0.05" value="1.1" oninput="onPitchChange()">
        <span>Cute 🌸</span>
        <span class="setting-val" id="pitchVal">1.1x</span>
      </div>
    </div>

    <div class="modal-actions">
      <button class="btn-test" onclick="testCurrentVoice()">🔊 Coba Suara</button>
      <button class="btn-save" onclick="saveAndCloseVoiceModal()">Simpan 💖</button>
    </div>

    <div class="reset-btn-row">
      <button class="reset-btn" onclick="resetAllProgress()">↺ Reset Progres Bintang &amp; Kartu (Mulai Ulang)</button>
    </div>
  </div>
</div>

<script>
/* =========================================================
   IOS / IPADOS AUDIO & SPEECH FIXES
   ========================================================= */
window._activeUtterances = [];
let audioCtx = null;
let audioUnlocked = false;

// Saved user preferences
let currentVoiceURI = localStorage.getItem('freya_voice_uri') || '';
let voiceSpeed = parseFloat(localStorage.getItem('freya_voice_speed')) || 0.88;
let voicePitch = parseFloat(localStorage.getItem('freya_voice_pitch')) || 1.1;

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

  try{
    const ctx = getAudioContext();
    if(ctx && ctx.state === 'suspended') ctx.resume();
  }catch(e){}

  try{
    if('speechSynthesis' in window){
      window.speechSynthesis.resume();
      const dummy = new SpeechSynthesisUtterance('');
      dummy.volume = 0;
      window.speechSynthesis.speak(dummy);
    }
  }catch(e){}
}

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
   VOICE LIST POPULATION & SELECTION
   ========================================================= */
let cachedVoices = [];

function getAvailableEnglishVoices(){
  if(!('speechSynthesis' in window)) return [];
  const all = window.speechSynthesis.getVoices() || [];
  return all.filter(v => v.lang && v.lang.toLowerCase().startsWith('en'));
}

function populateVoiceSelect(){
  if(!('speechSynthesis' in window)) return;
  cachedVoices = getAvailableEnglishVoices();
  const select = document.getElementById('voiceSelect');
  if(!select) return;

  select.innerHTML = '';
  if(cachedVoices.length === 0){
    select.innerHTML = '<option value="">🌸 Suara Bawaan Sistem (Default)</option>';
    return;
  }

  cachedVoices.forEach(v => {
    const opt = document.createElement('option');
    opt.value = v.voiceURI;
    let displayName = v.name;
    if(v.lang) displayName += ` (${v.lang})`;
    opt.textContent = displayName;

    if(currentVoiceURI && v.voiceURI === currentVoiceURI){
      opt.selected = true;
    }
    select.appendChild(opt);
  });

  if(!currentVoiceURI && cachedVoices.length > 0){
    const natural = cachedVoices.find(v => v.name.includes('Samantha') || v.name.includes('Natural') || v.name.includes('Siri')) || cachedVoices[0];
    currentVoiceURI = natural.voiceURI;
    select.value = natural.voiceURI;
  }
}

if('speechSynthesis' in window){
  window.speechSynthesis.onvoiceschanged = () => {
    populateVoiceSelect();
  };
}

function getActiveVoice(){
  if(!cachedVoices.length) cachedVoices = getAvailableEnglishVoices();
  if(currentVoiceURI){
    const found = cachedVoices.find(v => v.voiceURI === currentVoiceURI);
    if(found) return found;
  }
  return cachedVoices.find(v => v.lang === 'en-US' || v.lang === 'en_US') || cachedVoices[0] || null;
}

function openVoiceModal(){
  playMagicalSound('pop');
  populateVoiceSelect();
  document.getElementById('speedSlider').value = voiceSpeed;
  document.getElementById('speedVal').textContent = voiceSpeed.toFixed(2) + 'x';
  document.getElementById('pitchSlider').value = voicePitch;
  document.getElementById('pitchVal').textContent = voicePitch.toFixed(2) + 'x';
  document.getElementById('voiceModal').classList.remove('hidden');
}

function closeVoiceModal(){
  playMagicalSound('pop');
  document.getElementById('voiceModal').classList.add('hidden');
}

function closeVoiceModalOnOutside(e){
  if(e.target.id === 'voiceModal'){
    closeVoiceModal();
  }
}

function onVoiceSelected(){
  const select = document.getElementById('voiceSelect');
  currentVoiceURI = select.value;
  localStorage.setItem('freya_voice_uri', currentVoiceURI);
}

function onSpeedChange(){
  const slider = document.getElementById('speedSlider');
  voiceSpeed = parseFloat(slider.value);
  document.getElementById('speedVal').textContent = voiceSpeed.toFixed(2) + 'x';
  localStorage.setItem('freya_voice_speed', voiceSpeed);
}

function onPitchChange(){
  const slider = document.getElementById('pitchSlider');
  voicePitch = parseFloat(slider.value);
  document.getElementById('pitchVal').textContent = voicePitch.toFixed(2) + 'x';
  localStorage.setItem('freya_voice_pitch', voicePitch);
}

function testCurrentVoice(){
  playMagicalSound('pop');
  onVoiceSelected();
  onSpeedChange();
  onPitchChange();
  speakSingle("Hello Freya! How are you doing today?", voicePitch, voiceSpeed);
}

function saveAndCloseVoiceModal(){
  onVoiceSelected();
  onSpeedChange();
  onPitchChange();
  playMagicalSound('sparkle');
  closeVoiceModal();
}

/* =========================================================
   TEXT TO SPEECH FUNCTIONS
   ========================================================= */
function speakSingle(text, pitch = null, rate = null, onEnd = null){
  try{
    if(!('speechSynthesis' in window)) return;
    unlockAudioOnIOS();

    window.speechSynthesis.resume();
    window.speechSynthesis.cancel();

    const effPitch = (pitch !== null) ? pitch : voicePitch;
    const effRate = (rate !== null) ? rate : voiceSpeed;

    setTimeout(() => {
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-US';
      u.rate = effRate;
      u.pitch = effPitch;

      const voice = getActiveVoice();
      if(voice) u.voice = voice;

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
      uA.rate = voiceSpeed;
      uA.pitch = Math.min(2.0, voicePitch * 1.15); // Unicorn

      const uB = new SpeechSynthesisUtterance(textB);
      uB.lang = 'en-US';
      uB.rate = voiceSpeed;
      uB.pitch = Math.max(0.6, voicePitch * 0.95); // Freya

      const voice = getActiveVoice();
      if(voice){
        uA.voice = voice;
        uB.voice = voice;
      }

      window._activeUtterances = [uA, uB];

      uB.onend = () => { window._activeUtterances = []; };
      uB.onerror = () => { window._activeUtterances = []; };

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
  speakSingle(card.q, voicePitch * 1.15, voiceSpeed);
}

function speakSpeakerB(){
  const card = activeCards[learnIndex];
  if(!card) return;
  playMagicalSound('pop');
  speakSingle(card.a, voicePitch * 0.95, voiceSpeed);
}

function speakQuizQuestion(){
  if(!quizState) return;
  const q = quizState.questions[quizState.index];
  if(q && q.speakText){
    playMagicalSound('pop');
    speakSingle(q.speakText, voicePitch, voiceSpeed);
  }
}

/* =========================================================
   DATA - All 11 Chapters with Indonesian Translations
   ========================================================= */
const CHAPTERS = """ + json.dumps(chapters_data, ensure_ascii=False) + """;

/* =========================================================
   STATE & PERSISTENT PROGRESS (10 STARS PER CHAPTER)
   - Max 10 stars per chapter (110 stars total)
   ========================================================= */
let progress = {};
let cardsSeen = {};

CHAPTERS.forEach(c => {
  progress[c.id] = 0;
  cardsSeen[c.id] = [];
});

function saveProgress(){
  try{
    localStorage.setItem('freya_english_stars_10', JSON.stringify(progress));
    localStorage.setItem('freya_english_cards_seen_10', JSON.stringify(cardsSeen));
  }catch(e){}
}

function loadProgress(){
  try{
    const rawStars10 = localStorage.getItem('freya_english_stars_10');
    if(rawStars10){
      const parsed = JSON.parse(rawStars10);
      Object.assign(progress, parsed);
    } else {
      // Migrate from old 3-star format if existing (e.g. 3 stars -> 10 stars, 2 stars -> 7 stars, 1 star -> 4 stars)
      const oldStars = localStorage.getItem('freya_english_stars') || localStorage.getItem('freya_english_progress');
      if(oldStars){
        const parsed = JSON.parse(oldStars);
        for(const k in parsed){
          const oldVal = parsed[k] || 0;
          progress[k] = Math.min(10, Math.round((oldVal / 3) * 10));
        }
        saveProgress();
      }
    }

    const rawSeen = localStorage.getItem('freya_english_cards_seen_10') || localStorage.getItem('freya_english_cards_seen');
    if(rawSeen){
      const parsed = JSON.parse(rawSeen);
      Object.assign(cardsSeen, parsed);
    }
  }catch(e){}
}
loadProgress();

function resetAllProgress(){
  if(confirm("Apakah Freya ingin mengulang semua bintang dan kartu dari awal? 🌸")){
    CHAPTERS.forEach(c => {
      progress[c.id] = 0;
      cardsSeen[c.id] = [];
    });
    saveProgress();
    closeVoiceModal();
    renderHome();
  }
}

let currentChapterIdx = 0;
let currentTopicFilter = "all";
let activeCards = [];
let learnIndex = 0;
let quizState = null;

/* Helper to render 10 stars cleanly */
function render10StarsHtml(count, max = 10){
  const validCount = Math.max(0, Math.min(max, count || 0));
  let html = '';
  for(let i = 0; i < max; i++){
    if(i < validCount){
      html += '<span class="star-item gold" title="Bintang ' + (i+1) + ' Emas">⭐</span>';
    } else {
      html += '<span class="star-item empty" title="Bintang ' + (i+1) + ' Kosong">⭐</span>';
    }
  }
  return html;
}

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
  const stars = progress[ch.id] || 0;
  document.getElementById('stHeaderBadge').textContent = ch.badge;
  document.getElementById('stHeaderTitleId').textContent = ch.title_id || ch.title;
  document.getElementById('stHeaderTitleEn').textContent = `Bab ${ch.number}: ${ch.title}`;
  document.getElementById('stHeaderSub').textContent = ch.sub_id || ch.sub;
  document.getElementById('stationStars').textContent = stars;

  // Header 10 stars display
  document.getElementById('stHeaderStarsRow').innerHTML = `${render10StarsHtml(stars)} (${stars}/10 ⭐)`;

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
   HOME SCREEN & 10-STAR PROGRESS CALCULATION
   ========================================================= */
function calculateChapterProgress(ch){
  const stars = Math.max(0, Math.min(10, progress[ch.id] || 0));
  const totalCards = getChapterTotalCount(ch);
  const seenSet = new Set(cardsSeen[ch.id] || []);
  const seenCount = Math.min(totalCards, seenSet.size);

  // 10 stars directly reflect 0% - 100% of subject mastery
  const percent = stars * 10;
  const isComplete = (stars >= 10);

  return {
    stars,
    totalCards,
    seenCount,
    percent,
    isComplete
  };
}

function renderHome(){
  let totalStarsEarned = 0;
  let completedIslands = 0;
  let totalCardsSeenCount = 0;
  let totalCardsAll = 0;

  CHAPTERS.forEach(ch => {
    const p = calculateChapterProgress(ch);
    totalStarsEarned += p.stars;
    if(p.isComplete) completedIslands++;
    totalCardsSeenCount += p.seenCount;
    totalCardsAll += p.totalCards;
  });

  const maxStarsTotal = CHAPTERS.length * 10; // 110 Stars total
  const overallPercentage = Math.round((totalStarsEarned / maxStarsTotal) * 100);

  // Topbar stars
  document.getElementById('totalStars').textContent = totalStarsEarned;
  document.getElementById('maxStars').textContent = maxStarsTotal;

  // Overall Progress Card
  document.getElementById('overallPercent').textContent = overallPercentage + '%';
  document.getElementById('overallBarFill').style.width = overallPercentage + '%';
  document.getElementById('overallStarsLabel').textContent = `${totalStarsEarned} / ${maxStarsTotal}`;
  document.getElementById('overallIslandsLabel').textContent = `${completedIslands} / ${CHAPTERS.length}`;
  document.getElementById('overallCardsLabel').textContent = `${totalCardsSeenCount} / ${totalCardsAll}`;

  // Render Every Chapter Card with its 10 STARS
  const list = document.getElementById('chaptersList');
  list.innerHTML = '';

  CHAPTERS.forEach((ch, i) => {
    const p = calculateChapterProgress(ch);
    const card = document.createElement('div');
    card.className = 'chapter-card' + (p.isComplete ? ' completed' : '');
    card.onclick = () => openChapter(i);

    const starsRowHtml = render10StarsHtml(p.stars);
    const badgeDoneClass = p.isComplete ? 'done' : '';
    const barDoneClass = p.isComplete ? 'done' : '';
    const badgeText = p.isComplete ? '👑 10/10 ⭐ (100%)' : `${p.stars}/10 ⭐ (${p.percent}%)`;

    card.innerHTML = `
      <div class="ch-top-row">
        <div class="ch-badge">${ch.badge}</div>
        <div class="ch-info">
          <div class="ch-tag">Pulau Impian ${ch.number} 🦄</div>
          <div class="ch-title">${ch.title}</div>
          <div class="ch-sub-id">${ch.title_id || ''}</div>
          <div class="ch-sub-en">${ch.topics.length} Topik • ${p.totalCards} Percakapan</div>
        </div>
        <div class="ch-arrow">›</div>
      </div>

      <!-- 10 Stars Progress for this Subject -->
      <div class="ch-prog-wrap">
        <div class="ch-prog-header">
          <span class="ch-stars-row">${starsRowHtml}</span>
          <span class="ch-pct-badge ${badgeDoneClass}">${badgeText}</span>
        </div>
        <div class="ch-bar-bg">
          <div class="ch-bar-fill ${barDoneClass}" style="width:${p.percent}%"></div>
        </div>
      </div>
    `;
    list.appendChild(card);
  });
}

/* =========================================================
   SECRET RESET: 5 Left Clicks on Freya Shyam Badge Resets Scores
   ========================================================= */
let freyaClickCount = 0;
let freyaClickTimer = null;

function handleFreyaNameClick(e){
  // Accept only primary/left mouse button (button === 0) or touch/tap
  if(e && e.button !== undefined && e.button !== 0) return;
  
  freyaClickCount++;
  playMagicalSound('pop');

  const badge = (e && e.currentTarget) || document.getElementById('freyaNameBadge');
  if(badge){
    badge.style.transform = 'scale(0.88)';
    setTimeout(() => { if(badge) badge.style.transform = ''; }, 120);
  }

  clearTimeout(freyaClickTimer);

  if(freyaClickCount >= 5){
    freyaClickCount = 0;
    
    // Reset all scores & progress across all chapters
    CHAPTERS.forEach(c => {
      progress[c.id] = 0;
      cardsSeen[c.id] = [];
    });

    try{
      localStorage.removeItem('freya_english_stars_10');
      localStorage.removeItem('freya_english_stars');
      localStorage.removeItem('freya_english_progress');
      localStorage.removeItem('freya_english_cards_seen_10');
      localStorage.removeItem('freya_english_cards_seen');
    }catch(err){}

    saveProgress();
    goHome();
    renderHome();
    playMagicalSound('sparkle');
    alert("🔄 Semua skor & bintang Freya berhasil di-reset ke 0! / All scores have been reset to 0! ⭐");
  } else {
    // Reset counter if next click is not within 3 seconds
    freyaClickTimer = setTimeout(() => {
      freyaClickCount = 0;
    }, 3000);
  }
}

/* =========================================================
   FLASHCARD MODE (Kartu Belajar)
   ========================================================= */
function startLearn(){
  playMagicalSound('pop');
  updateActiveCards();
  if(!activeCards.length) return;
  learnIndex = 0;
  renderLearnCard(true);
  show('screen-learn');
}

function recordCardSeen(){
  const ch = CHAPTERS[currentChapterIdx];
  if(!cardsSeen[ch.id]) cardsSeen[ch.id] = [];
  if(!cardsSeen[ch.id].includes(learnIndex)){
    cardsSeen[ch.id].push(learnIndex);
    saveProgress();
  }
}

function renderLearnCard(autoPlay = true){
  const card = activeCards[learnIndex];
  const total = activeCards.length;

  recordCardSeen();

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
  mainBtn.textContent = (learnIndex === total - 1) ? 'Selesai! Main Kuis 10 ⭐ 🎯' : 'Lanjut 🌸 →';

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
   QUIZ MODE FOR FREYA (10 QUESTIONS = UP TO 10 STARS)
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
  const pool = getAllChapterCards();
  let selected = shuffle(pool).slice(0, 10);
  while(selected.length < 10){
    selected.push(pool[Math.floor(Math.random() * pool.length)]);
  }

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

function renderQuizLiveStars(){
  const count = quizState ? quizState.correctCount : 0;
  const el = document.getElementById('quizLiveStars');
  if(el){
    el.innerHTML = render10StarsHtml(count, 10);
  }
  const scoreBadge = document.getElementById('quizLiveScore');
  if(scoreBadge){
    scoreBadge.textContent = `${count} / 10 ⭐`;
  }
}

function startQuiz(){
  playMagicalSound('sparkle');
  const questions = buildQuizQuestions();
  quizState = {
    questions: questions,
    index: 0,
    correctCount: 0
  };
  renderQuizLiveStars();
  renderQuizQuestion();
  show('screen-quiz');
}

function renderQuizQuestion(){
  const q = quizState.questions[quizState.index];
  document.getElementById('quizProgressText').textContent = `Soal ${quizState.index + 1} dari ${quizState.questions.length} 🦄`;
  renderQuizLiveStars();

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

  if(q.speakText) speakSingle(q.speakText, voicePitch, voiceSpeed);
}

function answerQuiz(btn, selectedText, q){
  const isCorrect = (selectedText === q.correct);
  document.querySelectorAll('.option').forEach(o => o.classList.add('disabled'));

  const fb = document.getElementById('quizFeedback');
  if(isCorrect){
    playMagicalSound('correct');
    btn.classList.add('correct');
    quizState.correctCount++;
    renderQuizLiveStars();
    fb.textContent = `Hebat Sekali Freya! Betul! ⭐ (${quizState.correctCount}/10 Bintang) 🎉✨`;
    fb.className = 'feedback good';
    speakSingle(q.speakText || q.correct, voicePitch, voiceSpeed);
  } else {
    playMagicalSound('wrong');
    btn.classList.add('wrong');
    document.querySelectorAll('.option').forEach(o => {
      if(o.textContent === q.correct) o.classList.add('correct');
    });
    fb.textContent = 'Hampir tepat! Jawaban yang benar ditandai ya, Freya! 💪🌸';
    fb.className = 'feedback bad';
    speakSingle(q.speakText || q.correct, voicePitch * 0.95, voiceSpeed);
  }

  setTimeout(() => {
    quizState.index++;
    if(quizState.index >= quizState.questions.length){
      finishQuiz();
    } else {
      renderQuizQuestion();
    }
  }, 1450);
}

function finishQuiz(){
  const ch = CHAPTERS[currentChapterIdx];
  const total = quizState.questions.length;
  const earnedStars = quizState.correctCount; // each right answer awards 1 star (0 to 10)

  // Log the stars into permanent progress!
  if(earnedStars > (progress[ch.id] || 0)){
    progress[ch.id] = earnedStars;
    saveProgress();
  }

  const currentBest = Math.max(progress[ch.id] || 0, earnedStars);

  document.getElementById('resultEmoji').textContent = earnedStars >= 8 ? '👑' : (earnedStars >= 5 ? '🦄' : '🌸');
  document.getElementById('resultTitle').textContent = earnedStars === 10
    ? 'Sempurna! 10 Bintang Emas! 👑✨' 
    : (earnedStars >= 7 ? 'Luar Biasa, Princess Freya! 🦄✨' : 'Bagus Sekali, Freya Cantik! 🌸');
  document.getElementById('resultSub').textContent = `Freya berhasil mengumpulkan ${earnedStars} dari 10 Bintang di Bab ini!`;

  // Render 10 stars on result screen
  document.getElementById('resultStars10').innerHTML = render10StarsHtml(earnedStars);

  document.getElementById('resultScore').textContent = `Nilai Kuis: ${earnedStars} / ${total} Soal Benar (${earnedStars * 10}%) ⭐ | Bintang Tersimpan: ${currentBest}/10 ⭐`;
  document.getElementById('retryBtn').textContent = earnedStars === 10 ? '🔁 Main Kuis Lagi 🎀' : '⭐ Main Lagi untuk 10 Bintang!';

  show('screen-result');
  if(earnedStars >= 4){
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
populateVoiceSelect();
show('screen-home');
</script>
</body>
</html>
"""

with open("Freya_Shyam_English.html", "w", encoding="utf-8") as f:
    f.write(html_code)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Upgraded to 10 stars per chapter (110 total stars) successfully!")
