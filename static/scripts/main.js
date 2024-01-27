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

// const toggleButton = document.getElementsByClassName('toggle_btn')
// const navMenu = document.getElementsByClassName('menu')
// const header = document.getElementsByTagName('header')
// const loginBtn = document.getElementsByClassName('toggle_btn')

// toggleButton.addEventListener('click', () => {
//     navMenu.classList.toggle('responsive')
//     header.classList.toggle('responsive')
//     loginBtn.classList.toggle('responsive')
// })

const toggleButton = document.querySelector('toggle_btn')
const navMenu = document.querySelector('menu')
const header = document.querySelector('header')
const loginBtn = document.gquerySelector('toggle_btn')


toggleButton.onclick = function () {
    // navMenu.classList.toggle('responsive')
    header.classList.toggle('responsive')
    // loginBtn.classList.toggle('responsive')
}


