window.onscroll=function(){
    scrollRotate();
};
function scrollRotate(){
    let image = document.getElementById("reload");
    image.style.transform = "rotate(" + window.pageYOffset/2 + "deg)";
}

function print_time(){
    var userda = document.getElementById('user_data');
    var hourda = document.getElementById('hour_data');
    var minda = document.getElementById('min_data');
    
    if(userda != null && hourda != null && minda != null){
        alert(userda.value + ' 번 사용자 ' + hourda.value + ' 시간 ' + minda.value + ' 분 설정을 완료하였습니다 !');
    }
    
}
