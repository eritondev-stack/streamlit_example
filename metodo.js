const iframes = parent.document.body.getElementsByTagName('iframe');
let container
for (const iframe of iframes) {
    if (iframe.srcdoc.indexOf("STREAMLIT-MODAL-IFRAME-{self.key}") !== -1) {
        container = iframe.parentNode.previousSibling;
        container.setAttribute('data-modal-container', 'true');
        container.setAttribute('key', '{self.key}');
        console.log(iframe)
    }
}
const para = document.createElement("p");
para.innerHTML = "Esse é um teste feito por mim manual, apenas com java script"
container.appendChild(para)