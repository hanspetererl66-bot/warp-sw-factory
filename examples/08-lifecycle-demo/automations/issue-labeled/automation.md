---
triggers:
  - provider: github
    event: issue_labeled
    filter:
      repos: [hanspetererl66-bot/lifecycle-demo-app]
      labels: [factory-ready]
---
A maintainer labeled an issue `factory-ready`. Start the lifecycle at the
requirements stage and follow the stages and gates in your instructions.
