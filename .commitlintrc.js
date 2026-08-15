module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    // raise body max line length so release-please messages don't fail
    'body-max-line-length': [2, 'always', 200],
  },
  // ignore Release Please related messages, customizations, and own bot trailers
  ignores: [
    (commit) => /Release Please|release-please|Co-authored-by: maibot-app/i.test(commit),
  ],
};
