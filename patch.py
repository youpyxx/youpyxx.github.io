from pathlib import Path
p=Path('/mnt/data/site_work/index.html')
s=p.read_text(encoding='utf-8')
s=s.replace('Номер студенческого</span><input id="reg-student-id"', 'Номер студенческого билета</span><input id="reg-student-id"')
s=s.replace('Ермолаева Дарья</p>\n      <p class="meta">ВМК · 1 курс, гр. 107</p>', 'Ермолаева Дарья Сергеевна</p>\n      <p class="meta">ВМК · 1 курс, гр. 119</p>')
s=s.replace('<h3>Ермолаева Дарья</h3>\n          <p>ВМК · 1 курс · группа 107</p>', '<h3>Ермолаева Дарья Сергеевна</h3>\n          <p>ВМК · 1 курс · группа 119</p>')
s=s.replace('<div><span>Группа</span><b>107</b></div>', '<div><span>Группа</span><b>119</b></div>')
start=s.index('  // ---------- schedule calendar ----------')
end=s.index('  // ---------- session / exams ----------', start)
new=r'''  // ---------- schedule calendar ----------
  // Персональное расписание группы 119 по таблице осеннего семестра 2026/2027.
  // На компьютере показываем Пн–Вс, на телефоне — Пн–Ср / Чт–Сб.
  const scheduleLessons = {
    1:[
      {start:'08:45',end:'10:20',n:'',r:'',type:''},
      {start:'10:30',end:'12:05',n:'Матанализ',r:'Емельянов Д.П. · ауд. 653',type:'discipline-math'},
      {start:'12:50',end:'14:25',n:'Математический анализ',r:'П-6 · доцент Никитин Алексей Антонович',type:'discipline-math'},
      {start:'14:35',end:'16:10',n:'Алгебра и геометрия',r:'Золотарёва Н.Д. · ауд. 787',type:'discipline-algebra'},
      {start:'16:50',end:'18:20',n:'Физическая культура',r:'спортзал',type:'discipline-pe'}
    ],
    2:[
      {start:'08:45',end:'10:20',n:'',r:'',type:''},
      {start:'10:30',end:'12:05',n:'Алгебра и геометрия',r:'Золотарёва Н.Д. · ауд. 779',type:'discipline-algebra'},
      {start:'12:50',end:'14:25',n:'Алгебра и геометрия',r:'П-5 · доцент Панфёров Валерий Семёнович',type:'discipline-algebra'},
      {start:'14:35',end:'16:10',n:'Практикум на ЭВМ',r:'Капитонова А.П. · ауд. 659 · Пашков В.Н. · 515',type:'discipline-practicum'},
      {start:'16:20',end:'17:55',n:'Иностранный язык',r:'Попотяпова Н.М. · ауд. 785 · Перцева З.Н. · 71',type:'discipline-foreign'}
    ],
    3:[
      {start:'08:45',end:'10:20',n:'Алгоритмы и алгоритмические языки',r:'П-13 · доцент Корухова Юлия Станиславовна',type:'discipline-algorithms'},
      {start:'10:30',end:'12:05',n:'Алгоритмы и алгоритмические языки',r:'П-13 · доцент Корухова Юлия Станиславовна',type:'discipline-algorithms'},
      {start:'12:50',end:'14:25',n:'Математический анализ',r:'П-11 · доцент Никитин Алексей Антонович',type:'discipline-math'},
      {start:'15:10',end:'18:50',n:'Межфакультетские курсы',r:'',type:'discipline-civics'}
    ],
    4:[
      {start:'08:45',end:'10:20',n:'БЗД',r:'Сладкова Н.В. · ауд. 614'},
      {start:'08:45',end:'10:20',n:'История России',r:'с 17.09 · Чубыкин И.В. · ауд. 523',type:'discipline-history',startsOn:'2026-09-17'},
      {start:'10:30',end:'12:05',n:'История России',r:'П-5 · Меркулова Анастасия Михайловна',type:'discipline-history'},
      {start:'12:50',end:'14:25',n:'Алгебра и геометрия',r:'П-5 · доцент Панфёров Валерий Семёнович',type:'discipline-algebra'},
      {start:'14:35',end:'16:10',n:'Матанализ',r:'Емельянов Д.П. · ауд. 615',type:'discipline-math'}
    ],
    5:[
      {start:'09:00',end:'10:30',n:'Физическая культура',r:'',type:'discipline-pe'},
      {start:'10:40',end:'12:15',n:'Иностранный язык',r:'Попотяпова Н.М. · ауд. 71',type:'discipline-foreign'},
      {start:'12:50',end:'14:25',n:'История России',r:'с 11.09 · Меркулова А.М. · ауд. 729',type:'discipline-history',startsOn:'2026-09-11'},
      {start:'14:35',end:'16:10',n:'Практикум на ЭВМ',r:'Капитонова А.П. · ауд. 659 · Пашков В.Н. · 515',type:'discipline-practicum'},
      {start:'16:20',end:'17:55',n:'Консультация: практикум на ЭВМ',r:'Капитонова А.П. · ауд. 659 · Никифоров А.Н. · 515',type:'discipline-practicum'}
    ],
    6:[
      {start:'08:45',end:'10:30',n:'Основы российской государственности',r:'П-13 · Ляховенко О.И.',type:'discipline-civics'}
    ]
  };

  // Для БЗД в четверг сохраняем отдельный объект с явным цветом.
  scheduleLessons[4][0].type='discipline-safety';

  const monthNames=['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря'];
  const monthNamesShort=['янв','фев','мар','апр','май','июн','июл','авг','сен','окт','ноя','дек'];
  const weekdayNames=['Вс','Пн','Вт','Ср','Чт','Пт','Сб'];
  const times = Array.from(new Map(
    Object.values(scheduleLessons).flat().map(x=>[x.start,{start:x.start,end:x.end}])
  ).values()).sort((a,b)=>a.start.localeCompare(b.start));

  const scheduleStart=new Date(2026,7,31); // Пн, 31 августа 2026
  const scheduleEnd=new Date(2027,0,31);   // Вс, 31 января 2027
  const weeks=[];
  for(let monday=new Date(scheduleStart); monday<=scheduleEnd; monday.setDate(monday.getDate()+7)){
    const days=[];
    for(let i=0;i<7;i++){
      const d=new Date(monday); d.setDate(monday.getDate()+i);
      if(d<=scheduleEnd) days.push({date:d,short:weekdayNames[d.getDay()]});
    }
    weeks.push(days);
  }

  let weekIndex=0;
  let mobileDayOffset=0;
  function fmtDate(d){return `${d.getDate()} ${monthNamesShort[d.getMonth()]}`;}
  function fmtRange(a,b){
    if(a.getMonth()===b.getMonth() && a.getFullYear()===b.getFullYear()) return `${a.getDate()} — ${b.getDate()} ${monthNames[b.getMonth()]} ${b.getFullYear()}`;
    return `${fmtDate(a)} ${a.getFullYear()} — ${fmtDate(b)} ${b.getFullYear()}`;
  }
  function dateOnly(d){return new Date(d.getFullYear(),d.getMonth(),d.getDate());}
  function getLesson(dayIndex,start,date){
    const items=scheduleLessons[dayIndex]||[];
    const candidates=items.filter(x=>x.start===start && x.n);
    return candidates.find(x=>!x.startsOn || dateOnly(date)>=dateOnly(new Date(x.startsOn))) || null;
  }

  function renderWeek(){
    const fullWeek=weeks[weekIndex]; if(!fullWeek?.length) return;
    const isMobile=window.matchMedia('(max-width: 860px)').matches;
    const mobileWeek=fullWeek.slice(0,6);
    const visibleDays=isMobile ? mobileWeek.slice(mobileDayOffset,mobileDayOffset+3) : fullWeek;
    if(isMobile && !visibleDays.length){mobileDayOffset=0;return renderWeek();}
    const first=visibleDays[0].date,last=visibleDays[visibleDays.length-1].date;
    document.getElementById('week-range').innerHTML=`${fmtRange(first,last)}<span class="week-day-date">${isMobile?'группа 119 · '+fmtDate(fullWeek[0].date)+' — '+fmtDate(fullWeek[fullWeek.length-1].date):'группа 119 · понедельник — воскресенье'}</span>`;
    let grid='<div class="cell head"></div>';
    visibleDays.forEach(d=>grid+=`<div class="cell head">${d.short}<span class="week-day-date">${fmtDate(d.date)}</span></div>`);
    times.forEach(t=>{
      grid+=`<div class="cell time"><span>${t.start}</span><small>${t.end}</small></div>`;
      visibleDays.forEach(d=>{
        const les=getLesson(d.date.getDay(),t.start,d.date);
        grid+=`<div class="cell">${les?`<div class="lesson ${les.type||''}"><b>${les.n}</b><span class="rm">${les.r}</span></div>`:''}</div>`;
      });
    });
    document.getElementById('week-grid').innerHTML=grid;
    if(isMobile){
      document.getElementById('week-prev').disabled=weekIndex===0&&mobileDayOffset===0;
      document.getElementById('week-next').disabled=weekIndex===weeks.length-1&&mobileDayOffset+3>=mobileWeek.length;
    }else{
      document.getElementById('week-prev').disabled=weekIndex===0;
      document.getElementById('week-next').disabled=weekIndex===weeks.length-1;
    }
  }

  document.getElementById('week-prev').addEventListener('click',()=>{
    const isMobile=window.matchMedia('(max-width: 860px)').matches;
    if(isMobile){
      if(mobileDayOffset>=3) mobileDayOffset-=3;
      else if(weekIndex>0){weekIndex--;mobileDayOffset=3;}
    }else if(weekIndex>0) weekIndex--;
    renderWeek();
  });
  document.getElementById('week-next').addEventListener('click',()=>{
    const isMobile=window.matchMedia('(max-width: 860px)').matches;
    if(isMobile){
      if(mobileDayOffset+3<6) mobileDayOffset+=3;
      else if(weekIndex<weeks.length-1){weekIndex++;mobileDayOffset=0;}
    }else if(weekIndex<weeks.length-1) weekIndex++;
    renderWeek();
  });
  window.addEventListener('resize',renderWeek);
  renderWeek();

  // ---------- lesson reminders ----------
  // Пока сайт статический, надёжные push-уведомления при полностью закрытом приложении
  // невозможны без push-сервера. Здесь реализованы напоминания, когда сайт/PWA открыт.
  function parseClock(s){const [h,m]=s.split(':').map(Number);return h*60+m;}
  function reminderKey(date,lesson,mins){return `lesson-reminder:${date.toISOString().slice(0,10)}:${lesson.start}:${mins}:${lesson.n}`;}
  function checkLessonReminders(){
    if(localStorage.getItem('studentNotifications')!=='on') return;
    if(!('Notification' in window) || Notification.permission!=='granted') return;
    const now=new Date();
    const dow=now.getDay(); if(dow===0) return;
    const minutesNow=now.getHours()*60+now.getMinutes();
    const reminderMinutes=Number(localStorage.getItem('studentReminder')||30);
    const lessons=scheduleLessons[dow]||[];
    lessons.forEach(lesson=>{
      if(!lesson.n || (lesson.startsOn && dateOnly(now)<dateOnly(new Date(lesson.startsOn)))) return;
      const diff=parseClock(lesson.start)-minutesNow;
      if(diff>=0 && diff<=reminderMinutes){
        const key=reminderKey(now,lesson,reminderMinutes);
        if(localStorage.getItem(key)) return;
        localStorage.setItem(key,'1');
        const room=lesson.r?.match(/ауд\.\s*[^·]+/)?.[0] || '';
        const body=`Через ${diff} мин. · ${lesson.start}–${lesson.end}${room?` · ${room}`:''}`;
        try{new Notification(`Скоро: ${lesson.n}`,{body,icon:'icon-192.png',tag:key});}catch(e){}
        showToast(`Скоро пара: ${lesson.n}`);
      }
    });
  }
  setInterval(checkLessonReminders,15000);
  checkLessonReminders();

'''
s=s[:start]+new+s[end:]
# Seed personalized default account only when there is no account at all.
needle="  const existingUser=JSON.parse(localStorage.getItem(AUTH_KEY)||'null'); if(existingUser && sessionStorage.getItem(SESSION_KEY)==='1'){setStudentName(existingUser); document.body.classList.add('authenticated'); startMainPage();}"
replacement="  const existingUser=JSON.parse(localStorage.getItem(AUTH_KEY)||'null'); if(existingUser && sessionStorage.getItem(SESSION_KEY)==='1'){setStudentName(existingUser); document.body.classList.add('authenticated'); startMainPage();}"
# Don't auto-seed a password; preserve the explicit registration flow.
s=s.replace(needle,replacement)
p.write_text(s,encoding='utf-8')
