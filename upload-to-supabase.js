#!/usr/bin/env node
/**
 * Supabase Storage Upload Script
 * Run this script to upload your Spool Checker app to Supabase Storage
 * 
 * Requirements: Node.js installed
 * Usage: node upload-to-supabase.js
 */

const fs = require('fs');
const https = require('https');

// Configuration
const SUPABASE_URL = 'https://mukczuwgyebdimvtcjuq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im11a2N6dXdneWViZGltdnRjanVxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk5MDA1NDgsImV4cCI6MjA4NTQ3NjU0OH0.F67m3cMx5C45Hus-AlvUZO_xhDuckWwlbYAvzt9b4Mg';
const FILE_PATH = './index.html';
const UPLOAD_PATH = 'index.html';

// Read the HTML file
console.log('📖 Reading file:', FILE_PATH);
const fileContent = fs.readFileSync(FILE_PATH, 'utf8');
const fileBuffer = Buffer.from(fileContent, 'utf8');

// Prepare upload URL
const uploadUrl = `${SUPABASE_URL}/storage/v1/object/webapp/${UPLOAD_PATH}`;

console.log('📤 Uploading to:', uploadUrl);

const options = {
    method: 'POST',
    headers: {
        'Authorization': `Bearer ${SUPABASE_KEY}`,
        'Content-Type': 'text/html',
        'Content-Length': fileBuffer.length,
    }
};

const req = https.request(uploadUrl, options, (res) => {
    let responseBody = '';

    res.on('data', (chunk) => {
        responseBody += chunk;
    });

    res.on('end', () => {
        console.log('\n📊 Status Code:', res.statusCode);
        
        if (res.statusCode === 200 || res.statusCode === 201) {
            console.log('✅ SUCCESS! Your app has been uploaded!');
            console.log('\n🌐 Your app is now live at:');
            console.log(`   ${SUPABASE_URL}/storage/v1/object/public/webapp/${UPLOAD_PATH}`);
            console.log('\n💡 You can now share this URL with anyone!');
        } else {
            console.log('❌ Upload failed:', responseBody);
            console.log('\n💭 Possible issues:');
            console.log('   - Storage bucket permissions');
            console.log('   - File already exists (try updating instead)');
            console.log('\n🔧 Try the manual upload method in HOSTING_GUIDE.md');
        }
    });
});

req.on('error', (error) => {
    console.error('❌ Error uploading file:', error.message);
    console.log('\n🔧 Please use the manual upload method:');
    console.log('   1. Go to: https://supabase.com/dashboard/project/mukczuwgyebdimvtcjuq');
    console.log('   2. Click Storage → webapp');
    console.log('   3. Upload index.html');
});

req.write(fileBuffer);
req.end();
