
try {
  new Function("import('/hacsfiles/frontend/main-1e77a276.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-1e77a276.js';
  document.body.appendChild(el);
}
  