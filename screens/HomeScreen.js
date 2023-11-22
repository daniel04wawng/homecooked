import React from 'react'
import { StyleSheet, Text, View, SafeAreaView, Image} from 'react-native'
import tw from "tailwind-react-native-classnames";
import NavOptions from  '../components/NavOptions';

const HomeScreen = () => {
    return (
      <SafeAreaView style={tw`bg-white h-full`}>
        <View style>
          <Image
            source={require('./HomeCooked.png')} // Assuming HomeCooked.jpg is in the same directory as your component file
            style={{ 
                width: 100, 
                height: 100, 
                resizeMode: 'contain',
            }} // Adjust the dimensions as needed
          />

          <NavOptions />
        </View>
      </SafeAreaView>
    );
  };
  
  export default HomeScreen;

const styles = StyleSheet.create({})