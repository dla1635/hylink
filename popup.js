
chrome.tabs.getSelected(null, function(tab) {
  
  if(tab.url.search("http")>=0){
    document.getElementById('inputURL').setAttribute("value",tab.url);
  }
  
});
