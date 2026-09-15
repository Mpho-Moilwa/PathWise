# PathWise Database Design

## 1. Purpose

This document defines the database structure for the PathWise platform.

The database will store user accounts, student profiles, academic information, opportunities, eligibility information, applications, saved opportunities and other information required by the PathWise matching system.

The database will use MySQL.

## 2. Database

Database name:

`pathwise`

Database management system:

`MySQL`

Backend technology:

`Python + FastAPI`

ORM:

`SQLAlchemy`

## 3. Design Principles

The PathWise database will follow these principles:

- Keep user authentication data separate from student profile data.
- Avoid storing repeated information in a single table.
- Use primary keys to uniquely identify records.
- Use foreign keys to establish relationships between tables.
- Store passwords only as secure hashes.
- Minimise the amount of personal information collected.
- Design the database so that it can support future PathWise features.
- Maintain consistency between the database, backend API and frontend.

## 4. User Roles

PathWise will initially support three main user roles:

- `STUDENT`
- `PROVIDER`
- `ADMIN`

### STUDENT

Students use PathWise to create profiles, receive recommendations, find opportunities, save opportunities and record application follow-ups.

### PROVIDER

Providers can eventually publish and manage opportunities such as bursaries, scholarships and other educational opportunities.

### ADMIN

Administrators manage the platform, verify opportunities, manage users and maintain platform security.

## 5. Users Table

The `users` table stores authentication and account-level information.

| Field | Type | Description |
|---|---|---|
| `id` | BIGINT | Unique user identifier |
| `email` | VARCHAR | User's login email |
| `password_hash` | VARCHAR | Secure password hash |
| `role` | VARCHAR | STUDENT, PROVIDER or ADMIN |
| `is_active` | BOOLEAN | Whether the account is active |
| `created_at` | DATETIME | Account creation date |
| `updated_at` | DATETIME | Last account update |

Primary key:

`id`

Unique constraint:

`email`

## 6. Student Profiles Table

The `student_profiles` table stores information used to understand and match students with opportunities.

| Field | Type | Description |
|---|---|---|
| `id` | BIGINT | Unique profile identifier |
| `user_id` | BIGINT | Related user account |
| `first_name` | VARCHAR | Student's first name |
| `last_name` | VARCHAR | Student's last name |
| `date_of_birth` | DATE | Student's date of birth |
| `province` | VARCHAR | Province/location |
| `institution` | VARCHAR | Current or intended institution |
| `study_level` | VARCHAR | Current study level |
| `field_of_study` | VARCHAR | Current or intended field |
| `created_at` | DATETIME | Profile creation date |
| `updated_at` | DATETIME | Last profile update |

Primary key:

`id`

Foreign key:

`user_id → users.id`

Relationship:

One user can have one student profile.

## 7. Relationship

The initial relationship is:

```text
users
  │
  │ 1 : 1
  ▼
student_profiles