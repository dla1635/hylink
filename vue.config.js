module.exports = { 
  "outputDir": "dist",
  "assetsDir": "static",
  "devServer": {
    "proxy": {
      "/api*": {
        "target": "http://localhost:8000/"
      },
      '/auth': {
        "target": 'http://localhost:8000/',
      }
    }
  },
  "transpileDependencies": [
    "vuetify"
  ]
}