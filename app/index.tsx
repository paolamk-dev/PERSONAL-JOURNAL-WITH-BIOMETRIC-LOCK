/**
 * Entry Point / Splash Screen
 * Initial screen that checks authentication and biometric status
 */

import { useEffect } from 'react';
import { View, Text, ActivityIndicator } from 'react-native';
import { useRouter } from 'expo-router';

export default function Index() {
  const router = useRouter();

  useEffect(() => {
    // TODO: Check authentication status
    // TODO: Check biometric lock status
    // For now, navigate to auth
    setTimeout(() => {
      router.replace('/(auth)/login');
    }, 1500);
  }, []);

  return (
    <View className="flex-1 items-center justify-center bg-primary">
      <Text className="text-white text-4xl font-bold mb-4">
        Luminary Journal
      </Text>
      <ActivityIndicator size="large" color="#ffffff" />
    </View>
  );
}
