import React, { useState } from 'react';
import {
  StyleSheet,
  View,
  Text,
  TextInput,
  Button,
  Image,
  ScrollView,
  Alert,
} from 'react-native';
import { getBingWallPapers } from '@/utils/api';

interface BingImage {
  url: string;
  title: string;
  caption: string;
}

export default function Index() {
  const [idx, setIdx] = useState<number>(0); // 日期范围
  const [n, setN] = useState<number>(1); // 图片数量
  const [images, setImages] = useState<BingImage[]>([]); // 图片数据

  const fetchImages = async () => {
    if (idx < 0 || idx > 7 || n < 1 || n > 8) {
      Alert.alert(
        'Invalid Input',
        'Please select a valid date range (0-7) and number of images (1-8).',
      );
      return;
    }

    try {
      const fetchedImages = await getBingWallPapers(idx, n);
      console.log('Fetched Images:', fetchedImages); // 打印返回数据
      setImages(fetchedImages);
    } catch (error) {
      console.error('Error fetching wallpapers:', error);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Today's Wallpaper</Text>

      {/* 用户输入部分 */}
      {/* <View style={styles.inputContainer}>
        <Text>Date Range (0 - 7):</Text>
        <TextInput
          style={styles.input}
          keyboardType="number-pad"
          placeholder="Enter idx (e.g., 0 for today)"
          value={idx.toString()}
          onChangeText={(text) => setIdx(Number(text) || 0)}
        />
      </View>
      <View style={styles.inputContainer}>
        <Text>Number of Images (1 - 18):</Text>
        <TextInput
          style={styles.input}
          keyboardType="number-pad"
          placeholder="Enter n (e.g., 3)"
          value={n.toString()}
          onChangeText={(text) => {
            const number = Number(text);
            if (number >= 1 && number <= 8) {
              setN(number); // 仅当输入值有效时更新状态
            } else {
              Alert.alert('Invalid Input', 'Please enter a value between 1 and 8.');
            }
          }}
        />
      </View> */}

      <View style={styles.inputContainer}>
        <Text>Date Range (0 - 7):</Text>
        <TextInput
          style={styles.input}
          keyboardType="number-pad"
          placeholder="Enter idx (e.g., 0 for today)"
          value={idx.toString()} // 绑定到状态 idx
          onChangeText={(text) => {
            const number = Number(text);
            if (!isNaN(number)) {
              setIdx(number); // 更新 idx 的状态
            }
          }}
        />
      </View>

      <View style={styles.inputContainer}>
        <Text>Number of Images (1 - 8):</Text>
        <TextInput
          style={styles.input}
          keyboardType="number-pad"
          placeholder="Enter n (e.g., 3)"
          value={n.toString()} // 绑定到状态 n
          onChangeText={(text) => {
            const number = Number(text);
            if (!isNaN(number)) {
              setN(number); // 更新 n 的状态
            }
          }}
        />
      </View>



      {/* 按钮触发 */}
      <Button title="Fetch Bing Images" onPress={fetchImages} />

      {/* 图片列表 */}
      <ScrollView>
        {images.map((image, index) => (
          <View key={index} style={styles.imageContainer}>
            <Image
              source={{ uri: image.url }}
              style={styles.image}
              onError={() => console.error(`Failed to load image: ${image.url}`)}
            />
            <Text style={styles.imageTitle}>{image.title}</Text>
            <Text style={styles.imageCaption}>{image.caption}</Text>
          </View>
        ))}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  inputContainer: {
    marginBottom: 20,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 8,
    borderRadius: 4,
    marginTop: 5,
  },
  imageContainer: {
    marginBottom: 16,
    alignItems: 'center',
  },
  image: {
    width: '100%',
    height: 200, // 必须设置高度
    borderRadius: 8,
  },
  imageTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 8,
  },
  imageCaption: {
    fontSize: 14,
    color: '#555',
    marginTop: 4,
    textAlign: 'center',
  },
});
