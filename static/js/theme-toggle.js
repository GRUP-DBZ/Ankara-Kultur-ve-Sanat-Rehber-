(function(){
  const btn = document.getElementById('themeToggle');
  const body = document.body;
  function applyTheme(theme){
    body.classList.remove('theme-dark','theme-light');
    body.classList.add(theme==='dark' ? 'theme-dark' : 'theme-light');
    try{ localStorage.setItem('theme', theme); }catch(e){}
    updateButton(theme);
  }
  function updateButton(theme){
    if(!btn) return;
    const t = theme || (localStorage.getItem('theme') || (body.classList.contains('theme-dark')? 'dark' : 'light'));
    btn.textContent = t === 'dark' ? '🌙' : '☀️';
    btn.setAttribute('aria-pressed', t === 'dark');
  }
  // determine initial theme
  let stored = null;
  try{ stored = localStorage.getItem('theme'); }catch(e){}
  if(stored){
    applyTheme(stored);
  } else if(body.classList.contains('theme-dark') || body.classList.contains('theme-light')){
    // respect existing class
    updateButton(body.classList.contains('theme-dark') ? 'dark' : 'light');
  } else if(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches){
    applyTheme('dark');
  } else {
    applyTheme('light');
  }

  if(btn){
    btn.addEventListener('click', function(e){
      const current = body.classList.contains('theme-dark') ? 'dark' : 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next);
    });
  }
})();
