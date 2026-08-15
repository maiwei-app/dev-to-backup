module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    // raise body max line length so release-please messages don't fail
    'body-max-line-length': [2, 'always', 200],
  },
  // ignore Release Please generated footers / messages
  ignores: [
    (commit) => /This PR was generated with Release Please/.test(commit),
  ],
};
