
try {
  new Function("import('/hacsfiles/frontend/main-42851b08.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-42851b08.js';
  document.body.appendChild(el);
}
  