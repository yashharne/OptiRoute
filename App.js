import React from "react";
import { Provider } from "react-native-paper";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { theme } from "./src/core/theme";
import { ToastProvider } from "react-native-toast-notifications";
import Toast, { BaseToast, ErrorToast } from "react-native-toast-message";
import { View, Text } from "react-native";
import {
  StartScreen,
  LoginScreen,
  RegisterScreen,
  MapView,
  ResetPasswordScreen,
  Dashboard,
} from "./src/screens";

const toastConfig = {
  success: (props) => (
    <BaseToast
      {...props}
      style={{ borderLeftColor: "pink" }}
      contentContainerStyle={{ paddingHorizontal: 15 }}
      text1Style={{
        fontSize: 15,
        fontWeight: "400",
      }}
    />
  ),
  error: (props) => (
    <ErrorToast
      {...props}
      text1Style={{
        fontSize: 17,
      }}
      text2Style={{
        fontSize: 15,
      }}
    />
  ),

  startToast: ({ text1, props }) => (
    <View
      style={{
        height: 60,
        width: "90%",
        backgroundColor: "#9cb8b4",
        borderRadius: 10,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text
        style={{
          color: "white",
          fontSize: 18,
        }}
      >
        {text1}
      </Text>
    </View>
  ),
  alreadyAddedToast: ({ text1, props }) => (
    <View
      style={{
        height: 60,
        width: "90%",
        backgroundColor: "#a69294",
        borderRadius: 10,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text
        style={{
          color: "white",
          fontSize: 18,
        }}
      >
        {text1}
      </Text>
    </View>
  ),
};

const Stack = createStackNavigator();

export default function App() {
  return (
    <>
      <ToastProvider
        renderType={{
          custom_type: (toast) => (
            <View style={{ padding: 15, backgroundColor: "blue" }}>
              <Text>{toast.message}</Text>
            </View>
          ),
        }}
      >
        <Provider theme={theme}>
          <NavigationContainer>
            <Stack.Navigator
              initialRouteName="StartScreen"
              screenOptions={{
                headerShown: false,
              }}
            >
              <Stack.Screen name="StartScreen" component={StartScreen} />
              <Stack.Screen name="LoginScreen" component={LoginScreen} />
              <Stack.Screen name="RegisterScreen" component={RegisterScreen} />
              {/* <Stack.Screen
            name="LocationPermission"
            component={LocationPermission}
          /> */}
              <Stack.Screen name="MapView" component={MapView} />
              <Stack.Screen name="Dashboard" component={Dashboard} />
              <Stack.Screen
                name="ResetPasswordScreen"
                component={ResetPasswordScreen}
              />
            </Stack.Navigator>
          </NavigationContainer>
        </Provider>
      </ToastProvider>
      <Toast config={toastConfig} />
    </>
  );
}