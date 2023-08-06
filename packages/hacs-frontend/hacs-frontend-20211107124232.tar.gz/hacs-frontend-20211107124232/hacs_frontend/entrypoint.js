
try {
  new Function("import('/hacsfiles/frontend/main-1c1ea4cd.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-1c1ea4cd.js';
  document.body.appendChild(el);
}
  