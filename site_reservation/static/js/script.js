

    AOS.init({
        duration: 1200, // duration of animations
        easing: 'ease-in-out', // easing function
        once: true // whether animations should happen only once
    });




    gsap.from(".animate", {
        duration: 1.5,
        opacity: 0,
        y: 50,
        stagger: 0.3
    });



    document.addEventListener('DOMContentLoaded', function() {
        const loginBtn = document.querySelector('a[href="#login"]');
        const modal = document.getElementById('loginModal');
        const closeModal = document.getElementById('closeModal');

        // Afficher le modal
        loginBtn.addEventListener('click', function(e) {
            e.preventDefault(); // Prévenir le comportement par défaut du lien
            modal.classList.remove('hidden');
        });

        // Fermer le modal
        closeModal.addEventListener('click', function() {
            modal.classList.add('hidden');
        });

        // Fermer le modal en cliquant en dehors de la boîte
        window.addEventListener('click', function(event) {
            if (event.target === modal) {
                modal.classList.add('hidden');
            }
        });
    });

    document.addEventListener('DOMContentLoaded', function() {
        const loginBtn = document.getElementById('openLoginModal');
        const modal = document.getElementById('loginModal');
        const closeModal = document.getElementById('closeModal');

        // Afficher le modal
        loginBtn.addEventListener('click', function(e) {
            e.preventDefault(); // Prévenir le comportement par défaut du lien
            modal.classList.remove('hidden');
        });

        // Fermer le modal
        closeModal.addEventListener('click', function() {
            modal.classList.add('hidden');
        });

        // Fermer le modal en cliquant en dehors de la boîte
        window.addEventListener('click', function(event) {
            if (event.target === modal) {
                modal.classList.add('hidden');
            }
        });
    });

    document.addEventListener('DOMContentLoaded', function() {
        const typewriterText = document.getElementById('typewriterText');
        const text = typewriterText.textContent;
        typewriterText.textContent = ''; // Clear text content initially
    
        let index = 0;
    
        // Fonction pour écrire le texte
        function typeWriter() {
            if (index < text.length) {
                typewriterText.textContent += text.charAt(index);
                index++;
                setTimeout(typeWriter, 100); // Ajustez la vitesse de frappe ici
            }
        }
    
        // Démarrer l'effet de machine à écrire
        typeWriter();
    
        // Gestion du modal
        const openLoginModal = document.getElementById('openLoginModal');
        const loginModal = document.getElementById('loginModal');
        const closeModal = document.getElementById('closeModal');
    
        openLoginModal.addEventListener('click', function(e) {
            e.preventDefault();
            loginModal.classList.remove('hidden');
        });
    
        closeModal.addEventListener('click', function() {
            loginModal.classList.add('hidden');
        });
    
        window.addEventListener('click', function(event) {
            if (event.target === loginModal) {
                loginModal.classList.add('hidden');
            }
        });
    });
    

    document.addEventListener('DOMContentLoaded', function () {
        const navbar = document.querySelector('nav');
        let lastScrollTop = 0;

        window.addEventListener('scroll', function () {
            const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

            if (currentScroll > lastScrollTop) {
                // Scrolling down
                navbar.classList.remove('navbar-visible');
                navbar.classList.add('navbar-hidden');
            } else {
                // Scrolling up
                navbar.classList.remove('navbar-hidden');
                navbar.classList.add('navbar-visible');
            }

            lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // For Mobile or negative scrolling
        });
    });


  // Initialize Swiper
  var swiper = new Swiper('.swiper-container', {
    loop: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

// Typewriter Effect
const typewriterText = document.getElementById('typewriterText');
const text = typewriterText.textContent;
typewriterText.textContent = '';
let i = 0;
const speed = 100; // Speed in milliseconds

function typeWriter() {
    if (i < text.length) {
        typewriterText.textContent += text.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}
typeWriter();

// Modal Handling
document.getElementById('openLoginModal').addEventListener('click', function() {
    document.getElementById('loginModal').classList.remove('hidden');
});

document.getElementById('closeModal').addEventListener('click', function() {
    document.getElementById('loginModal').classList.add('hidden');
});

// AOS Initialization
AOS.init();