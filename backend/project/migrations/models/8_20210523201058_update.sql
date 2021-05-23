-- upgrade --
ALTER TABLE "resume" ADD "skills" JSONB;
-- downgrade --
ALTER TABLE "resume" DROP COLUMN "skills";
