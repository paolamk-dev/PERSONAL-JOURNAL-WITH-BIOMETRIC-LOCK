# Quick Start Guide - Luminary Journal

This guide will help you get the Luminary Journal app running on your local machine in under 10 minutes.

## Prerequisites

Before you begin, make sure you have:

- ✅ **Node.js 18+** installed ([Download](https://nodejs.org/))
- ✅ **npm** or **yarn** package manager
- ✅ **Expo CLI** (will be installed if not present)
- ✅ **Expo Go app** on your phone ([iOS](https://apps.apple.com/app/expo-go/id982107779) | [Android](https://play.google.com/store/apps/details?id=host.exp.exponent))

## Step 1: Install Dependencies

```bash
npm install
```

This will install all required packages including:
- Expo SDK 51+
- React Native
- Firebase
- Supabase
- NativeWind
- And more...

## Step 2: Set Up Environment Variables

### Quick Setup (For Testing Only)

For a quick test, you can skip Firebase/Supabase setup temporarily. The app will run with warnings but you can see the UI:

```bash
cp .env.example .env
```

The placeholder values in `.env` will allow the app to start, but authentication and data storage won't work.

### Full Setup (Recommended)

1. **Create Firebase Project**:
   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Create a new project
   - Enable Authentication → Email/Password
   - Create a Firestore Database
   - Copy your config from Project Settings

2. **Create Supabase Project**:
   - Go to [Supabase](https://supabase.com/)
   - Create a new project
   - Go to Storage → Create bucket named `journal-photos` (set to private)
   - Copy your URL and anon key from Settings → API

3. **Update `.env` file**:

```env
# Firebase
EXPO_PUBLIC_FIREBASE_API_KEY=your_actual_key
EXPO_PUBLIC_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
EXPO_PUBLIC_FIREBASE_PROJECT_ID=your_project_id
EXPO_PUBLIC_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
EXPO_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
EXPO_PUBLIC_FIREBASE_APP_ID=your_app_id

# Supabase
EXPO_PUBLIC_SUPABASE_URL=https://your_project.supabase.co
EXPO_PUBLIC_SUPABASE_ANON_KEY=your_actual_key
```

## Step 3: Start the Development Server

```bash
npm start
```

This will start the Expo development server and display a QR code.

## Step 4: Run the App

### On Your Phone (Easiest)

1. Open **Expo Go** app on your phone
2. Scan the QR code from your terminal
3. The app will load on your device

### On iOS Simulator (Mac only)

```bash
npm run ios
```

### On Android Emulator

```bash
npm run android
```

### On Web Browser

```bash
npm run web
```

## 🎉 You're Ready!

The app should now be running! You'll see:

1. **Splash Screen** - "Luminary Journal" with loading indicator
2. **Login Screen** - Sign in form (placeholder for now)
3. Navigate through the app to explore the UI

## Current Features (UI Only)

Since backend integration is not yet complete, you can:

- ✅ View all screens and navigation
- ✅ See the UI design and layout
- ✅ Test navigation between screens
- ❌ Cannot register/login yet (Phase 2)
- ❌ Cannot create entries yet (Phase 3)
- ❌ Cannot upload photos yet (Phase 4)

## Troubleshooting

### "Cannot find module" errors

```bash
rm -rf node_modules package-lock.json
npm install
```

### Metro bundler issues

```bash
npm start --clear
```

### iOS build issues

```bash
cd ios && pod install && cd ..
npm run ios
```

### Android build issues

- Make sure Android Studio is installed
- Ensure ANDROID_HOME environment variable is set
- Check that an emulator is running

### Expo Go connection issues

- Ensure your phone and computer are on the same WiFi network
- Try using tunnel mode: `npm start --tunnel`

## Next Steps

1. **Explore the UI**: Navigate through all screens to see the design
2. **Configure Firebase**: Set up authentication to test login
3. **Configure Supabase**: Set up storage to test photo uploads
4. **Read PROJECT_STATUS.md**: See what features are planned
5. **Check masterprompt.md**: Understand the full project vision

## Useful Commands

```bash
# Start dev server
npm start

# Clear cache and restart
npm start --clear

# Run on specific platform
npm run ios
npm run android
npm run web

# Check for issues
npm run lint (if configured)

# View logs
npm start -- --verbose
```

## Need Help?

- Check **README.md** for detailed setup instructions
- Read **PROJECT_STATUS.md** for current implementation status
- Review **masterprompt.md** for complete project specifications

## Development Workflow

1. Make code changes in your editor
2. Save the file
3. Expo will automatically reload the app
4. Check the terminal for any errors
5. Test the changes on your device/simulator

---

**Happy Coding! 🚀**

Remember: This is a work in progress. Phase 1 (setup) is complete.
Phase 2 (authentication) is next on the roadmap.
