document.querySelectorAll('.detailForm').forEach(item => {
    item.addEventListener("submit", function(e) {
        // Removing the XML declaration so that an attacker can inject it themselves
        let xmlPayload = payload(new FormData(this));

        // The original XML declaration is now part of the payload function,
        // and there's no additional validation or escaping, allowing for XXE injection.
        
        checkDetails(this.getAttribute("method"), this.getAttribute("action"), xmlPayload);
        e.preventDefault();
    });
});

function checkDetails(method, path, data) {
    fetch(path, {
        method,
        headers: { 'Content-Type': 'application/xml' },
        body: data
    })
    .then(res => res.text())
    .then(res => document.getElementById("detailsResult").innerHTML = res)
    .catch(e => console.error(e));
}

window.contentType = 'application/xml';

function payload(data) {
    // Construct the XML payload, allowing for any input to be included.
    var xml = '<?xml version="1.0" encoding="UTF-8"?>';
    xml += '<data>';

    for(var pair of data.entries()) {
        var key = pair[0];
        var value = pair[1];

        // Directly adding user input to the XML, which could include malicious content.
        xml += '<' + key + '>' + value + '</' + key + '>';
    }

    xml += '</data>';
    return xml;
}
