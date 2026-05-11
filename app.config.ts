import { ConfigContext, ExpoConfig } from 'expo/config';

export default ({ config }: ConfigContext): ExpoConfig => ({
  ...config,
  name: 'Luminary Journal',
  slug: 'luminary-journal',
  version: '1.0.0',
  orientation: 'portrait',
  icon: './assets/icon.png',
  userInterfaceStyle: 'light',
  newArchEnabled: true,
  scheme: 'luminary-journal',
  splash: {
    image: './assets/splash-icon.png',
    resizeMode: 'contain',
    backgroundColor: '#6366F1',
  },
  ios: {
    supportsTablet: true,
    bundleIdentifier: 'com.luminaryjournal.app',
    infoPlist: {
      NSFaceIDUsageDescription: 'We use Face ID to securely access your personal journal.',
      NSCameraUsageDescription: 'We need access to your camera to add photos to your journal entries.',
      NSPhotoLibraryUsageDescription: 'We need access to your photo library to add photos to your journal entries.',
    },
  },
  android: {
    adaptiveIcon: {
      foregroundImage: './assets/adaptive-icon.png',
      backgroundColor: '#6366F1',
    },
    package: 'com.luminaryjournal.app',
    permissions: [
      'USE_BIOMETRIC',
      'USE_FINGERPRINT',
      'CAMERA',
      'READ_EXTERNAL_STORAGE',
      'WRITE_EXTERNAL_STORAGE',
    ],
  },
  web: {
    favicon: './assets/favicon.png',
  },
  plugins: [
    'expo-router',
    [
      'expo-local-authentication',
      {
        faceIDPermission: 'Allow Luminary Journal to use Face ID to securely access your journal.',
      },
    ],
    [
      'expo-image-picker',
      {
        photosPermission: 'Allow Luminary Journal to access your photos to add them to your journal entries.',
        cameraPermission: 'Allow Luminary Journal to use your camera to take photos for your journal entries.',
      },
    ],
  ],
  extra: {
    EXPO_PUBLIC_FIREBASE_API_KEY: process.env.EXPO_PUBLIC_FIREBASE_API_KEY,
    EXPO_PUBLIC_FIREBASE_AUTH_DOMAIN: process.env.EXPO_PUBLIC_FIREBASE_AUTH_DOMAIN,
    EXPO_PUBLIC_FIREBASE_PROJECT_ID: process.env.EXPO_PUBLIC_FIREBASE_PROJECT_ID,
    EXPO_PUBLIC_FIREBASE_STORAGE_BUCKET: process.env.EXPO_PUBLIC_FIREBASE_STORAGE_BUCKET,
    EXPO_PUBLIC_FIREBASE_MESSAGING_SENDER_ID: process.env.EXPO_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
    EXPO_PUBLIC_FIREBASE_APP_ID: process.env.EXPO_PUBLIC_FIREBASE_APP_ID,
    EXPO_PUBLIC_SUPABASE_URL: process.env.EXPO_PUBLIC_SUPABASE_URL,
    EXPO_PUBLIC_SUPABASE_ANON_KEY: process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY,
    eas: {
      projectId: 'your-eas-project-id', // Update this when setting up EAS
    },
  },
});
