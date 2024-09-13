# AASYP Chat System

This project is a chat system built with a backend using Django and a frontend using a modern JavaScript framework.

## Prerequisites

- Docker
- Docker Compose
- Node.js and npm

## Getting Started

### First-Time Setup

1. **Install frontend dependencies**:
   Navigate to the `frontend` directory and run `npm install` to install all necessary dependencies.

   ```bash
   cd frontend
   npm install
   cd ..
   ```
2. **Build and start the Docker containers**:
   Run the following command to build and start the Docker containers.

   ```bash
   docker compose up --build
   ```
3. **Run database migrations**:
   After the containers are up and running, navigate to the `backend` directory and run the following command to apply the database migrations.

   ```bash
   docker compose exec web python manage.py migrate
   ```
