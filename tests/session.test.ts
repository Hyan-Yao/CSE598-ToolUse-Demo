import { test } from "node:test";
import assert from "node:assert/strict";
import { create, get, destroy } from "../src/session.ts";

test("create returns a token", () => assert.match(create("alice").token, /^[0-9a-f]{32}$/));
test("get finds a live session", () => { const s = create("bob"); assert.equal(get(s.token)?.user, "bob"); });
test("destroy removes a session", () => { const s = create("bob"); destroy(s.token); assert.equal(get(s.token), undefined); });
