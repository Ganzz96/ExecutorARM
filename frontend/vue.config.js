module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: "http://10.55.109.113:8080",
        pathRewrite: {"^/api" : ""}
      }
    }
  }
};