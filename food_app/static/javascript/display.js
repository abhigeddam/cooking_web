const Fav = (id, img, name) => {
  var x = window.location.href.split("api")[0];
  x = x + "db/" + "favoratie/?id=" + id + "&name=" + name + "&img=" + img;
  fetch(x);
};
const recipe = (id, img, name) => {
  var x = window.location.href.split("db")[0];
  x = x + "api/list/display/?id=" + id;
  x = x + "&image=" + img;
  x = x + "&name=" + name;
  window.location = x;
};
const cancelicon = (id) => {
  var x = document.getElementById(id);
  x.style.display = "flex";
};
