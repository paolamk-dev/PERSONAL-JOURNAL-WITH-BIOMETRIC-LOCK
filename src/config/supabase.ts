/**
 * Supabase Configuration
 * Initialize and export Supabase client for image storage
 */

import { createClient } from '@supabase/supabase-js';
import Constants from 'expo-constants';

// Supabase configuration from environment variables
const supabaseUrl = Constants.expoConfig?.extra?.EXPO_PUBLIC_SUPABASE_URL || process.env.EXPO_PUBLIC_SUPABASE_URL || '';
const supabaseAnonKey = Constants.expoConfig?.extra?.EXPO_PUBLIC_SUPABASE_ANON_KEY || process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY || '';

// Validate Supabase configuration
const validateSupabaseConfig = () => {
  if (!supabaseUrl || !supabaseAnonKey) {
    console.warn('Missing Supabase configuration.');
    console.warn('Please update your .env file with valid Supabase credentials.');
  }
};

validateSupabaseConfig();

// Initialize Supabase client
export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    persistSession: false, // We're using Firebase for auth
  },
});

// Supabase storage constants
export const STORAGE_BUCKET = 'journal-photos';
export const SIGNED_URL_EXPIRY = 3600; // 1 hour in seconds
