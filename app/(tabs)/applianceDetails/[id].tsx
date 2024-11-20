// import React from 'react';
// import { StyleSheet, View, Text } from 'react-native';
// import { useLocalSearchParams } from 'expo-router';

// export default function ApplianceDetails() {
//   const params = useLocalSearchParams();
//   const { name, brand, model, current_status } = params;

//   // 解析 repairs 和 investments 参数
//   const repairs = params.repairs ? JSON.parse(params.repairs as string) : [];
//   const investments = params.investments ? JSON.parse(params.investments as string) : [];

//   return (
//     <View style={styles.container}>
//       <Text style={styles.title}>{name}</Text>
//       <Text>Brand: {brand}</Text>
//       <Text>Model: {model}</Text>
//       <Text>Status: {current_status}</Text>
//       <Text>Repairs:</Text>
//       {repairs.length > 0 ? (
//         repairs.map((repair: any, index: number) => (
//           <View key={index} style={styles.detailContainer}>
//             <Text>Date: {repair.repair_date}</Text>
//             <Text>Description: {repair.repaired_description}</Text>
//             <Text>Cost: ${repair.cost}</Text>
//           </View>
//         ))
//       ) : (
//         <Text>No repair history.</Text>
//       )}
//       <Text>Investments:</Text>
//       {investments.length > 0 ? (
//         investments.map((investment: any, index: number) => (
//           <View key={index} style={styles.detailContainer}>
//             <Text>Date: {investment.investment_date}</Text>
//             <Text>Description: {investment.investment_description}</Text>
//             <Text>Cost: ${investment.cost}</Text>
//           </View>
//         ))
//       ) : (
//         <Text>No investment history.</Text>
//       )}
//     </View>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     padding: 16,
//     backgroundColor: '#fff',
//   },
//   title: {
//     fontSize: 20,
//     fontWeight: 'bold',
//     marginBottom: 10,
//   },
//   detailContainer: {
//     marginVertical: 8,
//     padding: 8,
//     backgroundColor: '#f0f0f0',
//     borderRadius: 8,
//   },
// });

import { useLocalSearchParams } from "expo-router";
import { View, Text, StyleSheet } from "react-native";

export default function ApplianceDetails() {
  const { id, name, brand, model, current_status, repairs, investments } = useLocalSearchParams();

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Appliance Details</Text>
      <Text>ID: {id}</Text>
      <Text>Name: {name}</Text>
      <Text>Brand: {brand}</Text>
      <Text>Model: {model}</Text>
      <Text>Status: {current_status}</Text>
      <Text>Repairs: {repairs}</Text>
      <Text>Investments: {investments}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: "#fff",
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 16,
  },
});

