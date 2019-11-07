<template>
    <section>
        <v-layout
          column
          wrap
          class="my-5"
          align-center
        >
          <v-flex xs12 sm4 text-xs-center class="my-5">
              <h2 class="headline">The best way to share your amazing stuff</h2>
              <p class="subheading text-center">
                No more restrictions, no more limits
              </p>
          </v-flex>
          <v-flex xs12 mt-5>
            <v-container grid-list-xl>
              <v-layout row wrap align-center>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-center">
                      <v-icon x-large class="blue--text text--lighten-2">public</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">편리한 기능</div>
                    </v-card-title>
                    <v-card-text class="text-center">
                      링크의 내용을 한눈에 파악한다! <br> 저희는 링크 입력만으로 <br> 
                      <strong>제목</strong>, <strong>내용(3줄 요약)</strong>, <strong>썸네일</strong>, <strong>태그</strong>를
                      <br> 자동으로 뽑아 카드로 만들어드립니다.
                      <br> <strong>라벨</strong>을 직접 만들어서 관리할 수 있습니다! 
                    </v-card-text>
                  </v-card>
                </v-flex>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-center">
                      <v-icon x-large class="blue--text text--lighten-2">flash_on</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline">빠른 검색</div>
                    </v-card-title>
                    <v-card-text class="text-center">
                      북마크를 헤매던 고객님!
                      <br> 태그와 라벨, 제목, 내용을 바탕으로 
                      <br> 빠르게 원하는 링크를 <strong>검색</strong>합니다.
                      <br> 화면에서 썸네일과 제목 등 원하는 정보만 
                      <br> 선택해서 볼 수 있게 필터링도 가능합니다!  
                    </v-card-text>
                  </v-card>
                </v-flex>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-center">
                      <v-icon x-large class="blue--text text--lighten-2">share</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">나만의 링크 모음</div>
                    </v-card-title>
                    <v-card-text class="text-center">
                      AI 공부를 위한 링크 모음! 
                      <br> 링크를 하나씩 복붙할 필요가 없습니다. 
                      <br> 블로그 게시글을 작성할 필요 없습니다. 
                      <br> 간단하게 원하는 링크 묶음을 <strong>공유</strong>하세요! 
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </section>
</template>

<script>
export default {
    name: 'Service',

}
</script>