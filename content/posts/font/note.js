// script to extract values from icomoon demo.html file
let els, out;
els = document.getElementsByClassName('unitRight');
out = '';
for (a of els) {
  if (!a.value.match(/[0-9]{2}/g)) {
    out.concat(`| ${a.value}`);
    console.log(a.value);
  }
}
console.log(out);
