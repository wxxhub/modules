function $(obj){
    return document.getElementById(obj);
}

function sp(){
    var tex = $('input_text').value;
    var nun =tex.length;
    if (nun >= 1){
        $('submit_button').src="/static/image/send.jpg";
        $('submit_button').disabled="";
    }else{
        $('submit_button').src="/static/image/plus.jpg";
        $('submit_button').disabled="disabled";
    }
}