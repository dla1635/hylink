# FrontEnd

## 폴더구조 

'''
src
├ assets			// img, font, css 등 모든 자원 
   ├ css		
       └ main.css
   ├ font
   └ img
├ commons		// 모든 js 코드
   ├ directives
   ├ fucntions
   ├ resources
   └ validations
├ config			// router를 비롯한 플러그인 config 파일들
   └ routers.js
├ shared-components	// 한개 이상의 페이지에서 사용되는 컴포넌트
   ├ SideBar.vue
   └ AppBar.vue   
├ spa			// 페이지 단위 폴더들로 구성, 각 폴더에는 해당 페이지를 구성하는 컴포넌트
   ├ Home
      └ Home.vue				
   ├ Main
      └ Main.vue				
   └ Community
      └ Community.vue	
├ vuex			// vuex store파일과 모듈 폴더
   ├ store.js
   └ modules		// vuex 모듈 파일
      └ layout.js 
├ App.vue
└ main.js
'''

참고 : https://medium.com/tldr-tech/vue-js-2-vuex-router-yarn-basic-configuration-version-2-7b9c489d43b3