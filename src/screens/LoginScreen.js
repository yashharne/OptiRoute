import React, { useState, useEffect } from "react";
import { TouchableOpacity, StyleSheet, View } from "react-native";
import { Text } from "react-native-paper";
import Background from "../components/Background";
import Logo from "../components/Logo";
import Header from "../components/Header";
import Button from "../components/Button";
import TextInput from "../components/TextInput";
import BackButton from "../components/BackButton";
import { theme } from "../core/theme";
import { emailValidator } from "../helpers/emailValidator";
import { passwordValidator } from "../helpers/passwordValidator";
import Geolocation from "react-native-geolocation-service";

// ...

export default function LoginScreen({ navigation }) {
  const [email, setEmail] = useState({ value: "", error: "" });
  const [password, setPassword] = useState({ value: "", error: "" });

  // const onLoginPressed = () => {
  //   const emailError = emailValidator(email.value);
  //   const passwordError = passwordValidator(password.value);
  //   if (emailError || passwordError) {
  //     setEmail({ ...email, error: emailError });
  //     setPassword({ ...password, error: passwordError });
  //     return;
  //   }
  //   navigation.reset({
  //     index: 0,
  //     routes: [{ name: "Dashboard" }],
  //   });
  // };

  const onLoginPressed = () => {
    const emailError = emailValidator(email.value);
    const passwordError = passwordValidator(password.value);
    if (emailError || passwordError) {
      setEmail({ ...email, error: emailError });
      setPassword({ ...password, error: passwordError });
      return;
    }

    navigation.reset({
      index: 0,
      routes: [
        {
          name: "Dashboard",
        },
      ],
    });

    // Request the user's location
    // Geolocation.getCurrentPosition(
    //   (position) => {
    //     // Get the latitude and longitude from the position
    //     const { latitude, longitude } = position.coords;

    //     // Navigate to the "Dashboard" screen while passing user location
    //     navigation.reset({
    //       index: 0,
    //       routes: [
    //         {
    //           name: "Dashboard",
    //           params: {
    //             userLocation: { latitude, longitude },
    //           },
    //         },
    //       ],
    //     });
    //     // navigation.navigate("Dashboard", { userLocation });
    //   },
    //   (error) => {
    //     // Handle location request error here
    //     console.log("Location request error: ", error);
    //     // You may choose to navigate to the "Dashboard" without location
    // navigation.reset({
    //   index: 0,
    //   routes: [
    //     {
    //       name: "Dashboard",
    //       params: {
    //         userLocation: null, // Pass null when location request fails
    //       },
    //     },
    //   ],
    // });
    //   },
    //   { enableHighAccuracy: true, timeout: 15000, maximumAge: 10000 }
    // );
  };

  return (
    <Background>
      <BackButton goBack={navigation.goBack} />
      <Logo />
      <Header textcolor="#09bdab">OPTIROUTE</Header>
      <Header>Welcome back.</Header>
      <TextInput
        label="Email"
        returnKeyType="next"
        value={email.value}
        onChangeText={(text) => setEmail({ value: text, error: "" })}
        error={!!email.error}
        errorText={email.error}
        autoCapitalize="none"
        autoCompleteType="email"
        textContentType="emailAddress"
        keyboardType="email-address"
      />
      <TextInput
        label="Password"
        returnKeyType="done"
        value={password.value}
        onChangeText={(text) => setPassword({ value: text, error: "" })}
        error={!!password.error}
        errorText={password.error}
        secureTextEntry
      />
      <View style={styles.forgotPassword}>
        <TouchableOpacity
          onPress={() => navigation.navigate("ResetPasswordScreen")}
        >
          <Text style={styles.forgot}>Forgot your password?</Text>
        </TouchableOpacity>
      </View>
      <Button mode="contained" onPress={onLoginPressed} textcolor={"#ffffff"}>
        Login
      </Button>
      <View style={styles.row}>
        <Text>Don’t have an account? </Text>
        <TouchableOpacity onPress={() => navigation.replace("RegisterScreen")}>
          <Text style={styles.link}>Sign up</Text>
        </TouchableOpacity>
      </View>
    </Background>
  );
}

const styles = StyleSheet.create({
  forgotPassword: {
    width: "100%",
    alignItems: "flex-end",
    marginBottom: 24,
  },
  row: {
    flexDirection: "row",
    marginTop: 4,
  },
  forgot: {
    fontSize: 13,
    color: theme.colors.secondary,
  },
  link: {
    fontWeight: "bold",
    color: theme.colors.primary,
  },
});
