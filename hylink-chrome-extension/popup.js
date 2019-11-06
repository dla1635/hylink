
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
      document.getElementById('url').setAttribute("value",tab.url);
    }
  }else{
    document.getElementById('loginform').style.display='block';
    document.getElementById('linkform').style.display='none';
  }
});



function loginServer(){
  
  // alert("a")
  
  console.log("login");

  var postUrl = "http://localhost:8000/auth/login/";
  // alert("b")
  var xhr = new XMLHttpRequest();
  xhr.open('POST', postUrl, true);
  
  var email = encodeURIComponent(document.getElementById("email").value);
  var password = encodeURIComponent(document.getElementById("password").value);;
  var params = 'email=' + email + '&password=' + password
  params = params.replace(/%20/g, '+');

  // Set correct header for form data 
  // xhr.setRequestHeader('Content-type', 'application/json');
  xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  // alert("gogo");
  console.log("login",params);
  
  // Handle request state change events
  xhr.onreadystatechange = function() { 
    // If the request completed
    if (xhr.readyState == 4) {
          console.log('ready');
      if (xhr.status == 200) {
        // If it was a success, close the popup after a short delay
        // 로그인 완료 처리
              // console.log("end");
              // localStorage.setItem("TOKEN_STORAGE_KEY","savingval")
              var json = JSON.parse(xhr.response);
              // console.log(json.token);
              
              localStorage.setItem("TOKEN_STORAGE_KEY",JSON.stringify(json));
              // localStorage.setItem("userId",json.user.email);
              alert("로그인완료");
              window.setTimeout(window.close, 1000);
              
          } else {
              // Show what went wrong
              // console.log('Error login: ',xhr.statusText);
              // alert("error");
              
          }
      }else{
        // console.log(xhr.readyState);
        // alert("what?")
      }
  };

  // Send the request and set status
  xhr.send(params);

}

function addlink(){
  console.log("addlink");
  var postUrl = "http://localhost:8000/api/link/";
  // alert("b")
  var xhr = new XMLHttpRequest();
  xhr.open('POST', postUrl, true);
  var linkurl = encodeURIComponent(document.getElementById("url").value);
  console.log(linkurl);
  var json = JSON.parse(localStorage.getItem("TOKEN_STORAGE_KEY"))
  var user ={
    "email" : json.user.email, 
    "pk" : json.user.pk,
  }
  linkurl = linkurl.replace(/%20/g, '+');
  var title ="";
  var thumbnail ="";
  var summary="";
  var sharable=null;
  var params = "url="+ linkurl+"&token="+json.token + "&title="+title+"&thumbnail="+thumbnail+"&summary="+summary+"&sharable="+sharable+"&user={email="+json.user.email+"}";
  // var params = {
  //   user : {
  //     email : json.user.email, 
  //     pk : json.user.pk,
  //   },
  //   url : linkurl,
  //   token : json.token,
  //   title: "",
  //   thumbnail: "",
  //   summary: "",
  //   sharable: null
  // } 
  console.log(params);
  console.log(JSON.stringify(params));
  xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  // alert("gogo");
  // console.log("save",params);
  
  // Handle request state change events
  xhr.onreadystatechange = function() { 
    // If the request completed
    if (xhr.readyState == 4) {
          console.log('ready');
      if (xhr.status == 200) {
        
        console.log("end");
        alert("저장완료");
        window.setTimeout(window.close, 1000);
              
      }else{
        console.log(xhr.statusText);
      }
    }
  };
  xhr.send(params);


}

window.addEventListener('load',function(evt){
  document.getElementById('loginButton').addEventListener('click', loginServer);
  document.getElementById('linkButton').addEventListener('click',addlink);
  document.getElementById('closePopUp').addEventListener('click', function(){
    window.close();
  });
  

})
