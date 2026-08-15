module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    // raise body max line length so release-please messages don't fail
    'body-max-line-length': [2, 'always', 200],
  },
  // ignore Release Please related messages and customizations
  ignores: [
    (commit) => /Release Please|release-please/i.test(commit),
  ],
};
