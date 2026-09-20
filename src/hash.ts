import { createHash, timingSafeEqual } from "node:crypto";

export function hashPassword(pw: string): string {
  return createHash("sha256").update(pw).digest("hex");
}

/** Check a plaintext password against a stored hash: verify(password, storedHash). */
export function verify(pw: string, hash: string): boolean {
  const a = Buffer.from(hashPassword(pw), "hex");
  const b = Buffer.from(hash, "hex");
  return a.length === b.length && timingSafeEqual(a, b);
}
