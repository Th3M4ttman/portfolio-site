const {createProxyMiddleware} = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/API',
    createProxyMiddleware({
      target: 'https://matt-harris-portfolio.Herokuapp.com:5000/',
      changeOrigin: true,
    })
  );
};