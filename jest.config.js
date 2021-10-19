// eslint-disable-next-line node/no-extraneous-require
const semver = require('semver')

let vueVersion = 2
try {
  // eslint-disable-next-line node/no-extraneous-require
  const Vue = require('vue/package.json')
  vueVersion = semver.major(Vue.version)
} catch (e) {}

let vueJest = null
try {
  vueJest = require.resolve(`vue-jest`)
} catch (e) {
  throw new Error(`Cannot resolve "vue-jest" module. Please make sure you have installed "vue-jest" as a dev dependency.`)
}

module.exports = {
  testEnvironment: 'jsdom',
  moduleFileExtensions: [
    'js',
    'jsx',
    'json',
    // tell Jest to handle *.vue files
    'vue'
  ],
  // support the same @ -> src alias mapping in source code
  moduleNameMapper: {
    '/^@\/(.*)$/': '<rootDir>/src/$1'
  },
  transformIgnorePatterns: ['/node_modules/(?!(vue-loading-overlay)/)'],
  transform: {
    // process *.vue files with vue-jest
    '^.+\\.(ts|tsx|js|jsx)$': '<rootDir>/node_modules/babel-jest',
    '^.+\\.vue$': vueJest,
    '.+\\.(css|styl|less|sass|scss|jpg|jpeg|png|svg|gif|eot|otf|webp|ttf|woff|woff2|mp4|webm|wav|mp3|m4a|aac|oga|avif)$':
        require.resolve('jest-transform-stub'),
  },
  // serializer for snapshots
  snapshotSerializers: [
    'jest-serializer-vue'
  ],
  testMatch: [
    '!node_modules/',
      '**/*.test.js'
  ],
  // https://github.com/facebook/jest/issues/6766
  testURL: 'http://localhost/',
  watchPlugins: [
    require.resolve('jest-watch-typeahead/filename'),
    require.resolve('jest-watch-typeahead/testname')
  ],
  setupFiles: ['<rootDir>/src/tests/setup.js'],
  collectCoverage: true,
  testResultsProcessor: 'jest-teamcity-reporter'
}
