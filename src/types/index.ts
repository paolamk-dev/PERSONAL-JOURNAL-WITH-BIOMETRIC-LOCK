/**
 * Type Definitions for Luminary Journal App
 * All TypeScript interfaces and types used throughout the application
 */

import { Timestamp } from 'firebase/firestore';

// ============================================================================
// User Types
// ============================================================================

export interface User {
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

// ============================================================================
// Entry Types
// ============================================================================

export type MoodType = 'happy' | 'neutral' | 'sad' | 'angry' | 'excited' | 'anxious';

export interface PhotoAttachment {
  id: string;
  url: string; // Supabase public URL
  storagePath: string; // path inside Supabase bucket
  caption: string;
  width: number;
  height: number;
  uploadedAt: Timestamp;
}

export interface JournalEntry {
  id: string;
  title: string;
  bodyHTML: string; // rich text stored as HTML string
  plainText: string; // stripped version for search indexing
  mood: MoodType;
  moodEmoji: string; // e.g. "😊"
  date: string; // "YYYY-MM-DD"
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

// ============================================================================
// Mood Tracking Types
// ============================================================================

export interface MoodEntry {
  date: string; // "YYYY-MM-DD"
  mood: MoodType;
  moodEmoji: string;
  entryId: string;
}

// ============================================================================
// Mood Metadata
// ============================================================================

export interface MoodMetadata {
  type: MoodType;
  emoji: string;
  label: string;
  color: string;
}

export const MOOD_OPTIONS: Record<MoodType, MoodMetadata> = {
  happy: { type: 'happy', emoji: '😊', label: 'Happy', color: '#FFD700' },
  neutral: { type: 'neutral', emoji: '😐', label: 'Neutral', color: '#A0AEC0' },
  sad: { type: 'sad', emoji: '😢', label: 'Sad', color: '#4299E1' },
  angry: { type: 'angry', emoji: '😠', label: 'Angry', color: '#F56565' },
  excited: { type: 'excited', emoji: '🤩', label: 'Excited', color: '#F687B3' },
  anxious: { type: 'anxious', emoji: '😰', label: 'Anxious', color: '#9F7AEA' },
};

// ============================================================================
// Authentication Types
// ============================================================================

export interface BiometricAuthResult {
  success: boolean;
  error?: string;
  biometricType?: 'fingerprint' | 'facial' | 'iris';
}

export interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isBiometricLocked: boolean;
  loading: boolean;
}

// ============================================================================
// Form Types
// ============================================================================

export interface EntryFormData {
  title: string;
  bodyHTML: string;
  mood: MoodType;
  tags: string[];
  photos: PhotoAttachment[];
  isPinned: boolean;
  isFavorite: boolean;
}

// ============================================================================
// Storage Types
// ============================================================================

export interface ImageUploadResult {
  success: boolean;
  url?: string;
  storagePath?: string;
  error?: string;
}

export interface ImageUploadProgress {
  loaded: number;
  total: number;
  percentage: number;
}

// ============================================================================
// Navigation Types (for expo-router)
// ============================================================================

export type RootStackParamList = {
  index: undefined;
  '(auth)/login': undefined;
  '(auth)/register': undefined;
  '(tabs)': undefined;
  '(tabs)/home': undefined;
  '(tabs)/calendar': undefined;
  '(tabs)/mood': undefined;
  '(tabs)/settings': undefined;
  'entry/[id]': { id: string };
  'entry/new': undefined;
};

// ============================================================================
// Error Types
// ============================================================================

export interface AppError {
  code: string;
  message: string;
  details?: unknown;
}

// ============================================================================
// Utility Types
// ============================================================================

export type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

export type RequireAtLeastOne<T, Keys extends keyof T = keyof T> = Pick<
  T,
  Exclude<keyof T, Keys>
> &
  {
    [K in Keys]-?: Required<Pick<T, K>> & Partial<Pick<T, Exclude<Keys, K>>>;
  }[Keys];
