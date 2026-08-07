/**
 * Wild Roots Hemp - Shopify Theme JavaScript
 * Main theme functionality: mobile menu, scroll reveals, header effects
 */
(function() {
  'use strict';

  // ============================================
  // MOBILE MENU TOGGLE
  // ============================================
  const menuToggle = document.getElementById('menuToggle');
  const mobileNav = document.getElementById('mobileNav');

  function toggleMobileMenu() {
    if (!menuToggle || !mobileNav) return;
    menuToggle.classList.toggle('active');
    mobileNav.classList.toggle('active');
    const isOpen = mobileNav.classList.contains('active');
    menuToggle.setAttribute('aria-expanded', isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
  }

  if (menuToggle) {
    menuToggle.addEventListener('click', toggleMobileMenu);
  }

  // Close mobile menu on link click
  if (mobileNav) {
    const mobileLinks = mobileNav.querySelectorAll('a');
    mobileLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        if (mobileNav.classList.contains('active')) {
          toggleMobileMenu();
        }
      });
    });
  }

  // Close mobile menu on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && mobileNav && mobileNav.classList.contains('active')) {
      toggleMobileMenu();
    }
  });

  // Close mobile menu on resize to desktop
  window.addEventListener('resize', function() {
    if (window.innerWidth >= 768 && mobileNav && mobileNav.classList.contains('active')) {
      toggleMobileMenu();
    }
  });

  // ============================================
  // SCROLL-TRIGGERED SECTION REVEALS
  // ============================================
  const revealElements = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          revealObserver.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      rootMargin: '0px 0px -50px 0px',
      threshold: 0.1
    });

    revealElements.forEach(function(el) {
      revealObserver.observe(el);
    });
  } else {
    // Fallback for browsers without IntersectionObserver
    revealElements.forEach(function(el) {
      el.classList.add('active');
    });
  }

  // ============================================
  // SMOOTH SCROLL FOR ANCHOR LINKS
  // ============================================
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        const header = document.getElementById('header');
        const headerHeight = header ? header.offsetHeight : 80;
        const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // ============================================
  // HEADER SCROLL EFFECTS
  // ============================================
  const header = document.getElementById('header');
  let lastScrollY = 0;
  let ticking = false;

  function updateHeader() {
    if (!header) return;
    const scrollY = window.pageYOffset;

    // Add shadow when scrolled
    if (scrollY > 20) {
      header.style.boxShadow = '0 2px 20px rgba(45, 74, 62, 0.12)';
    } else {
      header.style.boxShadow = '0 2px 8px rgba(45, 74, 62, 0.08)';
    }

    lastScrollY = scrollY;
    ticking = false;
  }

  window.addEventListener('scroll', function() {
    if (!ticking) {
      requestAnimationFrame(updateHeader);
      ticking = true;
    }
  });

  // ============================================
  // HERO VIDEO HANDLING
  // ============================================
  const heroVideo = document.querySelector('.hero-banner video');
  if (heroVideo) {
    heroVideo.play().catch(function(error) {
      console.log('Autoplay prevented, showing poster image');
    });
  }

  // ============================================
  // INITIALIZE: Trigger reveals for visible elements
  // ============================================
  window.addEventListener('load', function() {
    revealElements.forEach(function(el) {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        el.classList.add('active');
      }
    });
  });

  console.log('Wild Roots Hemp theme loaded');

})();
