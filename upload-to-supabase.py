#!/usr/bin/env python3
"""
Supabase Storage Upload Script
Run this script to upload your Spool Checker app to Supabase Storage

Requirements: Python 3 with requests library (pip install requests)
Usage: python3 upload-to-supabase.py
"""

import sys

try:
    import requests
except ImportError:
    print("❌ Error: 'requests' library not found")
    print("💡 Install it with: pip install requests")
    sys.exit(1)

# Configuration
SUPABASE_URL = 'https://mukczuwgyebdimvtcjuq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im11a2N6dXdneWViZGltdnRjanVxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk5MDA1NDgsImV4cCI6MjA4NTQ3NjU0OH0.F67m3cMx5C45Hus-AlvUZO_xhDuckWwlbYAvzt9b4Mg'
FILE_PATH = './index.html'
UPLOAD_PATH = 'index.html'

def upload_file():
    """Upload the HTML file to Supabase Storage"""
    
    # Read the HTML file
    print(f'📖 Reading file: {FILE_PATH}')
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f'❌ Error: File not found: {FILE_PATH}')
        print('💡 Make sure index.html is in the same directory as this script')
        return False
    
    # Prepare upload
    upload_url = f'{SUPABASE_URL}/storage/v1/object/webapp/{UPLOAD_PATH}'
    print(f'📤 Uploading to: {upload_url}')
    
    headers = {
        'Authorization': f'Bearer {SUPABASE_KEY}',
        'Content-Type': 'text/html',
    }
    
    try:
        # Upload the file
        response = requests.post(
            upload_url,
            headers=headers,
            data=html_content.encode('utf-8')
        )
        
        print(f'\n📊 Status Code: {response.status_code}')
        
        if response.status_code in [200, 201]:
            print('✅ SUCCESS! Your app has been uploaded!')
            print('\n🌐 Your app is now live at:')
            print(f'   {SUPABASE_URL}/storage/v1/object/public/webapp/{UPLOAD_PATH}')
            print('\n💡 You can now share this URL with anyone!')
            return True
        else:
            print(f'❌ Upload failed: {response.text}')
            print('\n💭 Possible issues:')
            print('   - Storage bucket permissions')
            print('   - File already exists (file might need to be deleted first)')
            print('\n🔧 Try the manual upload method in HOSTING_GUIDE.md')
            return False
            
    except requests.exceptions.RequestException as e:
        print(f'❌ Error uploading file: {e}')
        print('\n🔧 Please use the manual upload method:')
        print('   1. Go to: https://supabase.com/dashboard/project/mukczuwgyebdimvtcjuq')
        print('   2. Click Storage → webapp')
        print('   3. Upload index.html')
        return False

if __name__ == '__main__':
    print('🚀 Supabase Storage Upload Tool')
    print('=' * 50)
    success = upload_file()
    sys.exit(0 if success else 1)
