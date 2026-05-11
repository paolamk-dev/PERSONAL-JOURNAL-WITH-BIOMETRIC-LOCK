/**
 * Mood Screen
 * Mood tracking and analytics
 */

import { View, Text } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

export default function MoodScreen() {
  return (
    <View className="flex-1 bg-gray-50">
      {/* Header */}
      <View className="bg-white px-6 pt-12 pb-4 border-b border-gray-200">
        <Text className="text-2xl font-bold text-gray-900">Mood Tracker</Text>
        <Text className="text-gray-600 mt-1">Track your emotional journey</Text>
      </View>

      {/* Placeholder */}
      <View className="flex-1 items-center justify-center">
        <Ionicons name="happy-outline" size={64} color="#D1D5DB" />
        <Text className="text-gray-500 text-center mt-4 text-base">
          Mood tracking coming soon
        </Text>
      </View>
    </View>
  );
}
