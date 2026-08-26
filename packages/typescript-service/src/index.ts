import lodash from "lodash";
import { z } from "zod";

const ConfigSchema = z.object({
  environment: z.enum(["development", "staging", "production"]),
  port: z.number().int().positive(),
  debug: z.boolean().default(false),
});

type Config = z.infer<typeof ConfigSchema>;

const appConfig: Config = ConfigSchema.parse({
  environment: process.env.NODE_ENV || "development",
  port: parseInt(process.env.PORT || "8080", 10),
  debug: process.env.DEBUG === "true",
});

console.log("🚀 typescript-service initialized with configuration:");
console.log(JSON.stringify(appConfig, null, 2));

const items = [1, 2, 3, 4, 5];
const shuffled = lodash.shuffle(items);
console.log(`🎲 Shuffled items using lodash: ${shuffled.join(", ")}`);
