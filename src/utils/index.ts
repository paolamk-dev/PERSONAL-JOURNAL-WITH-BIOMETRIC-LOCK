/**
 * Utility Functions
 * Reusable helper functions used throughout the app
 */

import { format, parseISO } from 'date-fns';
import { WORDS_PER_MINUTE_READING, DATE_FORMAT, DISPLAY_DATE_FORMAT } from '../constants';

/**
 * Format a date object to YYYY-MM-DD string for database storage
 */
export const formatDateForDB = (date: Date): string => {
  return format(date, DATE_FORMAT);
};

/**
 * Format a date string for display
 */
export const formatDateForDisplay = (dateString: string): string => {
  try {
    const date = parseISO(dateString);
    return format(date, DISPLAY_DATE_FORMAT);
  } catch (error) {
    console.error('Error formatting date:', error);
    return dateString;
  }
};

/**
 * Parse a date string to Date object
 */
export const parseDateString = (dateString: string): Date => {
  return parseISO(dateString);
};

/**
 * Get today's date in YYYY-MM-DD format
 */
export const getTodayDateString = (): string => {
  return formatDateForDB(new Date());
};

/**
 * Strip HTML tags from a string to get plain text
 */
export const stripHTMLTags = (html: string): string => {
  return html.replace(/<[^>]*>/g, '').trim();
};

/**
 * Count words in a text string
 */
export const countWords = (text: string): number => {
  const plainText = stripHTMLTags(text).trim();
  if (!plainText) return 0;
  return plainText.split(/\s+/).length;
};

/**
 * Calculate estimated reading time in minutes
 */
export const calculateReadTime = (text: string): number => {
  const wordCount = countWords(text);
  const minutes = Math.ceil(wordCount / WORDS_PER_MINUTE_READING);
  return Math.max(1, minutes); // Minimum 1 minute
};

/**
 * Truncate text to a specified length with ellipsis
 */
export const truncateText = (text: string, maxLength: number): string => {
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength).trim() + '...';
};

/**
 * Validate email format
 */
export const isValidEmail = (email: string): boolean => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

/**
 * Generate a slug from a title
 */
export const slugify = (text: string): string => {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');
};

/**
 * Calculate streak between two dates
 */
export const calculateStreak = (lastEntryDate: string, todayDate: string): number => {
  try {
    const last = parseISO(lastEntryDate);
    const today = parseISO(todayDate);
    const diffTime = Math.abs(today.getTime() - last.getTime());
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays;
  } catch (error) {
    console.error('Error calculating streak:', error);
    return 0;
  }
};

/**
 * Check if a streak is still active (entry was yesterday or today)
 */
export const isStreakActive = (lastEntryDate: string): boolean => {
  const today = getTodayDateString();
  const daysDiff = calculateStreak(lastEntryDate, today);
  return daysDiff <= 1;
};

/**
 * Format file size in bytes to human-readable format
 */
export const formatFileSize = (bytes: number): string => {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
};

/**
 * Debounce function
 */
export const debounce = <T extends (...args: any[]) => any>(
  func: T,
  wait: number
): ((...args: Parameters<T>) => void) => {
  let timeout: NodeJS.Timeout | null = null;

  return (...args: Parameters<T>) => {
    if (timeout) clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  };
};

/**
 * Deep clone an object
 */
export const deepClone = <T>(obj: T): T => {
  return JSON.parse(JSON.stringify(obj));
};

/**
 * Check if two objects are deeply equal
 */
export const deepEqual = (obj1: any, obj2: any): boolean => {
  return JSON.stringify(obj1) === JSON.stringify(obj2);
};

/**
 * Generate a random ID (fallback if uuid fails)
 */
export const generateRandomId = (): string => {
  return Date.now().toString(36) + Math.random().toString(36).substring(2);
};
