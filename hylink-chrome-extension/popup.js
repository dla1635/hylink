
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
  // document.cookie = 'cross-site-cookie=bar; SameSite=None; Secure';
  console.log("login");

  var postUrl = "http://13d31f75.ngrok.io/auth/login/";
  var xhr = new XMLHttpRequest();
  xhr.open('POST', postUrl, true);
  var email = encodeURIComponent(document.getElementById("email").value);
  var password = encodeURIComponent(document.getElementById("password").value);;
  var params = 'email=' + email + '&password=' + password
  params = params.replace(/%20/g, '+');

  xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

  // Handle request state change events
  xhr.onreadystatechange = function() { 
    // If the request completed
    if (xhr.readyState == 4) {
      console.log('ready');
      if (xhr.status == 200) {
        // 로그인 완료 처리
        // console.log("end");
        // localStorage.setItem("TOKEN_STORAGE_KEY","savingval")
        var json = JSON.parse(xhr.response);
        // localStorage.setItem("TOKEN_STORAGE_KEY",JSON.stringify(json));
        console.log(xhr.getAllResponseHeaders());
        
        if (xhr.getAllResponseHeaders().indexOf("csrftoken") >= 0) {
          console.log("have");
          console.log("header:", xhr.getResponseHeader("csrftoken"));
          var header = xhr.getResponseHeader('csrftoken');
        }

        console.log("abcd");
        console.log(header);
        localStorage.setItem("userId",json.user.email);
        localStorage.setItem("TOKEN_STORAGE_KEY",JSON.stringify(json));
        alert("로그인완료");
        document.getElementById('loginform').style.display='none';
        document.getElementById('linkform').style.display='block';
        // window.setTimeout(window.close, 1000);
      } else {
        // Show what went wrong
        console.log('Error login: ',xhr.statusText);
        // alert("error");      
        }
      }
  };

  // Send the request and set status
  xhr.send(params);

}

function addlink(){
  console.log("addlink");
  var postUrl = "http://13d31f75.ngrok.io/api/exlink/";
  // var csrftoken = getCookie('csrftoken');
  
  // print("csrf:",csrftoken);
  var xhr = new XMLHttpRequest();
  xhr.open('POST', postUrl, true);
  var linkurl = encodeURIComponent(document.getElementById("url").value);
  console.log(linkurl);
  var json = JSON.parse(localStorage.getItem("TOKEN_STORAGE_KEY"))
 
  linkurl = linkurl.replace(/%20/g, '+');
  var title= "";
  var thumbnail= "";
  var summary= "";
  var sharable= null;
  var params= "email="+json.user.email+"&url=" + linkurl+"&title=" + title+"&thumbnail=" + thumbnail+"&summary=" + summary+"&sharable=" + sharable;  
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
  // console.log(params);
  // console.log(JSON.stringify(params))
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
        // window.setTimeout(window.close, 1000);
              
      }else{
        console.log(xhr.statusText);
      }
    }
  };
  xhr.send(params);
}

function addlinkGet(){
  console.log("addlink by get");
  var getUrl = "http://13d31f75.ngrok.io/api/exlink/";

  var xhr = new XMLHttpRequest();
  xhr.open('GET', getUrl, false);
  var linkurl = encodeURIComponent(document.getElementById("url").value);
  console.log(linkurl);
  var json = JSON.parse(localStorage.getItem("TOKEN_STORAGE_KEY"))
  
  var params= "email="+json.user.email+"&url=" + linkurl;  
  params = params.replace(/%20/g, '+');
  
  console.log(params);
  xhr.send(params);

}

// chrome.tabs.executeScript({
//   code: 'performance.getEntriesByType("resource").map(e => e.name)',
// }, data => {
//   if (chrome.runtime.lastError || !data || !data[0]) return;
  
//   const urls = data[0].map(url => url.split(/[#?]/)[0]);
 
//   const uniqueUrls = [...new Set(urls).values()].filter(Boolean);

//   Promise.all(
//     uniqueUrls.map(url =>
//       new Promise(resolve => {
//         chrome.cookies.getAll({url}, resolve);
//       })
//     )
//   ).then(results => {
//     // convert the array of arrays into a deduplicated flat array of cookies
//     const cookies = [
//       ...new Map(
//         [].concat(...results)
//           .map(c => [JSON.stringify(c), c])
//       ).values()
//     ];

//     // do something with the cookies here
//     console.log(uniqueUrls, cookies);
//   });
// });


// function getCookie(name) {
//   var cookieValue = null;
//   if (document.cookie && document.cookie !== '') {
//     console.log("A");
//       var cookies = document.cookie.split(';');
//       for (var i = 0; i < cookies.length; i++) {
//           var cookie = cookies[i].trim();
//           // Does this cookie string begin with the name we want?
//           if (cookie.substring(0, name.length + 1) === (name + '=')) {
//               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//               break;
//           }
//       }
//   }else{
    

//   }
//   console.log("B");
//   return cookieValue;
// }

// var setCookie = function(name, value, exp) {
//   var date = new Date();
//   date.setTime(date.getTime() + exp*24*60*60*1000);
//   document.cookie = name + '=' + value + ';expires=' + date.toUTCString() + ';path=/';
//   };
  
// var getCookie = function(name) {
//   var value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
//   return value? value[2] : null;
//   };
  

window.addEventListener('load',function(evt){
  document.getElementById('loginButton').addEventListener('click', loginServer);
  document.getElementById('linkButton').addEventListener('click',addlink);
  document.getElementById('closePopUp').addEventListener('click', function(){
    window.close();
  });
  

})
