// This small script only improves the mobile menu.
// The website still works as normal static HTML if JavaScript is disabled.
const menuButton = document.querySelector(".nav-toggle");
const menu = document.querySelector("#main-menu");

if (menuButton && menu) {
  menuButton.addEventListener("click", () => {
    const isOpen = menu.classList.toggle("is-open");
    menuButton.setAttribute("aria-expanded", String(isOpen));
  });
}
