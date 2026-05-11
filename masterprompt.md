# Claude Code Prompt: Biometric Personal Journal App (React Native + Expo)

---

## ROLE

You are a senior React Native / Expo mobile engineer with deep expertise in
biometric authentication, Firebase Firestore, Supabase Storage, local device
security, and production-grade mobile UI/UX. You write clean, scalable,
well-commented code following modern React Native best practices. You think
in phases, never skip error handling, and always consider edge cases specific
to mobile environments (offline state, device compatibility, permissions).

---

## TASK

Build a complete, fully functional **Personal Biometric Journal** mobile
application using React Native and Expo. The app is a private diary where
users authenticate via Face ID or Fingerprint before accessing any content.
The app supports rich text journal entries, daily photo attachments, a
calendar-based entry browser, mood tagging, and writing streaks. Firebase
Firestore is the primary database and Supabase Storage handles all image
uploads. The project must be built in clearly defined phases, each fully
complete and tested before moving to the next.

---

## CONTENT

### Project Identity

- **App Name:** Luminary Journal
- **Platform:** iOS and Android (Expo Managed Workflow)
- **Language:** TypeScript (strict mode)
- **Expo SDK:** 51+
- **Node version:** 18+

---

### Tech Stack (Exact Libraries)

| Concern                  | Library / Tool                                      |
|--------------------------|-----------------------------------------------------|
| Framework                | React Native + Expo SDK 51                          |
| Language                 | TypeScript                                          |
| Navigation               | expo-router (file-based routing)                    |
| Biometric Auth           | expo-local-authentication                           |
| Firebase (DB + Auth)     | firebase (v10 modular SDK)                          |
| Image Storage            | @supabase/supabase-js (Storage Buckets)             |
| Rich Text Editor         | @10play/tentap-editor                               |
| Image Picker             | expo-image-picker                                   |
| File System              | expo-file-system                                    |
| Calendar View            | react-native-calendars                              |
| Secure Storage           | expo-secure-store                                   |
| State Management         | Zustand                                             |
| Styling                  | NativeWind (TailwindCSS for React Native)           |
| Icons                    | @expo/vector-icons (Ionicons)                       |
| Date Handling            | date-fns                                            |
| Unique IDs               | uuid                                                |
| Image Compression        | expo-image-manipulator                              |
| Notifications (streaks)  | expo-notifications                                  |
| Splash / Assets          | expo-splash-screen                                  |
| Env Variables            | expo-constants + .env via app.config.ts             |

---

### Firebase Setup (Firestore)

#### Collections & Data Models

**Collection: `users/{userId}`**
```ts
{
  uid: string;
  email: string;
  displayName: string;
  createdAt: Timestamp;
  streakCount: number;
  lastEntryDate: string; // "YYYY-MM-DD"
  totalEntries: number;
  biometricEnabled: boolean;
  autoLockSeconds: number; // default: 60
}
```

**Collection: `users/{userId}/entries/{entryId}`**
```ts
{
  id: string;
  title: string;
  bodyHTML: string;        // rich text stored as HTML string
  plainText: string;       // stripped version for search indexing
  mood: "happy" | "neutral" | "sad" | "angry" | "excited" | "anxious";
  moodEmoji: string;       // e.g. "😊"
  date: string;            // "YYYY-MM-DD"
  createdAt: Timestamp;
  updatedAt: Timestamp;
  wordCount: number;
  readTimeMinutes: number;
  photos: PhotoAttachment[];
  coverPhotoUrl: string | null;
  tags: string[];
  isPinned: boolean;
  isFavorite: boolean;
}
```

**Type: `PhotoAttachment`**
```ts
{
  id: string;
  url: string;            // Supabase public URL
  storagePath: string;    // path inside Supabase bucket
  caption: string;
  width: number;
  height: number;
  uploadedAt: Timestamp;
}
```

**Collection: `users/{userId}/moods/{YYYY-MM-DD}`**
```ts
{
  date: string;
  mood: string;
  moodEmoji: string;
  entryId: string;
}
```

---

### Supabase Setup (Storage)

- **Bucket name:** `journal-photos`
- **Bucket type:** Private (accessed via signed URLs)
- **Storage path pattern:** `{userId}/{entryId}/{photoId}.jpg`
- **Image handling rules:**
  - Compress all images to max 1200px width before upload
  - Convert to JPEG at 80% quality using expo-image-manipulator
  - Generate a signed URL (valid for 1 hour) when rendering
  - On entry deletion, delete all associated Supabase files
  - On photo removal from an entry, delete the specific Supabase file

---

### App Architecture & Folder Structure