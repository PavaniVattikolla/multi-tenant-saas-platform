#!/usr/bin/env python3
"""
Screen Recording Script for Multi-Tenant SaaS Platform Demo
Records screen with captions overlay and command demonstrations
"""
import subprocess
import sys
import os
import time
import json
from pathlib import Path
from datetime import datetime

print("\n" + "="*70)
print("MULTI-TENANT SAAS PLATFORM - DEMO RECORDING TOOL")
print("="*70 + "\n")

class ScreenRecorder:
    def __init__(self):
        self.output_dir = Path.home() / "Videos"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.output_file = self.output_dir / "saas_platform_demo.mp4"
        self.fps = 24
        self.resolution = "1920x1080"
        
    def check_ffmpeg(self):
        """Check if FFmpeg is installed"""
        try:
            subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
            print("[OK] FFmpeg is installed")
            return True
        except:
            print("[ERROR] FFmpeg not found. Install with:")
            print("  Windows: choco install ffmpeg")
            print("  Mac: brew install ffmpeg")
            print("  Linux: sudo apt-get install ffmpeg")
            return False
    
    def record_screen(self):
        """Record screen using FFmpeg with audio"""
        print(f"\n[INFO] Recording to: {self.output_file}")
        print("[INFO] Resolution: 1920x1080 @ 24 fps")
        print("[INFO] Audio: System audio")
        print("\nInstructions:")
        print("1. Arrange your windows (GitHub in browser, Terminal visible)")
        print("2. Press ENTER to start recording")
        print("3. Perform demo steps:")
        print("   - Show docker-compose.yml in editor")
        print("   - Run: docker-compose up -d")
        print("   - Wait for containers to start (30 sec)")
        print("   - Run: curl http://localhost:5000/api/health")
        print("   - Show API response")
        print("   - Open http://localhost:3000 in browser")
        print("   - Show application UI")
        print("4. When finished, press Ctrl+C in recording terminal")
        print("\n" + "-"*70)
        
        input("\nPress ENTER to start recording...")
        
        # FFmpeg command for screen recording
        ffmpeg_cmd = [
            "ffmpeg",
            "-f", "gdigrab",  # Windows screen capture
            "-framerate", "24",
            "-i", "desktop",
            "-f", "dshow",  # Windows audio
            "-i", "audio=\"Microphone\"",
            "-c:v", "libx264",
            "-preset", "fast",
            "-c:a", "aac",
            "-q:a", "5",
            "-pix_fmt", "yuv420p",
            str(self.output_file)
        ]
        
        try:
            print("\n[RECORDING] Screen capture started")
            print("[RECORDING] Press Ctrl+C when finished\n")
            subprocess.run(ffmpeg_cmd, check=False)
            print("\n[RECORDING] Completed")
            return True
        except KeyboardInterrupt:
            print("\n[RECORDING] Stopped by user")
            return True
        except Exception as e:
            print(f"[ERROR] Recording failed: {e}")
            return False
    
    def record_screen_gdigrab_audio(self):
        """Alternative: Record screen with system audio on Windows"""
        ffmpeg_cmd = [
            "ffmpeg",
            "-f", "gdigrab",
            "-framerate", "24",
            "-i", "desktop",
            "-f", "dshow",
            "-i", "audio=\"Stereo Mix\"",  # May need to enable in Windows
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "23",
            "-c:a", "aac",
            "-q:a", "5",
            "-pix_fmt", "yuv420p",
            str(self.output_file)
        ]
        return ffmpeg_cmd
    
    def get_demo_checklist(self):
        """Return demo checklist for reference"""
        checklist = {
            "Architecture Overview": [
                "Show multi-tenant-saas-platform GitHub repository",
                "Point out main components (backend, frontend, database)",
                "Show docker-compose.yml file"
            ],
            "Docker Setup": [
                "Show directory structure in terminal",
                "Explain three containers: DB (5432), Backend (5000), Frontend (3000)",
                "Run: docker-compose up -d",
                "Wait 30 seconds for containers to start"
            ],
            "Health Verification": [
                "Run: docker ps (show all 3 containers running)",
                "Run: curl http://localhost:5000/api/health",
                "Show JSON response: {status: ok}"
            ],
            "API Testing": [
                "Show API endpoints documentation",
                "Run: curl -X POST http://localhost:5000/api/auth/register",
                "Show successful registration response"
            ],
            "Frontend Demo": [
                "Open http://localhost:3000 in browser",
                "Show login page",
                "Demonstrate multi-tenant UI features"
            ],
            "Conclusion": [
                "Summarize key features (multi-tenancy, Docker, full-stack)",
                "Mention scalability and production-ready nature"
            ]
        }
        return checklist
    
    def run(self):
        """Main execution"""
        if not self.check_ffmpeg():
            print("\n[ABORT] FFmpeg is required. Please install it.")
            return False
        
        print("\n" + "="*70)
        print("DEMO RECORDING CHECKLIST")
        print("="*70)
        
        checklist = self.get_demo_checklist()
        for section, items in checklist.items():
            print(f"\n{section}:")
            for i, item in enumerate(items, 1):
                print(f"  {i}. {item}")
        
        print("\n" + "="*70)
        print("Recording Tips:")
        print("- Speak clearly and at normal pace")
        print("- Use natural language, no need for perfection")
        print("- Show what you're doing step by step")
        print("- Pause for 2-3 seconds at key moments so viewers can follow")
        print("="*70)
        
        success = self.record_screen()
        
        if success and self.output_file.exists():
            size_mb = self.output_file.stat().st_size / 1024 / 1024
            print(f"\n[SUCCESS] Recording saved: {self.output_file}")
            print(f"[INFO] File size: {size_mb:.1f} MB")
            print(f"[INFO] Duration: ~6-8 minutes recommended")
            print("\nNext steps:")
            print("1. Review the recording")
            print("2. Upload to YouTube (Settings > Visibility: Unlisted)")
            print("3. Copy the YouTube URL")
            print("4. Paste in Partnr submission form")
            print("5. Submit!\n")
            return True
        else:
            print("\n[ERROR] Recording was not completed successfully.")
            return False

if __name__ == "__main__":
    try:
        recorder = ScreenRecorder()
        success = recorder.run()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        sys.exit(1)
