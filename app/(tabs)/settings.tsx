/**
 * Settings Screen
 * App settings and user preferences
 */

import { View, Text, TouchableOpacity, ScrollView, Alert } from 'react-native';
import { useRouter } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';

export default function SettingsScreen() {
  const router = useRouter();

  const handleLogout = () => {
    Alert.alert(
      'Logout',
      'Are you sure you want to logout?',
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Logout',
          style: 'destructive',
          onPress: () => {
            // TODO: Implement logout
            router.replace('/(auth)/login');
          },
        },
      ]
    );
  };

  return (
    <View className="flex-1 bg-gray-50">
      {/* Header */}
      <View className="bg-white px-6 pt-12 pb-4 border-b border-gray-200">
        <Text className="text-2xl font-bold text-gray-900">Settings</Text>
        <Text className="text-gray-600 mt-1">Manage your preferences</Text>
      </View>

      <ScrollView className="flex-1">
        {/* Account Section */}
        <View className="mt-6 bg-white">
          <View className="px-6 py-3 border-b border-gray-200">
            <Text className="text-gray-500 text-xs font-semibold uppercase">Account</Text>
          </View>

          <TouchableOpacity className="flex-row items-center px-6 py-4 border-b border-gray-200">
            <Ionicons name="person-outline" size={24} color="#6B7280" />
            <Text className="text-gray-900 text-base ml-4 flex-1">Profile</Text>
            <Ionicons name="chevron-forward" size={20} color="#9CA3AF" />
          </TouchableOpacity>
        </View>

        {/* Security Section */}
        <View className="mt-6 bg-white">
          <View className="px-6 py-3 border-b border-gray-200">
            <Text className="text-gray-500 text-xs font-semibold uppercase">Security</Text>
          </View>

          <TouchableOpacity className="flex-row items-center px-6 py-4 border-b border-gray-200">
            <Ionicons name="finger-print" size={24} color="#6B7280" />
            <Text className="text-gray-900 text-base ml-4 flex-1">Biometric Lock</Text>
            <Ionicons name="chevron-forward" size={20} color="#9CA3AF" />
          </TouchableOpacity>

          <TouchableOpacity className="flex-row items-center px-6 py-4 border-b border-gray-200">
            <Ionicons name="time-outline" size={24} color="#6B7280" />
            <Text className="text-gray-900 text-base ml-4 flex-1">Auto-Lock Timer</Text>
            <Ionicons name="chevron-forward" size={20} color="#9CA3AF" />
          </TouchableOpacity>
        </View>

        {/* App Section */}
        <View className="mt-6 bg-white">
          <View className="px-6 py-3 border-b border-gray-200">
            <Text className="text-gray-500 text-xs font-semibold uppercase">App</Text>
          </View>

          <TouchableOpacity className="flex-row items-center px-6 py-4 border-b border-gray-200">
            <Ionicons name="notifications-outline" size={24} color="#6B7280" />
            <Text className="text-gray-900 text-base ml-4 flex-1">Notifications</Text>
            <Ionicons name="chevron-forward" size={20} color="#9CA3AF" />
          </TouchableOpacity>

          <TouchableOpacity className="flex-row items-center px-6 py-4 border-b border-gray-200">
            <Ionicons name="information-circle-outline" size={24} color="#6B7280" />
            <Text className="text-gray-900 text-base ml-4 flex-1">About</Text>
            <Ionicons name="chevron-forward" size={20} color="#9CA3AF" />
          </TouchableOpacity>
        </View>

        {/* Logout Button */}
        <View className="mt-6 mx-6 mb-6">
          <TouchableOpacity
            className="bg-red-500 rounded-lg py-4 items-center"
            onPress={handleLogout}
          >
            <Text className="text-white font-semibold text-base">Logout</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </View>
  );
}
