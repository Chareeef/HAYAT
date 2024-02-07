// NAVLINKS ACTIVE CLASS

let section = document.querySelectorAll('section');
let navLink = document.querySelectorAll('header nav a');

window.onscroll = () => {
    section.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id')

        if (top >= offset && top < offset + height) {
            navLink.forEach(links => {
                links.classList.remove('active')
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active')
            });
        };
    });
};

// NAVBAR RESPONSIVENESS TOGGLE

const toggleButton = document.querySelector('.toggle_btn');
const header = document.querySelector('#header');
const toggleBtnIcon = document.querySelector('.toggle_btn');

toggleButton.onclick = function () {
    header.classList.toggle('responsive');
    const isOpen = header.classList.contains('responsive');

    toggleBtnIcon.innerHTML = isOpen ? '&cross;' : '&backcong;';
};


// BACK TO TOP BUTTON

var backToTopButton = document.getElementById("backToTopBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    backToTopButton.style.display = "block";
  } else {
    backToTopButton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
backToTopButton.onclick = function() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
};
