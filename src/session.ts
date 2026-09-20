import { randomBytes } from "node:crypto";

export interface Session {
  user: string;
  token: string;
  createdAt: number;
}

const sessions = new Map<string, Session>();

export function create(user: string): Session {
  const s = { user, token: randomBytes(16).toString("hex"), createdAt: Date.now() };
  sessions.set(s.token, s);
  return s;
}

export function get(token: string): Session | undefined {
  return sessions.get(token);
}

export function destroy(token: string): boolean {
  return sessions.delete(token);
}
