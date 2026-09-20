import { test } from "node:test";
import assert from "node:assert/strict";
import { login } from "../src/login.ts";

test("login accepts a valid password", () => {
  const s = login("alice", "correct horse battery staple");
  assert.ok(s, "expected a session for a valid password");
  assert.equal(s.user, "alice");
});
test("login rejects a wrong password", () => assert.equal(login("alice", "wrong"), null));
test("login rejects an unknown user", () => assert.equal(login("mallory", "hunter2"), null));
test("login rejects an empty password", () => assert.equal(login("bob", ""), null));
test("login is case-sensitive on username", () => assert.equal(login("Alice", "correct horse battery staple"), null));
