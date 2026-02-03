# Spool Checker

A mobile-friendly web app for calculating remaining 3D printer filament weight. Select your spool type from the database or enter custom empty spool weight, weigh your spool with filament, and instantly see how much filament remains.

## Features

- **Smart Calculator**: Calculate remaining filament by subtracting empty spool weight from total weight
- **Spool Database**: Pre-loaded database of popular filament brands and their empty spool weights
- **Search & Filter**: Quick search through spool brands and materials
- **Admin Panel**: Password-protected interface for managing the spool database
- **Image Support**: Visual identification with spool images
- **Mobile-First Design**: Optimized for mobile devices with iOS-style interface
- **Cloud Sync**: Supabase backend for data storage and synchronization

## Tech Stack

- **Frontend**: React (via CDN), vanilla JavaScript
- **Backend**: Supabase (PostgreSQL database + Storage)
- **Hosting**: Static hosting (Netlify, Cloudflare Pages, Vercel, etc.)
- **Styling**: Custom CSS with mobile-first design

## Getting Started

### Prerequisites

- A Supabase account ([sign up here](https://supabase.com))
- Node.js (optional, for local development server)

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd spool-checker
   ```

2. **Set up Supabase**

   a. Create a new project at [supabase.com](https://supabase.com)

   b. Create the `spool_types` table:
   ```sql
   CREATE TABLE spool_types (
     id BIGSERIAL PRIMARY KEY,
     brand TEXT NOT NULL,
     material TEXT,
     spool_type TEXT NOT NULL,
     empty_weight INTEGER NOT NULL,
     kg NUMERIC(3,1) DEFAULT 1.0,
     image_url TEXT,
     created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
   );
   ```

   c. Create a storage bucket for images:
   - Go to Storage in your Supabase dashboard
   - Create a new public bucket named `spool-images`

   d. Enable Row Level Security (optional but recommended):
   ```sql
   -- Allow public read access
   CREATE POLICY "Public read access" ON spool_types
     FOR SELECT USING (true);

   -- Allow authenticated insert/update/delete (optional)
   CREATE POLICY "Authenticated write access" ON spool_types
     FOR ALL USING (auth.role() = 'authenticated');
   ```

3. **Configure the app**

   Update the Supabase credentials in both files:
   - `index.html` (line 485-486)
   - `admin.html` (line 557-558)

   ```javascript
   const SUPABASE_URL = 'https://your-project.supabase.co';
   const SUPABASE_ANON_KEY = 'your-anon-key-here';
   ```

   Update the admin password in `admin.html` (line 559):
   ```javascript
   const ADMIN_PASSWORD = 'your-secure-password';
   ```

4. **Run locally** (optional)
   ```bash
   npm install
   npm run dev
   ```

   Or use any static file server:
   ```bash
   # Python
   python -m http.server 3000

   # PHP
   php -S localhost:3000
   ```

5. **Deploy**

   Deploy to your preferred static hosting platform:
   - **Netlify**: Drag and drop or connect your Git repo
   - **Cloudflare Pages**: Connect your Git repo
   - **Vercel**: Connect your Git repo
   - **GitHub Pages**: Enable in repository settings

## Usage

### Main App (index.html)

1. Open the app in your browser
2. Search for your spool brand or manually enter empty spool weight
3. Weigh your spool with filament and enter the total weight
4. The app calculates remaining filament weight instantly

### Admin Panel (admin.html)

1. Navigate to `/admin.html`
2. Enter the admin password
3. Add, edit, or delete spool types
4. Upload images for visual identification
5. Search and filter through existing entries

## Project Structure

```
spool-checker/
├── index.html          # Main calculator app
├── admin.html          # Admin panel for managing database
├── _headers            # HTTP headers for hosting platforms
├── .gitignore          # Git ignore rules
├── .env.example        # Environment variables template
├── package.json        # Node.js dependencies
└── README.md           # This file
```

## Database Schema

### `spool_types` Table

| Column       | Type    | Description                          |
|-------------|---------|--------------------------------------|
| id          | BIGINT  | Primary key                          |
| brand       | TEXT    | Spool brand name (e.g., "Elegoo")   |
| material    | TEXT    | Material type (e.g., "PLA+")        |
| spool_type  | TEXT    | Spool type (Plastic/Cardboard/Metal)|
| empty_weight| INTEGER | Empty spool weight in grams         |
| kg          | NUMERIC | Filament weight in kilograms        |
| image_url   | TEXT    | URL to spool image                  |
| created_at  | TIMESTAMP| Record creation timestamp          |

## Security Notes

- Admin password is stored in plain text in the client-side code (for demo purposes)
- For production use, consider implementing proper authentication using Supabase Auth
- The Supabase anon key is safe to expose in client-side code if RLS is properly configured
- Consider implementing rate limiting for the admin panel

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT

## Support

For issues or questions, please open an issue on GitHub.
