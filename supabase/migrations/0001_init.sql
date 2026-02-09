-- DocDrop-AI initial schema (created manually in Supabase SQL editor)
-- Note: This file is the source of truth for reproducing the DB schema.

-- Enable UUID generation (often already enabled in Supabase)
create extension if not exists "pgcrypto";

create table if not exists public.documents (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null,
  filename text not null,
  storage_path text not null,
  mime_type text not null,
  size_bytes bigint not null,
  status text not null default 'ready',
  created_at timestamptz not null default now()
);

create index if not exists documents_user_id_idx on public.documents(user_id);
create index if not exists documents_created_at_idx on public.documents(created_at);

create table if not exists public.chunks (
  id uuid primary key default gen_random_uuid(),
  document_id uuid not null references public.documents(id) on delete cascade,
  user_id uuid not null,
  chunk_index int not null,
  text text not null,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create index if not exists chunks_document_id_idx on public.chunks(document_id);
create index if not exists chunks_user_id_idx on public.chunks(user_id);

