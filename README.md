# Luminary Journal

A secure, feature-rich personal journal app built with React Native and Expo, featuring biometric authentication, rich text editing, photo attachments, and mood tracking.

## 🚀 Features

- **Biometric Authentication**: Secure access via Face ID or Fingerprint
- **Rich Text Editor**: Write formatted journal entries
- **Photo Attachments**: Add multiple photos to each entry with captions
- **Mood Tracking**: Track your emotional state over time
- **Calendar View**: Browse entries by date
- **Writing Streaks**: Stay motivated with daily writing goals
- **Tags & Search**: Organize and find entries easily
- **Auto-Lock**: Automatic security lock after inactivity

## 🛠 Tech Stack

- **Framework**: React Native + Expo SDK 51+
- **Language**: TypeScript (strict mode)
- **Navigation**: expo-router (file-based routing)
- **Authentication**: Firebase Auth + expo-local-authentication
- **Database**: Firebase Firestore
- **Image Storage**: Supabase Storage
- **State Management**: Zustand
- **Styling**: NativeWind (TailwindCSS for React Native)
- **Rich Text**: @10play/tentap-editor

## 📋 Prerequisites

- Node.js 18+
- npm or yarn
- Expo CLI
- iOS Simulator (for iOS development) or Android Emulator (for Android development)
- Firebase account and project
- Supabase account and project

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd luminary-journal
```

### 2. Install dependencies

```bash
npm install
```

### 3. Configure Firebase

1. Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
2. Enable Authentication (Email/Password)
3. Create a Firestore database
4. Get your Firebase configuration

### 4. Configure Supabase

1. Create a Supabase project at [Supabase](https://supabase.com/)
2. Create a storage bucket named `journal-photos`
3. Set the bucket to private
4. Get your Supabase URL and anon key

### 5. Environment Variables

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

Update `.env` with your Firebase and Supabase credentials:

```
EXPO_PUBLIC_FIREBASE_API_KEY=your_firebase_api_key
EXPO_PUBLIC_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
EXPO_PUBLIC_FIREBASE_PROJECT_ID=your_project_id
EXPO_PUBLIC_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
EXPO_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
EXPO_PUBLIC_FIREBASE_APP_ID=your_app_id

EXPO_PUBLIC_SUPABASE_URL=https://your_project.supabase.co
EXPO_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### 6. Run the app

```bash
# Start development server
npm start

# Run on iOS
npm run ios

# Run on Android
npm run android

# Run on web
npm run web
```

## 📁 Project Structure

```
luminary-journal/
├── app/                    # Expo Router app directory
│   ├── (auth)/            # Authentication screens
│   ├── (tabs)/            # Main app tabs
│   ├── entry/             # Entry screens
│   └── _layout.tsx        # Root layout
├── src/
│   ├── components/        # Reusable components
│   ├── config/            # Configuration files
│   ├── constants/         # App constants
│   ├── hooks/             # Custom React hooks
│   ├── services/          # API services
│   ├── stores/            # Zustand stores
│   ├── types/             # TypeScript types
│   └── utils/             # Utility functions
├── assets/                # Images, fonts, etc.
└── global.css            # NativeWind global styles
```

## 🔒 Security

- All journal entries are private and user-specific
- Biometric authentication required to access the app
- Images stored in private Supabase bucket with signed URLs
- Automatic lock after inactivity
- Secure storage for sensitive data

## 📝 Development Status

This project is currently in **initial setup phase**. The basic structure and authentication screens have been created, but many features are still under development:

- ✅ Project structure
- ✅ Authentication UI
- ✅ Basic navigation
- ⏳ Firebase integration
- ⏳ Biometric authentication
- ⏳ Rich text editor
- ⏳ Photo uploads
- ⏳ Calendar view
- ⏳ Mood tracking
- ⏳ Streak tracking

## 🤝 Contributing

This is a personal project, but suggestions and feedback are welcome!

## 📄 License

[Add your license here]

## 🙏 Acknowledgments

- Expo team for the amazing framework
- Firebase for backend services
- Supabase for image storage
- All open-source library maintainers
