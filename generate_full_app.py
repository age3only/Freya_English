import json

with open("spoken_english_data.json", "r", encoding="utf-8") as f:
    chapters_data = json.load(f)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Spoken English">
<title>Spoken English in Dialogues 🦜</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;700;800&family=Nunito:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>
  :root{
    --ocean:#2EC4E8;
    --ocean-dark:#1B9DC0;
    --sand:#FFE29A;
    --jungle:#3FBF7F;
    --jungle-dark:#2A9C63;
    --coral:#FF6F5E;
    --coral-dark:#E8503F;
    --plum:#2B2250;
    --cream:#FFFDF7;
    --sun:#FFC94A;
    --lock:#B8C4D9;
    --card-bg:#FFFFFF;
  }
  *{box-sizing:border-box; -webkit-tap-highlight-color: transparent;}
  html,body{
    margin:0; padding:0; height:100%;
    font-family:'Nunito', sans-serif;
    background:
      radial-gradient(circle at 15% 8%, #FFF3C4 0%, transparent 45%),
      radial-gradient(circle at 90% 5%, #C9F2E8 0%, transparent 40%),
      linear-gradient(180deg, #BDEFFB 0%, #E9F8E4 55%, #FFF3D6 100%);
    color:var(--plum);
    overflow-x:hidden;
    -webkit-user-select:none;
    user-select:none;
  }
  h1,h2,h3,.display{ font-family:'Baloo 2', sans-serif; }
  button{ font-family:inherit; cursor:pointer; border:none; }
  .screen{ min-height:100vh; padding:20px 16px 60px; position:relative; max-width:680px; margin:0 auto; }
  .hidden{ display:none !important; }

  /* ---------- TOP BAR ---------- */
  .topbar{
    display:flex; align-items:center; justify-content:space-between;
    margin-bottom:18px;
  }
  .topbar .stars{
    background:var(--cream); border-radius:999px; padding:8px 16px;
    font-weight:900; font-size:16px; box-shadow:0 3px 0 rgba(43,34,80,0.12);
    display:flex; align-items:center; gap:6px;
  }
  .backbtn{
    background:var(--cream); width:44px; height:44px; border-radius:50%;
    font-size:20px; box-shadow:0 3px 0 rgba(43,34,80,0.12);
    display:flex; align-items:center; justify-content:center;
    transition:transform .12s ease;
  }
  .backbtn:active{ transform:translateY(2px); box-shadow:0 1px 0 rgba(43,34,80,0.12); }

  /* ---------- HOME / MAP ---------- */
  .hero{ text-align:center; margin-bottom:12px; }
  .kiki{ font-size:60px; display:inline-block; animation:bob 2.6s ease-in-out infinite; }
  @keyframes bob{ 0%,100%{transform:translateY(0) rotate(-3deg);} 50%{transform:translateY(-8px) rotate(3deg);} }
  .hero h1{ font-size:28px; margin:6px 0 4px; color:var(--plum); }
  .hero p{ margin:0; font-weight:700; color:var(--ocean-dark); font-size:15px; }

  .chapter-grid{
    display:flex; flex-direction:column; gap:12px; margin-top:22px;
  }
  .chapter-card{
    background:var(--cream); border-radius:22px; padding:16px 20px;
    display:flex; align-items:center; gap:16px;
    box-shadow:0 6px 0 rgba(43,34,80,0.12);
    transition:transform .15s ease, box-shadow .15s ease;
    cursor:pointer; text-align:left;
  }
  .chapter-card:active{ transform:translateY(3px); box-shadow:0 3px 0 rgba(43,34,80,0.12); }
  .ch-badge{
    width:62px; height:62px; border-radius:50%; flex:0 0 auto;
    display:flex; align-items:center; justify-content:center;
    font-size:30px; box-shadow:0 4px 0 rgba(43,34,80,0.14);
    background:var(--sand);
  }
  .ch-info{ flex:1; }
  .ch-number{ font-weight:800; font-size:12px; text-transform:uppercase; letter-spacing:1px; color:var(--ocean-dark); }
  .ch-title{ font-family:'Baloo 2',sans-serif; font-weight:700; font-size:20px; color:var(--plum); line-height:1.2; }
  .ch-sub{ font-size:13px; font-weight:700; color:#6B7280; margin-top:2px; }
  .ch-stars{ font-size:15px; color:var(--sun); font-weight:800; margin-top:4px; }
  .ch-arrow{ font-size:22px; color:#A0AEC0; }

  /* ---------- STATION MENU SCREEN ---------- */
  .station-header{ text-align:center; margin-bottom:18px; }
  .station-header .badge{ font-size:56px; }
  .station-header h2{ margin:6px 0 2px; font-size:26px; }
  .station-header .sub{ font-weight:700; color:var(--ocean-dark); font-size:15px; }
  
  .topic-selector-wrap{ margin:18px 0 16px; text-align:left; }
  .topic-selector-label{ font-weight:800; font-size:14px; color:var(--plum); margin-bottom:6px; display:block; }
  .topic-select{
    width:100%; padding:12px 14px; border-radius:14px; border:2px solid #E2E8F0;
    font-family:'Nunito',sans-serif; font-size:15px; font-weight:700;
    color:var(--plum); background:#fff; outline:none; box-shadow:0 2px 0 rgba(43,34,80,0.06);
  }

  .mode-buttons{ display:flex; flex-direction:column; gap:14px; margin-top:20px; }
  .mode-btn{
    padding:18px 22px; border-radius:20px; font-weight:800; font-size:17px;
    display:flex; align-items:center; gap:14px; box-shadow:0 5px 0 rgba(43,34,80,0.16);
    color:#fff; text-align:left;
  }
  .mode-btn:active{ transform:translateY(3px); box-shadow:0 2px 0 rgba(43,34,80,0.16); }
  .mode-btn .icon{ font-size:28px; }
  .mode-btn.learn{ background:linear-gradient(135deg, var(--ocean), var(--ocean-dark)); }
  .mode-btn.play{ background:linear-gradient(135deg, var(--coral), var(--coral-dark)); }
  .mode-btn small{ display:block; font-weight:700; font-size:12.5px; opacity:0.92; margin-top:2px; }

  /* ---------- FLASHCARDS ---------- */
  .card-wrap{ margin-top:6px; }
  .progress-info{ text-align:center; font-weight:800; font-size:14px; color:var(--ocean-dark); margin-bottom:12px; }
  .progress-bar-bg{ width:100%; height:8px; background:#E2E8F0; border-radius:999px; margin-bottom:16px; overflow:hidden; }
  .progress-bar-fill{ height:100%; background:var(--coral); width:0%; transition:width .2s ease; border-radius:999px; }

  .dialogue-card{
    background:var(--cream); border-radius:28px; padding:26px 20px 22px;
    box-shadow:0 8px 0 rgba(43,34,80,0.14); text-align:left;
    display:flex; flex-direction:column; gap:14px; min-height:300px; justify-content:center;
  }
  .card-topic-tag{
    align-self:flex-start; background:#EFF6FF; color:#2563EB; font-weight:800;
    font-size:12px; padding:4px 12px; border-radius:12px; text-transform:uppercase; letter-spacing:0.5px;
  }
  .bubble{
    border-radius:18px; padding:14px 18px; font-size:16px; font-weight:700; line-height:1.4;
    position:relative;
  }
  .bubble-speaker{
    font-size:12px; font-weight:900; text-transform:uppercase; letter-spacing:0.5px;
    margin-bottom:4px; display:flex; align-items:center; gap:6px;
  }
  .bubble.speaker-a{
    background:#E0F2FE; color:#0369A1; border-bottom-left-radius:4px;
  }
  .bubble.speaker-b{
    background:#DCFCE7; color:#15803D; border-bottom-right-radius:4px; align-self:flex-end; width:95%;
  }
  .card-note{
    background:#FEF3C7; border-left:4px solid #F59E0B; padding:10px 14px; border-radius:8px;
    font-size:13px; font-weight:700; color:#92400E; margin-top:4px; line-height:1.4;
  }
  .card-audio-row{
    display:flex; justify-content:center; gap:10px; margin-top:10px;
  }
  .listen-btn{
    background:var(--sun); color:var(--plum); border-radius:999px; padding:10px 22px;
    font-weight:900; font-size:15px; box-shadow:0 4px 0 rgba(43,34,80,0.16);
    display:inline-flex; align-items:center; gap:8px; transition:transform .12s ease;
  }
  .listen-btn:active{ transform:translateY(2px); box-shadow:0 2px 0 rgba(43,34,80,0.16); }

  .card-nav{ display:flex; justify-content:space-between; align-items:center; margin-top:20px; gap:12px; }
  .nav-btn{
    background:var(--cream); width:54px; height:54px; border-radius:50%; font-size:22px;
    box-shadow:0 4px 0 rgba(43,34,80,0.12); display:flex; align-items:center; justify-content:center;
  }
  .nav-btn:disabled{ opacity:0.35; pointer-events:none; }
  .finish-btn{
    flex:1; background:linear-gradient(135deg, var(--jungle), var(--jungle-dark)); color:#fff;
    font-weight:900; font-size:16px; padding:15px; border-radius:18px;
    box-shadow:0 5px 0 rgba(43,34,80,0.16);
  }
  .finish-btn:active{ transform:translateY(2px); box-shadow:0 3px 0 rgba(43,34,80,0.16); }

  /* ---------- QUIZ ---------- */
  .quiz-wrap{ margin-top:6px; }
  .quiz-top{ display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; }
  .quiz-hearts{ font-size:20px; letter-spacing:4px; }
  .quiz-progress{ font-weight:800; font-size:14px; color:var(--ocean-dark); }
  
  .quiz-question{
    background:var(--cream); border-radius:24px; padding:24px 20px; text-align:center;
    box-shadow:0 6px 0 rgba(43,34,80,0.14); margin-bottom:18px;
  }
  .quiz-question .kicker{ font-weight:800; font-size:13px; color:var(--ocean-dark); margin-bottom:6px; }
  .quiz-question .qtext{ font-family:'Baloo 2',sans-serif; font-weight:700; font-size:20px; color:var(--plum); line-height:1.3; }
  .quiz-listen-icon{ margin-top:8px; display:inline-block; font-size:20px; cursor:pointer; background:#F1F5F9; border-radius:50%; width:36px; height:36px; line-height:36px; text-align:center; }

  .options{ display:flex; flex-direction:column; gap:12px; }
  .option{
    background:var(--cream); border-radius:16px; padding:16px 18px; font-weight:800; font-size:15px;
    text-align:left; box-shadow:0 4px 0 rgba(43,34,80,0.12); color:var(--plum); line-height:1.4;
    transition:all .12s ease;
  }
  .option:active{ transform:translateY(2px); box-shadow:0 2px 0 rgba(43,34,80,0.12); }
  .option.correct{ background:#D9F5E3 !important; box-shadow:0 4px 0 #7FCE9C !important; color:var(--jungle-dark) !important; }
  .option.wrong{ background:#FFE1DD !important; box-shadow:0 4px 0 var(--coral) !important; color:var(--coral-dark) !important; }
  .option.disabled{ pointer-events:none; }
  .feedback{ text-align:center; font-weight:900; font-size:16px; min-height:24px; margin-top:14px; }
  .feedback.good{ color:var(--jungle-dark); }
  .feedback.bad{ color:var(--coral-dark); }

  /* ---------- RESULT ---------- */
  .result-wrap{ margin:40px auto 0; text-align:center; }
  .result-wrap .big-emoji{ font-size:74px; animation:pop .5s ease; }
  @keyframes pop{ 0%{transform:scale(0);} 70%{transform:scale(1.18);} 100%{transform:scale(1);} }
  .result-wrap h2{ font-size:26px; margin:10px 0 4px; }
  .result-wrap p{ font-weight:700; color:var(--ocean-dark); font-size:16px; }
  .result-stars{ font-size:42px; margin:16px 0; letter-spacing:6px; }
  .result-score-tag{ font-size:18px; font-weight:900; color:var(--plum); margin-bottom:16px; }
  .result-buttons{ display:flex; flex-direction:column; gap:12px; margin-top:24px; }

  .confetti{ position:fixed; inset:0; pointer-events:none; z-index:50; overflow:hidden; }
  .confetti span{ position:absolute; top:-20px; font-size:24px; animation:fall linear forwards; }
  @keyframes fall{ to{ transform:translateY(110vh) rotate(360deg); opacity:0.3; } }

  .footer-note{ text-align:center; font-size:12px; color:#7C8AA6; font-weight:700; margin-top:30px; }
</style>
</head>
<body>

<div class="confetti" id="confetti"></div>

<!-- ===================== HOME SCREEN ===================== -->
<section class="screen" id="screen-home">
  <div class="topbar">
    <div style="width:44px;"></div>
    <div class="stars">⭐ <span id="totalStars">0</span> / <span id="maxStars">0</span> Stars</div>
  </div>
  <div class="hero">
    <div class="kiki">🦜</div>
    <h1>Spoken English Dialogues</h1>
    <p>Practice real-life English dialogues with audio &amp; quizzes!</p>
  </div>

  <div class="chapter-grid" id="chaptersGrid"></div>

  <div class="footer-note">Tap 🔊 anytime to hear natural English pronunciation!</div>
</section>

<!-- ===================== STATION MENU SCREEN ===================== -->
<section class="screen hidden" id="screen-station">
  <div class="topbar">
    <button class="backbtn" onclick="goHome()">←</button>
    <div class="stars">⭐ <span id="stationStars">0</span> / 3</div>
  </div>
  <div class="station-header">
    <div class="badge" id="stHeaderBadge">🤝</div>
    <h2 id="stHeaderTitle">Good Manners</h2>
    <div class="sub" id="stHeaderSub">Greetings, Politeness &amp; Social Etiquette</div>
  </div>

  <div class="topic-selector-wrap">
    <label class="topic-selector-label" for="topicDropdown">Select Topic to Practice:</label>
    <select class="topic-select" id="topicDropdown" onchange="onTopicChange()"></select>
  </div>

  <div class="mode-buttons">
    <button class="mode-btn learn" onclick="startLearn()">
      <span class="icon">📖</span>
      <span>Dialogue Flashcards<small>Read, listen &amp; speak full conversations</small></span>
    </button>
    <button class="mode-btn play" onclick="startQuiz()">
      <span class="icon">🎯</span>
      <span>Interactive Quiz<small>Test your response skills &amp; earn stars!</small></span>
    </button>
  </div>
</section>

<!-- ===================== FLASHCARD SCREEN ===================== -->
<section class="screen hidden" id="screen-learn">
  <div class="topbar">
    <button class="backbtn" onclick="showStation()">←</button>
    <div class="progress-info" id="learnProgressText">Card 1 of 10</div>
  </div>
  <div class="card-wrap">
    <div class="progress-bar-bg">
      <div class="progress-bar-fill" id="learnProgressBar"></div>
    </div>
    
    <div class="dialogue-card">
      <div class="card-topic-tag" id="cardTopicTag">Topic</div>

      <div class="bubble speaker-a">
        <div class="bubble-speaker">👤 Speaker A</div>
        <div id="cardTextA">Hello!</div>
      </div>

      <div class="bubble speaker-b">
        <div class="bubble-speaker">🗣️ Speaker B</div>
        <div id="cardTextB">Hi there!</div>
      </div>

      <div class="card-note hidden" id="cardNote"></div>

      <div class="card-audio-row">
        <button class="listen-btn" onclick="speakCurrentDialogue()">🔊 Listen to Dialogue</button>
      </div>
    </div>

    <div class="card-nav">
      <button class="nav-btn" id="prevBtn" onclick="prevCard()">←</button>
      <button class="finish-btn" id="cardMainBtn" onclick="nextCard()">Next →</button>
      <button class="nav-btn" id="listenSmallBtn" onclick="speakCurrentDialogue()">🔊</button>
    </div>
  </div>
</section>

<!-- ===================== QUIZ SCREEN ===================== -->
<section class="screen hidden" id="screen-quiz">
  <div class="topbar">
    <button class="backbtn" onclick="showStation()">←</button>
    <div class="quiz-hearts" id="quizHearts">❤️❤️❤️</div>
  </div>
  <div class="quiz-wrap">
    <div class="quiz-top">
      <div class="quiz-progress" id="quizProgressText">Question 1/5</div>
    </div>
    <div class="quiz-question">
      <div class="kicker" id="quizKicker">How would you reply to:</div>
      <div class="qtext" id="quizQ">Good morning! How are you?</div>
      <div class="quiz-listen-icon" onclick="speakQuizQuestion()">🔊</div>
    </div>
    <div class="options" id="quizOptions"></div>
    <div class="feedback" id="quizFeedback"></div>
  </div>
</section>

<!-- ===================== RESULT SCREEN ===================== -->
<section class="screen hidden" id="screen-result">
  <div class="result-wrap">
    <div class="big-emoji" id="resultEmoji">🎉</div>
    <h2 id="resultTitle">Outstanding Job!</h2>
    <p id="resultSub">You completed Good Manners!</p>
    <div class="result-stars" id="resultStars">⭐⭐⭐</div>
    <div class="result-score-tag" id="resultScore">Score: 5 / 5</div>
    <div class="result-buttons">
      <button class="finish-btn" onclick="retryQuiz()" id="retryBtn">🔁 Play Again</button>
      <button class="mode-btn learn" onclick="goHome()">🏝️ Back to Chapters Map</button>
    </div>
  </div>
</section>

<script>
/* =========================================================
   DATA - All 11 Chapters from "Spoken English in Dialogues"
   ========================================================= */
const CHAPTERS = """ + json.dumps(chapters_data, ensure_ascii=False) + """;

/* =========================================================
   STATE & PERSISTENCE
   ========================================================= */
let progress = {};
CHAPTERS.forEach(c => progress[c.id] = 0);

function saveProgress(){
  try{ localStorage.setItem('spoken_english_progress', JSON.stringify(progress)); }catch(e){}
}
function loadProgress(){
  try{
    const raw = localStorage.getItem('spoken_english_progress');
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
   TEXT TO SPEECH (Web Speech API)
   Alternates voices/pitches for Speaker A & Speaker B!
   ========================================================= */
function speak(text, pitch = 1.0, rate = 0.92, onEnd = null){
  try{
    if(!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US';
    u.rate = rate;
    u.pitch = pitch;
    if(onEnd) u.onend = onEnd;
    window.speechSynthesis.speak(u);
  }catch(e){}
}

function speakCurrentDialogue(){
  const card = activeCards[learnIndex];
  if(!card) return;
  // First speak Speaker A (pitch 1.15) then Speaker B (pitch 0.95)
  speak(card.q, 1.12, 0.9, () => {
    setTimeout(() => {
      speak(card.a, 0.95, 0.9);
    }, 450);
  });
}

function speakQuizQuestion(){
  if(!quizState) return;
  const q = quizState.questions[quizState.index];
  if(q) speak(q.qText, 1.05, 0.9);
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
  renderHome();
  show('screen-home');
}

function openChapter(idx){
  currentChapterIdx = idx;
  currentTopicFilter = "all";
  showStation();
}

function showStation(){
  const ch = CHAPTERS[currentChapterIdx];
  document.getElementById('stHeaderBadge').textContent = ch.badge;
  document.getElementById('stHeaderTitle').textContent = `Chapter ${ch.number}: ${ch.title}`;
  document.getElementById('stHeaderSub').textContent = ch.sub;
  document.getElementById('stationStars').textContent = progress[ch.id];

  // Populate dropdown
  const select = document.getElementById('topicDropdown');
  select.innerHTML = `<option value="all">⭐ All Topics in Chapter (${getChapterTotalCount(ch)} Dialogues)</option>`;
  ch.topics.forEach((t, i) => {
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = `${t.title} (${t.items.length})`;
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
   HOME SCREEN RENDER
   ========================================================= */
function renderHome(){
  const totalEarned = Object.values(progress).reduce((a, b) => a + b, 0);
  document.getElementById('totalStars').textContent = totalEarned;
  document.getElementById('maxStars').textContent = CHAPTERS.length * 3;

  const grid = document.getElementById('chaptersGrid');
  grid.innerHTML = '';

  CHAPTERS.forEach((ch, i) => {
    const count = getChapterTotalCount(ch);
    const card = document.createElement('div');
    card.className = 'chapter-card';
    card.onclick = () => openChapter(i);

    const stars = '⭐'.repeat(progress[ch.id]) + '☆'.repeat(3 - progress[ch.id]);

    card.innerHTML = `
      <div class="ch-badge">${ch.badge}</div>
      <div class="ch-info">
        <div class="ch-number">Chapter ${ch.number}</div>
        <div class="ch-title">${ch.title}</div>
        <div class="ch-sub">${ch.topics.length} Sections • ${count} Real Dialogues</div>
        <div class="ch-stars">${stars}</div>
      </div>
      <div class="ch-arrow">›</div>
    `;
    grid.appendChild(card);
  });
}

/* =========================================================
   FLASHCARD MODE
   ========================================================= */
function startLearn(){
  updateActiveCards();
  if(!activeCards.length) return;
  learnIndex = 0;
  renderLearnCard();
  show('screen-learn');
}

function renderLearnCard(){
  const card = activeCards[learnIndex];
  const total = activeCards.length;

  document.getElementById('cardTopicTag').textContent = card.topicTitle || 'Spoken Dialogue';
  document.getElementById('cardTextA').textContent = card.q;
  document.getElementById('cardTextB').textContent = card.a;

  const noteEl = document.getElementById('cardNote');
  if(card.note){
    noteEl.textContent = '💡 Vocabulary Note: ' + card.note;
    noteEl.classList.remove('hidden');
  } else {
    noteEl.classList.add('hidden');
  }

  document.getElementById('learnProgressText').textContent = `Dialogue ${learnIndex + 1} of ${total}`;
  const pct = Math.round(((learnIndex + 1) / total) * 100);
  document.getElementById('learnProgressBar').style.width = pct + '%';

  document.getElementById('prevBtn').disabled = (learnIndex === 0);
  const mainBtn = document.getElementById('cardMainBtn');
  mainBtn.textContent = (learnIndex === total - 1) ? 'Finish & Start Quiz 🎯' : 'Next →';

  speakCurrentDialogue();
}

function nextCard(){
  if(learnIndex < activeCards.length - 1){
    learnIndex++;
    renderLearnCard();
  } else {
    startQuiz();
  }
}

function prevCard(){
  if(learnIndex > 0){
    learnIndex--;
    renderLearnCard();
  }
}

/* =========================================================
   QUIZ MODE
   Generates contextual dialogue tests & vocabulary checks
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
  const sampleCount = Math.min(8, pool.length);
  const selected = shuffle(pool).slice(0, sampleCount);

  return selected.map(item => {
    const distractors = shuffle(pool.filter(c => c.q !== item.q)).slice(0, 2);
    const options = shuffle([item.a, distractors[0].a, distractors[1].a]);
    return {
      kicker: "How would you naturally reply to:",
      qText: item.q,
      correct: item.a,
      options: options
    };
  });
}

function getAllChapterCards(){
  const ch = CHAPTERS[currentChapterIdx];
  const list = [];
  ch.topics.forEach(t => t.items.forEach(i => list.push(i)));
  return list;
}

function startQuiz(){
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
  document.getElementById('quizHearts').textContent = '❤️'.repeat(quizState.lives) + '🖤'.repeat(3 - quizState.lives);
  document.getElementById('quizProgressText').textContent = `Question ${quizState.index + 1} of ${quizState.questions.length}`;

  document.getElementById('quizKicker').textContent = q.kicker;
  document.getElementById('quizQ').textContent = q.qText;

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

  speak(q.qText, 1.05, 0.92);
}

function answerQuiz(btn, selectedText, q){
  const isCorrect = (selectedText === q.correct);
  document.querySelectorAll('.option').forEach(o => o.classList.add('disabled'));

  const fb = document.getElementById('quizFeedback');
  if(isCorrect){
    btn.classList.add('correct');
    fb.textContent = 'Spot on! Exactly right! 🎉';
    fb.className = 'feedback good';
    quizState.correctCount++;
    speak(q.correct, 0.98, 0.92);
  } else {
    btn.classList.add('wrong');
    document.querySelectorAll('.option').forEach(o => {
      if(o.textContent === q.correct) o.classList.add('correct');
    });
    fb.textContent = 'Not quite! The best reply is highlighted.';
    fb.className = 'feedback bad';
    quizState.lives--;
    speak(q.correct, 0.95, 0.92);
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
  }, 1300);
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

  document.getElementById('resultEmoji').textContent = passed ? '🎉' : '💪';
  document.getElementById('resultTitle').textContent = passed ? 'Fantastic Job!' : 'Keep Practicing!';
  document.getElementById('resultSub').textContent = passed 
    ? `You mastered Chapter ${ch.number}: ${ch.title}!`
    : `Good effort! Review the flashcards and try again!`;
  document.getElementById('resultStars').textContent = passed ? ('⭐'.repeat(stars) + '☆'.repeat(3 - stars)) : '☆☆☆';
  document.getElementById('resultScore').textContent = `Correct: ${quizState.correctCount} / ${total} (${Math.round(ratio*100)}%)`;
  document.getElementById('retryBtn').textContent = passed ? '🔁 Play Again' : '🔁 Try Again';

  show('screen-result');
  if(passed) launchConfetti();
}

function retryQuiz(){
  startQuiz();
}

/* =========================================================
   CONFETTI
   ========================================================= */
function launchConfetti(){
  const holder = document.getElementById('confetti');
  const emojis = ['🎉', '⭐', '✨', '🏆', '🎊', '👏'];
  for(let i = 0; i < 26; i++){
    const span = document.createElement('span');
    span.textContent = emojis[Math.floor(Math.random() * emojis.length)];
    span.style.left = (Math.random() * 96) + 'vw';
    span.style.animationDuration = (2 + Math.random() * 1.8) + 's';
    span.style.fontSize = (16 + Math.random() * 20) + 'px';
    holder.appendChild(span);
    setTimeout(() => span.remove(), 4000);
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
    f.write(html_template)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Generated both Freya_Shyam_English.html and index.html successfully!")
