const menuButton = document.querySelector(".menu-toggle");
const navigation = document.querySelector(".site-nav");

if (menuButton && navigation) {
  menuButton.addEventListener("click", () => {
    const isOpen = menuButton.getAttribute("aria-expanded") === "true";
    menuButton.setAttribute("aria-expanded", String(!isOpen));
    navigation.classList.toggle("is-open", !isOpen);
  });

  navigation.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      menuButton.setAttribute("aria-expanded", "false");
      navigation.classList.remove("is-open");
    }
  });
}

const year = document.querySelector("#year");
if (year) year.textContent = String(new Date().getFullYear());

const galleryFilters = document.querySelectorAll(".gallery-filter");
const hardwareCards = document.querySelectorAll(".hardware-card");
const galleryCount = document.querySelector(".gallery-count");

if (galleryFilters.length && hardwareCards.length && galleryCount) {
  galleryCount.textContent = `Showing ${hardwareCards.length} products`;

  galleryFilters.forEach((filter) => {
    filter.addEventListener("click", () => {
      const category = filter.dataset.filter;
      let visibleCount = 0;

      hardwareCards.forEach((card) => {
        const isVisible = category === "all" || card.dataset.category === category;
        card.hidden = !isVisible;
        if (isVisible) visibleCount += 1;
      });

      galleryFilters.forEach((button) => {
        const isActive = button === filter;
        button.classList.toggle("is-active", isActive);
        button.setAttribute("aria-pressed", String(isActive));
      });

      galleryCount.textContent = `Showing ${visibleCount} ${visibleCount === 1 ? "product" : "products"}`;
    });
  });
}
