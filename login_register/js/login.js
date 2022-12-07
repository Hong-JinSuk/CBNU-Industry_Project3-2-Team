function login(){
    var id = document.querySelector('#id');
    var pw = document.querySelector('#pw');

    if(id.value == id.value||pw.value==pw.value){
        alert("cant login")
    }
    else{
        alert("로그인 되었습니다 !")
        location.href='admin.html';
    }
}

function back(){
    history.go(-1);
}
