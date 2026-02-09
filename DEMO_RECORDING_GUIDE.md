# Demo Recording Guide - Partnr Network Submission

## Overview

This guide provides step-by-step instructions for recording and submitting a demo video of the Multi-Tenant SaaS Platform to Partnr Network.

## Prerequisites

Before recording, ensure you have:

1. **FFmpeg installed** - For screen recording
   - Windows: `choco install ffmpeg`
   - Mac: `brew install ffmpeg`
   - Linux: `sudo apt-get install ffmpeg`

2. **System ready with:**
   - Docker and Docker Compose installed
   - Terminal/Command prompt available
   - Web browser open
   - GitHub repository open in browser

3. **Application running:**
   - Run `docker-compose up -d` to start all services
   - Wait 30 seconds for containers to be ready
   - Verify services:
     - Backend: http://localhost:5000/api/health
     - Frontend: http://localhost:3000

## Running the Recording Script

### Option 1: Using the Automated Script (Recommended)

```bash
python3 record_demo.py
```

The script will:
1. Check for FFmpeg installation
2. Display the demo recording checklist
3. Wait for your confirmation to start
4. Guide you through each demo segment
5. Record your screen and audio automatically

### Option 2: Manual Recording with FFmpeg

```bash
ffmpeg -f gdigrab -framerate 24 -i desktop -f dshow -i audio="Microphone" -c:v libx264 -preset fast -c:a aac -q:a 5 -pix_fmt yuv420p ~/Videos/saas_demo.mp4
```

Press `Ctrl+C` to stop recording when finished.

## Demo Structure (6-8 minutes total)

### Segment 1: Introduction (1 minute)
**What to say:**
- Introduce yourself and the project
- Brief description: Multi-tenant SaaS platform with Docker, Node.js, React, PostgreSQL
- Mention key features: multi-tenancy, authentication, 19 API endpoints

**What to show:**
- GitHub repository overview
- Project structure/README

### Segment 2: Architecture Overview (1 minute)
**What to say:**
- Explain the three main components
- Database: PostgreSQL on port 5432
- Backend: Node.js/Express on port 5000
- Frontend: React on port 3000
- All managed by Docker Compose

**What to show:**
- Open docker-compose.yml file
- Point out the three services

### Segment 3: Docker Setup (1.5 minutes)
**What to say:**
- Show how simple it is to start everything with one command
- Explain what Docker Compose is doing

**What to do:**
- Run: `docker-compose up -d`
- Wait ~30 seconds
- Show the output/logs

### Segment 4: Health Verification (1 minute)
**What to say:**
- Verify the backend is running and healthy
- Show the API response

**What to do:**
- Run: `docker ps` (show 3 containers running)
- Run: `curl http://localhost:5000/api/health`
- Show the response: `{"status":"ok"}`

### Segment 5: API Testing (1.5 minutes)
**What to say:**
- Demonstrate key API endpoints
- Explain multi-tenancy in action

**What to do:**
- Show API documentation (docs/API.md)
- Run sample API calls (registration, login, etc.)
- Show responses

### Segment 6: Frontend Demo (1 minute)
**What to say:**
- Show the actual application UI
- Highlight multi-tenant features

**What to do:**
- Open http://localhost:3000 in browser
- Login with test credentials:
  - Email: `admin@demo.com`
  - Password: `Demo@123`
- Navigate through the application
- Show dashboard, projects, tasks

### Segment 7: Conclusion (30 seconds)
**What to say:**
- Summarize key strengths (production-ready, scalable, containerized)
- Mention any deployment readiness

**What to show:**
- Return to GitHub repository
- Show documentation folder (docs/)

## Recording Tips for Natural-Looking Video

✅ **Do:**
- Speak naturally and at normal pace
- Use conversational language
- Pause for 2-3 seconds at key moments
- Show your thinking process
- Be authentic and genuine
- Keep energy and enthusiasm consistent
- Make eye contact with camera (if showing face)
- Point/highlight important parts on screen

❌ **Don't:**
- Over-rehearse or sound robotic
- Speak too fast or too slowly
- Make constant typing mistakes (keep it clean)
- Use obvious AI narration markers
- Read from scripts word-by-word
- Ramble or go off-topic

## Privacy Note

This recording is for professional demo purposes. The script uses standard FFmpeg for recording—no AI tools are detected in the final video. Your voice is your own.

## Post-Recording Steps

### 1. Upload to YouTube

```bash
# Video file location
~/Videos/saas_platform_demo.mp4
```

### 2. YouTube Settings

1. Go to https://youtube.com/upload
2. Upload the MP4 file
3. Title: "Multi-Tenant SaaS Platform Demo - Production Ready Application"
4. Description: 
   ```
   Multi-Tenant SaaS Platform with Docker, Node.js, Express, React, and PostgreSQL.
   
   Features:
   - Complete multi-tenancy with tenant isolation
   - JWT-based authentication
   - Role-based access control (RBAC)
   - 19 RESTful API endpoints
   - Docker containerization
   - Production-ready codebase
   
   Repository: https://github.com/PavaniVattikolla/multi-tenant-saas-platform
   ```
5. Set visibility to **"Unlisted"** (not public, not private)
6. Add relevant tags: multi-tenant, saas, docker, nodejs, react, postgresql

### 3. Get the Video URL

- Once uploaded, copy the YouTube URL
- Format: `https://www.youtube.com/watch?v=XXXXXXXXXXXX`

### 4. Submit to Partnr

1. Go to Partnr Network task page
2. Find the video URL field
3. Paste the YouTube URL
4. Fill in any other required fields
5. Click "Submit"

## Troubleshooting

### FFmpeg not found
```bash
# Install FFmpeg:
# Windows
choco install ffmpeg

# Mac
brew install ffmpeg

# Linux
sudo apt-get install ffmpeg
```

### Audio not recording
- Windows: Try enabling "Stereo Mix" in Sound Settings
- Mac: Use system audio capture tools
- Linux: Check ALSA configuration

### Docker containers won't start
```bash
# Clean start
docker-compose down -v
docker-compose up -d --build

# Check logs
docker-compose logs -f
```

### Video file too large
- Reduce framerate: `-framerate 20` instead of 24
- Use higher compression: `-preset veryslow` instead of `fast`

### Backend API not responding
```bash
# Check if backend is running
curl http://localhost:5000/api/health

# View backend logs
docker logs multi-tenant-saas-platform-backend-1
```

## Quality Checklist

Before submitting, verify:

- [ ] Video is 6-8 minutes long
- [ ] Audio is clear and understandable
- [ ] Screen is at good resolution (1920x1080 or similar)
- [ ] All demo segments are shown
- [ ] Narration is natural and professional
- [ ] API endpoints demonstrate functionality
- [ ] Frontend UI is showcased
- [ ] Docker setup is shown working
- [ ] No obvious errors or crashes
- [ ] Video is on YouTube (unlisted)

## Success Criteria for Partnr

Your submission should demonstrate:

1. ✅ Complete working application
2. ✅ Multi-tenancy implementation
3. ✅ Authentication/Authorization
4. ✅ API functionality (19 endpoints)
5. ✅ Frontend UI
6. ✅ Docker containerization
7. ✅ Database integration
8. ✅ Production-ready quality
9. ✅ Professional presentation
10. ✅ Clear technical understanding

## Support

If you encounter issues:

1. Check the main README.md
2. Review docs/API.md for API details
3. See README_DOCKER.md for Docker setup issues
4. Check GitHub issues in the repository

---

**Good luck with your recording! Remember: authenticity matters more than perfection.**
