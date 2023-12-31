import React, { useState, useEffect } from "react";
import * as Location from "expo-location";
import { TextInput, FlatList, Text, View, Linking } from "react-native";
import Background from "../components/Background";
import Header from "../components/Header";
import ItemListItem from "../components/ItemListItem";
import Paragraph from "../components/Paragraph";
import Button from "../components/Button";
import RNPickerSelect from "react-native-picker-select";
import itemData from "../components/ItemData";
import { useToast } from "react-native-toast-notifications";
import Toast, { BaseToast, ErrorToast } from "react-native-toast-message";

export default function Dashboard({ navigation }) {
  const [item, setItem] = useState("");
  const [itemsList, setItemsList] = useState([]);
  const [location, setLocation] = useState(null);
  const [errorMsg, setErrorMsg] = useState(null);
  const [selectedItem, setSelectedItem] = useState(null);

  const toast = useToast();

  const intermediatePoints = [
    { latitude: 18.462479201186422, longitude: 73.83214922869587 }, // gaming cafe
    { latitude: 18.465359165007385, longitude: 73.83478852247687 }, // polyhub
  ];

  useEffect(() => {
    const fetchLocation = async () => {
      try {
        let { status } = await Location.requestForegroundPermissionsAsync();
        if (status !== "granted") {
          setErrorMsg("Permission to access location was denied");
          return;
        }

        let location = await Location.getCurrentPositionAsync({});
        setLocation(location);
        toast.show("Location is available!", {
          type: "custom",
          placement: "bottom",
          duration: 5000,
          offset: 30,
          animationType: "slide-in",
        });
      } catch (error) {
        // Handle any errors that occur during location fetching
        console.error("Location request error: ", error);
        setErrorMsg("Failed to fetch location.");
      }
    };

    // const timeoutPromise = new Promise((_, reject) => {
    //   setTimeout(() => {
    //     reject(new Error("Location request timeout"));
    //   }, 100000); // Adjust the timeout duration (in milliseconds) as needed
    // });

    Promise.race([fetchLocation()]).catch((error) => {
      console.error(error);
      navigation.reset({
        index: 0,
        routes: [{ name: "LoginScreen" }],
      });
    });
  }, []);

  const itemsData = itemData;

  const addItem = () => {
    if (selectedItem && !itemsList.includes(selectedItem)) {
      setItemsList([...itemsList, selectedItem]);
    } else if (itemsList.includes(selectedItem)) {
      Toast.show({
        type: "alreadyAddedToast",
        text1: "Item already added!",
      });
      // toast.show("Item already added!", {
      //   type: "custom",
      //   placement: "bottom",
      //   duration: 4000,
      //   offset: 30,
      //   animationType: "zoom-in",
      // });
    }
  };

  const clearItem = (itemToClear) => {
    const updatedItems = itemsList.filter((item) => item !== itemToClear);
    setItemsList(updatedItems);
  };

  const clearItems = () => {
    setItemsList([]);
    setClearList(true);
  };

  const givePathOverview = () => {
    const origin = location.coords;
    const destination = {
      // College
      latitude: 18.46313753807985,
      longitude: 73.83434475316888,
    };

    navigation.navigate("MapView", {
      origin,
      destination,
      intermediatePoints,
    });
  };

  const giveGoogleMapsPath = () => {
    const origin = location.coords;
    const destination = {
      // College
      latitude: 18.46313753807985,
      longitude: 73.83434475316888,
    };

    const originStr = `${origin.latitude},${origin.longitude}`;
    const destinationStr = `${destination.latitude},${destination.longitude}`;
    const waypointsStr = intermediatePoints
      .map((point) => `${point.latitude},${point.longitude}`)
      .join("|");

    const googleMapsURL = `https://www.google.com/maps/dir/?api=1&origin=${originStr}&destination=${destinationStr}&waypoints=${waypointsStr}`;

    Linking.openURL(googleMapsURL).catch((err) =>
      console.error("An error occurred: ", err)
    );
  };

  return (
    <Background>
      {/* <Logo /> */}
      <Header>
        <View
          style={{
            flexDirection: "row",
            alignItems: "center",
            gap: 20,
          }}
        >
          <View>
            {errorMsg ? (
              <Text>{errorMsg}</Text>
            ) : location ? (
              <View>
                <Text>Latitude: {location.coords.latitude}</Text>
                <Text>Longitude: {location.coords.longitude}</Text>
              </View>
            ) : (
              <Text>Getting location...</Text>
            )}
          </View>
          <Button
            mode="outlined"
            style={{
              width: 100,
              backgroundColor: "#8282a8",
            }}
            onPress={() =>
              navigation.reset({
                index: 0,
                routes: [{ name: "StartScreen" }],
              })
            }
            textcolor={"white"}
          >
            Logout
          </Button>
        </View>
      </Header>

      <Header>Let’s start</Header>
      <Paragraph>Input items you want to buy!</Paragraph>

      <RNPickerSelect
        placeholder={{
          label: "Select an item to add",
          value: null,
        }}
        onValueChange={(value) => setSelectedItem(value)}
        items={itemData}
        value={selectedItem}
        style={{
          inputIOS: {
            textAlign: "center",
            fontSize: 16,
            color: "blue",
            backgroundColor: "lightgray",
          },
          inputAndroid: {
            textAlign: "center",
            fontSize: 16,
            color: "#4c4c4d",
            backgroundColor: "lightgray",
          },
          placeholder: {
            color: "gray",
          },
        }}
      />

      <Button
        mode="outlined"
        bgcolor="#c9bdbd"
        textcolor={"#525050"}
        onPress={addItem}
      >
        Add Item
      </Button>

      <FlatList
        data={itemsList}
        renderItem={({ item }) => (
          <ItemListItem item={item} onClearItem={clearItem} />
        )}
      />

      {location ? (
        <View style={{ width: 300 }}>
          <Button mode="outlined" bgcolor="#cce8dc" onPress={givePathOverview}>
            Get Path Overview
          </Button>
          <Button
            mode="outlined"
            bgcolor="#cce8dc"
            onPress={giveGoogleMapsPath}
          >
            Start Navigation
          </Button>
        </View>
      ) : (
        <Button>Location information is not available!</Button>
      )}
    </Background>
  );
}
