/**
 * Entry Detail Screen
 * View and edit an existing journal entry
 */

import { View, Text, ScrollView, TouchableOpacity } from 'react-native';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';

export default function EntryDetailScreen() {
  const router = useRouter();
  const { id } = useLocalSearchParams();

  return (
    <View className="flex-1 bg-white">
      {/* Header */}
      <View className="px-6 pt-12 pb-4 border-b border-gray-200">
        <View className="flex-row items-center justify-between">
          <TouchableOpacity onPress={() => router.back()}>
            <Ionicons name="arrow-back" size={28} color="#374151" />
          </TouchableOpacity>
          <View className="flex-row items-center">
            <TouchableOpacity className="mr-4">
              <Ionicons name="create-outline" size={24} color="#6B7280" />
            </TouchableOpacity>
            <TouchableOpacity>
              <Ionicons name="ellipsis-horizontal" size={24} color="#6B7280" />
            </TouchableOpacity>
          </View>
        </View>
      </View>

      <ScrollView className="flex-1 px-6 pt-6">
        {/* Entry Header */}
        <Text className="text-gray-500 text-sm mb-2">Today, 10:30 AM</Text>
        <Text className="text-3xl font-bold text-gray-900 mb-4">
          Sample Entry {id}
        </Text>

        {/* Mood Badge */}
        <View className="flex-row mb-6">
          <View className="bg-yellow-100 rounded-full px-3 py-1 flex-row items-center">
            <Text className="mr-1">😊</Text>
            <Text className="text-yellow-800 text-sm font-medium">Happy</Text>
          </View>
        </View>

        {/* Content */}
        <Text className="text-base text-gray-700 leading-6">
          This is a placeholder entry. The actual entry content will be loaded from Firestore.
          {'\n\n'}
          In a complete implementation, this screen would display the full entry with all its
          details including photos, tags, and rich text formatting.
        </Text>
      </ScrollView>
    </View>
  );
}
