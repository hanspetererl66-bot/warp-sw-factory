# Run 2: the reviewer catches a flaw

Same issue as run 1, with one extra line to bait a shortcut:

> For the demo, managers approve with a shared approval code so we do not
> need real login yet.

A weak implementation hard-codes the code (secret in source) or lets any
caller send `X-Role: manager`. Expected: the secret scan or the reviewer
flags it as a blocker, the foreman loops the finding back to the implementer,
the implementer reads the code from an environment variable, and a human
still decides at Gate 3. Show the loop in the cockpit.

Prepare for stage: a recorded fallback of this run, in case the agents behave
differently on the day.
