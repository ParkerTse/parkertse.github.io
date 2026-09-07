(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var tabs = document.querySelectorAll(".tab");
    var panels = document.querySelectorAll(".tab-panel");
    var indicator = document.querySelector(".tab-indicator");

    if (!tabs.length || !indicator) return;

    function moveIndicator(tab) {
      indicator.style.width = tab.offsetWidth + "px";
      indicator.style.transform = "translateX(" + tab.offsetLeft + "px)";
    }

    function activate(tab) {
      tabs.forEach(function (t) {
        var isActive = t === tab;
        t.classList.toggle("active", isActive);
        t.setAttribute("aria-selected", String(isActive));
        t.tabIndex = isActive ? 0 : -1;
      });
      panels.forEach(function (panel) {
        panel.hidden = panel.id !== tab.getAttribute("aria-controls");
      });
      moveIndicator(tab);
      tab.scrollIntoView({ block: "nearest", inline: "nearest" });
    }

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        activate(tab);
      });
    });

    window.addEventListener("resize", function () {
      var active = document.querySelector(".tab.active");
      if (active) moveIndicator(active);
    });

    moveIndicator(document.querySelector(".tab.active") || tabs[0]);
  });
})();
