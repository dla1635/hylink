
// 익스탠션 클릭시 현재탭 링크가 입력폼에 들어감
chrome.tabs.getSelected(null, function(tab) {
  // TOKEN_STORAGE_KEY있으면 로그인 된거
  // if(tab.url.search("http")>=0){
  //   document.getElementById('url').setAttribute("value",tab.url);
  // }
  if(localStorage.getItem("TOKEN_STORAGE_KEY") === null){
    // 로그인 정보가 없다면
    document.getElementById('loginform').style.display='block';
    document.getElementById('linkform').style.display='none';
  }else if(localStorage.getItem("TOKEN_STORAGE_KEY") != null){
    // 로그인 정보가 있다면
    document.getElementById('loginform').style.display='none';
    document.getElementById('linkform').style.display='block';
    if(tab.url.search("http")>=0){
      document.getElementById('inputURL').setAttribute("value",tab.url);
    }
  }else{
    document.getElementById('loginform').style.display='block';
    document.getElementById('linkform').style.display='none';
  }
});


function login(){
  var postUrl = "127.0.0.1:8000/auth/login/";
  var xhr = new XMLHttpRequest();
  xhr.open('POST', postUrl, true);
  
  var id = encodeURIComponent(document.getElementById("email").value);
  var password = encodeURIComponent(document.getElementById("password").value);;
  var params = 'id=' + id + '&password=' + password
  params = params.replace(/%20/g, '+');
}

window.addEventListener('load',function(evt){
  document.getElementById('loginform').addEventListener('submit', loginform);
  document.getElementById('closePopUp').addEventListener('click', function(){
    window.close();
  });
  

})
