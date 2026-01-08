# SpendWise – Backend Documentation

## Overview

SpendWise is a personal finance management application designed to help users track income and expenses, manage monthly budgets, analyze spending patterns, and monitor upcoming bills. This repository contains the **backend implementation**, which serves as the single source of truth for all financial data and business logic.

The backend exposes secure REST APIs consumed by a React/TypeScript frontend. All sensitive calculations and data aggregation are handled server-side to ensure accuracy, security, and scalability.

---

## Tech Stack

* **Backend Framework:** Node.js (Express) / Python (Flask or FastAPI)
* **Database:** PostgreSQL / MySQL
* **Authentication:** JWT (JSON Web Tokens)
* **ORM / Query Layer:** Prisma / SQLAlchemy / Sequelize
* **Hosting:** Render

---

## Features Supported

* User authentication (signup & login)
* Dashboard summary (balance, spending, budgets, bills)
* Income & expense tracking
* Category-based budgeting
* Spending analytics
* Upcoming bill tracking

---

## Backend Architecture

The backend follows a layered architecture:

1. **Routes / Controllers** – Handle HTTP requests and responses
2. **Services** – Contain business logic and aggregations
3. **Models** – Represent database entities
4. **Middleware** – Authentication and request validation
5. **Database** – Persistent storage

All protected routes require a valid JWT token.

---

## Database Design

### Users

Stores registered user information.

```
users
- id (PK)
- name
- email (unique)
- password_hash
- created_at
```

---

### Categories

Defines income and expense categories.

```
categories
- id (PK)
- name
- type (income / expense)
- icon
```

---

### Transactions

Stores all income and expense records.

```
transactions
- id (PK)
- user_id (FK → users.id)
- category_id (FK → categories.id)
- amount
- type (income / expense)
- description
- transaction_date
- created_at
```

---

### Budgets

Stores monthly budget limits per category.

```
budgets
- id (PK)
- user_id (FK → users.id)
- category_id (FK → categories.id)
- monthly_limit
- month
- year
```

---

### Bills

Tracks upcoming and recurring bills.

```
bills
- id (PK)
- user_id (FK → users.id)
- title
- amount
- due_date
- status (pending / paid)
- created_at
```

---

## Application Workflow

### Authentication Flow

1. User signs up or logs in
2. Backend validates credentials
3. JWT token is generated and returned
4. Frontend stores token securely
5. Token is included in all protected API requests

---

### Dashboard Flow

1. User accesses dashboard after login
2. Frontend calls `GET /api/dashboard`
3. Backend authenticates user via JWT
4. Backend aggregates data from transactions, budgets, and bills
5. Consolidated dashboard data is returned
6. Frontend renders summary cards, charts, and lists

---

## API Endpoints

### Authentication

```
POST /api/auth/signup
POST /api/auth/login
```

---

### Dashboard

```
GET /api/dashboard
```

**Returns:**

* Total balance
* Monthly spending
* Budget remaining
* Upcoming bills summary
* Recent transactions
* Analytics-ready data

---

### Transactions

```
POST   /api/transactions
GET    /api/transactions
GET    /api/transactions/:id
PUT    /api/transactions/:id
DELETE /api/transactions/:id
```

---

### Budgets

```
POST /api/budgets
GET  /api/budgets
GET  /api/budgets/breakdown
```

---

### Analytics

```
GET /api/analytics/expenses
GET /api/analytics/income
```

---

### Bills

```
POST /api/bills
GET  /api/bills
PUT  /api/bills/:id
```

---

## Security

* JWT-based authentication
* Passwords stored using secure hashing
* User ID derived from token, not client input
* All financial calculations handled on backend

---

## Environment Variables

```
DATABASE_URL=
JWT_SECRET=
PORT=
```

---

## Running the Project Locally

1. Clone the repository
2. Install dependencies
3. Configure environment variables
4. Run database migrations
5. Start the server

---

## Deployment

The backend is deployed on **Render** with automatic deployments enabled from the main branch.

---

## Future Enhancements

* Bill due-date notifications
* Budget overspending alerts
* Recurring transactions
* Multi-currency support
* Report export (PDF/CSV)

---

## License

This project is for educational and portfolio purposes.
