let tabla = document.querySelector("#tabla");
let form = document.querySelector("form");

form.addEventListener('submit', (e) => {
    e.preventDefault();
    fetch(form.action, {
        method: form.method,
        body: new URLSearchParams(new FormData(form))
    }).then(response => response.json())
    .then(data => renderizar(data))
}, false);


function renderizar(data) {
    var content = '<thead class="head"><tr><th>Entity Group</th><th>Word</th><th>Score</th></tr></thead><tbody>'
    data.forEach(Mateo => {
        content += `<tr><td>${Mateo.entity}</td><td>${Mateo.word}</td><td>${Mateo.score}</td></tr>`
    })    
    content += '</tbody></table><br><h3>Pretty Cool Right ヽ(°◇° )ノ</p>'
    tabla.innerHTML = content;
}