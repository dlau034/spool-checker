# Spool Checker - Project Context

## Project Overview
Spool Checker is a 3D filament calculator web application built with React and Supabase. It helps users track and manage 3D printer filament spools, with both a public-facing calculator interface and an admin panel for managing inventory.

## Technology Stack
- **Frontend**: React 18 with Babel (inline JSX compilation)
- **Styling**: CSS (no preprocessors, vanilla CSS)
- **Backend**: Supabase for authentication and database
- **Deployment**: Static HTML files with Netlify headers configuration

## Project Structure
```
spool-checker/
├── index.html          # Main filament calculator app
├── admin.html          # Admin panel for inventory management
├── README.md           # Basic project description
├── _headers            # Netlify header configuration
└── .claude/            # Claude Code configuration
```

## Key Features

### Main App (index.html)
- 3D filament spool calculator
- Mobile-responsive design
- Integration with Supabase for data persistence
- Clean UI with iOS-inspired design language

### Admin Panel (admin.html)
- Authentication/login system
- Inventory management interface
- Data table for spool management
- Responsive mobile layout

## Design System
- **Color Scheme**:
  - Primary: #14786F (teal)
  - Background: #F8F9FA (light gray)
  - Text: #1C1C1E (dark)
  - Borders: #E8E8E8 (light gray)
- **Font**: SF Pro Display, system fonts fallback
- **UI Components**: iOS/Apple design language inspiration

## Important Notes
- Both HTML files use inline React and Babel for simplicity (no build process needed)
- Supabase client loaded via CDN
- Mobile-first design with responsive layout
- Header components are separated and shared between pages

## Recent Changes
- Removed password display text (security improvement)
- Fixed admin panel table scrolling on mobile
- Separated header component
- Admin panel responsive fixes

## Next Steps for Development
- Continue admin panel improvements
- Enhance data management features
- Optimize mobile experience
- Add more filament calculation features
