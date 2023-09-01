module.exports = {
  configureWebpack: (config) => {
    config.resolve.fallback = {
      stream: require.resolve('stream-browserify'),
      buffer: require.resolve('buffer'),
    };
  },
};
