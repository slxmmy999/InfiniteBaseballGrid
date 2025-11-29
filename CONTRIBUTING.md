**Introduction**

Welcome — thanks for considering contributing to Infinite Baseball Grid. This document explains how to get the project running locally, how the app uses the database, recommended development workflows, and how to open a quality pull request.

**Project overview**
- Frontend: Nuxt (Vue) in the repository root — pages/components in `components/` and `pages/`.
- Backend: Python `Quart` app in `server/server.py` with supporting modules in `server/`.
- Database: MongoDB (used for community statistics and shared grids).

**Quick setup (local development)**
1. Clone the repo and open the project folder.
2. Frontend dependencies (Node.js + npm):
   - Install dependencies: `npm install`
   - Run the frontend in dev mode (Nuxt): `npm run dev`.
3. Backend dependencies (Python 3.12+ recommended):
   - Create a virtual environment:
     ```bash
     python3 -m venv .venv
     . .venv/bin/activate
     python -m pip install --upgrade pip
     pip install -r requirements.txt
     ```
   - Environment variables: create a `.env` file (see `.env.example`) in the project root and add values.
   - Start the backend (development):
     ```bash
     .venv/bin/python server/server.py
     ```
   - Or run with an ASGI server for better behavior: `hypercorn server.server:app --bind 0.0.0.0:8000`

**Database (MongoDB)**
- The server reads `DB_CONNECTION_STRING` (from `.env` or environment). 
- Collections used:
  - `matchup-statistics`: stores pick frequencies per team-pair and player.
  - `shared-grids`: stores shared grid payloads by UUID.
- Running Mongo locally (Docker recommended):
  ```bash
  docker run -d --name mongo -p 27017:27017 mongo:6
  ```
- Optional web GUI (mongo-express):
  ```bash
  docker network create mongo-net
  docker run -d --name mongo --network mongo-net -p 27017:27017 mongo:6
  docker run -d --name mongo-express --network mongo-net -p 8081:8081 \
    -e ME_CONFIG_MONGODB_SERVER=mongo mongo-express
  # Open http://localhost:8081
  ```


**How validation & rarity work (short)**
- The server validates player answers by calling the MLB stats API (`server/BaseballData.py`). If validation succeeds it returns `picture`, `name`, and `rarity_score`.
- The `rarity_score` comes from Mongo (`matchup-statistics`).

**Coding conventions**
- Python: follow PEP8, type hints are used in many modules. Keep changes minimal and focused.
- JavaScript/Vue: follow project style, use existing component structure. Keep templates clean and avoid global side effects.

**Testing / running checks**
- There are currently no automated tests in the project. If you add tests, include instructions in this file and use `pytest` for Python and an appropriate test runner for the frontend.

**Pull requests**
1. Fork the repo and create a feature branch named descriptively (e.g. `fix/validate-player-db-error` )
2. Keep commits small and atomic; write clear commit messages.
3. Open a PR against `main` with a description of the change, the motivation, and any setup steps to test it.
4. If your change affects runtime configuration, update `.env.example` and document the variables.




Thanks for contributing — welcome aboard!
