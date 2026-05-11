/**
 * Home Screen
 * Main feed showing recent journal entries
 */

import { View, Text, TouchableOpacity, ScrollView } from 'react-native';
import { useRouter } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';

export default function HomeScreen() {
  const router = useRouter();

  return (
    <View className="flex-1 bg-gray-50">
      {/* Header */}
      <View className="bg-white px-6 pt-12 pb-4 border-b border-gray-200">
        <View className="flex-row justify-between items-center">
          <View>
            <Text className="text-2xl font-bold text-gray-900">My Journal</Text>
            <Text className="text-gray-600 mt-1">Welcome back!</Text>
          </View>
          <TouchableOpacity
            className="bg-primary rounded-full w-12 h-12 items-center justify-center"
            onPress={() => router.push('/entry/new')}
          >
            <Ionicons name="add" size={28} color="white" />
          </TouchableOpacity>
        </View>
      </View>

      {/* Streak Card */}
      <View className="mx-6 mt-4 bg-gradient-to-r from-primary to-secondary rounded-xl p-4">
        <View className="flex-row items-center justify-between">
          <View>
            <Text className="text-white text-lg font-semibold">Writing Streak</Text>
            <Text className="text-white/80 mt-1">Keep up the great work!</Text>
          </View>
          <View className="bg-white/20 rounded-full px-6 py-3">
            <Text className="text-white text-3xl font-bold">0</Text>
            <Text className="text-white/80 text-xs text-center">days</Text>
          </View>
        </View>
      </View>

      {/* Entries List */}
      <ScrollView className="flex-1 px-6 mt-4">
        <Text className="text-gray-900 font-semibold text-lg mb-3">Recent Entries</Text>

        {/* Empty State */}
        <View className="items-center justify-center py-12">
          <Ionicons name="book-outline" size={64} color="#D1D5DB" />
          <Text className="text-gray-500 text-center mt-4 text-base">
            No entries yet
          </Text>
          <Text className="text-gray-400 text-center mt-2">
            Tap the + button to create your first entry
          </Text>
        </View>
      </ScrollView>
    </View>
  );
}
