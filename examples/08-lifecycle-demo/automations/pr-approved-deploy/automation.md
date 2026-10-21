---
triggers:
  - provider: github
    event: pull_request_labeled
    filter:
      repos: [hanspetererl66-bot/lifecycle-demo-app]
      labels: [approve-deploy]
---
A human merged this pull request and added the `approve-deploy` label. That
label is Gate 4. Verify the PR is merged and the label was added by a human,
then dispatch the deployer.
