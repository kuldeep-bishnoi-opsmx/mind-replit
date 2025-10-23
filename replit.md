# Mind Coach AI Agent

## Overview
A full-stack personal mental wellness assistant application that provides AI-driven supportive conversations, mood tracking, daily wellness tips, and journaling features.

## Current State
The application is successfully set up and running in the Replit environment with:
- ✅ Backend (FastAPI) running on port 8000
- ✅ Frontend (React + Vite) running on port 5000
- ✅ PostgreSQL database configured
- ✅ All dependencies installed
- ⚠️ Requires API keys to fully function (OPENAI_API_KEY, JWT_SECRET)

## Recent Changes
- **2025-10-23**: Initial setup completed
  - Created missing backend router files (chat, mood, journal, tips)
  - Configured Vite dev server for Replit proxy (host: 0.0.0.0, port: 5000, HMR settings)
  - Updated CORS to allow all origins for Replit environment
  - Fixed backend host to localhost:8000
  - Installed core Python dependencies (without heavy ML dependencies)
  - Configured workflows for frontend and backend
  - Fixed merge conflict in README
  - Added .gitignore for Python and Node.js
  - Disabled transformers library to reduce dependencies (sentiment analysis temporarily disabled)

## Project Architecture

### Backend (`/backend`)
- **Framework**: FastAPI (Python 3.11)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT tokens with bcrypt password hashing
- **AI Integration**: OpenAI GPT-4o for chat responses
- **API Port**: 8000 (localhost)

### Frontend (`/frontend`)
- **Framework**: React 19 + TypeScript
- **Build Tool**: Vite 7
- **Styling**: TailwindCSS + ShadCN UI components
- **Router**: React Router v7
- **Port**: 5000 (0.0.0.0)

### Database Schema
- **Users**: Email/password authentication, user profiles
- **Moods**: Daily mood tracking with sentiment analysis
- **Journal Entries**: Private diary with AI-generated prompts
- **Chat Sessions**: AI conversation history
- **Chat Messages**: Individual messages within sessions
- **Wellness Tips**: Daily tips and affirmations
- **User Tip Views**: Track which tips users have seen

## Environment Variables Required

### Backend (Set in Replit Secrets)
- `DATABASE_URL`: PostgreSQL connection string (✅ configured)
- `OPENAI_API_KEY`: OpenAI API key for GPT-4o (⚠️ needs to be set)
- `JWT_SECRET`: Secret key for JWT token signing (⚠️ needs to be set)
- `GOOGLE_CLIENT_ID`: (Optional) For Google OAuth
- `GOOGLE_CLIENT_SECRET`: (Optional) For Google OAuth

### Frontend
- `VITE_API_URL`: Backend API URL (currently set to http://localhost:8000)

## Key Features
1. **AI Chat Coach**: Empathetic conversations powered by GPT-4o
2. **Mood Tracker**: Daily mood logging with sentiment analysis
3. **Journal**: Private journaling with AI-generated prompts
4. **Wellness Tips**: Personalized daily affirmations and advice
5. **Authentication**: Secure email/password login with JWT

## Development Notes
- Frontend uses Vite with HMR configured for Replit's proxy environment
- Backend CORS allows all origins for development
- Database migrations handled by Alembic
- Sentiment analysis feature temporarily disabled (transformers library removed to reduce dependencies)
- Backend runs on localhost (127.0.0.1) while frontend binds to 0.0.0.0

## Next Steps for Users
1. Set OPENAI_API_KEY in Replit Secrets for AI chat functionality
2. Set JWT_SECRET in Replit Secrets for authentication
3. (Optional) Configure Google OAuth for social login
4. Deploy the application when ready

## Known Issues
- Minor HMR websocket warning in browser console (harmless, doesn't affect functionality)
- Sentiment analysis disabled (can be re-enabled by installing transformers and torch)

## User Preferences
- None documented yet

## API Endpoints
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /chat/` - Send message to AI coach
- `GET /chat/sessions` - Get user's chat sessions
- `POST /mood/` - Log a mood entry
- `GET /mood/` - Get mood history
- `POST /journal/` - Create journal entry
- `GET /journal/` - Get journal entries
- `GET /journal/prompt/generate` - Get AI-generated journal prompt
- `GET /tips/daily` - Get daily wellness tip
