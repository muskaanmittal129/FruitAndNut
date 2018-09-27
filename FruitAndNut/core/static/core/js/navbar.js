var navbar = document.getElementById("navbarContent");
var links = navbar.getElementsByClassName("nav-item");
for (var i = 0; i < links.length; i++) {
  links[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
