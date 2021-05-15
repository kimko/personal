-- upgrade --
ALTER TABLE "resume" ADD "summary" JSONB;
-- downgrade --
ALTER TABLE "resume" DROP COLUMN "summary";
