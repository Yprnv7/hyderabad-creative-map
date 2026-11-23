/* ==========================================================================
   DECCAN CANVAS — Authentication & Session Manager
   Case-Insensitive Usernames & Protected Member/Curator Access
   ========================================================================== */

const AuthManager = (() => {
  const STORAGE_KEY = 'deccan_canvas_auth_session';
  
  // Authorized Users (Usernames are strictly case-insensitive)
  const CREDENTIALS = {
    'gowri': {
      password: 'M@rcus',
      role: 'curator',
      label: 'Gowri'
    },
    'abhinav': {
      password: 'M@@ngini',
      role: 'curator',
      label: 'Abhinav'
    },
    'curator': {
      password: 'charminar99',
      role: 'curator',
      label: 'Deccan Curator'
    },
    'member': {
      password: 'deccan2026',
      role: 'member',
      label: 'Creative Member'
    }
  };

  function checkSession() {
    try {
      const session = localStorage.getItem(STORAGE_KEY);
      if (!session) return null;
      const data = JSON.parse(session);
      // Valid for 30 days
      if (Date.now() - data.loginTime < 30 * 24 * 60 * 60 * 1000) {
        return data;
      }
      logout();
      return null;
    } catch (e) {
      return null;
    }
  }

  function login(username, password) {
    // Normalizes username to lowercase for case-insensitivity
    const cleanUser = (username || '').trim().toLowerCase();
    const cleanPass = (password || '').trim();

    const record = CREDENTIALS[cleanUser];
    if (record && record.password === cleanPass) {
      const session = {
        username: cleanUser,
        role: record.role,
        label: record.label,
        loginTime: Date.now()
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(session));
      return { success: true, session };
    }

    return { 
      success: false, 
      error: 'Invalid username or password. Please verify your credentials.' 
    };
  }

  function logout() {
    localStorage.removeItem(STORAGE_KEY);
    const gate = document.getElementById('auth-gate');
    if (gate) {
      gate.classList.remove('unlocked');
      const errorMsg = document.getElementById('auth-error');
      if (errorMsg) errorMsg.classList.remove('visible');
      const passInput = document.getElementById('auth-password');
      if (passInput) passInput.value = '';
    }
  }

  function initUI(onUnlockCallback) {
    const gate = document.getElementById('auth-gate');
    const form = document.getElementById('auth-form');
    const userInput = document.getElementById('auth-username');
    const passInput = document.getElementById('auth-password');
    const errorMsg = document.getElementById('auth-error');
    const lockBtn = document.getElementById('lock-btn');
    const userBadge = document.getElementById('user-role-badge');
    const curatorBtn = document.getElementById('curator-toggle-btn');

    // Check existing valid session
    const existing = checkSession();
    if (existing) {
      if (gate) gate.classList.add('unlocked');
      updateUserBadge(existing);
      if (typeof onUnlockCallback === 'function') onUnlockCallback(existing);
    }

    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const user = userInput.value;
        const pass = passInput.value;
        const res = login(user, pass);

        if (res.success) {
          if (gate) gate.classList.add('unlocked');
          if (errorMsg) errorMsg.classList.remove('visible');
          updateUserBadge(res.session);
          if (typeof onUnlockCallback === 'function') onUnlockCallback(res.session);
        } else {
          if (errorMsg) {
            errorMsg.textContent = res.error;
            errorMsg.classList.add('visible');
          }
          if (passInput) {
            passInput.value = '';
            passInput.focus();
          }
        }
      });
    }

    if (lockBtn) {
      lockBtn.addEventListener('click', (e) => {
        e.preventDefault();
        logout();
      });
    }

    function updateUserBadge(session) {
      if (userBadge) {
        userBadge.textContent = (session.label || session.username).toUpperCase();
        userBadge.style.color = 'rgb(var(--c-yellow))';
      }
      if (curatorBtn) {
        curatorBtn.style.display = session.role === 'curator' ? 'inline-flex' : 'none';
      }
    }
  }

  return {
    checkSession,
    login,
    logout,
    initUI
  };
})();

window.AuthManager = AuthManager;
