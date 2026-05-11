/**
 * New Entry Screen
 * Create a new journal entry
 */

import { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  Alert,
} from 'react-native';
import { useRouter } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';

export default function NewEntryScreen() {
  const router = useRouter();
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [saving, setSaving] = useState(false);

  const handleSave = async () => {
    if (!title.trim() || !content.trim()) {
      Alert.alert('Error', 'Please add a title and content to your entry');
      return;
    }

    setSaving(true);
    // TODO: Save entry to Firestore
    setTimeout(() => {
      setSaving(false);
      Alert.alert('Success', 'Entry saved successfully!', [
        { text: 'OK', onPress: () => router.back() },
      ]);
    }, 1000);
  };

  const handleCancel = () => {
    if (title.trim() || content.trim()) {
      Alert.alert(
        'Discard Entry?',
        'Are you sure you want to discard this entry?',
        [
          { text: 'Keep Editing', style: 'cancel' },
          { text: 'Discard', style: 'destructive', onPress: () => router.back() },
        ]
      );
    } else {
      router.back();
    }
  };

  return (
    <View className="flex-1 bg-white">
      {/* Header */}
      <View className="px-6 pt-12 pb-4 border-b border-gray-200">
        <View className="flex-row items-center justify-between">
          <TouchableOpacity onPress={handleCancel}>
            <Ionicons name="close" size={28} color="#374151" />
          </TouchableOpacity>
          <Text className="text-lg font-semibold text-gray-900">New Entry</Text>
          <TouchableOpacity
            onPress={handleSave}
            disabled={saving}
            className={saving ? 'opacity-50' : ''}
          >
            <Text className="text-primary font-semibold text-base">
              {saving ? 'Saving...' : 'Save'}
            </Text>
          </TouchableOpacity>
        </View>
      </View>

      <ScrollView className="flex-1 px-6 pt-6">
        {/* Title Input */}
        <TextInput
          className="text-2xl font-bold text-gray-900 mb-4"
          placeholder="Title"
          placeholderTextColor="#9CA3AF"
          value={title}
          onChangeText={setTitle}
          editable={!saving}
        />

        {/* Content Input */}
        <TextInput
          className="text-base text-gray-700 leading-6"
          placeholder="Start writing your thoughts..."
          placeholderTextColor="#9CA3AF"
          value={content}
          onChangeText={setContent}
          multiline
          textAlignVertical="top"
          editable={!saving}
          style={{ minHeight: 400 }}
        />
      </ScrollView>

      {/* Toolbar */}
      <View className="border-t border-gray-200 px-6 py-3 flex-row items-center justify-around">
        <TouchableOpacity className="items-center p-2">
          <Ionicons name="image-outline" size={24} color="#6B7280" />
        </TouchableOpacity>
        <TouchableOpacity className="items-center p-2">
          <Ionicons name="happy-outline" size={24} color="#6B7280" />
        </TouchableOpacity>
        <TouchableOpacity className="items-center p-2">
          <Ionicons name="pricetag-outline" size={24} color="#6B7280" />
        </TouchableOpacity>
        <TouchableOpacity className="items-center p-2">
          <Ionicons name="star-outline" size={24} color="#6B7280" />
        </TouchableOpacity>
      </View>
    </View>
  );
}
