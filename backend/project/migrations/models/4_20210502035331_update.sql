-- upgrade --
ALTER TABLE "resume" ADD "public_id" VARCHAR(6) NOT NULL UNIQUE;
-- downgrade --
ALTER TABLE "resume" DROP COLUMN "public_id";
