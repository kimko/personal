-- upgrade --
ALTER TABLE "resume" RENAME COLUMN "shortDescription" TO "short_description";
-- downgrade --
ALTER TABLE "resume" RENAME COLUMN "short_description" TO "shortDescription";
