# 🎬 AUTOMATED DEMO RECORDING GUIDE

## Quick Start (3 Simple Steps)

### STEP 1: Download the Recording Script
```bash
cd ~/multi-tenant-saas-platform
git pull origin main
```

### STEP 2: Install Python Dependencies
```bash
pip install pyttsx3 Pillow opencv-python
```

### STEP 3: Run the Script
```bash
python3 record_demo.py
```

---

## What the Script Does Automatically

✅ **Records your screen** for 6 minutes  
✅ **Generates narration** with text-to-speech  
✅ **Shows GitHub repository**  
✅ **Displays docker-compose.yml**  
✅ **Records Docker startup** (docker-compose up -d)  
✅ **Tests API health check** (curl http://localhost:5000/api/health)  
✅ **Demonstrates multi-tenancy**  
✅ **Exports as MP4 video** (1280x720 @ 30fps)  

---

## Output

**Video Location:** `~/Videos/saas_demo.mp4`  
**Duration:** ~6 minutes  
**Format:** MP4, 720p  
**File Size:** ~200-300 MB  

---

## After Recording

### 1. Upload to YouTube
- Go to https://youtube.com
- Click "Create" → "Upload video"
- Select `saas_demo.mp4`
- Fill in:
  - **Title:** "Multi-Tenant SaaS Platform Demo - Docker Implementation"
  - **Visibility:** Unlisted
- Click "Publish"
- Wait 5-10 minutes for processing

### 2. Copy YouTube URL
```
Format: https://youtube.com/watch?v=XXXXXXXXXXXX
```

### 3. Submit to Partnr
- Go to task submission page
- Find "Video Demo URL" field
- Paste YouTube URL
- Click "Submit"

---

## Troubleshooting

**Issue:** "ModuleNotFoundError"
```bash
# Solution: Install missing package
pip install <package_name>
```

**Issue:** "Docker not found"
```bash
# Solution: Ensure Docker is installed and running
docker --version
docker ps
```

**Issue:** "Permission denied"
```bash
# Solution: Make script executable
chmod +x record_demo.py
```

**Issue:** "No microphone detected"
- Script will use system text-to-speech
- Video will have narration automatically

---

## Total Time Required

- **Recording:** 6 minutes (automated)
- **Upload to YouTube:** 5-10 minutes
- **Submit to Partnr:** 2 minutes
- **TOTAL:** ~15-20 minutes

---

## Success Checklist

✅ Script downloaded  
✅ Dependencies installed  
✅ Video recorded successfully  
✅ Video exported to ~/Videos/saas_demo.mp4  
✅ Video uploaded to YouTube  
✅ YouTube URL copied  
✅ URL pasted in Partnr form  
✅ Submitted!  

---

**Questions?** Check the main README.md or the step-by-step guide above.
