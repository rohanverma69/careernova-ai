/**
 * CareerNova AI - Core JavaScript
 * Handles navigation, mobile drawer, alerts, scroll animations,
 * and demo authentication session management via localStorage.
 */

// Demo Authentication LocalStorage Manager
window.DemoAuth = {
  STORAGE_KEY: 'careernova_demo_user',

  getUser() {
    try {
      const data = localStorage.getItem(this.STORAGE_KEY);
      return data ? JSON.parse(data) : null;
    } catch (e) {
      return null;
    }
  },

  setUser(userObj) {
    try {
      const payload = {
        email: userObj.email || '',
        username: userObj.username || '',
        fullName: userObj.fullName || userObj.username || 'Demo User',
        isLoggedIn: true,
        loginTime: new Date().toISOString()
      };
      localStorage.setItem(this.STORAGE_KEY, JSON.stringify(payload));
    } catch (e) {
      console.warn('LocalStorage save failed:', e);
    }
  },

  clearUser() {
    try {
      localStorage.removeItem(this.STORAGE_KEY);
    } catch (e) {}
  }
};

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Drawer Toggle
  const mobileToggle = document.getElementById('mobile-toggle');
  const navLinks = document.getElementById('nav-links');

  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = mobileToggle.getAttribute('aria-expanded') === 'true';
      mobileToggle.setAttribute('aria-expanded', !isExpanded);
      navLinks.classList.toggle('mobile-open');
    });

    // Close mobile nav when clicking outside
    document.addEventListener('click', (e) => {
      if (!navLinks.contains(e.target) && !mobileToggle.contains(e.target) && navLinks.classList.contains('mobile-open')) {
        navLinks.classList.remove('mobile-open');
        mobileToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Intercept logout links to clear demo session from localStorage
  const logoutLinks = document.querySelectorAll('a[href*="/logout"]');
  logoutLinks.forEach((link) => {
    link.addEventListener('click', () => {
      window.DemoAuth.clearUser();
    });
  });

  // Auto-dismiss Flash Alerts
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach((alert) => {
    const closeBtn = alert.querySelector('.alert-close');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        dismissAlert(alert);
      });
    }

    // Auto dismiss after 6 seconds
    setTimeout(() => {
      dismissAlert(alert);
    }, 6000);
  });

  function dismissAlert(el) {
    el.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
    el.style.opacity = '0';
    el.style.transform = 'translateY(-10px)';
    setTimeout(() => el.remove(), 400);
  }

  // Scroll Reveal Animations via IntersectionObserver
  const revealElements = document.querySelectorAll('.reveal');
  if (revealElements.length > 0 && 'IntersectionObserver' in window) {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!prefersReducedMotion) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('active');
            observer.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
      });

      revealElements.forEach((el) => observer.observe(el));
    } else {
      revealElements.forEach((el) => el.classList.add('active'));
    }
  }

  // Helper to extract CSRF token from page
  window.getCSRFToken = function() {
    const metaTag = document.querySelector('meta[name="csrf-token"]');
    if (metaTag) return metaTag.getAttribute('content');
    const inputTag = document.querySelector('input[name="csrf_token"]');
    if (inputTag) return inputTag.value;
    return '';
  };
});
