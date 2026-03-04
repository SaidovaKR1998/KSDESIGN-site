// Инициализация AOS (анимации при скролле)
AOS.init({
    duration: 1000,
    once: true,
    offset: 100
});

// Навигация с изменением при скролле
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Плавный скролл к якорям
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Валидация формы
document.querySelector('form')?.addEventListener('submit', function(e) {
    const name = this.querySelector('input[name="name"]');
    const phone = this.querySelector('input[name="phone"]');
    const email = this.querySelector('input[name="email"]');

    if (name.value.trim() === '') {
        e.preventDefault();
        alert('Пожалуйста, введите имя');
        name.focus();
    } else if (phone.value.trim() === '') {
        e.preventDefault();
        alert('Пожалуйста, введите телефон');
        phone.focus();
    } else if (email.value.trim() === '') {
        e.preventDefault();
        alert('Пожалуйста, введите email');
        email.focus();
    }
});
