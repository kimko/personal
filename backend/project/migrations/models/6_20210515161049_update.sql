-- upgrade --
ALTER TABLE "resume" ADD "summary" JSONB NOT NULL;
-- downgrade --
ALTER TABLE "resume" DROP COLUMN "summary";
