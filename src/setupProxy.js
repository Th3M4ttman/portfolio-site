const {createProxyMiddleware} = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/API',
    createProxyMiddleware({
      target: 'https://matt-harris-portfolio.herokuapp.com:5000/API/',
      changeOrigin: true,
    })
  );
};