oninput = function(e) {
    let target = e.target;
    if (target.value == '') {
        target.parentElement.className = 'entry';
    } else {
        target.parentElement.className = 'entry full';
    }
};
