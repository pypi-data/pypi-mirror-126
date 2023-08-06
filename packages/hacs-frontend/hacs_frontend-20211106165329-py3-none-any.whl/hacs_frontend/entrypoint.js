
try {
  new Function("import('/hacsfiles/frontend/main-5345dc77.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-5345dc77.js';
  document.body.appendChild(el);
}
  