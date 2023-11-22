import React, { useState } from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { CheckBox, Input } from 'react-native-elements';

const GenerateRecipeScreen = () => {
    const [dietaryRestrictions, setDietaryRestrictions] = useState({
        vegetarian: false,
        vegan: false,
        glutenFree: false,
        dairyFree: false,
        other: false,
    });
    const [otherText, setOtherText] = useState('');

    const handleCheckBoxToggle = (restriction) => {
        setDietaryRestrictions((prevRestrictions) => ({
            ...prevRestrictions,
            [restriction]: !prevRestrictions[restriction],
        }));

        // If "Other" is unchecked, clear the otherText state
        if (restriction === 'other' && !dietaryRestrictions.other) {
            setOtherText('');
        }
    };

    const handleGenerateRecipe = () => {
        // Implement the logic to generate a recipe based on the user input and dietary restrictions
        console.log('Dietary restrictions:', dietaryRestrictions);
        console.log('Other text:', otherText);
        // Add your logic here to generate a recipe using the dietary restrictions
    };

    return (
        <View style={styles.container}>
            <Text>
                Enter any Dietary Restrictions
            </Text>
            <CheckBox
                title="Vegetarian"
                checked={dietaryRestrictions.vegetarian}
                onPress={() => handleCheckBoxToggle('vegetarian')}
            />
            <CheckBox
                title="Vegan"
                checked={dietaryRestrictions.vegan}
                onPress={() => handleCheckBoxToggle('vegan')}
            />
            <CheckBox
                title="Gluten-Free"
                checked={dietaryRestrictions.glutenFree}
                onPress={() => handleCheckBoxToggle('glutenFree')}
            />
            <CheckBox
                title="Dairy-Free"
                checked={dietaryRestrictions.dairyFree}
                onPress={() => handleCheckBoxToggle('dairyFree')}
            />
            <CheckBox
                title="Other"
                checked={dietaryRestrictions.other}
                onPress={() => handleCheckBoxToggle('other')}
            />
            {dietaryRestrictions.other && (
                <Input
                    placeholder="Specify other dietary restriction"
                    onChangeText={(text) => setOtherText(text)}
                    value={otherText}
                />
            )}
            <Button
                title="Next"
                onPress={handleGenerateRecipe}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
});

export default GenerateRecipeScreen;
