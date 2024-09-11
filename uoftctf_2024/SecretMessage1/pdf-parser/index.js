import { getDocument } from "pdfjs-dist";

async function GetTextFromPDF(path) {
    let doc = await getDocument(path).promise;
    let page1 = await doc.getPage(1);
    let content = await page1.getTextContent();
    let strings = content.items.map(function(item) {
        return item.str;
    });
    return strings;
}

GetTextFromPDF('D:/Denis/Documents/CTF/uoftctf-2024/SecretMessage1/secret.pdf')
.then(data => console.log(data));