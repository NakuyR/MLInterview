def returnJs():
    return """
<script>
window.onload = function() {
    var logo = top.document.getElementsByClassName("u-image u-logo u-image-1")[0];
    logo.addEventListener("click", ()=> {top.document.getElementsByClassName('css-qbe2hs edgvbvh1')[0].click()});

    var menuBar = top.document.getElementsByClassName("u-button-style u-nav-link");
    menuBar[1].addEventListener("click", ()=> {top.document.getElementsByClassName('css-qbe2hs edgvbvh1')[0].click()});
    menuBar[2].addEventListener("click", ()=> {top.document.getElementsByClassName('css-qbe2hs edgvbvh1')[1].click()});
    menuBar[3].addEventListener("click", ()=> {top.document.getElementsByClassName('css-qbe2hs edgvbvh1')[2].click()});

    menuBar[4].addEventListener("click", ()=> {top.document.getElementsByClassName('css-qbe2hs edgvbvh1')[0].click()});
    menuBar[5].addEventListener("click", ()=> {top.document.getElementsByClassName('css-qbe2hs edgvbvh1')[1].click()});
    menuBar[6].addEventListener("click", ()=> {top.document.getElementsByClassName('css-qbe2hs edgvbvh1')[2].click()});
}
</script>"""