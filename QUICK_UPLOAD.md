# ⚡ Quick Upload Guide - 2 Minutes!

Since Claude's environment doesn't have network access, here's the super simple manual upload process:

## 🎯 Option 1: Upload via Dashboard (Easiest - 2 minutes)

### Step-by-Step:

1. **Open your Supabase Dashboard**
   - Go to: https://supabase.com/dashboard/project/mukczuwgyebdimvtcjuq
   - Or: https://supabase.com/dashboard → Click your project

2. **Navigate to Storage**
   - Click "Storage" in the left sidebar (looks like a folder icon)

3. **Open the webapp bucket**
   - You'll see a bucket called "webapp"
   - Click on it

4. **Upload the file**
   - Click the "Upload file" button (top right)
   - Select `index.html` from your downloads
   - Click "Upload"

5. **Get your live URL**
   - Once uploaded, click on the file name `index.html`
   - You'll see a public URL like:
   ```
   https://mukczuwgyebdimvtcjuq.supabase.co/storage/v1/object/public/webapp/index.html
   ```
   - Copy this URL - this is your live app! 🎉

## 🎯 Option 2: Use Upload Scripts (If you prefer command line)

I've created two upload scripts for you:

### Using Python:
```bash
# Make sure you have requests installed
pip install requests

# Run the upload script
python3 upload-to-supabase.py
```

### Using Node.js:
```bash
# Run the upload script (no extra dependencies needed)
node upload-to-supabase.js
```

Both scripts will automatically upload your app and give you the live URL.

## ✨ After Upload

Your app will be **instantly live** at:
```
https://mukczuwgyebdimvtcjuq.supabase.co/storage/v1/object/public/webapp/index.html
```

### Test it:
- Open the URL in any browser
- Search for spools (Elegoo, Bambu Lab, etc.)
- Try the calculator
- The database is already connected and working!

### Share it:
- Send the URL to anyone
- No login required
- Works on any device
- Automatically syncs with your Supabase database

## 🔄 To Update Later

Just re-upload the file to replace the old version:
1. Go back to Storage → webapp
2. Delete the old `index.html` (or upload will update it)
3. Upload the new version

## 💡 Pro Tip: Bookmark Your App

Add this to your browser bookmarks for quick access:
```
https://mukczuwgyebdimvtcjuq.supabase.co/storage/v1/object/public/webapp/index.html
```

---

**That's it!** Your app is ready to go live in just 2 minutes. 🚀
