function create_id(){
    var id = document.querySelector('#id');
    var pw = document.querySelector('#pw');
    var a_pw = document.querySelector('#a_pw');
    if(id.value==""||pw.value==""||a_pw.value==""){
        alert("cant account")
    }
    else{
        if(pw.value!==a_pw.value){
            alert("cant account")
        }
        else{
            alert("회원가입 되었습니다 !")
        }
    }
}

function back(){
    history.go(-1);
}