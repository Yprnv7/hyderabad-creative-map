/* ==========================================================================
   DECCAN CANVAS — Authentication & Session Manager
   Supports Member Access & Curator Roles with Local Persistence
   ========================================================================== */

const AuthManager = (() => {
  const STORAGE_KEY = 'deccan_canvas_auth';
  
  // Valid Credentials Matrix
  const CREDENTIALS = {
    'member': {
      password: 'deccan2026',
      role: 'member',
      label: 'Creative Member'
    },
    'curator': {
      password: 'charminar99',
      role: 'curator',
      label: 'Deccan Curator'
    },
    'founder': {
      password: 'jubileehills',
      role: 'curator',
      label: 'Studio Founder'
    }
  };
  
  // Single passkey shortcuts
  const PASSKEYS = ['HYD-CREATIVE-2026', 'CHARMINAR99', 'DECCAN2026'];

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

  function login(usernameOrPasskey, password = '') {
    const cleanUser = (usernameOrPasskey || '').trim().toLowerCase();
    const cleanPass = (password || '').trim();

    // Check passkey first
    const upperPasskey = (usernameOrPasskey || '').trim().toUpperCase();
    if (PASSKEYS.includes(upperPasskey)) {
      const session = {
        username: 'member_passkey',
        role: upperPasskey === 'CHARMINAR99' ? 'curator' : 'member',
        loginTime: Date.now()
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(session));
      return { success: true, session };
    }

    // Check username & password
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
      error: 'Invalid credentials. Use member / deccan2026 or curator / charminar99.' 
    };
  }

  function logout() {
    localStorage.removeItem(STORAGE_KEY);
    const gate = document.getElementById('auth-gate');
    if (gate) {
      gate.classList.remove('unlocked');
      const errorMsg = document.getElementById('auth-error');
      if (errorMsg) errorMsg.classList.remove('visible');
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
      gate.classList.add('unlocked');
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
          gate.classList.add('unlocked');
          errorMsg.classList.remove('visible');
          updateUserBadge(res.session);
          if (typeof onUnlockCallback === 'function') onUnlockCallback(res.session);
        } else {
          errorMsg.textContent = res.error;
          errorMsg.classList.add('visible');
          passInput.value = '';
          passInput.focus();
        }
      });
    }

    if (lockBtn) {
      lockBtn.addEventListener('click', () => {
        logout();
      });
    }

    function updateUserBadge(session) {
      if (userBadge) {
        userBadge.textContent = session.role === 'curator' ? 'CURATOR' : 'MEMBER';
        userBadge.style.color = session.role === 'curator' ? 'var(--accent-heritage)' : 'var(--accent-cafe)';
      }
      if (curatorBtn) {
        curatorBtn.style.display = session.role === 'curator' ? 'flex' : 'none';
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
