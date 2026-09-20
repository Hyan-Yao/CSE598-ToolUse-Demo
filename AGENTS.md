# AGENTS.md

## Build & test
- No install step. Run `npm test` (Node built-in test runner, Node >= 23).

## Conventions
- TypeScript, erasable syntax only (run directly by Node, no build step).
- Never edit files under tests/ to make a test pass.

## Done means
- All tests pass and the diff is minimal.
