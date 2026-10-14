# Memory schema

Use a small schema that can be backed by SQLite or Markdown. Store only information needed for future work.

## SQLite

Suggested table:

```sql
CREATE TABLE IF NOT EXISTS memory_entries (
  id INTEGER PRIMARY KEY,
  project TEXT NOT NULL,
  topic TEXT NOT NULL,
  content TEXT NOT NULL,
  source TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'active'
);
CREATE INDEX IF NOT EXISTS memory_project_topic
  ON memory_entries(project, topic, status);
```

Use ISO 8601 timestamps, parameterized SQL, and explicit status values such as `active`, `superseded`, or `archived`. Avoid storing secrets or raw conversation dumps.

## Markdown record

```markdown
# YYYY-MM-DD ? Project / topic
- Decision: concise, verifiable statement.
- Reason: evidence or user instruction behind it.
- Source: repository path, URL, or session reference.
- Status: active | superseded | archived
```

Keep one topic per record. An index should list project, topic, date, and path. Resolve conflicts using current user instructions and current project evidence.
