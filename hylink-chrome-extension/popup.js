
// 익스탠션 클릭시 현재탭 링크가 입력폼에 들어감
chrome.tabs.getSelected(null, function(tab) {
  // TOKEN_STORAGE_KEY있으면 로그인 된거
  if(localStorage.getItem("TOKEN_STORAGE_KEY") === null){
    // 로그인 정보가 없다면
    document.getElementById('login-form').style.display='block';
    document.getElementById('link-form').style.display='none';
  }else if(localStorage.getItem("TOKEN_STORAGE_KEY") != null){
    // 로그인 정보가 있다면
    document.getElementById('login-form').style.display='none';
    document.getElementById('link-form').style.display='block';
    if(tab.url.search("http")>=0){
      document.getElementById('inputURL').setAttribute("value",tab.url);
    }
  }else{
    document.getElementById('login-form').style.display='block';
    document.getElementById('link-form').style.display='none';
  }
  
});
