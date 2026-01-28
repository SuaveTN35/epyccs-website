/**
 * EPYC Courier Service - Main JavaScript
 * Handles navigation, forms, and interactive elements
 */

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    initMobileMenu();

    // Smooth Scrolling for anchor links
    initSmoothScroll();

    // Header scroll behavior
    initHeaderScroll();

    // Form handling
    initForms();

    // Dropdown menus
    initDropdowns();

    // Set minimum date for date inputs
    initDateInputs();
});

/**
 * Mobile Menu
 */
function initMobileMenu() {
    const toggle = document.querySelector('.mobile-menu-toggle');
    const nav = document.querySelector('.nav');
    const body = document.body;

    if (!toggle || !nav) return;

    toggle.addEventListener('click', function() {
        toggle.classList.toggle('active');
        nav.classList.toggle('active');
        body.classList.toggle('menu-open');
    });

    // Close menu when clicking on a link
    const navLinks = nav.querySelectorAll('a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            toggle.classList.remove('active');
            nav.classList.remove('active');
            body.classList.remove('menu-open');
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!nav.contains(e.target) && !toggle.contains(e.target)) {
            toggle.classList.remove('active');
            nav.classList.remove('active');
            body.classList.remove('menu-open');
        }
    });
}

/**
 * Smooth Scrolling
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Header Scroll Behavior
 */
function initHeaderScroll() {
    const header = document.querySelector('.header');
    if (!header) return;

    let lastScroll = 0;

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;

        // Add shadow when scrolled
        if (currentScroll > 10) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        // Hide/show header on scroll (optional - uncomment if desired)
        // if (currentScroll > lastScroll && currentScroll > 100) {
        //     header.classList.add('hidden');
        // } else {
        //     header.classList.remove('hidden');
        // }

        lastScroll = currentScroll;
    });
}

/**
 * Dropdown Menus
 */
function initDropdowns() {
    const dropdowns = document.querySelectorAll('.has-dropdown');

    dropdowns.forEach(dropdown => {
        const link = dropdown.querySelector('a');
        const menu = dropdown.querySelector('.dropdown');

        if (!link || !menu) return;

        // Toggle on click for mobile
        link.addEventListener('click', function(e) {
            if (window.innerWidth <= 1024) {
                e.preventDefault();
                dropdown.classList.toggle('open');
            }
        });

        // Close when clicking outside
        document.addEventListener('click', function(e) {
            if (!dropdown.contains(e.target)) {
                dropdown.classList.remove('open');
            }
        });
    });
}

/**
 * Form Handling
 */
function initForms() {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            // Basic validation
            if (!validateForm(form)) {
                return;
            }

            // Collect form data
            const formData = new FormData(form);
            const data = Object.fromEntries(formData);

            // Show loading state
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;

            // Send to n8n webhook
            fetch('https://suavetn35.app.n8n.cloud/webhook/533d09d5-511e-41fb-b99a-8b0349cfafa6', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    name: data.name || '',
                    company: data.company || '',
                    email: data.email || '',
                    phone: data.phone || '',
                    service: data.service || '',
                    time: data.time || '',
                    pickup: data.pickup || '',
                    delivery: data.delivery || '',
                    size: data.size || '',
                    temperature: data.temperature ? 'Yes' : 'No',
                    recurring: data.recurring ? 'Yes' : 'No',
                    instructions: data.instructions || '',
                    source: 'Website Quote Form'
                })
            })
            .then(response => {
                // Show success message
                showFormMessage(form, 'success', 'Thank you! We\'ll contact you within 1 hour during business hours.');
                form.reset();
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            })
            .catch(error => {
                console.error('Form submission error:', error);
                showFormMessage(form, 'success', 'Thank you! We\'ll contact you within 1 hour during business hours.');
                form.reset();
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            });
        });
    });
}

/**
 * Form Validation
 */
function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');

    // Clear previous errors
    form.querySelectorAll('.error').forEach(el => el.classList.remove('error'));
    form.querySelectorAll('.error-message').forEach(el => el.remove());

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            field.classList.add('error');

            const errorMsg = document.createElement('span');
            errorMsg.className = 'error-message';
            errorMsg.textContent = 'This field is required';
            field.parentNode.appendChild(errorMsg);
        }

        // Email validation
        if (field.type === 'email' && field.value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(field.value)) {
                isValid = false;
                field.classList.add('error');

                const errorMsg = document.createElement('span');
                errorMsg.className = 'error-message';
                errorMsg.textContent = 'Please enter a valid email address';
                field.parentNode.appendChild(errorMsg);
            }
        }

        // Phone validation
        if (field.type === 'tel' && field.value) {
            const phoneRegex = /^[\d\s\-\(\)\+]{10,}$/;
            if (!phoneRegex.test(field.value)) {
                isValid = false;
                field.classList.add('error');

                const errorMsg = document.createElement('span');
                errorMsg.className = 'error-message';
                errorMsg.textContent = 'Please enter a valid phone number';
                field.parentNode.appendChild(errorMsg);
            }
        }
    });

    return isValid;
}

/**
 * Show Form Message
 */
function showFormMessage(form, type, message) {
    // Remove existing messages
    const existingMsg = form.querySelector('.form-message');
    if (existingMsg) existingMsg.remove();

    // Create message element
    const msgEl = document.createElement('div');
    msgEl.className = `form-message form-message-${type}`;
    msgEl.textContent = message;

    // Insert at top of form
    form.insertBefore(msgEl, form.firstChild);

    // Scroll to message
    msgEl.scrollIntoView({ behavior: 'smooth', block: 'center' });

    // Auto-remove after 10 seconds
    setTimeout(() => {
        msgEl.remove();
    }, 10000);
}

/**
 * Initialize Date Inputs
 */
function initDateInputs() {
    const dateInputs = document.querySelectorAll('input[type="date"]');
    const today = new Date().toISOString().split('T')[0];

    dateInputs.forEach(input => {
        input.setAttribute('min', today);
        if (!input.value) {
            input.value = today;
        }
    });
}

/**
 * Animate elements on scroll (optional enhancement)
 */
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    document.querySelectorAll('.service-card, .feature-item, .testimonial-card, .stat-item').forEach(el => {
        observer.observe(el);
    });
}

/**
 * Phone number formatting
 */
function formatPhoneNumber(input) {
    let value = input.value.replace(/\D/g, '');
    if (value.length > 10) value = value.slice(0, 10);

    if (value.length >= 6) {
        value = `(${value.slice(0, 3)}) ${value.slice(3, 6)}-${value.slice(6)}`;
    } else if (value.length >= 3) {
        value = `(${value.slice(0, 3)}) ${value.slice(3)}`;
    }

    input.value = value;
}

// Add phone formatting to phone inputs
document.querySelectorAll('input[type="tel"]').forEach(input => {
    input.addEventListener('input', function() {
        formatPhoneNumber(this);
    });
});
