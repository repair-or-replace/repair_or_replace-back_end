import React, { useEffect, useState } from 'react';
import { StyleSheet, View, Text, FlatList, ActivityIndicator, Pressable } from 'react-native';
import { useRouter } from 'expo-router'; // 引入路由
import { fetchPropertyAddresses } from '@/utils/api'; // 导入 API 函数

interface Appliance {
  id: string;
  name: string;
  brand: string;
  model: string;
  current_status: string;
  repairs: any[];
  investments: any[];
}

interface Property {
  id: number;
  address_line_1: string;
  appliances: Appliance[];
}

export default function MeScreen() {
  const [properties, setProperties] = useState<Property[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const router = useRouter(); // 路由实例

  useEffect(() => {
    const loadPropertyAddresses = async () => {
      setLoading(true);
      const fetchedProperties = await fetchPropertyAddresses();
      setProperties(fetchedProperties);
      setLoading(false);
    };

    loadPropertyAddresses();
  }, []);

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#0000ff" />
        <Text>Loading Properties...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Properties and Appliances</Text>
      <FlatList
        data={properties}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.propertyContainer}>
            <Text style={styles.propertyId}>Property ID: {item.id}</Text>
            <Text style={styles.propertyAddress}>Address: {item.address_line_1}</Text>
            <Text style={styles.appliancesTitle}>Appliances:</Text>
            {item.appliances.length > 0 ? (
              <FlatList
                data={item.appliances}
                keyExtractor={(appliance) => appliance.id.toString()}
                renderItem={({ item: appliance }) => (
                  <Pressable
                    onPress={() => {
                      console.log('Navigating to:', {
                        pathname: `/(tabs)/applianceDetails/${appliance.id}`,
                        params: {
                          name: appliance.name,
                          brand: appliance.brand,
                          model: appliance.model,
                          current_status: appliance.current_status,
                          repairs: JSON.stringify(appliance.repairs),
                          investments: JSON.stringify(appliance.investments),
                        },
                      });

                      router.push({
                        // pathname: `/applianceDetails/${appliance.id}`,
                        pathname: '/applianceDetails/[id]',
                        params: {
                          id: appliance.id,
                          name: appliance.name,
                          brand: appliance.brand,
                          model: appliance.model,
                          current_status: appliance.current_status,
                          repairs: JSON.stringify(appliance.repairs),
                          investments: JSON.stringify(appliance.investments),
                        },
                      });
                    }}
                  >
                    <View style={styles.applianceContainer}>
                      <Text style={styles.applianceName}>Name: {appliance.name}</Text>
                      <Text>Brand: {appliance.brand}</Text>
                      <Text>Model: {appliance.model}</Text>
                      <Text>Status: {appliance.current_status}</Text>
                    </View>
                  </Pressable>

                )}
              />
            ) : (
              <Text style={styles.noAppliances}>No appliances found.</Text>
            )}
          </View>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 16,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  propertyContainer: {
    marginBottom: 16,
    padding: 16,
    backgroundColor: '#f9f9f9',
    borderRadius: 8,
  },
  propertyId: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  propertyAddress: {
    fontSize: 14,
    color: '#555',
    marginBottom: 8,
  },
  appliancesTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 8,
  },
  applianceContainer: {
    marginTop: 8,
    padding: 8,
    backgroundColor: '#e9e9e9',
    borderRadius: 8,
  },
  applianceName: {
    fontSize: 14,
    fontWeight: 'bold',
  },
  noAppliances: {
    fontSize: 14,
    color: '#888',
    fontStyle: 'italic',
  },
});
