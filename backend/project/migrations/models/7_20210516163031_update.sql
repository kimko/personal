-- upgrade --
ALTER TABLE "resume" ADD "jobs" JSONB;
-- downgrade --
ALTER TABLE "resume" DROP COLUMN "jobs";
