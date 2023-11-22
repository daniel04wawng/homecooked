import React from "react";
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { Provider } from 'react-redux'
import { store } from './store';
import HomeScreen from './screens/HomeScreen';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import GenerateRecipeScreen from "./screens/GenerateRecipeScreen";
import CalendarScreen from "./screens/CalendarScreen";

export default function App() {
  const Stack = createStackNavigator();

  return (
    <Provider store={store}>
  <NavigationContainer>
    <SafeAreaProvider>
      <Stack.Navigator initialRouteName="HomeScreen">
        <Stack.Screen
          name='HomeScreen' 
          component={HomeScreen} 
          options={{
            headerShown:false, 
          }}
        />
        <Stack.Screen
          name='GenerateRecipeScreen' 
          component={GenerateRecipeScreen} 
          options={{
            headerShown:false, 
          }}
        />
        <Stack.Screen
          name='CalendarScreen' 
          component={CalendarScreen} 
          options={{
            headerShown:false, 
          }}
        />
      </Stack.Navigator>
    </SafeAreaProvider>
  </NavigationContainer>  
</Provider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
