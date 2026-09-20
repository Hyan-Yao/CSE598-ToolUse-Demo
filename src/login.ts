import { hashPassword, verify } from "./hash.ts";
import { create } from "./session.ts";
import type { Session } from "./session.ts";

interface User {
  name: string;
  hash: string;
}

const users = new Map<string, User>([
  ["alice", { name: "alice", hash: hashPassword("correct horse battery staple") }],
  ["bob", { name: "bob", hash: hashPassword("hunter2") }],
]);

export function login(username: string, pw: string): Session | null {
  const user = users.get(username);
  if (!user || !pw) return null;
  if (!verify(user.hash, pw)) return null;
  return create(user.name);
}
