import { z } from 'zod';

export const userSchema = z.object({
  id: z.number(),
  uuid: z.string(),
  email: z.string(),
});

export type User = z.infer<typeof userSchema>;
