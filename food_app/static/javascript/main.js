const filters = () => {
  var x = document.getElementById("filters");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
};

const contribute = () => {
  var x = document.getElementById("db-form");
  x.style.display = "flex";
};
window.onclick = function (event) {
  var x = document.getElementById("db-form");
  if (event.target == x) {
    x.style.display = "none";
  }
};
