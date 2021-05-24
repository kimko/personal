-- upgrade --
ALTER TABLE "resume" ALTER COLUMN "public_id" TYPE VARCHAR(20) USING "public_id"::VARCHAR(20);
-- downgrade --
ALTER TABLE "resume" ALTER COLUMN "public_id" TYPE VARCHAR(6) USING "public_id"::VARCHAR(6);
