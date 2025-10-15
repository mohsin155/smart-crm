# Domain-Driven Design (DDD) Folder Structure for REST API

This document explains the purpose of each folder in a DDD-style Node.js/TypeScript REST API project.

---
## Tech Stack

Code : Python fast api
Package manager : uv
App managment : uvicorn
Database : Postgres


## 🏗️ Overview

Domain-Driven Design (DDD) promotes separation of concerns by isolating **business logic**, **application logic**, and **infrastructure**.  
This makes the codebase easier to maintain, extend, and test.

Typical folder structure:

```
src/
├── api/
├── core/
├── domain/
├── infrastructure/
├── models/
├── schemas/
├── services/
└── utils/
```

---

## 📁 Folder Explanations

### 1. `api/`
**Purpose:** Handles incoming HTTP requests and outgoing responses.

**Contains:**
- Controllers and routers
- Middleware (authentication, validation, etc.)

**Example:**
```ts
// api/controllers/authController.ts
import { loginUser } from "../../services/authService";

export const login = async (req, res) => {
  const token = await loginUser(req.body);
  res.json({ token });
};
```

---

### 2. `core/`
**Purpose:** Application-wide shared logic (config, errors, constants).

**Contains:**
- Configuration and environment setup
- Custom error classes
- Global types or interfaces

**Example:**
```ts
// core/errors/AppError.ts
export class AppError extends Error {
  constructor(public message: string, public statusCode = 500) {
    super(message);
  }
}
```

---

### 3. `domain/`
**Purpose:** The heart of the application — **business logic** and **domain models**.

**Contains:**
- Entities (e.g., `User`, `Session`)
- Value Objects
- Domain Services

**Example:**
```ts
// domain/entities/User.ts
export class User {
  constructor(private email: string, private passwordHash: string) {}

  changePassword(newHash: string) {
    this.passwordHash = newHash;
  }
}
```

---

### 4. `infrastructure/`
**Purpose:** Handles **external systems** (database, APIs, message queues).

**Contains:**
- Database repositories
- ORM models
- Third-party integrations

**Example:**
```ts
// infrastructure/repositories/UserRepository.ts
import { prisma } from "../db";

export const findUserByEmail = async (email: string) => {
  return prisma.user.findUnique({ where: { email } });
};
```

---

### 5. `models/`
**Purpose:** Represents **data structures** for persistence or transfer.

**Contains:**
- ORM models
- Data Transfer Objects (DTOs)
- Mappers between domain and database layers

**Example:**
```ts
// models/UserModel.ts
export interface UserModel {
  id: string;
  email: string;
  passwordHash: string;
}
```

---

### 6. `schemas/`
**Purpose:** Defines validation and serialization rules for requests/responses.

**Contains:**
- Input validation schemas (Zod/Joi/Yup)
- OpenAPI/Swagger schemas

**Example:**
```ts
// schemas/loginSchema.ts
import { z } from "zod";

export const loginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(6),
});
```

---

### 7. `services/`
**Purpose:** Application logic (use cases) that orchestrates domain and infrastructure.

**Contains:**
- Use cases (`RegisterUser`, `LoginUser`, etc.)
- Business workflows

**Example:**
```ts
// services/authService.ts
import { findUserByEmail } from "../infrastructure/repositories/UserRepository";
import { verifyPassword, generateToken } from "../utils/authHelpers";

export const loginUser = async ({ email, password }) => {
  const user = await findUserByEmail(email);
  if (!user || !(await verifyPassword(password, user.passwordHash))) {
    throw new Error("Invalid credentials");
  }
  return generateToken(user.id);
};
```

---

### 8. `utils/`
**Purpose:** Generic helper functions that are stateless and reusable.

**Contains:**
- Cryptography helpers
- String/date utilities
- Miscellaneous helpers

**Example:**
```ts
// utils/authHelpers.ts
import jwt from "jsonwebtoken";
export const generateToken = (userId: string) =>
  jwt.sign({ userId }, process.env.JWT_SECRET!, { expiresIn: "1h" });
```

---

## 🔁 Layer Interaction Flow

```
Request → api/controller → services → domain → infrastructure
                                      ↑
                                      └── utils/core/helpers
```

Each layer depends **inward**, never outward:
- `api` depends on `services`
- `services` depend on `domain` and `infrastructure`
- `domain` depends on nothing external

---

## ✅ Benefits of This Structure
- **Separation of concerns**
- **Testability**
- **Scalability**
- **Maintainability**
- **Framework-agnostic domain logic**
