/**
 * App Constants
 * All application-wide constants and configuration values
 */

// App Information
export const APP_NAME = 'Luminary Journal';
export const APP_VERSION = '1.0.0';

// Biometric Settings
export const DEFAULT_AUTO_LOCK_SECONDS = 60;
export const AUTO_LOCK_OPTIONS = [30, 60, 120, 300, 600]; // 30s, 1m, 2m, 5m, 10m

// Entry Settings
export const WORDS_PER_MINUTE_READING = 200; // Average reading speed
export const MAX_TAGS_PER_ENTRY = 10;
export const MAX_PHOTOS_PER_ENTRY = 10;

// Image Settings
export const MAX_IMAGE_WIDTH = 1200;
export const IMAGE_QUALITY = 0.8; // 80% JPEG quality
export const IMAGE_FORMAT = 'jpeg';

// Storage Settings
export const SUPABASE_BUCKET = 'journal-photos';
export const SIGNED_URL_EXPIRY = 3600; // 1 hour

// Date Formats
export const DATE_FORMAT = 'yyyy-MM-dd'; // For database storage
export const DISPLAY_DATE_FORMAT = 'MMMM d, yyyy'; // For UI display
export const CALENDAR_DATE_FORMAT = 'yyyy-MM-dd';

// Firestore Collection Names
export const COLLECTIONS = {
  USERS: 'users',
  ENTRIES: 'entries',
  MOODS: 'moods',
} as const;

// Error Messages
export const ERROR_MESSAGES = {
  BIOMETRIC_NOT_AVAILABLE: 'Biometric authentication is not available on this device.',
  BIOMETRIC_NOT_ENROLLED: 'No biometric credentials are enrolled. Please set up Face ID or Fingerprint in your device settings.',
  BIOMETRIC_FAILED: 'Biometric authentication failed. Please try again.',
  CAMERA_PERMISSION_DENIED: 'Camera permission is required to take photos.',
  PHOTO_LIBRARY_PERMISSION_DENIED: 'Photo library permission is required to select photos.',
  IMAGE_UPLOAD_FAILED: 'Failed to upload image. Please try again.',
  ENTRY_SAVE_FAILED: 'Failed to save journal entry. Please try again.',
  ENTRY_DELETE_FAILED: 'Failed to delete journal entry. Please try again.',
  NETWORK_ERROR: 'Network error. Please check your connection and try again.',
  UNKNOWN_ERROR: 'An unexpected error occurred. Please try again.',
} as const;

// Success Messages
export const SUCCESS_MESSAGES = {
  ENTRY_SAVED: 'Entry saved successfully!',
  ENTRY_DELETED: 'Entry deleted successfully!',
  PHOTO_UPLOADED: 'Photo uploaded successfully!',
  SETTINGS_SAVED: 'Settings saved successfully!',
} as const;

// Notification Settings
export const NOTIFICATION_CHANNEL = {
  ID: 'streak-reminders',
  NAME: 'Streak Reminders',
  DESCRIPTION: 'Reminders to maintain your writing streak',
} as const;

// Animation Durations (in milliseconds)
export const ANIMATION_DURATION = {
  SHORT: 200,
  MEDIUM: 300,
  LONG: 500,
} as const;

// Pagination
export const ENTRIES_PER_PAGE = 20;

// Search
export const MIN_SEARCH_CHARACTERS = 3;
export const SEARCH_DEBOUNCE_MS = 300;
