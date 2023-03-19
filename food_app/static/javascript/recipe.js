const recipe = (id, img, name) => {
  console.log(name);
  var x = window.location.href.split("?")[0];
  x = x + "display/?id=" + id;
  x = x + "&image=" + img;
  x = x + "&name=" + name;
  window.location = x;
};
const recipeinternal = (id, img, name) => {
  var x = window.location.href.split("?")[0];
  x = x + "display_internal/?id=" + id;
  x = x + "&image=" + img;
  x = x + "&name=" + name;
  window.location = x;
};
