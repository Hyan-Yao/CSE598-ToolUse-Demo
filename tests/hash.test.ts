import { test } from "node:test";
import assert from "node:assert/strict";
import { hashPassword, verify } from "../src/hash.ts";

test("hash is deterministic", () => assert.equal(hashPassword("x"), hashPassword("x")));
test("hash differs for different input", () => assert.notEqual(hashPassword("x"), hashPassword("y")));
test("verify accepts the right password", () => assert.equal(verify("pw", hashPassword("pw")), true));
test("verify rejects the wrong password", () => assert.equal(verify("nope", hashPassword("pw")), false));
