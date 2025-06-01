// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add active class to navbar links
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navLinks.forEach(navLink => navLink.classList.remove('active'));
        link.classList.add('active');
    });
});

// Initialize tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
});

// Form validation for service creation
const serviceForm = document.querySelector('#service-form');
if (serviceForm) {
    serviceForm.addEventListener('submit', function(e) {
        const title = document.querySelector('#id_title').value;
        const description = document.querySelector('#id_description').value;
        const rate = document.querySelector('#id_rate').value;

        if (!title || !description || !rate) {
            e.preventDefault();
            alert('Please fill in all required fields');
        }
    });
}
