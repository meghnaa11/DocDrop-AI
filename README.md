# DocDrop-AI

## Current status
- Supabase project: `https://fhzrdodpjivnzmslonoy.supabase.co`
- Auth: Email OTP / magic-link flow enabled via redirect allowlist
- Storage bucket: `documents` (private)
- DB schema: `supabase/migrations/0001_init.sql` applied in Supabase SQL editor

## Repo layout (early)
- `backend/`: FastAPI API (coming next)
- `frontend/`: React (Vite) app (coming next)
- `supabase/migrations/`: database migrations (source of truth)

## Next step
Scaffold the FastAPI backend skeleton (`/health`, env config), then scaffold the React app.
