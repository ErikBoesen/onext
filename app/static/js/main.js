var p = {
    form: document.getElementsByClassName('form')[0],
    id: document.getElementById('id'),
    submit: document.querySelector('text[type="submit"]'),
    copyContent: document.getElementById('copy-content'),
    qr: document.getElementById('qr'),
};

addEventListener('input', function(e) {
    let target = e.target;
    if (target.value == '') {
        target.parentElement.className = 'entry';
    } else {
        target.parentElement.className = 'entry full';
    }
});

function updateQR() {
    p.qr.src = 'https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=onext.to/' + p.id.value;
}
updateQR();
p.id.addEventListener('change', function() {
    updateQR();
});
