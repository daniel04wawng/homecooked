import React from 'react';
import { FlatList, StyleSheet, Text, View, TouchableOpacity, ImageBackground } from 'react-native';
import tw from "tailwind-react-native-classnames"; 
import { Icon } from 'react-native-elements';
import { useNavigation } from '@react-navigation/native';

const data = [
  {
    id: '123',
    title: 'Generate Recipes',
    image: require('./Food-Picture.png'),
    screen: "GenerateRecipeScreen"
  },
  {
    id: '456',
    title: 'View Calendar',
    image: require('./Calendar-Picture.png'),
    screen: 'CalendarScreen'
  }
];


const NavOptions = () => {
    const navigation = useNavigation();

    return (
      <FlatList
        data={data}
        keyExtractor={(item) => item.id}
        horizontal
        renderItem={({ item }) => (
          <TouchableOpacity
          onPress={() => navigation.navigate(item.screen)}  
          style={tw`p-2 pl-4 pb-3 pt-4 bg-gray-200 m-2 w-40`}
          >
            <View>
              <ImageBackground
                source={item.image}
                style={{
                  width: 120,
                  height: 120,
                  resizeMode: "contain",
                }}
              >
                {/* Empty view for image background */}
              </ImageBackground>
              <View style={{ marginTop: 10 }}>
                {/* Other content or components can be added here */}
                <Text style={tw`mt-2 font-semibold`}>
                  {item.title}
                </Text>
                <Icon
                  style={tw`p-2 bg-black rounded-full w-10 mt-4`} // Move style inside Icon component
                  name='arrowright' 
                  color='white' 
                  type='antdesign'
                />
              </View>
            </View>
          </TouchableOpacity>
        )}
      />
    );
  };

export default NavOptions;

const styles = StyleSheet.create({});