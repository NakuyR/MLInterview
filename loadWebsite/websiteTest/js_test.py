def returnJs():
    return """
<script>
window.addEventListener('load', function() {
    setTimeout(function(){
        var textArea = top.document.getElementsByClassName("stTextArea");
        var ta = top.document.getElementsByClassName("st-bc st-bx st-by st-bz st-c0 st-c1 st-c2 st-c3 st-c4 st-c5 st-c6 st-b7 st-c7 st-c8 st-c9 st-ca st-cb st-cc st-cd st-ae st-af st-ag st-ah st-ai st-aj st-bw st-ce st-cf st-cg st-ch st-ci");

        console.log(textArea.length);
        console.log(ta.length);

        for (let i=0; i<textArea.length; i++) {
            textArea[i].style = "";
            ta[i].placeholder = "질문에 대한 답변을 적어주세요";
        }
    }, 10);
})
</script>"""