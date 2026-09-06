# Aesthetic Gemini Scrapbook & Travel Diary

This is a secure, production-ready AI application deployed on Google Cloud Run for the Hack2Skill Ideathon. 

## Features (Phase 3)
**AI Aesthetic Memory Architect:** Users log raw travel text, and Gemini automatically structures it into beautiful scrapbook pages, suggesting optimal photo placements, color palettes, and miniature aesthetic embellishments.

## Architecture & Security
* **Authentication:** Firebase Auth with backend JWT verification.
* **Database:** Firestore with strict User-Isolation rules.
* **Secrets:** Google Cloud Secret Manager handles the `GEMINI_API_KEY`.
* **Hosting:** Containerized via Docker and deployed on Google Cloud Run.

## Deployment Steps
1. Connect this repository to Google Cloud Run.
2. Select "Continuously deploy from a repository".
3. Point to the `Dockerfile`.
4. Allow unauthenticated invocations for public web access.
5. Bind the `GEMINI_API_KEY` via Google Cloud Secret Manager.
